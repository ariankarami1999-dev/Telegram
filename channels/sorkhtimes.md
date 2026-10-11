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
<img src="https://cdn4.telesco.pe/file/KYGBn2ju5zM-6h5jXh0lXD1ijRVRY9OctGDLVnilMnYSYCf5Z9T4bXn0EXdkcq45qTnqb6ypvv1_-p5FjMQgJ-D7Xcv-iV61wAmnEk-U-BEIvLD2qkeDJ5ozTZe4P2_cp48UtPKY955xZQV4GaSUUfFM4lHlKjSh-RNaq6xqwL2ru5xdlJL8WH38vqa27aEkcM0XbQ7SjjLwl8jyakkV3n0QsjLdgkuZcYVYL06ATDg31CBI79953OlK8c1cge2i4VSpC1375tocI4_UnCyLVw8B9NN7xEv6GiBYDRp4WV5xIurBjsqubJclIpOO-FOndzjHifyFc1pL7WAFvLbe9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 01:40:53</div>
<hr>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5DjvjXiBF8aa3TDEGgZSp09CWHNHsUe6-2ZB4dk2xdsEbeYIcfaLYwc_PDs2TPDGV6bTaTOdHeAy_LalXe-hjUOAhbp8y15nkr7AVE5LtBWicX9bhisMbkPsfjzAtNn0ZvaaoSsWO4R0xLnWqEJac7-bWtt9ednXiSqVWw7JLSga6YHFNphSy-iekJsZT-vLtlsbF_l8us-_2wwv7odhg9pIlric4mjXCN6uB_BmiIiKHSSDceyMzDd6Zh_vBH3NnHWq6BdhLMziVEuftZJMCKcQ8y5syw_51U_iK-l9FW1TO89VTTePhz8_Q_PeamWx__yZZFeeBJ6i3ZF-lPSTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[
تراکتور
🔴
🆚
🔴
الشمال
]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط حمله خطرناکی دارد؛ اما میانگین ۱.۶۷ گل خورده نشان می‌دهد در فاز دفاعی آسیب‌پذیر است. تقابل قدرت هجومی الشمال با ساختار دفاعی تراکتور، کلید بازی خواهد بود؛ تراکتور شانس خوبی برای کسب امتیاز دارد، اما غافلگیری در ضدحملات دور از انتظار نیست.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 531 · <a href="https://t.me/SorkhTimes/141327" target="_blank">📅 01:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/141326" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAvERf5Ak9nfHWkJRfroxPAmPNfIDlh-kAd16JRD702EM_sdStY2GZG0NgCZyWHHEJr6IP1U1rrSOmDHKrjYns_HQH6sbmmGK6KhG32ai7gsiLcCXr-8oeAOeP5-Pkkixm7SfugFfI3JA3yGUvF7n6pVUETnYr88j-x28xk05mIGlLJdcE30Bl5ixs3SWbuVOV4RpmNpw2UtVKOdIaK3mMCq090ZNEkmRMg_L0A6uAHe6nc8flfy3Z0-_TWkCQQ9WwF52nozafwFyQtdiCftzZar58ENGUZ4oF9Rb_hfha2RI2H339un839wmWsuOAxHGAzYT_Ua2ghT8GESQ4EUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
واکنش علی بازگشا به شایعاتی که برای برهم زدن آرامش تیم ساخته شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/141325" target="_blank">📅 00:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=ecZQPtKtJQyFcTwH2H4pJg5KDx-ggfZulCeviSb_FnyfV4WaClneSQ4aeifSKj9F-S6F92cAiJ_mfsaP9kJ3w_55OwzxlHAjPi7LF4b8HyTBPrPO1BEEbsFkttM02Sya2MVzqJyT4YBhjnYnS8GtNqmVo8rRIxxrjnox7poTkVHWNCHFrbZXa8lhciUcq9neBSF-CD__fZQ3w3s5P2BDRXtdNKV_7negtQIv_0KmHE8J05F14LNMBYZwD87uMpCYZKV3D7p-eFHArKxtqvDO-LUdVQlqy8AllXoD5PGzX727AOIc9oeN6aST1BZOJZWdGaNb1kFGoBjbAZMWX58HKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6166ade5b.mp4?token=ecZQPtKtJQyFcTwH2H4pJg5KDx-ggfZulCeviSb_FnyfV4WaClneSQ4aeifSKj9F-S6F92cAiJ_mfsaP9kJ3w_55OwzxlHAjPi7LF4b8HyTBPrPO1BEEbsFkttM02Sya2MVzqJyT4YBhjnYnS8GtNqmVo8rRIxxrjnox7poTkVHWNCHFrbZXa8lhciUcq9neBSF-CD__fZQ3w3s5P2BDRXtdNKV_7negtQIv_0KmHE8J05F14LNMBYZwD87uMpCYZKV3D7p-eFHArKxtqvDO-LUdVQlqy8AllXoD5PGzX727AOIc9oeN6aST1BZOJZWdGaNb1kFGoBjbAZMWX58HKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/141324" target="_blank">📅 22:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
پشمااااااااااااااتون بریزه
‼️
🚨
🚨
🚨
با دستور مسعود پزشکیان رییس جمهور جمهوری اسلامی هواپیمایی مخصوص رییس جمهور برای سفر مستقیم استقلال به دوحه در اختیار تیم استقلال تهران قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/141323" target="_blank">📅 22:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=rA98G5ip5zO0MgfC89vlvXdkHPAF6zsUAOSiEPW8yCVUAad0atnqGNZzbp-ckd-SYE-5Mk9E7i9ayX2rkvLSLNHMxDunKnFHcKC6EAXYztJrHsXTfwE-z5tpAhRci4z1y2YzhZ5GxVkGLkdWqV3Zo_MhusrJL6-vkyTA4P16HryF-tFtD--wKyn6xvrBDbNuHxF_ZES-8ueyM49Em9pFIH7Ude0KW_5Z-YbXGJLJ39guFg2x2evC0oEzaeugk80mrxXW3Ic-eDof2E_Xc8YQoDrdZmmyXL1JDZpl2MpmJ2LJ50xV0oQxsmRunaylq_6n3CxYKQX7eVVkVIdbgVcyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=rA98G5ip5zO0MgfC89vlvXdkHPAF6zsUAOSiEPW8yCVUAad0atnqGNZzbp-ckd-SYE-5Mk9E7i9ayX2rkvLSLNHMxDunKnFHcKC6EAXYztJrHsXTfwE-z5tpAhRci4z1y2YzhZ5GxVkGLkdWqV3Zo_MhusrJL6-vkyTA4P16HryF-tFtD--wKyn6xvrBDbNuHxF_ZES-8ueyM49Em9pFIH7Ude0KW_5Z-YbXGJLJ39guFg2x2evC0oEzaeugk80mrxXW3Ic-eDof2E_Xc8YQoDrdZmmyXL1JDZpl2MpmJ2LJ50xV0oQxsmRunaylq_6n3CxYKQX7eVVkVIdbgVcyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/141322" target="_blank">📅 22:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvR_kEK101sbW5CFdlW-WzXOY5npkfukyB2Gz8bXST73Wv5h2cQVxWyFK26vdOFIf9O0g4m0csSy-hp-0UWZ4Fv5aqHtw9KlsPwSbaNaKZOX3mWa-WhztjUivOrIBLJgtxf3NGRK94caZcK71I90X_94g0CPkzXE7mnUgJNl1JPVBl_E67JYc0Voc1KnWQLOIaEDBdRNRWukLQL4oH5VzAvem3lisly_O4gVokBY1oi1atCEggsRLRDy2tt9yv4It-HZMBm1BNNQfXzO32WlOG1dRHW_NNcixIgJbmku8U4F4bP9vIAWBwAcZlAvoHEHxY6KonpYcH6YN7QwQ-x5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دانیال ایری از بعد بازی با خیبر در دسترس کادرفنی پرسپولیس خواهد بود/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/141321" target="_blank">📅 22:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp0UB6jW4Nbq9xGLkulA8JVHzjY6YEyH4zjIB_K1pZw9zHQX2e-rfyemXlLlRSOcNPtiV5HQF5LudchKxWILtFzr6TlEqu2qk0gxAMaKuMw952FdYN6DY_c03GNu9tukdozqYHM5BZWMQ0IvYkCVOk5cfVbw6onYV2sUP8Tc5mQeTJS1BKK_5EK3jTn6J1MNk0VFnhIZ02Zies5PQ9RCoQKRJqIugeJgMnu_t-Z9-p34Ay3jlyBN-KzD4tXHhwyc8vteYVEzkPSEGGk0F1o2-syAvbajWYUiKNYGE3NLvgKhHUlPhQu0hAfuJ3I9r8178JsXRbWc-S7v6LsVR_eR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/141320" target="_blank">📅 22:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDjKsAgHDpp6R-KwHSiLBbhYipI1pr_E-Dm_3t9CxmSFWRqxFREUfdbF9qPK8xGhVdo-hUfegkiBIIyDeOoMebKVzTf4q0cOElEqXABnd2k6mvEv9JPUZAZiPqm2e3plpBnRtKaMmkYXX1J49XELjbu1gk2C-GVh3jJ3X1Oh6QsrVkuS2rgJRmU-_RyZPooiQ3johaR_QDtcHgAjpfxK_LKQD3ZVUMZ1lZADMnKvWq0mLx0Nhy8xNufpNAGcorHRlB4uV9OQ5V3LxxYyqkNBYpiXPqomxUZCCyB4iRekdSy7C3Ag4t9R8FfDC8jem3vdZVaZlswTMMFIF97SgftQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
فوتبالی: تارتار قصد دارد پست دنیل گرا را تغییر دهد و از او در پست هافبک تدافعی استفاده کند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/141319" target="_blank">📅 22:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
باشگاه انقلاب تهران به دلیل بی حجابی تعطیل شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/141318" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qptULSh6VybIhN0KkdE7Q1F6CELnXDgEfAqnz_P13HqALsvqLbcZ1Fqi4zD1qK322vxKJu8Dir0KReJq9GMRL6RDPkcu6sWwTpprxFsNzP2eQ9dVOfENRp-JVJiJLtGxIVAboQL_2OqsjbXzqUrOFwTg51b1OgvlGV5kde0Lmqt688KVmMJGOPyfpShjvGuxO-eOLvpgRteHYI3siE63C0PP3hdbOnXnCau6vUnpr-ceRM9DLiMzTOCo6qRo0CD4BlbMQY1uM6AcwIM51nYenfqxGs6oU4STS61u5tUB-K_jvRVkAalDEdXqbRr710ZPHC_caLlvgdxkC2R05MxAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیانکونری در کمین ۳ امتیاز؛ کالیاری سدِ راه بانوی پیر!
🔥
⚡️
[
کالیاری
🔴
🆚
⚫️
یوونتوس
]
⚽️
یوونتوس از نظر کیفیت فردی و تجربه، دست بالاتر را دارد؛ اما کالیاری در خانه می‌تواند با پرس و ضدحملات دردسرساز شود. کلید بازی برای یووه، شکستن دفاع فشرده حریف و استفاده از موقعیت‌های ابتدایی است؛ هرچه بازی طولانی‌تر بدون گل بماند، فشار بیشتر می‌شود.
سناریوی محتمل: برتری یوونتوس در مالکیت و موقعیت‌سازی، با احتمال بردی نزدیک و کم‌گل.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/141317" target="_blank">📅 20:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری
✨
میلاد محمدی در لیست مازاد تیم‌ بلاروسی قرار گرفته است و به زودی از این تیم جدا خواهد‌شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141316" target="_blank">📅 19:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9yd7hoqnwSqri5dIPryumfqArcg7sbhyusFlrqHKhxD2LkIikiyLbnfDIWTPn1MbhU4T97qFrwbExi3Vgwkr5AMK43NJFMpyDQziJox36ivUcNwvsL1jxl1daAmsTcCBXUjrPQOD2w6eChcyvGcmJFfUzJKFv6nbIHTP1gun6Jk8myt0mPQVClziLXHJjTJYuYkEwKWP1kQv0mQnkjdR5fLVs6EdJC1FaxT-7Z11xokjI1DT0HU-0a-I5TIFQBKaHeAI9Uxh1uEm_q2hBJJGMtH5oS6O0jt_LHHFYtFIinGcvElg1NNdjq2RtSaTb5fR8meWEznTcwENIRyyp_cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر فاصله دارن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141315" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
پرسپولیس بزودی اقدامات نهایی خود را برای جذب عباس کهریزی انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/141314" target="_blank">📅 18:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYjiTV4uEha2TfpFYJP4BxLzOVIq7j_gFOYjcD8m2UKeCgl02orBIS0td2wWZApJPegRmSlbZnfQdpjiJXBZF7SCTRjw9iVNmQFygVWtC-O-r2Q3KtJhtlQQX0YrPkQnhKohAIBJhegqLmtnYWUdGkw1afmqaZMwGdYH5QZ-mbyGUkMh4wTx9r-crnZGUB3y-zT6oQFZusGJjctiUpvE70MIkgpeWT9cubKqMF1ZsU1pgMh0f-Azu0YJjcQm1jO0zC2Qj71p31GzBVaf51_997bugTOT7RwC5s-pYWwVlalWQnmuJFi27ZMR13qHXuxvsCvV5AuYSd3bHT1i900D_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
علیپور؛ کابوس همیشگی صنعت نفت
🔥
🔴
علی‌رغم بازگشت تازه از مصدومیت، علی علیپور در نیمه دوم وارد زمین شد و از روی نقطه پنالتی گلزنی کرد
🔴
او پیش از این دیدار ۶ بار دروازه صنعت نفت را باز کرده بود و با این گل، شمار گل‌هایش را به عدد ۷ رساند تا برترین گلزن تقابل‌های یک دهه اخیر پرسپولیس و صنعت نفت لقب بگیرد
👏
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141313" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/141312" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
✅
مهدی طارمی زمینه آزادی ۸ زندانی شد
👍
مهدی طارمی در طرح حمایت از حقوق اجتماعی و رفاه زندانیان نیازمند استان تهران، زمینه آزادی ۸ زندانی را فراهم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141311" target="_blank">📅 16:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فوری ؛ خبرگزاری ایسنا :
🔴
🔴
🔴
فیفا در جواب استعلام باشگاه استقلال ، پاسخ داده که یاسر آسانی رسما فسخ کرده است و بازی کردنش غیرقانونی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141310" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
با تصمیم زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141309" target="_blank">📅 14:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141308" target="_blank">📅 13:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
#شنیده_ها
⛔
⛔
استقلال با هواپیمای تشریفات دولتی ( ریاست جمهوری ) راهی قطر شده.
⛔
⛔
نکته: تحریم هوایی آمریکا شامل هواپیمای مقامات دولتی نمی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141307" target="_blank">📅 13:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
گفته میشه دولت قطر به تیم فوتبال استقلال قراره مثل آمریکا ویزا ساعتی بده تا این باشگاه برای بازی با الغرافه مشکلی نداشته باشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141306" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhN9yjs-yn1kdLgMIfeIVgMQhSC-g0usXfylQ6dLN-pH-d5QZLXjbpZXYg9VPrQX5-GPkbB6PEYeC4dtjCZMG-bOUqcch3Ht15kW3nE_TZjlA8UqYO5r1TpAyVtt6GQ9TPlrlOfVN_jWa6OVOZ_V_dH4K3ueA_xJe1aVGy2bdOzVuS8VGU6F-LzjvCeJxgtWYY0lrRYM4rju1fnGY4nB6l3m1R3Qs_if4WLiy8Lok1rDYLCYWdEK4B-gHEELNVIU1UYsfuGZ-TeNrNz1cOoM0nlkNF2xPY718GvygOE2aM6liz0Gzl0gxePjM9CZMDPufVnqUaXecaTIYErbFHlBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیژن حیدری داور بازی‌ معوقه پرسپولیس - خیبر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
😀
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141305" target="_blank">📅 13:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFCKu8NhH4zC-lfTD7y-UMYC8SPNiLmXwxiXwlEqr5DLWW5UHjHoA7LVLfMEf6AoNnZAS3NtxzXFKYHGlkekj3IsyIp1emuJnrj-HoPhY1tVqDL-oQ-t2IvAFn9VElLERlnO8uoulzuQ6sE43OcNNjlh8aZ93nESSZNVmSFXAx_YFisQDn_xz3F4O11SKg2Bzq3f7p1jBsP2PM48BautKYgEDNEL5nbt-4akND91tUE8E9OlXlL5T15hfKtraMKmz6MaYf7tqo6up_Tu2rvvnWvzpzz1yTO_xHm08XdwvPCPmNaXEXmdX9ThL6HCwZUJxlDmsLkoTNuyfE1OpV-1Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool
🆚
🔵
Man City
⏰
Tonight 19:00
🏟
Anfield
🟣
سیتی در ۵ بازی لیگ ۱۳ گل زده و با میانگین ۲.۶ گل، قدرت تمام‌کنندگی بالاتری نسبت به لیورپولِ ۷ گله داشته؛ در مقابل، قرمزها در آنفیلد از امتیاز میزبانی بهره می‌برند. غیبت الکساندر ایساک و کودی خاکپو می‌تونه قدرت هجومی لیورپول رو کاهش بده، درحالی‌که هالند با ۵ گل بهترین تهدید سیتی محسوب می‌شه.
از نظر مدل آماری Opta، شانس برد سیتی ۴۰.۷٪، لیورپول ۳۴.۶٪ و مساوی ۲۴.۷٪ برآورد شده؛ برتری آماری خفیف با سیتی است.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141304" target="_blank">📅 13:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIS5RjRKZo4Z3yJWsjMzVT2XXgyXvNWOihRS47gEHzZmUfWZLmr4GifyS4O3Nw9Sl1QKgigozduzqnWbnsDYhfbmljIwV2IRNY_QcLTrWqwSz27aaw1TjJ6doalssIBksQ7Z9am12k-BwtRVgON-Lk8uN4hMG3D6WCnaYYY2BpQ0s4uCVIS4uWOs3Y-S6kGOLSv2sqmaaXJTAvb67fEMiJTjN75e48pB3zkA33ix51B4ko8JoXAi8kRlgAzpOCHnoHpdkjvUiMGBM3g9KyPOqOfu9DdfJy3ah3Q5a9VEamKl6ZYAmHAKNollLHeFjARTqmRDaxGggfBU4hNqsc_taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ابرقویی تارتار رو راضی نکرد؛ با بازگشت کنعانی و ایری، احتمالاً دوباره نیمکت‌نشین میشه.
🎙
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/141303" target="_blank">📅 12:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇷
👤
🎙
برانکو ایوانکوویچ: می‌توانم بگویم بهترین نتایج ایران در 40 سال اخیر را من به دست آوردم؛ قهرمان بازی‌های آسیایی شدیم و به جام جهانی 2006 صعود کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141302" target="_blank">📅 12:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
درخشش سرخ‌پوشان ازبکستانی پرسپولیس در رسانه‌های کشورشان!
🗣️
ایگور سرگیف با پاس گل در دقیقه ۵ و اوستون اورونوف با گلزنی در دقیقه ۸۴، نقش مهمی در پیروزی ۳-۱ پرسپولیس مقابل صنعت نفت داشتن.
🗣
درخشش این دو ملی‌پوش ازبکستانی مورد توجه رسانه‌های کشورشون قرار گرفته…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141301" target="_blank">📅 12:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
⚽️
گل‌های پرسپولیس در بازی تدارکاتی دیروز مقابل فولاد هرمزگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/141300" target="_blank">📅 12:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/141299" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=Qesrsp3IyPbaJFeAdqr01lGHvpYT_RCRN3tQSPxgstSxQcQbHxAdLYNIpECrrVij1SXRep0kJ03I66ox7eB1ODasU81oczYTrG_HeRShANLAdqe3O0gfiBpCY3zfZzsywzaGFNSRuzpH-opWbLSUKpVp0rRZVtWKesM8AGRWAfgGcmCkdlEXuYnV4eS6scGvbZemPF-anHeVNs6IIACVEWwo2-3X7Gge76HVrs9kaOiFLxjgoUqzht_OxCiXUN3dTne6IuGb4h5tk4LJNk0KhJLybKEFfIpHAbhVvWVficWsgoxOBFjgrl_m_UGmhxuozutkWf50vo-b6E8K4CfWCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf86a8d14.mp4?token=Qesrsp3IyPbaJFeAdqr01lGHvpYT_RCRN3tQSPxgstSxQcQbHxAdLYNIpECrrVij1SXRep0kJ03I66ox7eB1ODasU81oczYTrG_HeRShANLAdqe3O0gfiBpCY3zfZzsywzaGFNSRuzpH-opWbLSUKpVp0rRZVtWKesM8AGRWAfgGcmCkdlEXuYnV4eS6scGvbZemPF-anHeVNs6IIACVEWwo2-3X7Gge76HVrs9kaOiFLxjgoUqzht_OxCiXUN3dTne6IuGb4h5tk4LJNk0KhJLybKEFfIpHAbhVvWVficWsgoxOBFjgrl_m_UGmhxuozutkWf50vo-b6E8K4CfWCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باشگاه با انتشار این ویدئو نوشت : نگاهی متفاوت به شانزدهمین گل ارونوف برای پرسپولیس
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141298" target="_blank">📅 09:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol7zvdhcJ87bQsYkZkGK6bBxednq6ndm3QqCxQwgeuPhDxcoxW-59EupwIas_O-dqGRQk0-MI_25gGj4HhIy9GmEuyXuwqYIA2981Y6_e9KQa6G6jqcdvaShMBN3KQI4niC0mMrOHXuz33aX2HMF5fWlsAbkyfrlYB5_aw2FIYUV48Wl-W5pImFnWuYVxo3DH8g6Xg7a3pmAVgbbGf6Bk7xHThbmFHYMNtK_Wrcwe6gIBJZk_8pc0uv-A0d_qh0ejRaWJAR2-lp4rKuf_YJyjtfXKeo9bg98NyxIszMQN5o3tNrvhk6hgyI76eBI8CAfsoyAQeORZ7v7IdkeSzlSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهرآبادی از هفته‌ی بعدی فرصت بیشتری برای بازی کردن برای پرسپولیس دراختیار خواهد داشت.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141297" target="_blank">📅 09:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la8gRG-0xjvZJVX7n78BBDtVfFjjuMXQCtiyQTNqrltgEpMTlQ4LtDOd4eV7c5p9deJ8jDhQoLIru9z6JvP2CNBRiKxVOzNV-0DASpRvN7NM7qtUHSWWtSkkIuOpuODflnzoRNUXzJtYcV6wYsQUUFF-O2O_gji8FrJlHQ1iNza8t8qxIIwlUNIuJvsFqd2II_Ter-WK9ZEjQfDxbiIowTCyMCRFK5IZB0-tS2BIigOW8XZ4DCbKfN0MbUf79Oh5d4O3j6kfkzTcv1btr33EYWMj676OfYHfr0JIg259gzwRxTEo2MM2Sy_jWX1-kxmpoK2o0KtakDCJrsVgA1vtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141296" target="_blank">📅 08:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141295">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=qNQCSn5KxXlMHBdPMv0WM_WCtkDrP1gY5uzjY_aL9x0pPIbMRex7Bl30bkQWNudFnn-nDy_iaPrUlZ2Bn-eVSWxgKkFrKxVTPXaT3T5U7TBnj3M5MRoFAQ44JanI5kpAmOZwbwR9hqAGRFoyV6u9B0ZRYOrCzEBzjPokLS3gtrh7iayFjSax4qoPFyEYR7AxcaLMEXSQhNYAte-mxZKR3ZRwv4ShZe9XYhq1GTEZXbUjgfZqR-fZEq7wlysi7M88POdPDPEMeSqo2kRzkBbEmvMd8xYhC8yxBRaOOgdzAzA-yW0WDPRQGC7ofxHO5iEkYrEmlweLynymFlmpLU4V5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=qNQCSn5KxXlMHBdPMv0WM_WCtkDrP1gY5uzjY_aL9x0pPIbMRex7Bl30bkQWNudFnn-nDy_iaPrUlZ2Bn-eVSWxgKkFrKxVTPXaT3T5U7TBnj3M5MRoFAQ44JanI5kpAmOZwbwR9hqAGRFoyV6u9B0ZRYOrCzEBzjPokLS3gtrh7iayFjSax4qoPFyEYR7AxcaLMEXSQhNYAte-mxZKR3ZRwv4ShZe9XYhq1GTEZXbUjgfZqR-fZEq7wlysi7M88POdPDPEMeSqo2kRzkBbEmvMd8xYhC8yxBRaOOgdzAzA-yW0WDPRQGC7ofxHO5iEkYrEmlweLynymFlmpLU4V5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141295" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141294">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vClGVuFXq3Vkiye6OdmSnoweSNCiRI3HaOM3rzTDDQJIuwOGBmxIn0n85k1zoIixhUzY2hohm7wWpSqA1moaMG0vI-bWXoo61l_41_DsRSC9XnYKhFoyxIP_r_OFVPoBXVE4hTzp2MSPzQepH8Hl4vA8ahz4aCdfi61hmNFWEIjw_CZDshWKFJcF12ypiRWReQr-_0aLBXqhOF1Vm77XPSYTntoV2zfFWrVGRoyV0qO8cq5b5NMrvnT0ak_4p4k74j1biN1xBNT1BxsZ9fFoQSfmIrn-qMMVmXXDV2NzBlpQf_BPTx46NWmYdHOirga8eq8G1y3EqkMWgINGLvtx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد خدابنده‌لو به اردوی بعدی تیم ملی دعوت خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141294" target="_blank">📅 23:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141293">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EsqUNk_0yYElkQmvLAeWX4hh_DT-KujXpDBHu5RW9L-sFj_yxNJJWWE9_6bveEid1R4wSAkJZ9nEfx-F6877_tihXhehloz6j64XjQ4Yca4j6h9KZr6UcR4kqUaUXHN4Ki1TYKNNer00FmWDTe1mND4AovH5IEX_oFvmBTnaCtzhV2apOPpaeqZ8PlIuDcnvZNHqoEwBphf3RW-PuIe2s44xJNB0JOmTlHS7Ba-bKYLZam8czt41dCAegN17uSmrpd0HfO3mflVsaupSmtV5xWDUPFWIXdAZoGxAgThR9Ffy12D2oabugyEB8lCf7B95ON-Jr5yGftqy6XLmtzpGV1ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EsqUNk_0yYElkQmvLAeWX4hh_DT-KujXpDBHu5RW9L-sFj_yxNJJWWE9_6bveEid1R4wSAkJZ9nEfx-F6877_tihXhehloz6j64XjQ4Yca4j6h9KZr6UcR4kqUaUXHN4Ki1TYKNNer00FmWDTe1mND4AovH5IEX_oFvmBTnaCtzhV2apOPpaeqZ8PlIuDcnvZNHqoEwBphf3RW-PuIe2s44xJNB0JOmTlHS7Ba-bKYLZam8czt41dCAegN17uSmrpd0HfO3mflVsaupSmtV5xWDUPFWIXdAZoGxAgThR9Ffy12D2oabugyEB8lCf7B95ON-Jr5yGftqy6XLmtzpGV1ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی: تو فرودگاه بغداد ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141293" target="_blank">📅 23:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141292">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg5amjOBBn8Oe0snl_bRdrR28e2UZHP4iRJgY7HbY-nOJcWR6Te33HrKxvA5o6mZeqtQX9mcVbHJlx2wCwA5CcvJfS1oZJcyiRQEHTodLU4y3OdFjOy7gUFbBLrtjjkC50C23apeEFbX5Cc9Xf-SVoF6GNGvaVtfz8c9kcnWAckMfTSWLAgtwbGPskooQBgP9li-LF1d5u5O3Dg9pPnEhPH5u9Lysz2EmjGRgn7o3Aplg08kImMAn_VGduZOlJ0auqEzXzJfJNDSyj6ifgOhxmCDuYbf9XnRbSwVQIxq96XJ_P5pRgH_dnlKbHJ9LcMxFvVcf9VOIGyhi9SOg0ASIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
⭕️
⭕️
علی علیپور و تیوی بیفوما با هم مجموعاً روی 73 درصد گلای این فصل پرسپولیس موثر بودن
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/141292" target="_blank">📅 23:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141291" target="_blank">📅 22:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
تاجرنیا: بیرانوند دوست دارد حضور در استقلال را تجربه کند.
😀
به صورت جدی درباره بیرانوند صحبتی نداشتیم اما به ما هم پیامهایی رسیده است. اما الان فرعباسی و خلیفه را داریم بنابراین بحث بیرانوند یک مقدار این موضوع از ما دور است.‌ در هر صورت او هم شایسته است…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141290" target="_blank">📅 22:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=Ulo7e9LfZHFEaFUFnqGSAHR7dRmaS251R5L_AgbXkTPRG5RVI0ivolEc9dwhhfldylVAw-vtrHfj78gOFKgP39LevnqFJr8mjQYJleQ_ncoLj5szaJRah0CiFhhQxeCkdnc-J7c4KRPs97GT_-m9pbYjgQH7D88jCBwwwILRV5dqRliruzSDzYgO0hfZGEdbYoKPM8QgFo9Wg-vGmcsHLoyXM7ItTiwlQolsieMm4jG0d9HAI2XSD8oHAi_g6LZJHxVNwEyyfI_-LnpFglDCw2FKzZ-T7aa4Ni8_4j6w1DAQhKS5zr3UhI8cvt3z1Lg_68rJwH_CH_gshtpC6yYMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fcc915c7d.mp4?token=Ulo7e9LfZHFEaFUFnqGSAHR7dRmaS251R5L_AgbXkTPRG5RVI0ivolEc9dwhhfldylVAw-vtrHfj78gOFKgP39LevnqFJr8mjQYJleQ_ncoLj5szaJRah0CiFhhQxeCkdnc-J7c4KRPs97GT_-m9pbYjgQH7D88jCBwwwILRV5dqRliruzSDzYgO0hfZGEdbYoKPM8QgFo9Wg-vGmcsHLoyXM7ItTiwlQolsieMm4jG0d9HAI2XSD8oHAi_g6LZJHxVNwEyyfI_-LnpFglDCw2FKzZ-T7aa4Ni8_4j6w1DAQhKS5zr3UhI8cvt3z1Lg_68rJwH_CH_gshtpC6yYMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕
محبوبیت؛ فراتر از تصور
🥹
🔴
هواداری که با وجود سختی‌های جسمانی و مشکلات مالی، خودش را به ورزشگاه می‌رساند تا پرسپولیس محبوبش را ببیند و تشویق کند، به معنای واقعی عشق به پیراهن سرخ را نشان می‌دهد
🔥
🔴
آقای بازیکن! قدر چنین هوادارانی را بدانید؛ آن‌ها بزرگ‌ترین سرمایه پرسپولیس هستند
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/141289" target="_blank">📅 22:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbC8aqINk0OGUzJymOgMlD0EaCQz5H5cqBaeBGQQYfthPACaw8pK5QUdvWQ5RrOWGjFpBzTXsA-xT5vgYCza1M7YMQ8wxq9oQmDjxs08xE8YLiwxYP4EA5nNVnhaSHYSvtbMGHCV14y_Y9GtMoLTDWLhDHRI1FUX17etEhxd2kZODCWsOhxPWuz1rTh1B90WZr2J39Ns_9_J7SAA3Uek54t6Kc_Hm5ERSV1Kusz_17vRNaGqhosBbBe3pMftlR4JVBgnVnIERnarBxyqMv5ieM70Uvqfz2KE9vrM_kkr11GKWmvAfy_7lvnWiLbGGUKVDMz7_Ql4PpHaiWD2PJ7bUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محبی؛ ترابیِ جدید برای اورونوف
⁉️
⭕
محمدمهدی محبی در ۷ بازی با ثبت ۲ گل و یک پاس گل، عملکرد قابل قبولی داشته است پاس گل اخیر او روی همکاری با اورونوف، نوید شکل‌گیری یک زوج جذاب را می‌دهد
🔴
محبی می‌تواند با تبدیل شدن به مکملی شبیه ترابی برای اورونوف، هم به پیشرفت خودش کمک کند و هم اورونوف را به اوج آمادگی برساند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141288" target="_blank">📅 22:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
خطیبی از هدایت فجر سپاسی برکنار شد
❌
با اعلام باشگاه فجر سپاسی رسول خطیلی از هدایت این تیم کنار رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141287" target="_blank">📅 22:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_j-47B6gFnP9zOepwfYYSLt_f_7FhUGelzrvwNA4KSbGDRAqXU9CCLbd7FjP9B-8HmaQJsWNR8Ai-L7VGlD_B26FQMwL7lfpx72gG4tHhMMuazAX-9FniXOBMJMio9BnMEw7izMfa-jZmyEGxoI_fqJ8q_8NtMaC2KDKcggutOcxjksYzNVnYe4XQULjPosEpNVC1h6dT79hfTYydiNQf3RrJsbnH27I_8KiaebEzjC9mauX7R7ZVtR8YfT6A0pgYcZN94hlIeAJPuLmcCuQjzS2MW4Iy1yusQIhzYMZHn_DR7nsl0HxSlv3ci5M0M8q17QDmzC_nkgP1OsVPOLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141286" target="_blank">📅 22:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141285">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsaT1tsyAxNiwvpjPN_7Tl_6_k8kZP5THf6fuWLFnttccE87pF7oq2GJqfrYiP2_2T-k5qbvnJj_XiXvIyjFWE_qTXoN6aZLqzXmJ2tMBYu2YfcO79y8uQ5JThgmhXn2pmxINepU_IKNYzdzusYgX92EXkNNRFIR7rNdPB_JR8OsOv0SH-58KjEh8XhX3cx2OZpLe23PGG-3XOshMhx3JNrajEjbS5lprXHRbdlT8Ji19lb4QMacgT_aFPe833mIxk8QT6y0S4Xnip6P_GKap4k1eh4dUPIviPk7CMbtzGqeexcZdI0ojEH8rpDQKl9k7H3ZJECiQ9HHCEjIHoOWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جدول لیگ برتر در پایان هفته هشتم
✔️
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/141285" target="_blank">📅 21:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=RStP_48WNga3cNOA0iAcC3b-iktvLzTNQtKHegK5xoNud4i1h9XUJVeJik6y-VJTR8SQsdj0Jv1B0OzKbBWku5pwSsKOvqfavgfgk__JDfC0xm7fyhPkh9rsZMOZvXy2LAu6YxhzgqBcJXy6xvpNFfvBqIbv0j2WeQlZKvw8vTsYuT5iv1EzQ-LIoU33GnqcrAGFNBM6_Tg5YUupO2qm2eUNxq7NnBo9xRs1m3cAefyrIug8-km4z-gjjem4ZYHYGEX4i1Joyv5yqSa8eaA73kEqQtatAvQaq8-e97_ExalRGVof92y0Hk3XjJZe3avVEj3HS5WEx1JT_Pk1QIi4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=RStP_48WNga3cNOA0iAcC3b-iktvLzTNQtKHegK5xoNud4i1h9XUJVeJik6y-VJTR8SQsdj0Jv1B0OzKbBWku5pwSsKOvqfavgfgk__JDfC0xm7fyhPkh9rsZMOZvXy2LAu6YxhzgqBcJXy6xvpNFfvBqIbv0j2WeQlZKvw8vTsYuT5iv1EzQ-LIoU33GnqcrAGFNBM6_Tg5YUupO2qm2eUNxq7NnBo9xRs1m3cAefyrIug8-km4z-gjjem4ZYHYGEX4i1Joyv5yqSa8eaA73kEqQtatAvQaq8-e97_ExalRGVof92y0Hk3XjJZe3avVEj3HS5WEx1JT_Pk1QIi4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پایان بازی پیکان و شمس آذر، رضا شکاری که پنالتی تیمش را خراب کرده بود، دل و دماغی برای خروج از زمین و رفتن به سمت رختکن نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141284" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=SKUWnmp5yJoQkzR_1cToUSs2smyLEGH5ib3Fu_QTRX7dvP9TgiNidlYj_ZkS7oXrwJn6qR92MwuZ6xJrL5lYUsMdDCz4hotCSjWpgWp0ZS_9weks5nU4Op6isPYTS09_FyiPNFsTrJsqlgazMAbWNx5y0whAUgDEFcK1si-CpOPY1NOGGWljNXxomJNWbUDXH8RYCgs-38Rg1IlAVgC5IBtAxy13wEmEmlo4osj7xjoSO3Ke7iARTvQf6HLVKx_KhHGOfEMoTnjppQh-hUbqFewREvCdK4hGtaZYmDgG-o5bm5tOGhn1BHTOry36qlEmlOPlsgTVJ0xo6yBS1HggMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=SKUWnmp5yJoQkzR_1cToUSs2smyLEGH5ib3Fu_QTRX7dvP9TgiNidlYj_ZkS7oXrwJn6qR92MwuZ6xJrL5lYUsMdDCz4hotCSjWpgWp0ZS_9weks5nU4Op6isPYTS09_FyiPNFsTrJsqlgazMAbWNx5y0whAUgDEFcK1si-CpOPY1NOGGWljNXxomJNWbUDXH8RYCgs-38Rg1IlAVgC5IBtAxy13wEmEmlo4osj7xjoSO3Ke7iARTvQf6HLVKx_KhHGOfEMoTnjppQh-hUbqFewREvCdK4hGtaZYmDgG-o5bm5tOGhn1BHTOry36qlEmlOPlsgTVJ0xo6yBS1HggMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساکت الهامی به بازیکن تیمش اینطوری سیلی زد
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141283" target="_blank">📅 20:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0eUqkKWtFKXEPjYr7Dbd8nD5X2Y_wOQbnVRFnIFdymuh1R6vKhjQZqAIPWZcfM2dGZ6eR5CuDnabcrHy4VBefljpvcQ1yUsrBM52RNZPQUhW46YWQLxD8VMWr7AwTcBhbV3YTNDAmLhNOx9FAC9mlan4Ui3BVO0q6nFZR8_A5KwSsUMDA3xlpa0HY_7NkmVURTg0uZggz0bga4tzp2FT90Ne_GVTOSF07B0n-J5rjQhW_wqOESLHUebUZ9Ow6r9BMYdN1SxplmSDfWewYwikPlIziB-KePhgfdr9dvx79rNKJRU4bATxZcytipIw65DcHgQ-HknsfMrBZF0Jl0Ozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid
🆚
🟡
Villarreal
⏰
Tonight 22:30
🏟
Estadio Bernabéu
🟠
رئال مادرید در ۷ بازی ابتدایی لالیگا ۱۸ گل زده و فقط ۸ گل دریافت کرده؛ میانگین ۲.۵۷ گل زده در هر بازی نشان‌دهنده قدرت هجومی بالای این تیم است. ویارئال نیز با ۱۳ گل زده و ۱۲ گل خورده، توان هجومی خوبی دارد اما در خط دفاع آسیب‌پذیرتر است. باتوجه به میزبانی رئال در برنابئو و اختلاف کیفیت دفاعی دو تیم، برتری رئال و احتمال گل‌زنی هر دو تیم از سناریوهای قابل بررسی این مسابقه است؛ البته پرسینگ و مالکیت بالای ویارئال می‌تواند بازی را رقابتی کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141282" target="_blank">📅 20:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141281" target="_blank">📅 20:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141280" target="_blank">📅 20:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
🔴
🔴
محسن ربیع‌خواه مهمان ویژه برنامه تلویزیون باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141279" target="_blank">📅 19:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
پویا اسمی که در بازی دیروز برای تیم بزرگسالان پرسپولیس به میدان رفت، امروزم در بازی مقابل جوانان استقلال فیکس بازی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141278" target="_blank">📅 19:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تیم پرسپولیس از دقایقی دیگر در دیداری دوستانه با بازیکنان ذخیره خود به مصاف فولاد هرمزگان می‌رود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141277" target="_blank">📅 17:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S1ZiH2Bx4GUx6z_FIqh4UCM3diULgmJLARpOROlsudPLHhZQs5dHM0SgViCrszQKw3LHilAedAEVLt8u2yaD4IqKkxqZgmv8UIB-rnRTanA8aE4xR3DGP9M4OAbB3_mOPNjQajuB0XzSCpDukvOX2GsmNRaxBU3mwrhCB_QzUjBjn_Lt_Weh9GdE8HKu5-WsdIj2vVVpC3bwAN2ybRLyc4mibrYp60i9_GslPplE24cybTcxXPbKw9BidsKlzZ5MQGIq1YsxKHuJECkCUoh0tSB7EvV5Kc9V9ABRuoYgeAmehAMW8_tqyQ6rh2wTFSqp3wUyB_xNKY4BlUy5c9xReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141276" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141275">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141275" target="_blank">📅 17:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141274" target="_blank">📅 17:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eW2MwCM9UkJr8c05-wHZh_KRrVLkYYicRslVW97pU8ifQ8sgz636WZjVDNA4_x8aQh-grG68RcK1hs_EzyeDnp6rW_SnijcEWtHnaQaOlrUFaIXOTbK-MdC-leuHPHj24nBhrVVl3CDnF-Q75WLRQK7XZfJ5V-9nhzNX8_W2s7D_E6z8qBsJ_uQurjEq1LOWEOz8azPR33fqj9BuHVDBmCFN7KoG9-sgDdYUL67WUpK-UffS_M9khdBibykD0MmCSpr8tJoeitkrjyU7gWAxY8Z_dZTnGi8JzntVyzg-4FhiQdeIxyq5p44DG8TbrhC_ZSr2GNfc2hy9UrfWgiojaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ارونوف با ۱۶ گل، دومین گلزن خارجی تاریخ پرسپولیس شد؛ فقط ۴ گل تا شکستن رکورد گولسیانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141273" target="_blank">📅 16:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141272" target="_blank">📅 16:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141271" target="_blank">📅 16:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141270" target="_blank">📅 16:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=LL8rYSA0r1_uFR8N31rIcmjOKYVo7pRZwfPvNDFa7JnDFKxkrZEOG2gXZtEenFalsVirPs_mrhCYXchENsDJ3rQMsczNlFlgRcb-dfpK_v7VJtt1q1kNP0uZgLIzQ8pYrY9hMI0qQYg9WL0Nk--VjGFtzKud6NqFLDk-H58lqpZ2P9a2Getu-eDEnSENkMiI-PLhSa7OM92VOZDB__QdrqdMwfT0O_jNEn_fYO0N9jxn5sStqMEhNhojIqvHOqmWMggUrqrIcbzGdW3kFbuT8SIxVqCGvoW0fOO3HuN1Bsvn0DKCh1htFEW9iaQpPwHAUN5kP6D_6wE1Cgq1prfOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=LL8rYSA0r1_uFR8N31rIcmjOKYVo7pRZwfPvNDFa7JnDFKxkrZEOG2gXZtEenFalsVirPs_mrhCYXchENsDJ3rQMsczNlFlgRcb-dfpK_v7VJtt1q1kNP0uZgLIzQ8pYrY9hMI0qQYg9WL0Nk--VjGFtzKud6NqFLDk-H58lqpZ2P9a2Getu-eDEnSENkMiI-PLhSa7OM92VOZDB__QdrqdMwfT0O_jNEn_fYO0N9jxn5sStqMEhNhojIqvHOqmWMggUrqrIcbzGdW3kFbuT8SIxVqCGvoW0fOO3HuN1Bsvn0DKCh1htFEW9iaQpPwHAUN5kP6D_6wE1Cgq1prfOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ضدحمله زیبا رو ببینید
🔥
🔥
🔥
❌
با ٣ پاسِ تک‌ضرب و پاس‌ تو عمقِ زیبای محبی به بیفوما تک‌به‌تک میشه اما حیف که این کارِ تیمی با گل تموم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141269" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELHzoW22YuoXb6-8qvxDW4Jeajq8jsbT8WkYIbQKmFxGcczdmJrk6IYg_oiPqo1QGlxoOKCvGuGIJto_jlXiimoEAbHRSU8Y3lxt2AvtgIIdjZJsrHtu6OTa8u72lLu1lEikmMtsNdUiIi1W8eFSxzOJZT_tfge-a7zNBWIti9Rj2hsupGQmowo4PyL0gugutuGZy5zolHXSaAq5vWy0E2YDnjtt8Uy5bXWMvg8cbBbF2ZnR4WTTBrXKjDAQpfiqdR4027GXGlasGRxdgcnztq_BF_IEWjWVu05tc8jFt_GAZ8sXPR7dZZE5FFR7raxFXhPc6kiGLhdg9eMf_adEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141268" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=EbkKhll_KZpBGcFGnBGZ8Vxyzo8PoFOwK3rJKBtFceONRsOTVGYYMF-O3vCAaAJMrl6IHL2nYfVSYkmYM_KL56Hq9j6xHU4z2PW3C-A5uJCPSAnJU2lda1_ekk6xhM2rfqigd1xdxZvB3BgKNGoQlNLfsJWsBn8ogySoyO8NCRWCfdgODhaYQVxoaaThDeCpK8h9H4LsXqjXfUULmFfrU2-UlIBfncH3xym8ohOUEXDkUf4NBw3ei97K5Urtr8AMoM9IetE9PuhDn91ZEdZbvcBZSCUSHCqr0T7LQTiDJbrOn3NApIjcMkSAapoXmoGhcqEMs-SU96dgKvQ81pIQnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=EbkKhll_KZpBGcFGnBGZ8Vxyzo8PoFOwK3rJKBtFceONRsOTVGYYMF-O3vCAaAJMrl6IHL2nYfVSYkmYM_KL56Hq9j6xHU4z2PW3C-A5uJCPSAnJU2lda1_ekk6xhM2rfqigd1xdxZvB3BgKNGoQlNLfsJWsBn8ogySoyO8NCRWCfdgODhaYQVxoaaThDeCpK8h9H4LsXqjXfUULmFfrU2-UlIBfncH3xym8ohOUEXDkUf4NBw3ei97K5Urtr8AMoM9IetE9PuhDn91ZEdZbvcBZSCUSHCqr0T7LQTiDJbrOn3NApIjcMkSAapoXmoGhcqEMs-SU96dgKvQ81pIQnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیفوما و آن فرارهای همیشگی‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141267" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گویا پویا اسمی که امروز به میدان رفت و جوانترین بازیکن تاریخ باشگاه شد یکی از بازیکنان مورد علاقه تارتار هستش و شدیدا بهش علاقه داره و بهش قول داده که بهش بازی بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141266" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
این وسط شله زرد هم فجر و شش تایی کرد ..رسول خطیبی ی تنه فجرو نابود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141265" target="_blank">📅 15:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
فووووووری
🔴
باشگاه پرسپولیس وویس هایی از ایجنت یاسر آسانی داره که به پرسپولیس گفته آسانی بازیکن آزاد هست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141264" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZmBWChS-48ReqIn8s2Qb9uKYm4128QFhrNp1gTLqtua452DOBAfIYrR8vkORW_tIp9O2iY9xsEiDmRCkVHGxpCANNWnmVPfj-Dtk1KiZi3Bqw5XQ7i8CEt6XvaH5iJwt1zVFnNidUFxYCOS19bXSAm4RkCaFNenPMv9tieVCafLBR0f-N2OOJgKG8wsuTabLzjuozCKJGjTqlEHUfCINwS7sB-SzzzQpzWbZVLZWOry66cL3PVHygaagw1zJeudig8tv9sCKXO-9ofkjU5T1TSGz9KnXLiw-bWLZR7Pi3w-IJPtVMySTauUvQ6A5qDkT8ezg8ty3i_1-BiDpitkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
نبرد حیثیتی در لیگ برتر؛ شیاطین سرخ مقابل تاتنهام، جدالی برای اثبات قدرت و تثبیت جایگاه!
[
منچستریونایتد
🔴
🆚
⚪️
ت
اتنهام
]
⚽️
منچستریونایتد با تکیه بر امتیاز میزبانی و قدرت در انتقال سریع توپ، به‌دنبال ضربه‌زدن به فضای پشت خط دفاع تاتنهام است. تاتنهام با پرسینگ و بازی مستقیم می‌تواند موقعیت‌های خطرناکی خلق کند، اما فضای خالی پشت مدافعانش نقطه‌ضعف مهمی خواهد بود.
سناریوی آماری محتمل: بازی پرموقعیت با شانس گلزنی هر دو تیم؛ نتیجه نهایی تا حد زیادی به کیفیت استفاده از موقعیت‌ها بستگی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141263" target="_blank">📅 14:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مهدی تاج غیرقانونی بودن قرارداد یاسر آسانی با استقلال رو یادآوری کرد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141262" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVy0nEV9NqKmaol9b7ruuCpjVcTg3TSy_cvi56oZaTq7zZbzwa-5JnHbj5Oeft7EPvx_ubKpJzeTxT_NXav0VCp6FhijcM9C0xJX8sjwqvS5f-z15eqyPjY94FECjri_cs9zoHP78aUn42S-sofWJpAggz3vQYyw7F5Vwht5luuEJkhQ0paCZ664rElbnhJfP4tZzMopNQswkwGSkTa25Jj36IES1f5hlAb6JOUsU8RosqTE2ob997iCFtU89CvK7RG6QF9XApHI8lriMViq_wtwGT00iXfLGJLbv0amqkpQ2O-KnirTg7tyEE4oJHjZIaz2oStbTjVf02bQ6TTr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141261" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141260" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141259">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
تیوی‌بیفوما وینگر33ساله پرسپولیس با نمره 7.8 بهترین‌بازیکن‌دیدار امشب‌سرخ‌ها برابر نفت شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141259" target="_blank">📅 12:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-34qW-8NZK3DI5cHNFp0Hv-er4LdnsGuqU00w3Ict1C5_8NrClaqHN3iL344qkheDox6-eFY_ghbpQl8PD5uT6xq27deeEy6qTCBa-9kyjJLnlJsP8Qlb8_BfKSsZ9eKG_LSnNFM4oGkSVPXkXX27saj3DDMdLW4ePIDbU1g9mqKC4jDMCRg_5p6rD1Z0WVrdpj1hq64XnTcJjVgFZ9Wi-qzFdjQveYVNIruhdxFx0CGidC1i2YOqnRTUk5JxCkpEBwyp0CpsJ7ZWxcV3ld8Nc9ScyweisxHndJ1vB_4kAQJFTbNl2NmD2rSG1JYDgJzwzLeZGqUVhr-HFfsIseeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141258" target="_blank">📅 12:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/141257" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/141256" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141255" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373367fda.mp4?token=uAMdTbljo2i33exzRBWexd2ST9EoBWI-B83jkn9q3vzNMwKhRJftvz9EAzEfr8peTKoaHVmpjfuLP47JzCy61ZMY7AGmUAgspDzaHFGDpafLC2hOzQB1OvmgpQVt7RjsFu_S6CW6UkNAreYgMbrLEC5JjzdXDMK-eug-5c0pSFf4k8kkAELlYN-5HJscFqEpqdr_B6XxQ8m2Yocm7neTjfvmEUQBEGpR15B3EUalFbS_xiuyh-gdlnZs2IOGgrAQaxG2qkUPO6QxHslybthcD0ah2ynypnKx5-NxjshyeuI8bf7M-YsyCDW9jy1XiaZaArYcWpsLW4_l46dJ-hU37A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373367fda.mp4?token=uAMdTbljo2i33exzRBWexd2ST9EoBWI-B83jkn9q3vzNMwKhRJftvz9EAzEfr8peTKoaHVmpjfuLP47JzCy61ZMY7AGmUAgspDzaHFGDpafLC2hOzQB1OvmgpQVt7RjsFu_S6CW6UkNAreYgMbrLEC5JjzdXDMK-eug-5c0pSFf4k8kkAELlYN-5HJscFqEpqdr_B6XxQ8m2Yocm7neTjfvmEUQBEGpR15B3EUalFbS_xiuyh-gdlnZs2IOGgrAQaxG2qkUPO6QxHslybthcD0ah2ynypnKx5-NxjshyeuI8bf7M-YsyCDW9jy1XiaZaArYcWpsLW4_l46dJ-hU37A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آنالیز محمد تقوی از بازی پرسپولیس-صنعت‌نفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/141254" target="_blank">📅 10:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141253" target="_blank">📅 09:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141252" target="_blank">📅 09:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
پویا اسمی که متولد 1 شهریور سال 1388 میباشد به جوان ترین بازیکن پرسپولیس در تاریخ لیگ برتر با 17 سال و 1 ماه و 16 روز سن تبدیل شد.
🛍
پیش از او این رکورد در اختیار احسان خرسندی مهاجم پرورش‌یافته آکادمی پرسپولیس بود که در 29 اردیبهشت 1381 در دیدار…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141251" target="_blank">📅 09:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141250" target="_blank">📅 09:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/141249" target="_blank">📅 08:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/141248" target="_blank">📅 08:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfrsX2jAEopW5OMFXURYoYE9BIS-dqMiniAyzf8od9a1hAAKNrVUfrJPctqXkSX2Wk63gauQHDM755XvicADAK3xtDWUwNgxErdV5qTDt8lKQc8DCAGKPJRLba7CdJ2dsc6i_ULrbGJSEfc2UeQHF-Z4pvvcI47oYh8ty0N3alwbcZhUZ9SiZ-lJZFFafWumeIytqAAIsUWFZ1J7rhmGeIBXnf3LWriIXBzuwG6PqQvpCRjZ0Dle1QtKkpR0PXjIUS8LQoVwssSEpyAMrHG3E3dz2AOin8NveYj8vsrQsgSqLXsQeZZBMiOj0MoXpTdzGinJXCiY_MP9oFwghD8l1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/141247" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/141246" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141245" target="_blank">📅 01:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141244" target="_blank">📅 23:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
#فوری/بیرانوند با دستور نظام وظیفه ممنوع الخروج است و امروز هم مجوز تمرین نداشته.
🚨
کریمی و نکونام می دانستند بیرانوند حق خروج ندارد و برای خوشایند زنوزی اخراجش کردند.
🚨
اکنون هم می خواهند سر هواداران را گرم کنند و به رسانه ها می گویند مشکل حل شده و به…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/141243" target="_blank">📅 23:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBw1EGOEog_zOXjBthDGFXzczKgl5EpITYPmUEXWrxaskeqba500WelpkYj3TZCpPQjJIfZ4fxSZ11LTOLtFq-ub0AXbMkVysFYZBDQFTSCs01XSS8-HPo_ijpM3_9DZ_GfGMMBvFKNDDe25GZXYiTPziWnkLsK0FmaIVM1Jbc5shR28lvhtAgpYHTIepPwaaB0A_G4cLLzBIj2cbxxkvn9rLG0hasB9IMFgy9GeW3gaBdp-tw8flvucxItxSwhAcdPCBd4Ne7N9aHYGKbOP17NsyAy8yQUhjjvlak2QydTT6egmwdrx9tLemdmDCpURR1UKW9MEiUD02EsleOr6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/141242" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!  علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/141241" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAb0ZJwYld7z6kspMQaIajfIocvd4U3S8DO2PNWwXDM0Q3FtX4YHSkKSMful6D2ABAvXVzr7R3dLl2oXQ3Eu20AMjDJnmxzHEv9N8kXmv5TeNUdxobvUyPy3c_TZjcDjAWKIglorWS5FSF_poaZWSZEgnGzeoCJWlMDsn5_A05ilWmZL4HOrefva9XrT2gej795eFA21LHvG9XViFs4u0AufF9jQf-MXuy-AYQIE31eMP9uNyAv3E60-fpICZ1Y4lLQk79hI-PARmFAqZBWkWyIskK9LlBKJmb0mk1Xr4YqZrTxMXy0onnM_5f6l0ttnBVo7uRvN_O9WEjVbokVLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
❌
محمد نوری پس از شکست مقابل پرسپولیس به صورت توافقی از صنعت نفت آبادان جدا شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/141240" target="_blank">📅 23:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=H39R8BkmO75n9PeFPqPzLXcOzfdOqWOB8aD-LB6ca97mpEPWMumVEswcyibrmKIoLcMpl2L0pUPoW2wEfZQC6p_uXotE30up3YKe9zK1YHQ4L0gyJdAJXmmSz4g-wuqfZ30LcLLFwPHBuk6zj7apGD7eUEqrZNLyq9alCPUq00yxEb9DtS-ckLBttNtmHhlq25IMdifHx421h6EvNCy3-2YpVUC_FbjsNdpKPVVI-hM2edw2VrISzH8e7LEo4quKy30l0-7ANdq7kfZ0R_s02GEAdZS_GE2NJEp5OgSW1B2qKVEta-Xnibrx_kD59gduITAsYPK84fntfW94cwdeBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=H39R8BkmO75n9PeFPqPzLXcOzfdOqWOB8aD-LB6ca97mpEPWMumVEswcyibrmKIoLcMpl2L0pUPoW2wEfZQC6p_uXotE30up3YKe9zK1YHQ4L0gyJdAJXmmSz4g-wuqfZ30LcLLFwPHBuk6zj7apGD7eUEqrZNLyq9alCPUq00yxEb9DtS-ckLBttNtmHhlq25IMdifHx421h6EvNCy3-2YpVUC_FbjsNdpKPVVI-hM2edw2VrISzH8e7LEo4quKy30l0-7ANdq7kfZ0R_s02GEAdZS_GE2NJEp5OgSW1B2qKVEta-Xnibrx_kD59gduITAsYPK84fntfW94cwdeBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141239" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
✅
تاج : آزادی تا 2028 باید مسقف بشه، وگرنه دیگه اجازه میزبانی نمیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/141238" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=W_I2f5NcDcPExTgfBs5Wtb7VyCFxBNptMh2Cdd7h90yTa3jA-XVOl6Aq_0HiqDd-gq_jB-r6gZrVt1r328iiWjGWao9Cvek8uPOqH-GV0KCPuAFwkHhEhfJcnKgAlVasdlwYA4b4cxjuSdfGlA6HYbAlpS-EEV29516DiPIokd73ikmv-aateHmaa17HBNfu3erc9Dfmhpju71Awwi3D6eLID2Wb5cAR7zsTI6Aq3jjRsrIkfvWteISS7wrPdPTtfqYBSU1hBllZv5SZcRzflKIqbxHmSP-qaEXKAeM-sUtxb7ZMJOKueyY7QWi6XX5mpeFnJ_ylLmbh7rK77O0KIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=W_I2f5NcDcPExTgfBs5Wtb7VyCFxBNptMh2Cdd7h90yTa3jA-XVOl6Aq_0HiqDd-gq_jB-r6gZrVt1r328iiWjGWao9Cvek8uPOqH-GV0KCPuAFwkHhEhfJcnKgAlVasdlwYA4b4cxjuSdfGlA6HYbAlpS-EEV29516DiPIokd73ikmv-aateHmaa17HBNfu3erc9Dfmhpju71Awwi3D6eLID2Wb5cAR7zsTI6Aq3jjRsrIkfvWteISS7wrPdPTtfqYBSU1hBllZv5SZcRzflKIqbxHmSP-qaEXKAeM-sUtxb7ZMJOKueyY7QWi6XX5mpeFnJ_ylLmbh7rK77O0KIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در اتفاقی غیرمنتظره پس از پایان دیدار با صنعت نفت، تعدادی از هواداران پرسپولیس با قرار دادن موانعی از جمله لاستیک خودرو در مسیر اتوبوس این تیم، مانع از حرکت آن شدند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/141237" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnbye6e9FCg3Gtoeyqh21PJPEfl4l06qC4eiBsG5BcbXcewHW8IZXF6D3zdgk6FU3opD4l7QDBmFRV5ZycNhZYvAclD9jo2txxXOC8mrCLg85ReTyO0hWlMnA21UeGjt3hIWGlonC5YJPjZAmTsJYaIJUVEROl8TwPohY4tzGVlgBdXwxjErAmVMpkuMtS1tVv67aGgAatx_ijwwSD6bDYmK04pk9gHj6oc_WOSz1zB5Wwmz_x19m9Jnd0bO0qP7fY_0W98bCgp9p-VnXu723rtF8nb8_zU8Wq-tTGm5l1qzk9l22Jk6a1HvXP3bxOwWI05V1sHTyy8mdVueuCJv9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/141236" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=hm3NExTfG3gwRXQ04tZGYvHT42nZ2u1PUfO0yxv673A_gouNXSsMuLOcGvlAqdPvo4LyGrdhLSr-RIs8aAyCzNPJCBKH7wcFRP3-OT3yDrIkTIudpJlNQUCspGSDP6bZi7T0G3vcWBOcdz25xYUTRPknAQMVVbiZ-D74Iy2OTlALjeZVMcvI7yx2SqD8Ck4sI3p6Ke4d3aoNvKcpgI2ApWWBW2l4uSORTFwGImdRKw5ZRwcqBNmOqnWazpE6Mc67xl_FzXzkHcjzhL1IHrf2mEg4Hj59OvqKSF3peC8kQDaEC6thjM9UKh3kQv03BOaTqGXHJWj9Ntn-5Tv4ngzO2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=hm3NExTfG3gwRXQ04tZGYvHT42nZ2u1PUfO0yxv673A_gouNXSsMuLOcGvlAqdPvo4LyGrdhLSr-RIs8aAyCzNPJCBKH7wcFRP3-OT3yDrIkTIudpJlNQUCspGSDP6bZi7T0G3vcWBOcdz25xYUTRPknAQMVVbiZ-D74Iy2OTlALjeZVMcvI7yx2SqD8Ck4sI3p6Ke4d3aoNvKcpgI2ApWWBW2l4uSORTFwGImdRKw5ZRwcqBNmOqnWazpE6Mc67xl_FzXzkHcjzhL1IHrf2mEg4Hj59OvqKSF3peC8kQDaEC6thjM9UKh3kQv03BOaTqGXHJWj9Ntn-5Tv4ngzO2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
❤️
فووووووووری ؛ بیرانوند رفته هتل محل اردوی بازیکنان تراکتور ولی توسط نگهبان هتل راه ندادنش و گفتند سیکتیر
😂
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/141235" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=BAFXyJ3mGF_2YBhwKKx8JTwglA9j7q-tF9iPSezeNPrZUXRBE4jP8wX89Wq_CrVguPHdSF_QepEkBiNP8WgSN_USc4ACxmyf6IPDN1EhSIlQa8PPYjBQTqYNhCJh66OcDl97423eOS13grYzF_qfSIwVr1SzgBYGftl0G1Nu-dSTyR9Cn9gRdlmQR-7S0MhjaxYEYw7QZPl7QyUaNJwiYUWjlNOI0IlUIMdV6PAWD0uf5clG63GOKUPJWWT3EJtlXUQx15B_7Tp0NVURNLEFb64LnLKPd7h_6eA5VJMgaH-EgU8EwCEl0Cdm2jfooTYkgi7_ACuFCtpLaLZ8rF7--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=BAFXyJ3mGF_2YBhwKKx8JTwglA9j7q-tF9iPSezeNPrZUXRBE4jP8wX89Wq_CrVguPHdSF_QepEkBiNP8WgSN_USc4ACxmyf6IPDN1EhSIlQa8PPYjBQTqYNhCJh66OcDl97423eOS13grYzF_qfSIwVr1SzgBYGftl0G1Nu-dSTyR9Cn9gRdlmQR-7S0MhjaxYEYw7QZPl7QyUaNJwiYUWjlNOI0IlUIMdV6PAWD0uf5clG63GOKUPJWWT3EJtlXUQx15B_7Tp0NVURNLEFb64LnLKPd7h_6eA5VJMgaH-EgU8EwCEl0Cdm2jfooTYkgi7_ACuFCtpLaLZ8rF7--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اتوبوس تیم ابوالفضل جلالیو جا گذاشته تو ورزشگاه
😐
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/141234" target="_blank">📅 22:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/141233" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/141232" target="_blank">📅 21:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
تارتار:
🔴
به خاطر گلی که خوردیم و موقعیت‌هایی که از دست دادیم ناراحتم
🔴
از شادی هواداران پرسپولیس خوشحالم؛ آنها همیشه باید خوشحال باشند
🔴
همه بازیکنان از کیفیت چمن استادیوم شهر قدس گلایه داشتند
🔴
از مسئولین کشور می‌خواهم ورزشگاه آزادی را هرچه زودتر آماده…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/141231" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPxqfRDgmXJu7GujdUb8_81wT-OdNd6Vl1TiIfarXWlL5lW6vhb-6sVwZCr_pb_xRxvu5HQhbdUlUuJBWitfwdTUf9w-Uoy6VzvhzXT-0NOnUyDH1CrC0XfIIeMUPP6UlTBhqOWcDxd1zIzSjZsKIeO6QTjAL4UgrFrbog64g7KvuQBIK9ibbRUgbg7z1k-_o8gdhmuim5vnSUXLlU7rqkvnXuU69OcKRpE3PJeo7AlQ4VsqONhODy_iwXSUQmYT1rQ41sdOHeIxquWybRSslGL7qILbn9XY155y7K3saabWEo3P9qRrkMVNpwMJZO_4DBB4FkGw8cXHLnnwNWxSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرخپوشان پس از کسب پیروزی، جشن خود را با هواداران تقسیم کردند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/141230" target="_blank">📅 20:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-ICDnpuqBbVr_T0HlFVg0IghLhrF4AnV7-TDmg3pB6ETWHwS_uOvxYmtm_vHMX70LDOQ8gbbLUjFeXJIg12-2Rd4j9fb3VFNRil80H20cSkklCs7-PEdoJvSUq7fUC_h5W35m8xjCMlMv23YODTWaZ_nLdMs9aoz8Qt_1gp2P0PFq_RMHSl2LSaLQGK5l937UCHHnfLYWO_UVUTnrWvVYma0M7ZqPxxCWlf1iyoezWjCkCNumR_RVLhLSj3TBHx1mqPppCELzVocS860Oc2QWk92CjHgI9j7qtYj7Xxui5eKP3UJwtEUXWWrKYBYKUKLwu8G8iOxB2T51IgpeS_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زنبورها در کمین سه امتیاز؛ وردربرمن آماده شوک در خانه دورتموند!
🔥
⚡️
[
دورتموند
🟡
🆚
🟢
وردربرمن
]
⚽️
دورتموند با ۱۲ امتیاز و آمار ۹ گل زده و تنها ۲ گل خورده در ۴ هفته، برتری آماری محسوسی نسبت به وردربرمن دارد که ۸ گل زده و ۸ گل دریافت کرده است. دورتموند در ۷ تقابل اخیر مقابل برمن شکست نخورده و با توجه به فرم هجومی میزبان، شانس بیشتری برای تسلط بر بازی دارد.
سناریوی محتمل: برد دورتموند؛ هرچند برمن با توجه به قدرت گل‌زنی‌اش می‌تواند برای خط دفاع دورتموند دردسرساز شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141229" target="_blank">📅 20:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141228" target="_blank">📅 20:13 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
