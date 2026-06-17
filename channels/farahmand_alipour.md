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
<img src="https://cdn4.telesco.pe/file/HZgd3rN0R4cYtz11uP4V7_rli696yxEQvqnAydyoN9WDYGotzNpHUdNu4DJaGgsgtZy32R1g6X9OqD2euTPT_8Dm-wt5kz44rgw8OF0nntmksYmRX1doMc56i3Tw1GLVlnIjD1T6i3tVpBhFj8R49orfECZ1VxGtyJwaoicB9Z1gdtWKYPzPTGx4-ZH1PL95AIobZD0rbegRAoxdliPfxtNvk-0aVAtT4D04r6Lo32-KQcamFz8_YZ7I6XRr9dQp_2pgdw00tCKrI3jw1juNj45uCytL2ZpZnydoynqv98WVKgIw-RhzRLU0B_qD4kGzzxoN7Vw487geeC5ZLorV4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgmlffjzE_qrw0K4fcb3LQ2iexas8EVdu0cykiuoK4Fy6L_MD8sZL-s_CTNJup1hheqtReGr-ZtUQdaH6BSDhOAqzSyHbLrkU-ifQRnNxZcf2M1FULmSmUS3Ai9YT9hEJObZx4gSJP10kRBTTRdSdYNz-cOHNOMaWYgFYuIJ-ma6lrEvxJsDEppERlOQSHXfux3C6cwwdgc1iMlHS_AxH0JhGsvoGGGPBDiOtsZ57LFJ4jHZG3JsrEwAF7S3_9fQfJFLZk2smlIaPORCNezHOhFJrg9Vc8vO14AyAlAnDHV2xLDVwmLEikTH2NsEpRbJU64XtwDF1Mt7fV8lFhsbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDMrI8sjMdcQthejeq3gW8GtkYqzNcYT-bFT8ZC2DlPDU4fC3yWfDazNq_DUd3YcFLcoiZFB56PexJFyl6MtXaAoIdZ7f-VtFtAMPZBqQu-RRBQY4jBw5MYX9JWYyge9xiS0ah0IvUgULsL_YAQmDHcixHj8gzfG6HmFoc6kWHkEb8oND8MZq6KXqG_ZP3FSmG1ymI5ayI8mEfiYD7FeVEFQzbwH8GvKaf9HS_XMUxGzWCK0nrsA4JKMzzJaKF7JcxHJLa_ek9m1QwQxHXqj5Cvu2CXuN4OOcYlaRtLf85d03HpZRi8I3j30cePJnMZKbYcMXUCn4lxXkZrk6RS3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKeAfFFZ7yFs2dPG71D-vguS7m_tGyjrM_7aOtKZesH3NAfyjMP_99LnYrvwFw12YerUneqhW1MnozlIg7sCBNZifPjorSA5nOuLG_qjkG5qed-ezX3pwZql1ZPKQORgh1OvDRA0tm6sWs4T3WjNKeWFH1zfuTgsmEOL00WffrKXZbkHcv7NZLA1mLVyLWZDQiNMPJxZGzE7LWYf7W92ciMlPb1sCxi9wKEw5HoWy5FIvB45ry39TeGeEx9AIuFbCPAWILoeDNe8QGYvtSggjoAxZtUzZfXQ7XiX6xHPSYGAUmucAu80xCT17Obm_JM5rcaLNF2hdZKaKf9eer7zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=beGd6hj4dpjXBpdn955zRb5hQ7qfIl7f-EHjDJx6hy60xaOkKVCfQwA9NNsmBW3tQA3TCtxi_5Esbndy-JRdLKLud8yPGXyKJ0-8Fr1ztUshMmwx6jtrsAtknKwcxM7vmF2xczF6vnStRqXXsmVqeUQ6RFx0cLjZf-yHM5iEWaR5HzpYq28KkDZvaoRKHNKlP2Wit32-Ab0M8Z_fV3X1wxuz-Vaz2fYp90WxWWJyFfmoMIQOCdNKTjPDi7IRjVK7hYAUrqhcIlgSQcNZyRynC6xEScO7_ANjJK3mYxrsd9MWvQKgEqTPFA_RICFtNmK9VQVoQyVuL0SqLonkwOd5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieEhutb2TPBsPUsSMePt1GI7n6UjUt7srBoymC4CUpnj6IeJ9qilmBBOwXxgYN6R4UIGC-jxrSlZfokCAtR_oD8AhpZFxo6ZVtDHDVzb3aK1QioXRSKLQsYgEDnnnDfBIxBPXhMRIqU4za2Om8NlmZCIgXHHiqTnbl3GJuD_9O2qJmQ09YWHvjf8jkANdnqQSS3lGXHuFAtqumIaQqAGP-mDaKfbJHJyO_4XVkFoV_l-mddx-Zip0ClI5hUEx_Gt7iC7Yzy61GE1WaWAf3vJ0QRo6x1fkcriVU9gFwRA6CNChdOKbsv612yZfy6X-JTAY3yv9pyzZttogBKi1DeONBUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieEhutb2TPBsPUsSMePt1GI7n6UjUt7srBoymC4CUpnj6IeJ9qilmBBOwXxgYN6R4UIGC-jxrSlZfokCAtR_oD8AhpZFxo6ZVtDHDVzb3aK1QioXRSKLQsYgEDnnnDfBIxBPXhMRIqU4za2Om8NlmZCIgXHHiqTnbl3GJuD_9O2qJmQ09YWHvjf8jkANdnqQSS3lGXHuFAtqumIaQqAGP-mDaKfbJHJyO_4XVkFoV_l-mddx-Zip0ClI5hUEx_Gt7iC7Yzy61GE1WaWAf3vJ0QRo6x1fkcriVU9gFwRA6CNChdOKbsv612yZfy6X-JTAY3yv9pyzZttogBKi1DeONBUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzOtuF0z5Wujey2F3OdslOG2FbUAK-T38vAZWIM9QzCUCQ20JiVQExwCGez6fwoNbJWiSNNRxxlPK2vksG5_HeghEPJeZjhmDrYSqah8o3nxHuUUjvhECSRciyTbV4EipyWQXQlJSUR_heBSgjgCF0VClBwY7qGB_MpJi-RudDpKIJKKyAH9n10R0_sTeNt5RohWiXt5eaRqDcVr6X9lB8dcUh7Mpy6yDMJRBcfJx8L3TmoiM_mUGjWyRIF7-V5pc6w_G-iIBEkUVB0Cs4njsqHjZlReNFavrEkDWaunhwI9RjU2lCzMHQXBmlosuieZr_mksFW1-vbSpo2aiAOQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMnAwp12NlLaDoxqO8kED0rGAKvT3WtaoQKSJR6_RmhFREk4uQ6s7PE2f93UJYqczht6t3pWXdFom9kuKirSPPM2WRtdhfsUHsDVK6b7xwD_gDDTkXKjlmTJgo7mQO6DkLt7b4S0etWolWbvKFylF9UNyfIXPm2RYZPLPIAZB1gG6LLlnYPTPVR_ArBRSWotu1PDSdN0jri6Ld5zG4G4WvsJmQzjpQO-SENr_qsOHFzVPhRoL-86RHLZQsiJ9mRUtgQ-6qy764CMwM1qwwYzxiu6t4UFkeLwunfxQz8DCgfVOgoDsmHE4hsbcv0QVbhJo6X7j4u_OCZxg7hWXk8rtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbwKMmlnjznzJhvSbLyX22gPN8odk7N2FNb0tye2wyZSqMvKL0-QndjFI_6t0B2nhdV7CfyJ-WepjxSNvQjPBveoNxCC5NABxPlgt7PrXtTBLdyUfwUBQ30ou9oQy2TA2cg9IbkSQru_5EKqMy60qHwvMyjEJl5BVa8ywaPNswnVaU9FdQoMUBMUY9engmHcc5QIottiqlyZShFsS-sVJ7BcDGXrhKOlvBrrhHLI-lLkZrsHO3BEhiavfJ0H1YZ0p5JSgUvEulSaCoYGV2k-cdExFSQb7mDHEFcvAHwrA2F_O2makb6davd6Lw29tDxsj-GIq6Ps6LjVBlqKuHjHVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhdSNZMTNhPrdn_c0Q37go-aYeV9k_WeiNGEivhwCCls7qEZG0JxEZx66UAodM6VNLuHeYCi-qneQyZ77HQ5qWpGXYf4D-dQHy_zQPS6RCoAJ7KG-dwnYCodpm9-iG9j9WNZhleZyohhqxOaaxmcgl2YJBbFs14-heUH8bt_O43xlr5KHnYrRLnz2ppTJ3ZYE3dN3bx1WwP--NaokdISqQcRUeaaqdmdsax7fLqUM7Jg5aGTY_d8AR0DR9OZYn10su335YJIAWsjW_rkP7sSIpQK4PprL_qys7mbpRgold2J0T4PMvR6qCJ-Ovu9gZg0ozmCSJqFpcRr5aX5U63z_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVG_ztyV0P_3m4VyfBtKxy6gMtx1td5H3osaROc8tPYdmMvyKjCp3O88Mis-yHX5TvvjjlCduuTSHBkXqaH3XCPDtX6g3UTk6Sg9s1IOFZ3uYdf9IkUCNL9Z34uOpoySZv6Ys-JoCocm-i59HO8B8lJ194fRnFPz_bG15fo5JmWeqtGX7KxKJjms26E1o6FxL3ebc_f0E5nAGfy2UxBjmm2pEPFFlXady8a_fUbTv459cwL17ukE4bmfbx_-RQRtmrUSsWdfqGSSJugIBj_rzlbsLiID1h2h9IBZ-cSt_7RrXKiYTwJJbKtnXx_BD1oJ-QmdsArMauCOUECjU-0Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ7wqajq0ZM0Djx3nloCOAYEKVNE-_coIWbugO5HcxnqyFeYxNp_07XcztXY6nE3SMVoPA3rZmPRnBbR4QPHpWGt0NnOKVZ0kMSgFlWn26q6VdvRcNDLOsNtPdCPvqSlaIE3ryqCfH_dh2i32KvwB_-0YFkJgT4WvGeaUdAWB7aElHhojN_HN0_L_xiPb0qO3PeN0W5O0itZMIdyNgf_x6p4wX0cmZLRCPKvRNNThdPWkNR9skjJdofxvYuVI7PDuzmBjJojy_KljoM2a8ycryUC78dYgAALtBqU_dhQ2PlUrq4-YNuEu6QJneVW1ZANk94Oa8l_D4fefO0DQShRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jAemEnTVgtF-EMz-N911hnA_XKm21LRBOPyAq1iZG6xyVD1kpTtTCO8pQ17Afd1FA_V7m3u7xwIrTce-aXjKUQjSrwZanlymrMVjZ0KpkEq_YBtd5CPm_icaz1w8PIW8rbcK48f9p6bkqyBG9QTI__HXUrY42OEDjkEG0tfZzG7lwrwp30Wc16mpKQ2fVQSZyKodOBesgXqqVu1kx85mLQKKEtbOBloAL2g9ifZu3cR5RvRoEm6IyqLfZ9X1PaYpl4i-oPU9k06e4cA-PfQJC0x4qRaPi9kD9-1PCFjurtLle2S4x9o-_0Ic9WH4r0837mOOmVl26BN5EEewr85_dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jAemEnTVgtF-EMz-N911hnA_XKm21LRBOPyAq1iZG6xyVD1kpTtTCO8pQ17Afd1FA_V7m3u7xwIrTce-aXjKUQjSrwZanlymrMVjZ0KpkEq_YBtd5CPm_icaz1w8PIW8rbcK48f9p6bkqyBG9QTI__HXUrY42OEDjkEG0tfZzG7lwrwp30Wc16mpKQ2fVQSZyKodOBesgXqqVu1kx85mLQKKEtbOBloAL2g9ifZu3cR5RvRoEm6IyqLfZ9X1PaYpl4i-oPU9k06e4cA-PfQJC0x4qRaPi9kD9-1PCFjurtLle2S4x9o-_0Ic9WH4r0837mOOmVl26BN5EEewr85_dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=fhKAITOsKryjVuVsPiuE1_Ugp6h-0cnX5sq7DbwKH6jyQKQQwRAZNAGMXlJLT7LV0m1Q1MM-NHvQA121pUGFFcCN0uL5qtPZrU_81jueq8pmdWn41CINgF18Z_MFZ6BzuZtddMJVJtyhrsnJ9XN8XYwfsZXhP4hVdr5q5qQlzRi2a5wV-QXw66kUSc22q3mLHmxFe0ftiIg-qmbXHSEgpAye1EZq3Zv_a8UD80ZMzrNg3ghufod3TyRvOylqaqAmpFxq1_lG6plmisHjBRl04wtO5FhQp5qKvxQ9wxLqATZA6N38MckG8hB6AuXvJtFuB7l-JCBG93pTFPmJSj484Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=fhKAITOsKryjVuVsPiuE1_Ugp6h-0cnX5sq7DbwKH6jyQKQQwRAZNAGMXlJLT7LV0m1Q1MM-NHvQA121pUGFFcCN0uL5qtPZrU_81jueq8pmdWn41CINgF18Z_MFZ6BzuZtddMJVJtyhrsnJ9XN8XYwfsZXhP4hVdr5q5qQlzRi2a5wV-QXw66kUSc22q3mLHmxFe0ftiIg-qmbXHSEgpAye1EZq3Zv_a8UD80ZMzrNg3ghufod3TyRvOylqaqAmpFxq1_lG6plmisHjBRl04wtO5FhQp5qKvxQ9wxLqATZA6N38MckG8hB6AuXvJtFuB7l-JCBG93pTFPmJSj484Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFw2T0O1U1McYOQHeNQoUQcSBQILU88nTrTUPuQEUnv-K0yFHHCNzK3roqDPMT4zmZgaRgbkAqy9spVx7lCWc1mwMd_o6EQaRjbq5mmDTZkwB4cAmzp6xInbgIR6SiKpYRbSPfVTlRNnMv-DYgBeqmFYNGbVa5e7wF7XWRDut188bkWf4wGcl-nVR082Av_hVMcHpIAFJqu9GcEekbQNejKvbpb2u1s1jKGlHt6sLiBSTp7ZBjD2Tnib1pNu_8F8l9MTYW5WjuPsECdU31JC97VpepjIfWq7AKJjZsH0TQ9xRRtlT0TYXStrIHnyhaCCaMkxTqjx0EooFXJ_DPrv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe771ReYIdekS6CAaRmbOsu3NXflO0TABJht_uao_QKzXmH22j4G24dAepXGK3at3_uRgeYwDD1GWQQGfmtxfRv9bVeYn-c6We3yUbT88OYm_HvDM_3tPe2eA5L3iL9ne-YtZILI2tF02-OE-riq_UkT9Tbffv3cXe4dxFozLyU9sDeapqFcRXM8MNNIkpAG6VHBQnBfQGXkQWjUnnBBe3UjYNMkGL-yInWxAdEQLOvLygHfUyPZT4WgtYLy4rIookXR2IZZKNGzLo3cGBB0BjUZYD_uDQHsDyJOjh2ZNWsEyGhrO6pc-iz-FnJG6W7a0ER-4YzGJd_35up5VQ-EIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky8WnwA3C2gOpesqaHjeJNxUNr9ThzQEUMKIvGMx16n6HbqDWh9murGZLc_WI3Wgzx768k8UhM9s1Y1La1m3A0dfMe1QX3xVP6g05VIC9m0adcGOfE6m7zXzkiLCJ7hCMIo6oqsX-Yf_AGmKRpxIY5cQ1BbSboO1F8vaBcR9uS8qMtTOqWbIX3zpJCz7zjTpKKpM41dCn3Dy54JSv4hdzyiA1HrlHVBTSNVV_xXk61SKtN48hsUfGY_3wpqaMuTvrAopweFZb7Y9uhUZRAxT5VpxfErgkvWWEmK9bLzdQYM0zS-mPclm8wfG4YXb-fHvEc7Klvm8nryNMzdHqkYe6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIDzUoFmJFhSegFYB3IXcekDD0afBTvxiNeghgN0QQqqrvh254kWsYOR3bF_NgtRs5_M_Lntn_p71sh6vQ2IRjlTINqvpMAhMTq0uXebOecd1jpqCt__EWcH4CsqKWOZcqj-zrHI28GC7VSRf-If_oohogQQnuJjpCF3SvS1Bb7DLrODwdnNl4PtTWcge3PGbbsHaOZEBxKzdLsvkx5M0Mmb6DfjIzmx0H7EqWyUydEXamib-wUcZ2MoXBnocOXkoYdSg6CCWIwCtvw4Ft2__HiyRGsY8X-U56gNljrfbbrs1TIowdj45U4mgrtoc6_EA44JWB6_0tfCx_3DU1Y_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXQx87erHZ4U7KJXYWZxHueEpX9M6A1VTaE95oYmFGYjcyfIq858DPL2vMn-6NLEbqQXwune-HYs8B2dc2xS1JCiVvDOATLPWS-dfvZ5GzeVaO-H6jNw4HgPNKOTbAeLFcGdWub-8zPBkzkf_AajT4LKBH7e9bsiidwk2XnGSodJ5UEy6BPxCxefE2kNdlsRl3Oc-1sC8x5c33Rdd1XKt5vBERmFkkdCgIt5sYgMwcFeTIPc3vdiWH3B_al4cVvgUw3a_UWkIELZ9_9X3HROZ-OKtWJMgPNL-lObskrbKvJK-4AhgQEWRRLVxyGS6TfzPrFAjOAJ2JmmIcAiNZMw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=Ac1gtGMyxGygIjdFozZnoJRXbeCdiCllUgGOPa1WcfJmnRbyl1MWkVs0oeEIIbdXt5HALcYAj0p8KG8cOwcZe02CJaiX89wxmsjxyV7HOtgjBVRGIvEXsT3NBM0jPj_d-Ex3cRMNw0KivQJeq0xYEFeveYzu0MAS6qq8aoqMOqFLRrMIh2b3g1KGA8etqQbiwcI9svRt19Z0oD-n5QygraPBvlKLAJ3RPzPmdZRo9voMpKOdtHNbCYC2GUJCJQLnz197j-OtTzfY-Hh-tk9s9tBxryzXLfE_6xTwYiUsIeFVd2RyAoXmF0DSIOln1YPq-MxYBD31xzG2a09VUvuCVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=Ac1gtGMyxGygIjdFozZnoJRXbeCdiCllUgGOPa1WcfJmnRbyl1MWkVs0oeEIIbdXt5HALcYAj0p8KG8cOwcZe02CJaiX89wxmsjxyV7HOtgjBVRGIvEXsT3NBM0jPj_d-Ex3cRMNw0KivQJeq0xYEFeveYzu0MAS6qq8aoqMOqFLRrMIh2b3g1KGA8etqQbiwcI9svRt19Z0oD-n5QygraPBvlKLAJ3RPzPmdZRo9voMpKOdtHNbCYC2GUJCJQLnz197j-OtTzfY-Hh-tk9s9tBxryzXLfE_6xTwYiUsIeFVd2RyAoXmF0DSIOln1YPq-MxYBD31xzG2a09VUvuCVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlJI3saTdQlWsSHxM7jiy2m5s6x1BB4rJHCBbEXa5yjm3i5ILHtTYaQ_0XsssGEg4nMgyOsgnxNqjVADyZri3_ZdtFornEtYEq_05Ui3GYtEKMp3EnlLDr1xEVhEEM9IiHgL2WZ83doa2-a0xelERq2xpHfjHDVhHlQJPkUqkNNY61QFswyneoi4t7tqI9fmzXMSnF_-gLVvqmqrFfp-k7NZ8A6XCjCpYvOub84Xp8FGk9FDsUpuqDz-E7clpJNFofI2cWNQnM0kRpEsfldf04w8NtaaGi04yQJ_OETmn2VTHFLHMMyxsR-N6i4JhM8ijh5jQDN4P5oMm1ppHQzIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEeST3lYKKby11qEzV4n9kNNS1Csu9kmwbtyJjxYIef9e02vRbIn2XWhoTLRHVWZW32POBiifnIdQhYMh9NZIwJSRD6CoMnyUpRR7bk_f58gRSDsrftiByMHb95i4q3THEXcT3CDputTvSkPY0hRqg6EfLjNdsMBWwsT3PpMHlurmC_KQx9kfYFqcLO1YBxhmez1ADQPrxoGA3M85SWc-Bsf4rFe0Pxv7d1SzjuAtvWXUIBjqwlJgwF5hDeY9jzcmu15rrKqySD5A2TeTIlXmaTpkVHTDdhngvHwr3S0MZHEr8h7L18gkGDOTYa4EKJPSMauKeV89y5xGTL6P7Vrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_xC0gxNWcvd6QB5hTcEyIXdUHUnIDTgnbEYZvxc7K9WMp6sAmKhzUn4Gee2sQ2FwY9sRMUlF9-JZERcd73xYeuVA1HGQAWarubu5iMOSjfDKrs0WFA2pQbt-nuLklACMlYLjTdz0Z6H9OzVAFcgRTmZNV9A3GNE4Z15UJMd9yiXbZBiP7oaEPJ7IpKcUFVKMVCL5CyOlOTiijDIs-54SZzIk5OmTZztXoOU_Zi478EQDpuZoILJCARRKB6iYw0Nidi3W_RPagMyG_mIoR1BY4b1Huxz7dQHQIzKTk5RrDl-Mq9pRevZrB_-FD1IgZeW0ELcekfo_MlWB6Ecsg6KZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtU04exR8t-4HetVEpNJ7mgtZ7jYpDvS3xgNe2Q4sISq4vaXblmmSrfDnZ2jJCCc_UojSJmEMA4eMgCAt4UsQ7np8CbrrvZQ6-14zwItT2B_5WDUMsFhnhZrhA2xX3iZ9AOvTIuGedKocgGlEy-VTARrl8ysbwYgSUgLmw3EuMtfxVrH1ANrd1TKGAsxaRrfYWFUD5NADS_oeTcq4dK4FElLjZhggZanjYwnqLZyBDsbOKn7YVhNqhbWGPsJbiQhA4zBbx5NRGIwPFOiZnqWWytt9tlzbUr_1nDQpXA5Fa8wgDdy7JX60qGNLx6hoXHoIMrcU_reE_4zN7M--Y0m1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkySyR6aSmcuf7RNahRDmoJnhWkFoVBboCqTWm2AQd4hFDGKplWnGZ25b_oEq26VcEcv23sTXZvEUf655jDz6FXOB7ZhDk68QgLV3Nx-7ut_2Nv1gAV9jD7xunULwJkKbcrrpRap1z_TIPWWJg6I1cD-o1niJMXbKFbWL7bQzuid0My-ZOn695QcSM0heimWt_VmJPs_385vQGBsEx82rSShlwdKdlhLgDe2V6VZlLyI8C0N1yuQ7O-mODPrXVmjH_YibZ8UJZxa89aIuCSoqw8tHePNe3zuws_PAlcUMUHaQmBJIDkExq6kEB4k1-nMrQNliT5ca0TLI9axX0iGbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8jzZlLXEFpnZ36RtnKUb2MOdlzQPrUNDb_G1CSbGkLzizgF4wKDR6rvyYxkOKuk-xo-mLcArcehihwVw5Gtl63dxa-VKVanGff2WqiexcRO68g7O3wyPFJ316-3YMjqy5j4JXtaPFAfueG64ab-w8bXBkdW9P3Rc3V6_brn43bbGVGqxtmAyPAQ7PbruLNiUnPXb2h4isTfmHP2VEQWvPP7BUh0_0T6OoQDXcRepxOvj5JVgPyS6WQ6gu06rp4xCh4llfthYPKVv828BAkrn_4h4gBhxecmSoK6uTrU8xJdXTcjrmxjXRI9EtC74k377Bth_23zu9UBuvL5G5zuCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnivmKaDQHCd92FFUIBZ2T6vuJADBzs1zWs5ELwEqTqYmyvtYBxsrJ0Q861HOLHW79bihJCyfRqIs02IIFpBFvKuoZUbebY3lfv_7OsykZ_l87-UQvuf7y7QLBLJNywEkJK8ksk6ntxTgy2A_iwO_fhVhzleaNNxtTqI7Hjpsqrc2dVVeRuIFXlWndJMb759qGfkLQYznbULn1--wg3h8-9HurKB8l-COKJqaV9vgjU7ZFNlrzNcRXGxKNXhJAFes3S6QPP59Fs5kC6rvBqpdOGw5bkzbrXXfieSkfNJVTvyAYd0cTA2O6Y0zK2ygwFn74ju8azJBibSxQBKMBtHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=spR4G16Ck9djv_0UrrFuC_CVOg3hDBtZ_4W7eAQ_zNINjdO174l28xrVgqenUQjW0eSTA1tlfw1KI8Vsat01BuogAmPOnuXtPsN3uhICY05hPm5ARsoGr6cbSTGPfaJQwybZWrCL2uBxVk0qQWZ8SUznALBx1VT1a02stB3cnJ0eZP9bu8VQ61oQMNsShR_YD4sG1UjW9DKi1OSR1DnbENOUujD7OT5i4t713_HvMZsR4lQ1DAY8X-_7zzmhUkYHVhB4ntl1r6H3EJmef0kX2C8qowqOGakGvleXAsjeDG4MHWnBQpoW0QEkEim5mSkRV-00mPKo4HfoKm8EdfFlfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=spR4G16Ck9djv_0UrrFuC_CVOg3hDBtZ_4W7eAQ_zNINjdO174l28xrVgqenUQjW0eSTA1tlfw1KI8Vsat01BuogAmPOnuXtPsN3uhICY05hPm5ARsoGr6cbSTGPfaJQwybZWrCL2uBxVk0qQWZ8SUznALBx1VT1a02stB3cnJ0eZP9bu8VQ61oQMNsShR_YD4sG1UjW9DKi1OSR1DnbENOUujD7OT5i4t713_HvMZsR4lQ1DAY8X-_7zzmhUkYHVhB4ntl1r6H3EJmef0kX2C8qowqOGakGvleXAsjeDG4MHWnBQpoW0QEkEim5mSkRV-00mPKo4HfoKm8EdfFlfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=XDyClNUexwrXsDZn6mbyOqW2mvujTD_Yr_TZYa-tLJFlDf7RV89V0xAjUjEheFPN_KzIziT4EV7MgalhCCKAWWiDEp91nVG0wyd5T79Tz3RU3-H_PYOb-xIjb3ht2BEocXsEToHw490cjXgAJ2OJ9bH2G5uofodbA6OrFXuCSU_TLoxq0gOWgkPCvdJSx5J9ZEkUdQiGDs1Q7WpG8YPbsK2yvuLidhavfRsPSP61IGpCS3YlpZzFJDtFg3cqpULCw55tbHxPafp8khnEVIDKtzI5R1gQ_t3l54HtPf65iJfMu7Ey-JKGkLQj17oP1MkXQ6jIj0rZp0pudpJd5fhVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=XDyClNUexwrXsDZn6mbyOqW2mvujTD_Yr_TZYa-tLJFlDf7RV89V0xAjUjEheFPN_KzIziT4EV7MgalhCCKAWWiDEp91nVG0wyd5T79Tz3RU3-H_PYOb-xIjb3ht2BEocXsEToHw490cjXgAJ2OJ9bH2G5uofodbA6OrFXuCSU_TLoxq0gOWgkPCvdJSx5J9ZEkUdQiGDs1Q7WpG8YPbsK2yvuLidhavfRsPSP61IGpCS3YlpZzFJDtFg3cqpULCw55tbHxPafp8khnEVIDKtzI5R1gQ_t3l54HtPf65iJfMu7Ey-JKGkLQj17oP1MkXQ6jIj0rZp0pudpJd5fhVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=XY1RWVv-I8hQSUCMjLW6WcfS19-c53DtWfzuqXCTli3uPlR-lQvpizS7oHEQ3CToYyDMnvoVV3zkZGkNQNlRYKubqsVkRvzoLJUOzRaupVeribAys_IHonNoutfbkgBoujC7-G6TURKAyvHC88auk_tn-neBaNDdn98CA_vP-G5U2YH6y9BqzpTaPfEhGmK8Vt-QaBGzJ-BVQWpkUj5waYPTDLHsIyPStsKrafvh7ciFWiXentJV_yzuArc1eBPcTNRLT0uww4Ia3PBtua919kcCbuTjtpa4Nm0BOF9gA80LHN_JS0yYsl19srbmYl4LiWXGJuy_zQ8rHnpF6flmQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=XY1RWVv-I8hQSUCMjLW6WcfS19-c53DtWfzuqXCTli3uPlR-lQvpizS7oHEQ3CToYyDMnvoVV3zkZGkNQNlRYKubqsVkRvzoLJUOzRaupVeribAys_IHonNoutfbkgBoujC7-G6TURKAyvHC88auk_tn-neBaNDdn98CA_vP-G5U2YH6y9BqzpTaPfEhGmK8Vt-QaBGzJ-BVQWpkUj5waYPTDLHsIyPStsKrafvh7ciFWiXentJV_yzuArc1eBPcTNRLT0uww4Ia3PBtua919kcCbuTjtpa4Nm0BOF9gA80LHN_JS0yYsl19srbmYl4LiWXGJuy_zQ8rHnpF6flmQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=ni8TX2pYnimxfzi8gx4Fsv77FawD6Q557_DtLgNj4TVpRGMpC2lUeDXqLaRodHbh0jDT9LfBOS18WYjzEMziMOsNKoehatQ6OShm3NQRO4Q-sJlVkNlfyM3ddXeBJFtDbrpguOX-T47e-dDkUYbA12cV3qIVgBGYuHeTYEKuaPJF43hNp9SLhs_haJcIZfSB6r6yls4WWdqusK326PDFqnSp8eSef8CQGxmKP6HDV65t_rS0EU276qWPW-AVuhVF9hua7-qE2IVo7vw0E68lqZ9x30dfUsmRAn6I1yeYdENY8lKdHddxXWcWoM6Jw3YJpAw_PvvjXmHwTj0gfuIQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=ni8TX2pYnimxfzi8gx4Fsv77FawD6Q557_DtLgNj4TVpRGMpC2lUeDXqLaRodHbh0jDT9LfBOS18WYjzEMziMOsNKoehatQ6OShm3NQRO4Q-sJlVkNlfyM3ddXeBJFtDbrpguOX-T47e-dDkUYbA12cV3qIVgBGYuHeTYEKuaPJF43hNp9SLhs_haJcIZfSB6r6yls4WWdqusK326PDFqnSp8eSef8CQGxmKP6HDV65t_rS0EU276qWPW-AVuhVF9hua7-qE2IVo7vw0E68lqZ9x30dfUsmRAn6I1yeYdENY8lKdHddxXWcWoM6Jw3YJpAw_PvvjXmHwTj0gfuIQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ZXd_wFaIheybeKKkm81G3p02unSdabsfpSIHkqphX1QOqHNLVRJzVdoEab_E7EgLulWTqKIIyopljEibsOcSW0tcaNVQN0M73ZFgx-at3M1JFvZOH-ObrMm2NfcRTDeAIlhYi42ewQZYwa7cSFrYI6NzJAfSsZV9snQNbBLsmora6mVD0TKjx2LN_0oAb0terGr93Reupf2N3apoTpivEE1D1w7TV2MgnJcgFUVU1EqUEshj1LQmtfVpjV2PRCVLtzNGKnol53EMGi95RWlRKigHORUe0zxbHYJ53o2pii_m1gXNW57Kn882cfznIQ0qya2fhomxqri1XFWjttllxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ZXd_wFaIheybeKKkm81G3p02unSdabsfpSIHkqphX1QOqHNLVRJzVdoEab_E7EgLulWTqKIIyopljEibsOcSW0tcaNVQN0M73ZFgx-at3M1JFvZOH-ObrMm2NfcRTDeAIlhYi42ewQZYwa7cSFrYI6NzJAfSsZV9snQNbBLsmora6mVD0TKjx2LN_0oAb0terGr93Reupf2N3apoTpivEE1D1w7TV2MgnJcgFUVU1EqUEshj1LQmtfVpjV2PRCVLtzNGKnol53EMGi95RWlRKigHORUe0zxbHYJ53o2pii_m1gXNW57Kn882cfznIQ0qya2fhomxqri1XFWjttllxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=NfXCrqjeBsNSJuncpI0jiz4tMp9bmlnl4ZOibbkSpGC4pATXb10VyfxtRiKWya9j31NuK-X9XmTESpi4zO5VRxmVohC8rmXAYUg_4SFZsUXyuUpS7qSt8U0UsgfWAlMnpoChsE0YFJnhYRzKvQ3oJky9QpsGs39i5mgzi2WhXSHayt9uAuwRR25RXDsJIETx9MoLJpuIm3Uxe4BjXP5Ue5nQRt0NmFKg3lo8JhTOxDSLeYE1zmo940tOKFgn8zKYNwaporJIPMb_MkJRKdZXa6qTcgR0u6VlM8gysup0BpezcArwSkgVS-ul2wwaaec8X5ibEYtbnZGwTITJ7xVIvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=NfXCrqjeBsNSJuncpI0jiz4tMp9bmlnl4ZOibbkSpGC4pATXb10VyfxtRiKWya9j31NuK-X9XmTESpi4zO5VRxmVohC8rmXAYUg_4SFZsUXyuUpS7qSt8U0UsgfWAlMnpoChsE0YFJnhYRzKvQ3oJky9QpsGs39i5mgzi2WhXSHayt9uAuwRR25RXDsJIETx9MoLJpuIm3Uxe4BjXP5Ue5nQRt0NmFKg3lo8JhTOxDSLeYE1zmo940tOKFgn8zKYNwaporJIPMb_MkJRKdZXa6qTcgR0u6VlM8gysup0BpezcArwSkgVS-ul2wwaaec8X5ibEYtbnZGwTITJ7xVIvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVY7R5P0qGAxMarB4E5mManmpL54f7XibHvgNt4RSvSfI8Nju5HH34qOvYbMc5dFY3I8NMNQm0W64uuuUzi9BvPYkdVzqTymdrt11j_x1ctEjEqvTjQYDqLaXpysn3doBR_wL9tvL3IoP91OAgMvIAbNVndkKRnTE0NbGZxky_ye8WYJH_XBfzSC6SDnJs-AjHZOgpDHKwj9l0PRahA0sEpUfb-QhZEfxJ8_J-ZXOq5TYM09V17Xbzw66X31dEiqDdCFxGc-XefW8LkAEstfsl2ekEu85UAmYEDqCQDerExUUx2pAluhySI9mGuETREtHDbd6F3QZqUrdCj-9qwONx5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVY7R5P0qGAxMarB4E5mManmpL54f7XibHvgNt4RSvSfI8Nju5HH34qOvYbMc5dFY3I8NMNQm0W64uuuUzi9BvPYkdVzqTymdrt11j_x1ctEjEqvTjQYDqLaXpysn3doBR_wL9tvL3IoP91OAgMvIAbNVndkKRnTE0NbGZxky_ye8WYJH_XBfzSC6SDnJs-AjHZOgpDHKwj9l0PRahA0sEpUfb-QhZEfxJ8_J-ZXOq5TYM09V17Xbzw66X31dEiqDdCFxGc-XefW8LkAEstfsl2ekEu85UAmYEDqCQDerExUUx2pAluhySI9mGuETREtHDbd6F3QZqUrdCj-9qwONx5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq-qNvB_-LINY1vHeI5ZExUOxWm4mza3w0Mw_14zImbvY4vhymnycCnJe5Pt4HvPSilLA3wFb2nF8VvxkE2Q0_YNOxAJJ1lS9YS0e6ahDM4qmckVlBMTUY_hiuBTl--_b48iCTcmFsdbVE79yqUOhW50--S4J8AQn0y-rzEUmEdS-AOIFLlphFkUXbV_0p4j4wVLwHo7oan67v8R7sM4LLm7Xhh1tsF1EgfwV-4TAK1yMq8oL8-9XlSw2BPKlBmvM9p9RAvlNs7o-xn8d5sGICsFR5EMvi_pXBQ9UBmhGBxHfFFcZ5vdNVOqm-h4Z6RITTVIdVlqEPXy1Qlo6xO0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=gK2FAOlLvtViwBxg0cgtzkbX4DmH1s6weUU-RREyBC6r2sOH6bIwIid3UNqKUJ0QPN67sEcTtQYavTv5BBE9DCGCp77O-w0DSEW-I0gO3j6pMd0Nw8pzFWWAn-nc6tyU6OOE63Ip6YvctyAFFUW8a7i_qkEE_vjbWwINApUnZljYlHoqY1MmqUVnaUXUrrN2BHiKGUvx_C9iPUTlSc3jREN2zIad0dbX8YmkW7y_VEeSBeAMtcordNBzBDADhXGwIebNgzX0pWnIbC6rKADxygFcAo-qEdJlxTENq28IXY1vEYeMo3tMXUuI-YJ1ByzC_mr4qGSA6COcEw2XUyO9Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=gK2FAOlLvtViwBxg0cgtzkbX4DmH1s6weUU-RREyBC6r2sOH6bIwIid3UNqKUJ0QPN67sEcTtQYavTv5BBE9DCGCp77O-w0DSEW-I0gO3j6pMd0Nw8pzFWWAn-nc6tyU6OOE63Ip6YvctyAFFUW8a7i_qkEE_vjbWwINApUnZljYlHoqY1MmqUVnaUXUrrN2BHiKGUvx_C9iPUTlSc3jREN2zIad0dbX8YmkW7y_VEeSBeAMtcordNBzBDADhXGwIebNgzX0pWnIbC6rKADxygFcAo-qEdJlxTENq28IXY1vEYeMo3tMXUuI-YJ1ByzC_mr4qGSA6COcEw2XUyO9Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3D7_j51YDWtBGwuARfbWIjREIR-P189sCvxcXxeX_SGfAjYMpkdR6IgR4GzaNp7Hyf1p9_KR3TWvCzqeSo7B14lRYU9wZ29OEpd_t2NaXS2FczwrWT8Utuli62iRtQmrD_MG_34lkID18wmTAyGc6bSpNeCWNqdV5PiWd-vxPN2tPXPkgBKYzG4sY3JMSQoqFZpmitfIKwNb3-m8pQEGqDsr64AeQYhb9z0IJ4U3BrzG0xp7RWvKwLWW1QGbQxgpi7K1mMAMw5Lch-dWACzYvGh8R9PsNYzcad9kwHUWeV69w5VkiKWuSjS2qg_uGEzY9UBk1vIt-aCSPc51Per7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXVSnYjgjT6ISIvg9qnCQKH8WAiClogVuaq57lI7NEaOPVNsUElvllni3MACqesdhTgrhR9DLn-o57fviNd6Q2TfQn4y2J4DDLzIiX-LUSxFIvYu1_01qATtRHSyNuQWPiojcMij5Ptmj1v9KWnoIjNAQgJU0INunrocEvsUdN7yUR-MZ2uWbvP5l8_We8jsQdKoTnqB6fxLbKl-c_5GZf_1XBAPCcoM-LtmLmTTYo7lI4vnp_ObTMnk3WSn5KT4RoWzLlGCMVd1zQ6rERAKC9Rau4QtM8RxisWa7Zyzf6ue9IFb2LBV_vp8Q57JRszmiHf1B6KZuIH-ZHyLHQC3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDIPR4agsI_fe3RftXSUAi0uGlH4rmKNcJjL9GZUtv01HQ8weH9WOd-d2AnULr_CT6PmNr3t6W5ytpU0G5OfrRQ4atU3xA0kI-GEChYptaFf_R5-o6J-rXSItivOoLl1kFUHFVAe0Q-lboPJwzPjayhdWxh8H9yZrPNzRI02NZ5oLN1i0wRzedC5zHRQppiWoWITmwosZMhX_y4ufcuAxOdPV03DVNNKl738qiMbHSaB2_kKFs8rRuFccfzNHQckzVfA5iz4hZ7GasIl2uolZDLiyCCXsqOvIN2QthvFzawll6lUKQaNpxbucFNjXyPykq1CYXS_mf7Y_e5uglvPkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=WTR23NjKnGMa-Z8eZza4ABTHxwcFgpPgBfcgCJPDWMQz13AASrhWvaH3hGp3WLyVTJITeW4QzbSukEdM9KzfpgeOJMx7s7rdXbiW0aaiLcXTwlu13PLmJ0UYk_iqpr_OsjmRPOpDyJ-e19DVOVZxRVc7r9bpCWAYUGPIJLUCzjlMJVg6ROoQ2r3xfancMeItWRc9nDB7IrLD0UR171sXmBD3unr4HbPHtxbcOCdUPPihgfPUyviAznKePjeC0FZ6hAWsMT6b_L4gxGSO_s7Smhk_iU9XKZeTPejQ-5o4FOeSszLY5kSLAF2l6S4BAdU_QqQDec_pFFlQruU2hc_42g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=WTR23NjKnGMa-Z8eZza4ABTHxwcFgpPgBfcgCJPDWMQz13AASrhWvaH3hGp3WLyVTJITeW4QzbSukEdM9KzfpgeOJMx7s7rdXbiW0aaiLcXTwlu13PLmJ0UYk_iqpr_OsjmRPOpDyJ-e19DVOVZxRVc7r9bpCWAYUGPIJLUCzjlMJVg6ROoQ2r3xfancMeItWRc9nDB7IrLD0UR171sXmBD3unr4HbPHtxbcOCdUPPihgfPUyviAznKePjeC0FZ6hAWsMT6b_L4gxGSO_s7Smhk_iU9XKZeTPejQ-5o4FOeSszLY5kSLAF2l6S4BAdU_QqQDec_pFFlQruU2hc_42g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL3YIyMpkldSf5PSS3sPzay4T7f4AUbehU1TSLb5dX7axm0PO1puOrADch8KPevwZ6rCJ7jrHc9ji5SrLbnMLnHdtcSfR9QA4p1OjsuXBmnLBp3V315zZvMU6DoRiB-Cbjuc4Fu9UhU5Azkl2pGp6P0r_RN7PEhUDdU4dyYadqxSUSSJ6mgwWwRl6HL8D43VZ7l8HX0qpsX_Yt999S9ks59aCGNMa5F-AQyNjretTzRY8vkMTgY6dA3j_ClS8OEdGF9epLbwGxH0oMH5MoRWZsRBchDoDOfxiGjddB0rniFEJRKoftakxmsLrAWNRS3K8MuYhpvxt8B5mNnyxsc7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1r4AYFGsKFiyzyS7dVBKXOzSqWkzrXVOUgGXvPYHJZBRgqwzC9D3BLbmk-l2DXJvHxAgu8HHwOy-heurNI2GrB6eZkF8A2JVJfy5oNtRxsUK0KUpgQIZdKn33RNvdAWpMs5q4o1TzZbYyHy_cvN1T_rxkCbb83yQwWcIgxew2XumVMjt4yRkVbn-gRqPms4OheJkcnXvET5o_w-FM43M6RMJyxYnQuUSX8-z4uH-pocKT5SgdvqC-1tKVft7NO6Xo6UjbWD3yC_gd63o8RXiuOggYn9NeqLOdPwC1Fz8LfukC8p8SslXA9K2hk4TPrFSq1rKXHwKBoWTz1UsYFVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OclPXocKgsKMIZIpaPvocz3jmdDm6acQUQ-ueTcp4Zvx78o-c56QYxG-7ii8bUf10hv_fD4S7podMnefjy5c00FpOMk0oTBogkIAHY3EWS9BceL6VYKjZU8YlIKlCvMf2bBm40jqiW1xpJPZfZi7-TNznZRH3hpEZsgRpqJYO1yZ8j6r2M7UCT0sWeBBm-yyyWT_tf68FkSoRNUl6YqBmi_SE9Fmt96mgLPpkQQQInFZwRSma1a8txpCmMZmgdRybkrEuHpXtC-RgiTcutaeytltqRfz2mWhgLwZHzPJt_JAa4fEEwqxecyD7Mkt5Q9L9f1tw6v_84omMPKC6_bmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Ga030Jr6eDDFBqM8zGCqOo2cX6sor7qVT1Fg2JUbNdK1aFM1iURGtFWvy-eL1JswM76a8QDt-oLptD-Xi-w-2G5px-8bhSyC0N8WK2xt162b0JDG4d_OJqy8u3jlUBoIIwSh2bPXo5QVlt4qmqVX5TnYGgm1V7sR2k-pa8JTQTs0p8lLIWdfefJqTg8nIYx8hkZNN7tPdydvHJtIuCXknewFlXbGlzUgQr37uU6jeicYG4hnVIrg_6VZRufQRSPaeXm7tOEMGNk7-kDqlYMR1PbVpOHDTKo00hVdfrxgVQmYXobVccDAXHLl4LsGOZWB6rLsrqEy8Xr1UJ1YXpug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=e3KZ4-fW7SFrXGV00x4BPc8YFf_O1rcEQiByHNJpoQ2E5OW57B6gX96fkABTPWGO3kXkREEmK-h-0BmFaxHaoy0NpVIvgkI0CR3Go1pBAil77gmQkAnQqjOe7k4ni_6qtdAgTKAkdhIzpZdtyfpF50FLKJQl4oUsJPT2M6qt-mvhn0b91pq6ZDc0zNj7-Q2BuNakqS0jLriZZqnrfH2XkLKPRrTYvnen0tOb6Z-s-0NqfRzaK5ieSAD023JZTpBCoImFfORxfAfbwYc-vVLBzM7nj5kq6b2Gxbghbjny49yjOLX26P-CTf4qvISA0BJDW_occSSNOPS-ACK-Ju48Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=e3KZ4-fW7SFrXGV00x4BPc8YFf_O1rcEQiByHNJpoQ2E5OW57B6gX96fkABTPWGO3kXkREEmK-h-0BmFaxHaoy0NpVIvgkI0CR3Go1pBAil77gmQkAnQqjOe7k4ni_6qtdAgTKAkdhIzpZdtyfpF50FLKJQl4oUsJPT2M6qt-mvhn0b91pq6ZDc0zNj7-Q2BuNakqS0jLriZZqnrfH2XkLKPRrTYvnen0tOb6Z-s-0NqfRzaK5ieSAD023JZTpBCoImFfORxfAfbwYc-vVLBzM7nj5kq6b2Gxbghbjny49yjOLX26P-CTf4qvISA0BJDW_occSSNOPS-ACK-Ju48Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM8fz-zqe1BUkglkNi_g3f27MJGIF7Khcs9xDeOmpchn9vmWrHO4eKFQXJ_InyGUJ--vF7bCQiRRzUxeQyDtYS-mFEjk2PARqucBsfGSHWHHAed_hMxAvqgHSCm5Gs4-egHoOxKzimu8esmg8SrgjLXCL6LUGfBagMlpDtzW5Gwt5k-g4P0EbhrFIwLoaFerI5zr5qlZ3AtuUrpL4bfKAUCqhgaYf_7zbLabBi3pebpXYeopXomAbdVf-R9R168TE7Z4c3ituktg3y40AahXnBze7pTl7rG4ljYYS50Eg1wIJ0esTubprrPoS0EqborF_Mq-5dx3t0F79bE7HjBV_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l36zdjmEa05QgJaaDp4_J7KzwANs4Dy4MnXiVh6vbdzFJLku4fA0HfDJCdIsURi_PaMdehW7khEO701UjuFIIGqaXptXSC5Xp93HqUW9SBQSUGR6WC471oeIl-DmWMbiYtQLZb2zBs7fV2NGjN61rdw_fF7GA-a7z86qLxAtc3PCDNSlmrp29Q_LJwuv7z6shEPRUdTFZC7otp8543nniXMo69ffciIbv9S83p6T91aCNzM2BkqVhLxY_FfjT8m9ceRkDxuZ5Yvp1sjvqaT_H-O97XHvI6A1t6efKx9gdLVIc6aiJaaICI0m78hh4mVVuMdJHluW5cTVdTXDEddnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=vhjyD8HqRuBB_21wTHYytK4bLGEB3CbFs0kb0lGPrMhPeyvULZV-mZbO7k60ce2Jy3KwFoXXsnWDsGTJU5Czz26OgKb9GUX2H5oBeO2iST0E6iDbPp9s6P2YuaUY5K_nmIO78whj_4TOsHOQiIJ2ccPl9qpEVdD5bHMg3zL33Q8-_5IcsuHf47Fub8QijztltlOkUYew8BJiQepJujhfD8DPSkOTjvVvp9TiBnS8iF-rFvXbYhGt5D5y_IWoC5IWQAXckTudwk8v0j-nrWCBRaGl2XN2qwU2TZ1_jhbVUbrhMD9edC89yAaa59jLwrXyztAqR2h2iQA-w_N0nkm8ZJ6IUEJGXF1GfUJ7pxeZBAUmGJEy8HImtZqMxG9dp8TVVcrSuDg-kBlDKQAciC5aPHDQThIKrIaHj9-gTOGjgiMiLGKPn554gXe-Mu8Flpl283vfoMDN08slNuwuh_RS-1DvVnTAUVzJRGGDfnJbYJI7_veWSE3acd-xdBd9_rgT7vASRjMtDZAUN1HZXZT7TNQZWW4Y37O4orJBYsqVJsoMMig7Hx7eh-cdInhQ7CCasDTY60yN804zy_3km9zKTd6g7_bSu07uxE832_fseyd9y_HcKvZJrWYKgIbxuTCKRrP2JQ4t24TMbvORYyriO-uO3PNjkwTxZhdYAVcr498" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=vhjyD8HqRuBB_21wTHYytK4bLGEB3CbFs0kb0lGPrMhPeyvULZV-mZbO7k60ce2Jy3KwFoXXsnWDsGTJU5Czz26OgKb9GUX2H5oBeO2iST0E6iDbPp9s6P2YuaUY5K_nmIO78whj_4TOsHOQiIJ2ccPl9qpEVdD5bHMg3zL33Q8-_5IcsuHf47Fub8QijztltlOkUYew8BJiQepJujhfD8DPSkOTjvVvp9TiBnS8iF-rFvXbYhGt5D5y_IWoC5IWQAXckTudwk8v0j-nrWCBRaGl2XN2qwU2TZ1_jhbVUbrhMD9edC89yAaa59jLwrXyztAqR2h2iQA-w_N0nkm8ZJ6IUEJGXF1GfUJ7pxeZBAUmGJEy8HImtZqMxG9dp8TVVcrSuDg-kBlDKQAciC5aPHDQThIKrIaHj9-gTOGjgiMiLGKPn554gXe-Mu8Flpl283vfoMDN08slNuwuh_RS-1DvVnTAUVzJRGGDfnJbYJI7_veWSE3acd-xdBd9_rgT7vASRjMtDZAUN1HZXZT7TNQZWW4Y37O4orJBYsqVJsoMMig7Hx7eh-cdInhQ7CCasDTY60yN804zy_3km9zKTd6g7_bSu07uxE832_fseyd9y_HcKvZJrWYKgIbxuTCKRrP2JQ4t24TMbvORYyriO-uO3PNjkwTxZhdYAVcr498" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=S8caYlu89JdAGcSdipPpQjvVhJXWHWwnlKCncvT5DU-zRw80QrGAUxs4-bwkxnw2MrJn4ow_7kWdFz9IURrCjCGpaSfHrCCsKx7T4_jRHu2vUWJOvan4sF8fANbBwBgeMfqcAQrR2nEiJn1mr1xfxgx4O6gV_pWqdifM3ITkMHoqcRiFVi1GvmJsJuNaOfO7LQUh5Wy1bw1gOG_ghpzXWCmfOnKhayo5HcBRMmEuiFG2h_38e2ryjF69dicjdVZci3E12_4oB3QSnVk8aBp7FWaKj8mUxOsbg01wSD6zlNJjsgenG4vQY1wzbMG6sNw5iUaPJGDD8NpJdaqqYG5orA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=S8caYlu89JdAGcSdipPpQjvVhJXWHWwnlKCncvT5DU-zRw80QrGAUxs4-bwkxnw2MrJn4ow_7kWdFz9IURrCjCGpaSfHrCCsKx7T4_jRHu2vUWJOvan4sF8fANbBwBgeMfqcAQrR2nEiJn1mr1xfxgx4O6gV_pWqdifM3ITkMHoqcRiFVi1GvmJsJuNaOfO7LQUh5Wy1bw1gOG_ghpzXWCmfOnKhayo5HcBRMmEuiFG2h_38e2ryjF69dicjdVZci3E12_4oB3QSnVk8aBp7FWaKj8mUxOsbg01wSD6zlNJjsgenG4vQY1wzbMG6sNw5iUaPJGDD8NpJdaqqYG5orA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0ZI9RFbmQf7ewyDfj3fa-4fVCeU91rl3-koNSjn6T-hnMGIfDysk_Bt1WdFideKR30X4OOxuwDqbIv-GswjupyE7XA0x40ILFx8du1XHEXkrxWJyQIoCsMI2ezJM8OXnncfiennTCejYQv71YkLoC_k1Y9rdL7OebzBw5UKCOrEW401aHor9ImEZz5a9JniY81d3kIXMrUfbqtZT91du4m61T44lgV-Y_7Rz_mmVPojroYeftHoYwIKFUQ-DtBnmnXgWrjC5lhDV68iKfpBZug10xqZWQ8R69vr3skAjrrrRGizLWNKY4vaE4vOUe5Zug9vZy9fUHAkDJR1Ah_SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=NxXKt23fVghfQ3ldeYy1lMcm2Du6ckMA-AxJZflZ7kg7eVuDnqxVY27J-1IKtnxmEmpmJI5mJlfAXZZc7BFJU1Hp3GrRBlCgETa8eyoH60-2RXA2ZgCUX6CF794BDhIvrdbdYo0bem3_OtMGXMyDMpIiuj4jFRGrnwyE4tthnsiDzAbupLADO9bbOL6Z9OBUJNCo-Q8BsyAI9_XIYCYVBbz5NmfxPcLdpjeSzaOh3N0fXfrqh6GC6pyeoR0pESMhdAXxpFUPTBi0-q92SJfqaZ9_zT6UjTDwkzHuIduZ4DNjQ2RM6yMwlRtSTsjCLqEsAUfmmJ9tCGOCNXE0I4a-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=NxXKt23fVghfQ3ldeYy1lMcm2Du6ckMA-AxJZflZ7kg7eVuDnqxVY27J-1IKtnxmEmpmJI5mJlfAXZZc7BFJU1Hp3GrRBlCgETa8eyoH60-2RXA2ZgCUX6CF794BDhIvrdbdYo0bem3_OtMGXMyDMpIiuj4jFRGrnwyE4tthnsiDzAbupLADO9bbOL6Z9OBUJNCo-Q8BsyAI9_XIYCYVBbz5NmfxPcLdpjeSzaOh3N0fXfrqh6GC6pyeoR0pESMhdAXxpFUPTBi0-q92SJfqaZ9_zT6UjTDwkzHuIduZ4DNjQ2RM6yMwlRtSTsjCLqEsAUfmmJ9tCGOCNXE0I4a-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6nq02hr7xYl1BKKkvHlOzT71zhIz3x270kRb-lHfri33dzlWeCXEAgpWr-K9Q49MNk5NGH_tunkFpBaC7Re2b5zVUA00N5KkYjMwHeuicwDgSnl1IMYLfUDOhXdu4lS53i8vaU8nQ_MJ2bDiMfWHDztbUkcg_nrTI4IRJUlqBL0l8f8-quedVyULmCGjkumCjfrFUglxrSc214rHpf3BsMNl728JIu7ah1vHuHxX6ILUbJCNUnca4i6OgDZrDMJMHncjDlcoReD5WsRy-2Hu_HSupntFeQ99S8rPuqj3sERfrAEw3RWwxsell_-s7stQazKsR56SgGJ7ZtAMSZU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=fmWWBTbnQcmQ_pESjwJEwD4gfvmRShHPM-s38s3T-vr1Mhl4fJ14DLEal2BiYV-0owcjaM_alwWSP3LgCzX_oUX_8Ltr4Q01CVlUDmojn1FN6iWdEqq8GLdF8mU-BaYdRI-FpKlGL1AV957KPKkUW1b2za5QSJEb4JNNeKixIaIZ1PZC27MWaNBXcZjBboYvdiRf9bER3ePB33fzCdddJ3AGM_rNn1UHUjxPkLYxhlWu7QMbAgYsnjAH7v-zZmBIZRXM0HW8zUvCv0eFp4-a07a-2eyUJmqBZ0bBExuGPPKq7rhmK68X0qEU5_bk1kzWMyfVc3h7XGl5HIBSAV2JzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=fmWWBTbnQcmQ_pESjwJEwD4gfvmRShHPM-s38s3T-vr1Mhl4fJ14DLEal2BiYV-0owcjaM_alwWSP3LgCzX_oUX_8Ltr4Q01CVlUDmojn1FN6iWdEqq8GLdF8mU-BaYdRI-FpKlGL1AV957KPKkUW1b2za5QSJEb4JNNeKixIaIZ1PZC27MWaNBXcZjBboYvdiRf9bER3ePB33fzCdddJ3AGM_rNn1UHUjxPkLYxhlWu7QMbAgYsnjAH7v-zZmBIZRXM0HW8zUvCv0eFp4-a07a-2eyUJmqBZ0bBExuGPPKq7rhmK68X0qEU5_bk1kzWMyfVc3h7XGl5HIBSAV2JzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=VijLlvIPyyChzFECPSPIC4yrx4c_80eZW8_jQRpOBicFe5bHNzC4VqUQ4YVhsVY3n-GpoDHnYwkuMHzvtiaDfeDuH0mzw7DdOKBkfRU6RGC3fiQQW9Hy-HzJ29xFFkVfI115lg4P_wMeg23Nm_kJyBnrFVXO8zpWBARHvU7ezd0M358Y1DZOxj9t99xie3erfWjIoGXxKwd785CiFfXp0OFKDoW1EC1hokMLRvoFlKMkyJyFTaDsjUboL63aCUgJ-yubgQJuvlfoxCn2R2vOyS2P4bkbEbUG8cSz5HfFnHxu9tq1gsSm_mCG4XUyixsZLqzPRXZy0fKBWx8Eih47XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=VijLlvIPyyChzFECPSPIC4yrx4c_80eZW8_jQRpOBicFe5bHNzC4VqUQ4YVhsVY3n-GpoDHnYwkuMHzvtiaDfeDuH0mzw7DdOKBkfRU6RGC3fiQQW9Hy-HzJ29xFFkVfI115lg4P_wMeg23Nm_kJyBnrFVXO8zpWBARHvU7ezd0M358Y1DZOxj9t99xie3erfWjIoGXxKwd785CiFfXp0OFKDoW1EC1hokMLRvoFlKMkyJyFTaDsjUboL63aCUgJ-yubgQJuvlfoxCn2R2vOyS2P4bkbEbUG8cSz5HfFnHxu9tq1gsSm_mCG4XUyixsZLqzPRXZy0fKBWx8Eih47XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KltkStWgUJENchaw2EJST1PXMsZSFQrjp2G9ZGFhKdu3_LiskJajAevSrg2OZos1C6yIrIrHOMuLfv-dTeYx0stysjLre0f1yBRiAFCf6x44vygNYg8IzurIyt4NNL0AWLa_kv7uu1lOI1T2jjjGYdZjtevvFMC9guKxI8CPfE5VuD4GHb8mbxDVvi-LhtNFc5QjFWLDVZORTwSU9Fz4VWDm59AmaCRP15yJ9ZpzDSj2XCesQwMfrO8mh2dPzEj2zTrMh2frydwFKUKWuv524Lvn91cybMX39SOeQ1xdwyp5vPZou5PCwFvW32WLyWZzceu3VxhPZebllMHrTyiO4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=lVM2hF6VpDtCLXHmnn2IhaTICXppln0yIR-cQxhSWmgamgqIJQnF6FY_bRQPkxzVmCBTAxyl8lmkkWybUFEAdqiG_CgfAHQ89X0Tt8BcxmpM_WwNJgQTNZe987xXb1dcVFQ4uBYWQSrFduuOk5SOcjecp5-EcLaaJif1PThluuBkRXYDDwfrhhKpyaQ9AlvHGkwi88F1_7AasodNZIOnfnxUb59HENDnKEiv-NYjsg1dI-FWvkgSnVBmXJnb42F8ay6tDvtEehiC50ikWFCOQYQ8q6yZjmL5ypVubqe1B3gxLL8-PPOKAYzSWDILTo7YSyVRTUZFrh-Jrm3FV6YwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=lVM2hF6VpDtCLXHmnn2IhaTICXppln0yIR-cQxhSWmgamgqIJQnF6FY_bRQPkxzVmCBTAxyl8lmkkWybUFEAdqiG_CgfAHQ89X0Tt8BcxmpM_WwNJgQTNZe987xXb1dcVFQ4uBYWQSrFduuOk5SOcjecp5-EcLaaJif1PThluuBkRXYDDwfrhhKpyaQ9AlvHGkwi88F1_7AasodNZIOnfnxUb59HENDnKEiv-NYjsg1dI-FWvkgSnVBmXJnb42F8ay6tDvtEehiC50ikWFCOQYQ8q6yZjmL5ypVubqe1B3gxLL8-PPOKAYzSWDILTo7YSyVRTUZFrh-Jrm3FV6YwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGNJFMlBhhXQJDHcyTr8DuYCD7cV4ZMu7G-TIX4_Q46w1day3bLfLErd7m8GlE5pqsORRP8je5l_CA4TbfILknvVUCoVJEm2wILY9ia0hiATv8Xiy0JjhLe7D9vEAs7BbrtNwHU2KEzwEnM3rL-Xp1xROsA1Idgb5MSdqlYZh092GJUfkgKLBJlXFePbKKxhRb7iOoQfOKc9F1i-J2MGuVQ7AqMkYvJrl-Ddkp7tlTH38DOw1T8ERjUJADZFZEub7ajpxpxIPwqvkCoP1QODYox7NBNZBozVxIKQsbI-26VjEfqZuK3C2bm01kmXlMUrpnIKqCUgPtz2ZVAYvdcjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkXJmIa_EU-kSOLXhxniSyn1EokCtmFJ-WVSap9CPHuDtjY6AaQP1M6B_Ojs0x5oq9XrjKMetF3_CrcsdYtR40OMKjqOhYDloy6pnXRPap1OukzriFIBaubnBNZjr_sjQKpcLh6kzZxLDnDc3r3Qma6NsWlCOioafsI8iZSD9rfeqEfBq1qtqd-zOS8uhuLFUP_Nk5Iyqgl3F1i2QZFgk7i0GHiKLcbPUvrvF4Mg6mDOXJYjdBQlQll6FiZplVEcYS7Llqr_d_ky7AKqD9hdeYPoo_FDXi4eezcNysKJz6fRlvvMrT5Vmau-RtcBjWuoCLP4iFzGR2qRXGFZCUdrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFYYpo6LG4986mgCs2ryqsHzeBuDYmP7xFAU23EtFbz4KT4wYquGfClNLosmTjvQJRCTJhzLfm7DyHJKB11vk2UmcwA4tvWimAS3AtT3XMq9iYCEAwou0OJu3MUaajZ4sdAxR67SWSwP-kEjDXi8wIGdqaNc0_Yje9ZFZmBNpoulue3DTF7uTvygBqZIpJRdT28zs2aac0txTrEV1zRb8RT4rjPiZLJQisoDDT5Ztc0zHyKDAsTX6jn8xx6mTFbb66Wqy6x54JzUoRYg9QnA94v-yTkQQJEOri_DtXz2rtWO8Sjp3_EZhKkk0RHSg2JNn-WJ4Q0iZBCfPM_2eIs-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1FpXdNfHllMNpeuGpZ2ffKa1MLMhN6g969dFzgdBw2NM4ttCM-_N2--HaSL3JT1wMwbKaYMlxelD7Am-xnmFWq2vpBpXrdUytu054uyQ4TxBjjUAHOhanu_b7yAtjadGXbB9EGlULFcZwcg4DTaDmb2sFfgfJNLj624NVeCKv5GTzWyGzExds9TwRm9gptO_jqZQDfpeg7wPTe0MOZ8nHR6o1Zn3WfFuFH-Ji3iQQd1ZBtP_Em308EnFwxzB3h4OBUNn2ZGcC8wOi3ENcwxXX7O90l4wmIKvP3EtBOsqtbmW0idIk-FneCCaEeIjHsLqUxK7BbG2GYhfVLwaJbZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkqNeLzIH1UtjzTiXMXWphKs75zA0sHYJdT46-pG42r9QzARGca7UEunRrn7ySnYvDw9YynMqJrSPBYsDzSqny7CdEe1rDEB0jk32EPiOPBE_OzbZKp_nqkJQJmWOmDJC3Q6U6xgzpJWvNP_z0CyCofC_wyozLWHPzJs1sThP8cx1LaZ84_mmnTylAsDEGcQBNVL98kwUhlgQTIuoYZHaIEBskf1uz5KdT0fFXZmXUU7h7DhgNkBwEK9XKB1AkwQE4mS4TH1k2Ff2rdT-d4QUzOYeAqTwVDXEq21kQCel0cbOnEpL-HMm9EANHFZ-dBfhHkOn29U0pLFC-zLDY3eCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcKXdAP5v4I1DwhuKIsr216rX10QOWK_2PQJ-wzUMOnphWkMVZOdvY6zVR5qULO-k68FuYTA5IipjCRGhd2e7oRz3CFkJaCgPg6yRXLF8vh6Ye6Xbthhh8lAGrQvF8PdBovF2_dAAbW77IqnhJcKciOY75LXUW46fGynLYLngq9Ki01RB41_dp-uHsRzLB8qA0Pt-CEfoUXVyrLyqc-vvPrI_ghjyuU5nSunaGPtHI4cfpaaefVy1VPn6PjgaHUB8pI9z5rQSyaiJYif-ZPMCGL8Nn6UAmkz32DIiggAKXuUfWJPMKm2QIyJ_4n4R4zskovBhNmySgIV1iyfuJ4T-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=Jt0NbdwPRdjF0q4eVSCbP0NP-vcOsldjVomfW2ez4oGhZsJznyQA8Y0Y5FthOaQRmjBajIVsRMKZA68HCSlGSkmITStrYKM4gyDS1vvr8rJDJc6sbNd8PgKShlT5H1fHp1qS9n0Ai4i3oSM8Ht4AvNtvwiAG32d9S2jA5-quOSaxsya06ARqyTIo0p9--1msoXryX__MQgX3oOxOu_AQ1QuCpE_L51YQSIsuGVEOPZEy2q9UBGQUAaJQvCUTTEAvpmn1y5_I67FdyoxwTq0IS7CQIBPzxttg6VgkDTzCvA2Zbw8PNROSqIxlJx_qTtrXhAT5v8bMpX10SVx8Jil-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=Jt0NbdwPRdjF0q4eVSCbP0NP-vcOsldjVomfW2ez4oGhZsJznyQA8Y0Y5FthOaQRmjBajIVsRMKZA68HCSlGSkmITStrYKM4gyDS1vvr8rJDJc6sbNd8PgKShlT5H1fHp1qS9n0Ai4i3oSM8Ht4AvNtvwiAG32d9S2jA5-quOSaxsya06ARqyTIo0p9--1msoXryX__MQgX3oOxOu_AQ1QuCpE_L51YQSIsuGVEOPZEy2q9UBGQUAaJQvCUTTEAvpmn1y5_I67FdyoxwTq0IS7CQIBPzxttg6VgkDTzCvA2Zbw8PNROSqIxlJx_qTtrXhAT5v8bMpX10SVx8Jil-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEd3aY7c-eii7fOqzsSA6lfNOZarfoXMILh2IhRMR1zIofx6jhgiePUW54I0nIcBKowV5w8ZL9-gcDhh5NARWnXUdtE5w6Rl7jsfdWjECK12oiRaTUqleeNNM4x-8m_W7zhlJ8-at27AScLao7o7BtAbxFzfM_01GqslptN03Gkr-yy1H-I5q2U4rO4O6wMI_3rdkj9Hh1-IP-Um_IGkQjv0ZItippptd_cUAMeo1_D7dILZ2awui300t46JNdeLLgQJ2foKIoV1DXHaU5aXV3TvlF1QCwSo-1UoQi1MY27lPr-YLZ8JiQgfT3Xj0xukAOq5w8GZr6N5jl9GPJZ_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPIzqJKn1WfkS6G4N_HMctu0HGg6M-rMwaGtm3p8s3yhKKZDxu9wCDfch47H0TZs5M3svPbhZyyF_t9hqnnJQPmfi8LNBYSGJFlS_6JhlachZFUSzs8yFIGzh6lK9f0N18YVnN4QcFzk922hicIsW4QnrNuHAMBuiFEwn2X8wZio3oQi5WxXtVwGkeEv8-xifg1291YBOjSGL8tMh4zy2y0hq06aw_LlvDPy_Hzb-Jw5vDkGlPO6CcIIK8Ju6dq5fEK3DYawF6amDPBAtzMSCs-Wn5w4qJltrMqsqPIc5mqKw_9om7OK4243CJeLSKTtY6HZFqa1_vMwhsMcS9PlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
