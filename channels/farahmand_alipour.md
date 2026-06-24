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
<img src="https://cdn4.telesco.pe/file/UGrTOBhuWzgOww0wXNEREE5BjVRiLPYFKvrvgDLUziz46mHJSGeuuPqkaGPQ_oKyab-gueii-mR-MpVg9nudsQyMrhY2ccggKL1HVOUmt6we3D6ZKsym2BO4B-Oa8FBcTHNLxNM3vU-YX9r77PYHLJ_RUwd3x4Ee8o6rjJISRJay-zYpBjOfUkF8nJrti_78iHuSH3y6zaGf1xy6kfTYRhqrgcayfChYNJlCt2PgooL6PMl2yyxC0Ks-6SL4WZvPe8X1vMii7IB8FdBAbjiuJrXkgTCoN3YyeAfHvqiCwI1Yc-FFi9zgR2Pcvn7Q-uaunI5pVhWoa0xXVAvqxJZu_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 00:37:27</div>
<hr>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=olPsU5oKiPfkflT8zn4bT-tRG_Sb61iYOuRJroEos1ryeUOij57W1doUJQKoX0s6tx6H5Vf4zxfmwEAufGS0A-ib21ZMME29U3jqWo-iQNVaI3lxyJtv1F6v9uBIfw7_uWF-Ko3M_7mrfMgW5eQ_qYECHxQsGsDDRMV6v2dTO0SwGnUo2nfaI6LXkNcMac-JXoNkSnpdo5nrSlNNAOPZ0ISJI92f5f3aLX-WRp5VSZWpqqJH-ybloupAlmgxZQls-tvjh6lWMAnZixNow8eIl-p4XYxLi4TLgMJPxBMPf9KLA54Yg0LABqTcm10AuWR6eRoLoRPUvBSDEoQ8bBkbqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=olPsU5oKiPfkflT8zn4bT-tRG_Sb61iYOuRJroEos1ryeUOij57W1doUJQKoX0s6tx6H5Vf4zxfmwEAufGS0A-ib21ZMME29U3jqWo-iQNVaI3lxyJtv1F6v9uBIfw7_uWF-Ko3M_7mrfMgW5eQ_qYECHxQsGsDDRMV6v2dTO0SwGnUo2nfaI6LXkNcMac-JXoNkSnpdo5nrSlNNAOPZ0ISJI92f5f3aLX-WRp5VSZWpqqJH-ybloupAlmgxZQls-tvjh6lWMAnZixNow8eIl-p4XYxLi4TLgMJPxBMPf9KLA54Yg0LABqTcm10AuWR6eRoLoRPUvBSDEoQ8bBkbqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-CMETcUc6r3II7t4-ot8tUzi7rgzXrmB5n_IBtuOJi7h_gmadMcLHlPTxgBgb825hnhkGL1gqKBJdSY8m9MSR3bZwNQPbYUXSra5B17mlc3A2DO5_WxmQO6lukzYfK4yxIICB4GIZO3sikuyD1vIuO93_5Ik-kHl3pkOD14jqNyvjEMJIQdH0pw_FEdu7bmOuF5kYoSPaN2iFUp8OvFdaP86bEXN7Xj2gQQppxAhRTxtXJNahBHbQ8Rp0ozC3ClRbLhmNe8eNEKM4kZFjOWBZNPjSVUq1deOGeyWXq4v1t64Ft2ofTCh6ANPNZxTKEbcaIkzEDpbRFbnaw4-e2ktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r65_cUMVECRh1d_kX9m8b7VQ0FZmDfcKjK5LsxSJDbvxHVp5xnYLKbeowLxfnN1TP8Im_mqoLpJkqLYkiQVBqM3GLdgd4iJJ-NJDgn0ZsSdo2fsakhBlvVnfI862S-zi1kWLoGe-xCe0YhQLYdCoes_jWGYN8dvH3lV3PhVnD2d3-vmdFEVO1Qjg8eGhBmeew8YDn2JCZ2m88iTbZLu2zI87dlLKDFjSdfoB-B00V3poqMiinoXrZ9ej_lJaaMkHyCNpihs3nT_PfmFbiyHpxISRFAdpcxHFXmAdXp0ULkmpgwd_kG1eNBm2gu3ADaJW0KDnI9h3O4PyiZLz8k4Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZeYh9RPtt8JT0oV05Krm6lQKse0sDn_VbsiLgusg5UJq7DLfgfvaO5DDXBQlVhPXjlMKV1zwjh8f9sqoKU28GzsB43QIYDpxpTJ0e0g-KrtHHhGS4692cNY6hU0e4x2iwC2T8MP9Bc8nb4mtxanQfjCtlht9UuMqRv_ynJipik5D4GgMNpaoQP_Ctq3ZFL4DpjdQJXZKYEfWK81xvCSye8Fer2WIZME9s9zGIwVPkT0Y0zjQFfxA5IloeqiV33Wi0Crvmt31e3H3ROTSHrl8HBryESJBwAU6jJfnYAAmNkR0jIQUB4C3TzKXOW-UabBhSWAIMjUBi-s25V_fnufYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=fjlzRJguP6AORE86-Vxp_Nuru0xwP5JTMmLpt60z2RVC45P-XIx9q-nU_n_-cRQPvdqX74o_2EeyMT2V7cF0jB67_YDLRjaWVLqwahFGgaPc1aGjoU16gGPlAzBZNhBZ3s6172U4-UXm0ebVpxIQOLDEEbj41eQgkR2j37umDnTurkDK3ajPPX8sHCdm1mQIgEgZr9eUp1SWEN0imDuzLFWybEKqp94QQFbkk0sOESK4YqVcQg9GrdxSSfAIFbYWJiZsx0mqZ3LGFHVSK2cAlsZszrtX5HJtX-x7Tjwreacoms5dO3aErbyAjf8Wf0vh8vNkDFShTMnB1GFhFcGRmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=fjlzRJguP6AORE86-Vxp_Nuru0xwP5JTMmLpt60z2RVC45P-XIx9q-nU_n_-cRQPvdqX74o_2EeyMT2V7cF0jB67_YDLRjaWVLqwahFGgaPc1aGjoU16gGPlAzBZNhBZ3s6172U4-UXm0ebVpxIQOLDEEbj41eQgkR2j37umDnTurkDK3ajPPX8sHCdm1mQIgEgZr9eUp1SWEN0imDuzLFWybEKqp94QQFbkk0sOESK4YqVcQg9GrdxSSfAIFbYWJiZsx0mqZ3LGFHVSK2cAlsZszrtX5HJtX-x7Tjwreacoms5dO3aErbyAjf8Wf0vh8vNkDFShTMnB1GFhFcGRmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EIDUG9LQ4wSJlBY8gwmwAu4gY3-H-MR9iAu7mh3c0epjT7rhZ1qWf4dAtqw59yZYCdKE43_WJEiQX2FEeHUc2oaiVuc3uppceq7ZHqR2QsBq4yOptIAHkf_GJcNI-ntqMxF2yl5xfiYsie18KtaOJD582iYX7FdLr1uwdoOikXwxGlUNr2eLTa0ioldr-xdFCB2UrQgl7DoX_5Ds3zi2hDyFhhYXjoe9HxnFLEi9PmBHDyUFILAkD7-TCsdleTFY3zHvV6HFP2p749kfEflFStMX3MeAKKTmeKNjXXXhb3_hklanylQzfTefaEqgYLb6NNT2a9K4D5BkbbgFekRscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=EIDUG9LQ4wSJlBY8gwmwAu4gY3-H-MR9iAu7mh3c0epjT7rhZ1qWf4dAtqw59yZYCdKE43_WJEiQX2FEeHUc2oaiVuc3uppceq7ZHqR2QsBq4yOptIAHkf_GJcNI-ntqMxF2yl5xfiYsie18KtaOJD582iYX7FdLr1uwdoOikXwxGlUNr2eLTa0ioldr-xdFCB2UrQgl7DoX_5Ds3zi2hDyFhhYXjoe9HxnFLEi9PmBHDyUFILAkD7-TCsdleTFY3zHvV6HFP2p749kfEflFStMX3MeAKKTmeKNjXXXhb3_hklanylQzfTefaEqgYLb6NNT2a9K4D5BkbbgFekRscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPDRXCCaAsWEQ5ugJtfGWGYpAWU9qBu_WnMjux-kgras2rzfcv-slvsocNSDc0Dj83Nzsq3xzr8gi-ttq8QQCkWmqVkNDgnOW0m-lf7W0pBkaFs25fm_wTHjAYRyxO4bb1z_jj09ea8KdpAS-qm5Hl8IbaA6a3oMBeuJe5dxEp2ON4qQ9VZD59oWEZ65R9Rp1aXls2CtqvUi2Ittt4P7hFEUF9v7-uUFK6DYpggK24BVndwPTPnYUdfeSMseqviT1TYJv4oVh5Bolr3qIRK7vhbwTRPiFl4gsktXduNI7CraOKfgqn44A2wMZnvoD11hVBpYVy5nHjb32OZQmK8-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usPK7IvLMbE2UrVNg14XzKb1Pv8ruo0TxPPpCPowNuUFEGOoqSv5awcv9RuLBicSXU7N87DXIGgmmratp_ZWxCoy_La-T7k6wO7WMZxa1MW85J6EYgUXuYI4OabOwibR0FM7igihJ242R629xobmfki2OQk10k-sLGpQ1TpHvvOfV0p13OM8b-aM1xXzuzBaNqhzis0fT8fqZlplZZ08h7jQazinZa_i6zLNGtWDg_d3Di2reReC8ZKXC8BphI2OAA3xD_GsEhaAbqhUOQoHOtj8MVyFFWBQ1_Ir96_Wsd0sSiPftMG00VAaGh-b7cxFU8-CkkV5QGzW6cC9gk1HrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9WsK6mM6FDYwL6c9T6XMyGLYW1hx947FmWK2ZsGZwbi_11ny8ndq2zz7s3eua1XEH0YJZgWtkGEGrWndCumhxM9fzuXFja6Z_d6eNCT85DG6tSUctSIKdD7PvYbEOW7UNMmsozbeyxEMy-DHzq_nkeerZxy_lFMpADRp1mADZW3c9JMaPL_l9vBb8VIt8VmUZXoKcjXzlYIWzEB3VTYDE3bJ_JzxLOEAOwTVNyf7dzudy9hBFXWyHRoJKE5hFCDrJD1E8Fh8-JvEeBFvXc3w2wJT2xA5q-4lY5bqQj0YHWIORD6VHS09HqMnUB4La3RtLV8_8CJYzTAm09Rsqu71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cttoojcoSiYXx9MfuaFQILFNLqqy76kyxHxMuzkcCQdyEeiKSnFiEf63VoLPi7AVm7UrQ-PHcQUyQZMmp6INvsSBYfYTVUVUcHboJQOBo-9dHhc9jP182ETz0NUGY4avXbl2_8n_pPjntyCg82rj-PIBZMXsAxHFQB2WiIajzwJdybi-_1BVOt49o9CFlD_6R_j6vSvFn4HaFuSlxiGiVI2V6R5fXB2Xr3tyf3OzKeBtIUQ1K_lFzpLbs93Sa9BGA-WnCwUpvkw6z9D4n_EQcaqHWoue4OqV6dkCZZY646FcVfKTT0nbsQuoe1bdZ29STH-hxlh3eBEaYt6T7ygL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqqjVy40McybRWo99TVR7ExDiS7iiPIpVhzO1pzRqpPgrKe-ofiZtx3Sig7wAgjOK96jnVIcYuBQ6BOHENT17znKb4rv2Ilyvc2GoU57OOJa-yfaHTXbgWYCgrdZFIimIzMwJwjzG33fHK21e6otuUajkaEdKdTgzHiZ-R0GlLVTdPY0MrJq7Odtbqw4PjnIf4KFP_BxPKVMX1P_dENU5ktLjZaT6c0Gicr6cEGTsV9BqNnrDM-ZWjm3BvDTUs_ONwmis7BOOSYYPpQBAHKbo_lEjjs8BbZve_rn9Ts8ou8w207RLrJWjvhKask2LbnjW7fLDst4JaeYgh6cx6NKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_R_YRsyMrs12jxk8kITv7wj-7ODSZu2wMhxuF-PsPdHbH_6I80z_VzIU5F0DMnQzeVkHKksYkcM9nH2mOLGNOSZl8sz8yFCs1tT5Mqb6wHLUGZtfgSXfTMbWGxQonFOUJshL_omTbDLK5Ox5UouH5UpaRufwVE2R0yxnt52EJmaLeEtyRPJrXWOTRFLHdA6O02M06Mt367iZW1_mtkyXlgTEtoKyckcqhOrjBbtHw3FzCu_OCxvzulzqm--ix7XBWbTabozdAgmEz_f-IPKvkqT6hAepdgSDtXtW7N9e-Gdk7wk1FE_G9xP4QZ355Cxko3RGtbL0QgFX1gAbmUEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uu0q4aoai919DZO01w9oKnqWVWnD6ST0u3vXxHIVHDFyw5TeHxbzbqUuTQStCpFjkq2TMw-kyVSEQUXhPqSYPTgdMwFdlzvpCWPbgHVCE6TPY6LUq6v8fGtOOHP_SlXDOHRa-Lev-Y6omhPOG1-1gAkMSs0x85lva8Dl031caxFAHXJY6CIyrcAHyQRBPwjqhQGRZ5VenbmNI6QVL4roW24t5hvDOLHL9IXrAowFnZkorrdPm9Q4a4V-RQq3YjE0uvgpKQT8afita2YfmGqqz7IomVjxjSxaWWiE3WyXx1zcCfyCYcrDbljdTgYeZmsyXmO0uslA2LgEDX8_rA_K0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfgJzCWDq66HFgaqdh9OVwNeHwqgVQt4pBIdM7ljrHrUSzORKyyPNT7Bt-6PsOhEtsr_61r0cSYyW6NorNavO-oBOpe-h6ZMrHSVnu6I0Yn79C1RJqWY7hl7gQpwbA1qtfKRS7nn4lDJibO2pt_gj3UqfdXf_Sqp1HZEASIwA7LhF6p9LIDRbQY4XFBo5DPhxQoWitaLyOYcxAiZ8Jxg5AZit_nuKQsMabL68h9NN1fpVWotcTt-mD8zPFvO-uGbOCmll4PY99SbMOrseLjqLF4vJ67a8TQ8Fze5ntX9WV1RcrzpftY7IghgA0-U5MyDsmEq8zL8MV2unh4H_LPuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObgEMBSQ3SY4C4wB4M39-2SHE8J8-AgzHNHMxlcL1KsRsoJe7wWLH9Sii-PXtF25tkZsjG5JuOm8AEhEC0YebhAW-9iHkXyXi8QDzMgock6RoXiYqBTNlKgY2MyF5kAUfj6eUt-DnADYLELHb3KsUaFCYztouVkQns9-l3wO7uOKfL_5FF99vlme02krJQEUL-6BJMqJGp9VM83lwNOHIYkn-J-z7O6JPWIgqPVpcso9ej8vGhPGIpOWKwHvGs01idrlyCnrw3QzoUY2L_2qpXT0f2FFvXyP7ZYho_1Lhi0P0ftERgtx8Y8r1cEbsL61WuUejRy42t_N9mJwwjP_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgy60DIFS2hyVX7AV4Q0rpf7FP0VQp-ZuqvII0FrcbGWmtyuGJ-0_XVubvsaERcjfztLQQ_czcUhb-zlSyfTE5YfwvUUiIILA_LfBhSIXspFGz8E2pgd609L7lSBD0Rilu44d6Q9ITumw4nuYMVmxEedxvtZV0v47iiqLwWt1boUgwcKd43kme-W6LNt_mXG_h2g8TiyZ98bpnT7oo5_zdru02V1XwSPGIyQmYAAvL7LJEqqN0epPiyagfFKhBAc0SQ2wcfYfqAKZcRSazedhJTGhivnVyPoo3Zw35mGo3hlps8HCn3PnG0VlbuLdMzT41_ExNCmF3QLo397CEhCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHkkPu6Q03vdTy2lh3N4b3VJFr40_N-gqS_cveMb3EZ_1wkU_amOEwRfFFyuXnUC_K1HDaSr0LdGXTpq_JWLQ-bGtrj8D7oudxpg28TB4ui-8NOoepcqUuUdN84hSuBFMolY-ZYb8HIProQeKvl2TbbGB9L48XvXHd_qbK3GzQvkQEztR5EuRulAcLOw9sljxXy2VKXyh_dFYrxzsaQ1mxn0NIp9N6V9K5TdrvoxXcS-ARwK7b4-fxdmyQIYKPDaESm8NZyID5jJoMyfwmgG9yNm0_rhNP5LncnmKm5sVF57M9NhcynC8fw-me7j2cHIjFAAjf19TqyWi02J2mT0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbbMCHOt6qyCK9rAvhXkL79ekEuXXxXHTEjY6_kqdAwY2vGf_AlWHlCfkCy0GioxeHWJZwqeFat9WNP9vELVpiC3QdwS86SE95YioeAxrPqoq94rfP_BVTNaQC3XeAPuR0SaMAitE0qg434_5T--vFcoR8dArS7MQa7td13OuDs-xB8gBCT-ccuwS_0tPWQ2l5FVQd6zdACX9fcWQ4PFICOH4_dKjSc8FBpBdcCU95djeORsYD7rP9lJgwRGWvrRg2CXeRYcjoqJoL2f3Z81_GlsZLy99sgpnyqHvD5JwXxULuJOJGdCHqC2B3-jZ9pX8o_V0zRPkFXBGW3-CbWdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQEEMmfedZH2k_n7UoKLKeqT2eTBLh4GYRQkYRL-cQqY0p_ChD4TTFj71R9cUoZr7i6hJSQrGH1OSNC5agAwlGpGaHyhAcJ8CoCSaHMUwe9ipjfvn_CYpNN48DO76rb45Y68Jqsza0KQS7fPih_tYsX08hmW41Xkk6c-n6mOI6BbGaOuT3KOglq4FLxDVGQWQwogkP1iB86X_t5XXygvh1IkKvw8MjtvQ224Lxiwid2UnuZgN3LcQME0mS-bAE7IO8UVcQjU77rmDZl2HrqvTmhlhUSU2KBmxR04Git4dF1wNUHl-ZDuk41PyPa9ytBsSYabyGEuKf6Ko_JshU1PvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbtzPkS9Sqx7f-W9yUQHZWcFxr8luZ7Y2yMMTJor0Mo3SLzxBXLg-sDran_XEB9SWAxTKbfJmGbE5FnZLrT4DHZyVKXt3nbalBx5WNkxSs6u5G1flI5nOZgAetONHZFcDCzHTEy4jQPUCh1b2CI-zqfTanVRVtFyGISeLGLc8pNszrNrtYxDC2y8_qOhcbxRBW7cHWwpA-TnucbXOpicsjQp-pFwjbDavbCj6emKU_baj-7wSXaua_Z31y5E4StqOcr1u0zsNkOw7P93LBoGg4OEAhh-es3sXEX1wdXhRXd2M_KVCouXXW-SSpmtCByfV1mOsIOokVXZtyJbZcfBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4zSynkilZMCocEGDYgv3ycnbiQCULaECwZqzkUvj9AIWsoGfYTS5gJZxvkvz4rgOS5rgrSHmHJiqZenUcGzrnV71b-wmwM0Wmnl4q2ZLGS3zceycA3fSeM-4Fx66f0mLhtJr2WnpMQAU9PDSocIDUIzRUfeqmgJt7AyBNHVjw5ONaICP9FaRnrXyYh7UYM3gyn77axbGXOLiOLhmObY23FShjYVVfV879NEE5-_ogCwehtQtTvbESN8rIMhdEXnbjW073gaG97IRj_N5P3Bx7iJiUxUHk5TY2dnOQtO3sRizaaedB0iwvhX304QGEtXM7g7uLE0Sg0QXb_0GYy07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=FTkWdYajoXuvsS2cqtPTLgWqzRtTGgOnafX8qOwgQ4RW_abOT6jEou71BhplS1Xn8Tk7tXOE_d2bOgeEOQ4NhEuzSicS7BlN2NrLfIgBJjPdOXMHkQXq80flYPxnHh-VdQpbjJ9F6D-2RRtaF1eHtvQn2rh6Jvg9-itAyHobbDpHWYoFUJtla2VQOrgu3crM1NbUmjbAPgu8Hz9VAmXPmAhdY6r77eV-MuViQfB5YxebJxYDyKjp_B5uHCGGGWIf9DkyGAom1znSitZIYoYj7_MeQM9Y8TbBYauJp6FaPXJMtmjmaEHwuIjk6-gs63WSOojXuDwd3o21Ly5kSUM2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=FTkWdYajoXuvsS2cqtPTLgWqzRtTGgOnafX8qOwgQ4RW_abOT6jEou71BhplS1Xn8Tk7tXOE_d2bOgeEOQ4NhEuzSicS7BlN2NrLfIgBJjPdOXMHkQXq80flYPxnHh-VdQpbjJ9F6D-2RRtaF1eHtvQn2rh6Jvg9-itAyHobbDpHWYoFUJtla2VQOrgu3crM1NbUmjbAPgu8Hz9VAmXPmAhdY6r77eV-MuViQfB5YxebJxYDyKjp_B5uHCGGGWIf9DkyGAom1znSitZIYoYj7_MeQM9Y8TbBYauJp6FaPXJMtmjmaEHwuIjk6-gs63WSOojXuDwd3o21Ly5kSUM2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7a2HiqciZBy_doZgXUq6-bo3288sPN0gemT2s6HKcyYxVcSZTrsiIFngrELWDOyF-e8KXldkKGVCBw3hXBmoGelcpO7iXsoOmvOx_xTKxFwlMAmnH3WILGt2B57feEp6i2kEbJulAYd1Uwwh352DdZDNNMqpTWEfboeBIXPgE-gIMYVRp6W6TLTuZ_s9w16JyYi_IABZ3lQBgg57KPlYD80ls7IzwT8s3rb5heQ9azTFXf7Atqz6F9f5XqCE_vzg6_RXP3mZgEjzyHr8dd_a4Y9srav3SlkaZr9WBSGbsTAgKnmJ-Zmtay70qegm6Oja07VKuCIUqwne17N_BP4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=cbN2hDTSJ65mi1skGjdl8T8pFgsx-FmKQMwOd0t4bwgAZHw2S_-dEE6KoFL9889nLNHrEHpRLc71vlOO2jksz8p3ezEE1KxTw4Y5rDU40EtUDRXs5Evpps0ZMDoZ1jp973hnW58O8ivh-ooOwbWJyNLzanhqQ9fBLQIalgQ0bdPefoWXvkivbdOixwor4yv0oPZqG7MZdAyGpMXN9CkTR8brg8KHQcGvC62eStn79sQf5BYiygKf-vNFtk62n3UeCFU2ybY7ljcW49_iUqSYb0MmLwoFURxkcwUQJQlMk8ZCOuPkw1Xl7NUFsY6AM5pKrGfXNmSQ-O8QZz__R212oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=cbN2hDTSJ65mi1skGjdl8T8pFgsx-FmKQMwOd0t4bwgAZHw2S_-dEE6KoFL9889nLNHrEHpRLc71vlOO2jksz8p3ezEE1KxTw4Y5rDU40EtUDRXs5Evpps0ZMDoZ1jp973hnW58O8ivh-ooOwbWJyNLzanhqQ9fBLQIalgQ0bdPefoWXvkivbdOixwor4yv0oPZqG7MZdAyGpMXN9CkTR8brg8KHQcGvC62eStn79sQf5BYiygKf-vNFtk62n3UeCFU2ybY7ljcW49_iUqSYb0MmLwoFURxkcwUQJQlMk8ZCOuPkw1Xl7NUFsY6AM5pKrGfXNmSQ-O8QZz__R212oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=u6godLqDmUVau8yP5SWaIP_y1wfraTs66MUKvpLKYv6aaITqgWJRo1SmOE4X56IF3EQFIoLqCd7rX6NGBw9JCc4K-rlpY6kYBxBGqeTs9_XXOwq9YF7TlO-NoFUKfDMaH38ZHYAL8lvULW_CHZrNApG2ojr3PFlqCWOxTACd82DWA3c2aLfth2NPQT_VnjmLQIRipNL9LSBnEATGZ69-6gV4csTSiDoKGXiu9bKPhqDS8DD6UQBPVVi4TvjBHWv7F16XIdSkuCEr2HupclQ39Ck3mR8JhgN2PgOnQmwtUn-kco3dR6Sz9FTVP31TEWLXAuGrj6xUsvlWNlI7UowAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=u6godLqDmUVau8yP5SWaIP_y1wfraTs66MUKvpLKYv6aaITqgWJRo1SmOE4X56IF3EQFIoLqCd7rX6NGBw9JCc4K-rlpY6kYBxBGqeTs9_XXOwq9YF7TlO-NoFUKfDMaH38ZHYAL8lvULW_CHZrNApG2ojr3PFlqCWOxTACd82DWA3c2aLfth2NPQT_VnjmLQIRipNL9LSBnEATGZ69-6gV4csTSiDoKGXiu9bKPhqDS8DD6UQBPVVi4TvjBHWv7F16XIdSkuCEr2HupclQ39Ck3mR8JhgN2PgOnQmwtUn-kco3dR6Sz9FTVP31TEWLXAuGrj6xUsvlWNlI7UowAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoFXdMXcHyGymxfoOopJISMe560owGISrUykq7pUNeuFW2j_23y0AsZKbQNUuxIsmm-2z7WJjvibE3yJlYgVo1YmC9SJ035RPvf1D2RlRsb45B4nRrruljg1wB_77BK5UbBSUryyOS9SmU25q1Y-FsRsMcu3g62jeYAk7uae69han5dJau-OA7cgbMW-JrGyVFQfeZnMFPlIKls81jTmxBy9d3Hu_94Hf6Jtc_RJCu2wZwU6oFv0v-ds-PR7orb-pJKUoWTf_cVXky_uoOg_d9Y2DoLipw054EJzlfeQSW80ZnGGwpDNx8pFQdXpFSGbbOfOWBRPs9zlO8_wCvqjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=QRwHTNZSuGjnKI7o7OJEgEBx9OS22ogvFlDKGT5bP2TyRMqU6eE8cW4Z-axWPLkrX8YCElddgU24kQKrx52tHBdmD_SbpMyY4Ul_Ker6-fdxCN9PJhmUEVJpSg73692EhzTJgVXEyTKw5G5qYERQ4-ZeTXsVBMhDthsQBaycR_xLvo5x86hDzwqrSlxjH3qT54PS2OYAuh-O3FZApb3M9s21zaH6kynJiG2tytTC_IAhA-ivq9RAI1QU86ME9M_z_1cnvhbJvSjc6QEeG8QDEEnJHRt1n9wZKvlhZiA7eHD3e9ec0I1rDPi97Dg0uBIpN-yDlzSPiQjpcccoyPg_Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=QRwHTNZSuGjnKI7o7OJEgEBx9OS22ogvFlDKGT5bP2TyRMqU6eE8cW4Z-axWPLkrX8YCElddgU24kQKrx52tHBdmD_SbpMyY4Ul_Ker6-fdxCN9PJhmUEVJpSg73692EhzTJgVXEyTKw5G5qYERQ4-ZeTXsVBMhDthsQBaycR_xLvo5x86hDzwqrSlxjH3qT54PS2OYAuh-O3FZApb3M9s21zaH6kynJiG2tytTC_IAhA-ivq9RAI1QU86ME9M_z_1cnvhbJvSjc6QEeG8QDEEnJHRt1n9wZKvlhZiA7eHD3e9ec0I1rDPi97Dg0uBIpN-yDlzSPiQjpcccoyPg_Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lagLkAZyvK7I9xVw7f3ZRjPKv4CmjmJ4QY2l50hmRI3PseZivSb5F4zMce_p7lxNtRJMcRPTG0rXKWsXuk4KJNLy7FVthxqmFd1QNjfXfJPyDjdFdfRgkksbEOBLFeL7Eh9ekdenhJusu7TiYV8mryxicvvXL4SQUTAvabSM_20tvt0NXKrqdyiE5hKfLEIVdlAFrhyp8e-YwVEPBtN9VGuZl4RinaKECcNuNQgSqy8iTU0bKYaUXauQOderpdRPb7U_DYldHLnkUlnejdz9pajxmP_uuiDJd1qlH72jbIVLOa7g7bKrss-GSfW99_oGNxLl2VUi3D3nFG6c_6O6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj9TR7GhexxHvzM0zVzF0yLdEIIIuiwwp6hjk85PHgt4fVZjDrqHi8UTLpQweQtUKy_AVd_ANlGbX-qAuCwJxk32Czoqut5cCevWBsGojRXlMpabgS87G3ReCaeIbL6vBR8CGrccdEo6A4ACfAmhVbgf0bBUjNUTy9oaTPQJV-MHEr9TxP8-lwOmDpcnTB2GNIyOG328pYtZwPOsGy9McquXq6Jtj705Yp_z1Ip5zgKnrq9-Fh_1JpMRTIVgB8_qKHcLfL3z6QFJ3Sd-6oo5DqUG4cBFQAV29MLQAq5xy1DnhEuKHdioEqUzHm5mAjKR0qMtgFvA2181AR11mQBcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meYnEDdkF9TI8pPCTKB6xYDZo4OiVH849lRarDx_l_g6NTpzSH97T4lM2ur-s0OVEDeEbJ1wdkk5wPJx-apms26cG6cBRlJd1LPTnFC_jviordDPG6utFPxPgZsjdbtkbnfxqk-4hjCnu1aJf4Dd1IFddKusfDTrw47RvMH59sY6UMBXh6aVTi7AqBUpY3Jxvt1ZIEgdUNqSiGzLRDlYgQhHWcapp64MkkEECJOxQryzksnhREnEZJhL8IFL2fKwdReDDo5PPp82ei3rJ-LSetzepfL1s1i4AFRGWvaHQEu-HGbvArehUPos-JSV7zDSMOLeVXIu_7usNKmj4GYz0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGpddSO7NfRazldnE8tHkacCDnnyHOC02XNNztkyhubnpn8lh0GM_3MQ_rf8wl0SUHERKLegMQ2l44LaB7EJ94aa6LN8GGroq7aiEKGpwfbTRBnKmIWT_RU1JUXkjIxcSg84uJq4b-_mp2q2rRqDlHHgkKoXCjRLNu4MuXTNuXf6giypzqCPANs4V35thy_Z8DEkXseJy3Fo13W-qZPMhBYu9Dum0CDdM9l2Hsh_YhBLLgxDtLL4LCLtC0vc2jNJGbcNkOmuqPE4jaF0df7R5-x6PPnmjKJQvPSlmT539i9YXe9wpTf6YohyL7vH4EAIS83XDWWrzcQNpjiAdUDzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=XRbxFxFS0W21ufEHVUKjlU8AEcTtoTVDtebJYX5hut7PAyIye9P03g8keb56AAOjbCQ6-dRjmkQj1bcixa2WCRKSpl2eDE7-jLwqH_V4VnaKRuTs8vwz_wegBdaIk8qk1zticdlW0jbCqEKb3BVGoT9RBzXa7Erk1-saF8T7b5CqCRbBQ81ar7vJ8z9dPTiDwGN9i7AXb0KnGmdUuRrzIHxht2ZiU87ey0meBUfsZ77HXleL_zia7bn0il-cXt4pLHT4h7LrqWqspBQkCSACXrQHriDF-aKpBHickriXc4f6yXc7b3Sn23jLckTJVCACO8NaGGH586c_5gXzMOh7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=XRbxFxFS0W21ufEHVUKjlU8AEcTtoTVDtebJYX5hut7PAyIye9P03g8keb56AAOjbCQ6-dRjmkQj1bcixa2WCRKSpl2eDE7-jLwqH_V4VnaKRuTs8vwz_wegBdaIk8qk1zticdlW0jbCqEKb3BVGoT9RBzXa7Erk1-saF8T7b5CqCRbBQ81ar7vJ8z9dPTiDwGN9i7AXb0KnGmdUuRrzIHxht2ZiU87ey0meBUfsZ77HXleL_zia7bn0il-cXt4pLHT4h7LrqWqspBQkCSACXrQHriDF-aKpBHickriXc4f6yXc7b3Sn23jLckTJVCACO8NaGGH586c_5gXzMOh7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=qlIKxZ4ND6oY3BC1QqG1s9zUTxKXDLuQhgJvRGRJt_V4J_9LaNA9nwafWqDYzUkcydj2hXtEDkta5UV_IG8KsBoc1328qvNEYjRbV9E6rTYs7VOBKbPdgclNmlfu5fS6StALddnuu84HMhX4w3R93HGSYl88bfRWXWGAkcH9ExP6giitK76gpS9Go3HrF2VLjvxYJyA7_1eLff_pEt0VBtAyUY2rXB9pDoUU9DvgaKuicMDpZkCn4pMO5nIrFm2fQY5JOybhYDPIDIkzGbzJ1c63kVmjcKnoCQY3OjCAS5E-eWO6SkZRrerUW8CMbij88cKl-cdQLviu1yL9covECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=qlIKxZ4ND6oY3BC1QqG1s9zUTxKXDLuQhgJvRGRJt_V4J_9LaNA9nwafWqDYzUkcydj2hXtEDkta5UV_IG8KsBoc1328qvNEYjRbV9E6rTYs7VOBKbPdgclNmlfu5fS6StALddnuu84HMhX4w3R93HGSYl88bfRWXWGAkcH9ExP6giitK76gpS9Go3HrF2VLjvxYJyA7_1eLff_pEt0VBtAyUY2rXB9pDoUU9DvgaKuicMDpZkCn4pMO5nIrFm2fQY5JOybhYDPIDIkzGbzJ1c63kVmjcKnoCQY3OjCAS5E-eWO6SkZRrerUW8CMbij88cKl-cdQLviu1yL9covECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=rsYpyXztK8K54btT7UlnBzKJ5IkmQc2EUNGJAj_EJEqP4ejA1rdsL_Z7xXbnpfSbTFuPy2JmFQRm-H909yz5JhL2tAUmMGaPpXK8HjSoMwGlwd1hlL8A4miiVa6Q5GZDAqJgFJVn-A-_Er-tIHzIAkr3zfeU-Qa07Iae-TBdYcIlcP_o6vHZ_Sc5u1zKr4H-8GlSoN0Vc23Um4QUcP4giYOsK7yVq7eMJ7iACk6heYJiUUIV4UeDni3jq6NgfHlhbOWWY5h_fy0rc0oV-8WF_jOMqVqEjaA6Eb9d0b6xYs7-odJ5A47ZAAfHb0SBw8KDvSFOaqwoyIwB2tqNQxkNvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=rsYpyXztK8K54btT7UlnBzKJ5IkmQc2EUNGJAj_EJEqP4ejA1rdsL_Z7xXbnpfSbTFuPy2JmFQRm-H909yz5JhL2tAUmMGaPpXK8HjSoMwGlwd1hlL8A4miiVa6Q5GZDAqJgFJVn-A-_Er-tIHzIAkr3zfeU-Qa07Iae-TBdYcIlcP_o6vHZ_Sc5u1zKr4H-8GlSoN0Vc23Um4QUcP4giYOsK7yVq7eMJ7iACk6heYJiUUIV4UeDni3jq6NgfHlhbOWWY5h_fy0rc0oV-8WF_jOMqVqEjaA6Eb9d0b6xYs7-odJ5A47ZAAfHb0SBw8KDvSFOaqwoyIwB2tqNQxkNvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=nZ-mrB4DFnHArdCHVXLemKjNf8D1f_bIu5XHe3ebZ8-X-dgJSis1KHFEOE6CuNBbNH9uWpoyzPZDv5OtbkcvNMNt6OBU7Bzdwo9FUeQ4NPex_bOcP8sOQ2N6k2s-z-tycbWpTP09I_AeYp0L-qpdt_0OEVXw7xo0OR9gvRjKTO23WOeuAgqC6RLXzufC2-s2Nh8CiTKjqHM790Voz3iJ0mXJuTAsdmK-BhI6PV5rORNwITmRwLa3qw_dqvnjcgZ489xstV6DAMLGaNdZNh0-g3wVBAFzoBIV7PYMEBvYVeVOm_IDPGey8MyXXTCN0vzjT6DM1o-bLYMexZLsBrK94X-JvsAU9Vacgxw2LGHuxHYL2eDfL1AUuyh6i6WAsNve55ouWVz5mMHIEFekbN7ire5U-OZZNl3TEbg9pNby9LppeoDECmci809Vl0GYWB2-sOdzshqDRw8dIVRQyXXY0LMvVuy9O8smwDlFemXCeFALi4gfMQLMQxOX4zxEgwmM6sWPLj_6ZdwGOSS5p3EQ7SLGbPmZIfBBEQ2y2tO3twBwlPn0bZMazUfVGX1XmvH7120dUqfnxRBjcXPHH7CzqDQMZ9LWu1fXchJUYAv6mqljQh1n4hW0bpbAQN-MvpOv6_c9V6c8Yo11wWql-QBdjeo2OG2ROLDCMixfPOtwl5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=nZ-mrB4DFnHArdCHVXLemKjNf8D1f_bIu5XHe3ebZ8-X-dgJSis1KHFEOE6CuNBbNH9uWpoyzPZDv5OtbkcvNMNt6OBU7Bzdwo9FUeQ4NPex_bOcP8sOQ2N6k2s-z-tycbWpTP09I_AeYp0L-qpdt_0OEVXw7xo0OR9gvRjKTO23WOeuAgqC6RLXzufC2-s2Nh8CiTKjqHM790Voz3iJ0mXJuTAsdmK-BhI6PV5rORNwITmRwLa3qw_dqvnjcgZ489xstV6DAMLGaNdZNh0-g3wVBAFzoBIV7PYMEBvYVeVOm_IDPGey8MyXXTCN0vzjT6DM1o-bLYMexZLsBrK94X-JvsAU9Vacgxw2LGHuxHYL2eDfL1AUuyh6i6WAsNve55ouWVz5mMHIEFekbN7ire5U-OZZNl3TEbg9pNby9LppeoDECmci809Vl0GYWB2-sOdzshqDRw8dIVRQyXXY0LMvVuy9O8smwDlFemXCeFALi4gfMQLMQxOX4zxEgwmM6sWPLj_6ZdwGOSS5p3EQ7SLGbPmZIfBBEQ2y2tO3twBwlPn0bZMazUfVGX1XmvH7120dUqfnxRBjcXPHH7CzqDQMZ9LWu1fXchJUYAv6mqljQh1n4hW0bpbAQN-MvpOv6_c9V6c8Yo11wWql-QBdjeo2OG2ROLDCMixfPOtwl5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=iF4qcqlDhgxrao_79-matU6wUb9L8YolPPTeJZnRZN11C5xeypB3EQHQQc9JoFc04UzN0BeN8uoK7ExWhiF4ZVsaAXmGvpBrBfLdCwtfBYcmpbbJICE8HOc83kEJl2OYPLFakHHmtEMLojmglSrrdIz9NmAWdwC8SDaC4PaxRw_bxLKL0P27k-Fr2wRCrL_nekIJ_BdEk6A10oNVPsssKQwzN86I2lkMFBpbAafOatqD1s4JTfC5ZGceEMlFyMXjaysNfRaEf7WiGtNOqxWLyjh-hAMRijmHsphRfi4ovO_CvK6nGGlof5a-QHTI-VFQ-8k_l6oV6cBhw3D9uO2y5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=iF4qcqlDhgxrao_79-matU6wUb9L8YolPPTeJZnRZN11C5xeypB3EQHQQc9JoFc04UzN0BeN8uoK7ExWhiF4ZVsaAXmGvpBrBfLdCwtfBYcmpbbJICE8HOc83kEJl2OYPLFakHHmtEMLojmglSrrdIz9NmAWdwC8SDaC4PaxRw_bxLKL0P27k-Fr2wRCrL_nekIJ_BdEk6A10oNVPsssKQwzN86I2lkMFBpbAafOatqD1s4JTfC5ZGceEMlFyMXjaysNfRaEf7WiGtNOqxWLyjh-hAMRijmHsphRfi4ovO_CvK6nGGlof5a-QHTI-VFQ-8k_l6oV6cBhw3D9uO2y5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=U8eCiAszXPHsGF8uOXj8S9WNdxuP3ZhR3y5mVa7187B0AdPaf5miTYMZY2AhmQA9muRZoGb1i2Cem_nUsbC_gSGzKdnCieyq62-Ls35Yy1CPb7wKgYdlzXqsFx9XvEc8p1qqPRHLK4869qbXIV80rcNyPQJUNYo85G0L3zuVYe8BfYCzwr3haBDOrWskp4TxyqH39PYqMubDwtlbXiIbfOPvC-eESM7ybdAhX-Ay1qeJxtm-_l0LKxcFQLIsKEoznxoFJKIVTSkJ8j1jXT4ZHdFFLANxH1U-sNE8y-ghnG6NlPcEUn20QVM5BUAEkwQqOSMBw2mBXjuoF0ICziA2KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=U8eCiAszXPHsGF8uOXj8S9WNdxuP3ZhR3y5mVa7187B0AdPaf5miTYMZY2AhmQA9muRZoGb1i2Cem_nUsbC_gSGzKdnCieyq62-Ls35Yy1CPb7wKgYdlzXqsFx9XvEc8p1qqPRHLK4869qbXIV80rcNyPQJUNYo85G0L3zuVYe8BfYCzwr3haBDOrWskp4TxyqH39PYqMubDwtlbXiIbfOPvC-eESM7ybdAhX-Ay1qeJxtm-_l0LKxcFQLIsKEoznxoFJKIVTSkJ8j1jXT4ZHdFFLANxH1U-sNE8y-ghnG6NlPcEUn20QVM5BUAEkwQqOSMBw2mBXjuoF0ICziA2KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaAPkKplSQ_5k1Fx3OlWJj0HJhbe1tZLS_2A-BCkdeOeT1mW4HHSA6prp9Ca9KVORduYu-7xq2sXtYVUk-6WYhiLSUSnRIQGeAxxzcyscROH5qBAhWxxonTBoYMDcGOEuWyLBzuQ-5__xYGObRSLZGmfBVqqRwEFLqP7F3pvcEe0FKKUdJh-rrdZirSTPG1sNrHIeIQf32KNSu40dOXist1-AbU1b_9h2j_tLJHN5AwnEASFT_lslo0c88DWGBwA4V_uZp_1FmBU_afcpHLAu8Vgr43jWNTJanuGP5M_lTZMyNqpS15Gdo06WEWUacyuM3GV3RiHTAIxiMiCmXUFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Nzy-G8HP_xYkjD8-9ecAELjk292YbbqKaqHA1_V-uEZ8AXqdQhTgDOReM1kxcYQIwCY1N3BVQuLFeTfH2lWwXL-UQbOGQuPaY5cnE1MRPXa7ocaDsPEcoCsB-X6VveM9_TJuTznAcGm6KOV45rECNQ2jwrkhkJN-lmVsk9E9s4jwk8ML54_XXhRXbUhaN2uu741Iiv4FkQuns6bKnmGIc1i7CV0pKN4GNEpxTyfI6f7tpVwMbenOTza8akTCBju02RpN5eBOq5V8_a5GI2bm9JQKQogyaLVpJdc8cSfPnDKC0RO5IaNv_eZIVqjwE-hv9hKW16IfaAcqYpGEJuqGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Nzy-G8HP_xYkjD8-9ecAELjk292YbbqKaqHA1_V-uEZ8AXqdQhTgDOReM1kxcYQIwCY1N3BVQuLFeTfH2lWwXL-UQbOGQuPaY5cnE1MRPXa7ocaDsPEcoCsB-X6VveM9_TJuTznAcGm6KOV45rECNQ2jwrkhkJN-lmVsk9E9s4jwk8ML54_XXhRXbUhaN2uu741Iiv4FkQuns6bKnmGIc1i7CV0pKN4GNEpxTyfI6f7tpVwMbenOTza8akTCBju02RpN5eBOq5V8_a5GI2bm9JQKQogyaLVpJdc8cSfPnDKC0RO5IaNv_eZIVqjwE-hv9hKW16IfaAcqYpGEJuqGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2KGylSRlPybYuwG3Ig7p6_Oiz9fQtLaE5RXRkryf9Sqgf_0vn4CVsDh5F2jxFDhEwGt0dCrnTZMMg6DmFncqzXD8SazKADQoJ6-VYAu188XmlN0bi_2I8IcCGQQeDXYlXqMJh1B08DUQ6FrqUC6PNxFoLob-Rpsgw4LqzkPdRUOFclpu3xjfZP4EcMNyIawaw2EKeR5jrENaAx-T-_qegnNmQdxCo2WbjM_dQhxZ4EDWCVaN3IRK-OkMidi65enAnmgVh1MZrVGIRET5hQ3dMLSneKTVHf-Wd3z6zyCF-6SG15sV81XBF3SyfuHif0CvIKGIcT7K3xOWgINR7BCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVPFrRfnbbjxui2FTP30a09sJT0qCR37PvDGwkfukHY_7g3R1Bj95lBfVkv8nSncvMLjuJAsT0UikrCXu2gzs04aMkrkzDWF54ydCv1YzrvkboaUUVQZNnnzvuT48FmjWMn7fNPrO0g-rEJrigqXjf2UXNSaGwYMv9pY_24ntFUTji4hywU-hg0RqThnEzPtvo0_1SqYbGM-MXp-qRpkSrbJr8UyeUU_WpmsXb4SlRU5lNjeqZKM5Vdie5VN3CbODMUPzRiiV6nzZGT4-znJW13Fg6tw1cuekt70iUTieof9ECpzWt-SDs5VklEjw7O9H7VSGSNXUwtsWSu1RUl99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=psP3CLzWc9Ai3JcdeMZ6DIohQgZErhPYclexox6OQ_40gaoKxt_1gMj2haRGFdBmIn5AZdF8kQVyecuocwuaP95Xt4md-M4WqWOMiw3YaN4nr24NviIbMrIJwRb0xO8YzBpPiTtaOhBEx2hnJycZmfaXc4sSt3RnA2Y1Nvk4EhOxes3V_8AbYGhiknRNQD2qF36urr_EjzkrVURspGD0YotyH7avlrFlzINJKKTvtM-cU7CgYvRrTguXhUVvnB06RRP3KnimLSds_eHZyKJwWfoqX-sA6sirQMM7OfsVlY6C5NQ78hjvc5YJ-bv4MW7D9gDrlVUk2plmq7f2gfrejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=psP3CLzWc9Ai3JcdeMZ6DIohQgZErhPYclexox6OQ_40gaoKxt_1gMj2haRGFdBmIn5AZdF8kQVyecuocwuaP95Xt4md-M4WqWOMiw3YaN4nr24NviIbMrIJwRb0xO8YzBpPiTtaOhBEx2hnJycZmfaXc4sSt3RnA2Y1Nvk4EhOxes3V_8AbYGhiknRNQD2qF36urr_EjzkrVURspGD0YotyH7avlrFlzINJKKTvtM-cU7CgYvRrTguXhUVvnB06RRP3KnimLSds_eHZyKJwWfoqX-sA6sirQMM7OfsVlY6C5NQ78hjvc5YJ-bv4MW7D9gDrlVUk2plmq7f2gfrejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=MlJoS3-SYoLOSef6WM750Xq5U_uuB8QsN4pf-VUCfR6CfVgRNmDR1jHCec_X9WhbQYUd2cLeCiOAfmY38EtZK3jNK3r9z9Zeq2Qjj6aHW3MjM878cVzmZDK3FVYRstoq_N4k5LNj8dqtjjVvpOpGTKlpegj1lw8wiZccvvpggwbg6Qdc68GpNkab_MirlA85qTZX57-CnreadvBk7KXzQJy5RJjT9Y9wWn_US8ZscSlUpTJFxFGJt4LyATDRpiZHrob73zSVp5M0e2v1K6roSNLNOA2NQ3HKDOojbZT38DeD6cgbWY5VdE62wPeAx4HaYUyvenIqVq9i-y42QqA3CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=MlJoS3-SYoLOSef6WM750Xq5U_uuB8QsN4pf-VUCfR6CfVgRNmDR1jHCec_X9WhbQYUd2cLeCiOAfmY38EtZK3jNK3r9z9Zeq2Qjj6aHW3MjM878cVzmZDK3FVYRstoq_N4k5LNj8dqtjjVvpOpGTKlpegj1lw8wiZccvvpggwbg6Qdc68GpNkab_MirlA85qTZX57-CnreadvBk7KXzQJy5RJjT9Y9wWn_US8ZscSlUpTJFxFGJt4LyATDRpiZHrob73zSVp5M0e2v1K6roSNLNOA2NQ3HKDOojbZT38DeD6cgbWY5VdE62wPeAx4HaYUyvenIqVq9i-y42QqA3CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KOjTJvTgii6gXxs6odyT_TDFwSShLRf-6xQZWbxhJ3nElf0sUzhOQj96oxcjABBo0thfMTsC8FqPVi7FhIEM-3p7x4XDz_JZWZo5cR5vJQFqe3qqd-A1dQOAmrdPF9RZqEKT7PLwAP93Pg8AHfZUEOIyLYMDRNqtgqB95KfMG08qCYvGjfTu5-Gc0Jkz-OjeR-Mwbh77X1rzCdCqG4njjnQlPv1zlSqnv5EAMCHykdmf1vkKZXRy4NkFv0oNegrimuBdxU6M_0lJ_fsy53kj6Md0-eWAjnApFv-yikpYpmAyzDnxavJKyp32W_Sv4LlSkEKXC2Adz2aKkajSzmpWog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=KOjTJvTgii6gXxs6odyT_TDFwSShLRf-6xQZWbxhJ3nElf0sUzhOQj96oxcjABBo0thfMTsC8FqPVi7FhIEM-3p7x4XDz_JZWZo5cR5vJQFqe3qqd-A1dQOAmrdPF9RZqEKT7PLwAP93Pg8AHfZUEOIyLYMDRNqtgqB95KfMG08qCYvGjfTu5-Gc0Jkz-OjeR-Mwbh77X1rzCdCqG4njjnQlPv1zlSqnv5EAMCHykdmf1vkKZXRy4NkFv0oNegrimuBdxU6M_0lJ_fsy53kj6Md0-eWAjnApFv-yikpYpmAyzDnxavJKyp32W_Sv4LlSkEKXC2Adz2aKkajSzmpWog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-qcNyJiW4_ZekCs6kfwlr_LayeblpnTTLc4Ft5fnLwWUa5Er5QS9eWKUl5GeBf8UYsOh-XwlxKk2bs-aNfNU77fY8OcvGGnVeJxjDUy61f9JI0bbeU0tRUoVNYiGmbP4R_Pef5ZocGa1BrGaTr1p9TUCG4xyLT54Yhk8B3Z_rKNURHfJ9g8B4_JWiwz4w_7RjF2JzguE1srFBfcL33X7QxcycFw0juk3Qhj6dn51dFRI9KbFsRC3bho584O1g6y3raHhVnC2cJ6K7bd4LsZCjkYrUHx2YzJNBtp8ldmovFvyGCsAMZ1Re10jChVlxSu1WHAZCu-VSsVhCqMytRojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=LhH1Xhazn-TKTUAethFrrPh43e1HFxmBWAIZlK29PkfRZCjqwdg2vfWOnUmv27yHDb0bzW0pMWFfSvOwDPbX5yZsbWhVjthllVDOg06_wOxqgeWAkP8s2bZZv9KtTUCG1X_LtGROYPD0vbNa70kHBpWmft5kxgnsbLEXPCUPMIJicaoPGQ5SZWdKyuqL4Q2ZbG4647Ih08ToI6dEa1r9XABpK05K-V85EadgXW7oyfQmnJEqI5EyAqIHRQB8fdxgRSOW2pq3QC4I_gHJeCi8bU0r32OlKaGpoQTm1sGvZOWn4M-t1CelYbRdi8MxzQwZyyeSS9utyHOxrHyG933jWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=LhH1Xhazn-TKTUAethFrrPh43e1HFxmBWAIZlK29PkfRZCjqwdg2vfWOnUmv27yHDb0bzW0pMWFfSvOwDPbX5yZsbWhVjthllVDOg06_wOxqgeWAkP8s2bZZv9KtTUCG1X_LtGROYPD0vbNa70kHBpWmft5kxgnsbLEXPCUPMIJicaoPGQ5SZWdKyuqL4Q2ZbG4647Ih08ToI6dEa1r9XABpK05K-V85EadgXW7oyfQmnJEqI5EyAqIHRQB8fdxgRSOW2pq3QC4I_gHJeCi8bU0r32OlKaGpoQTm1sGvZOWn4M-t1CelYbRdi8MxzQwZyyeSS9utyHOxrHyG933jWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=m38PwSgAKVa2lI75uwfkGld-Q_YIcnxqNUdFHgeF3oVFO209HrgGtmXxBBhJ4oTLsRBpB8UEPDAAh7JJ7VL8BzZNF-coSbftPeZ7ZwCAPpCFfmIN19WHSI141imtTd8G_iL83oE0yc-MRJ_HIXkZ3-G3oAYIir5e6Ed1VQu4YT-c1zLMYIwa_rt1IBlknwCaN_ECvDWSjeu7Lraka7d7jPla7wBxPu1I3I1JsZUkSb67lAEfenlZHflFW-YFcO3QcIcKHg9_z0bUVHTbjG7gXQKlRUj39vkEO656bfTSceOClBPsYY7BKrtDd2R2N08ujzlP82MOUm1wDloWJcC-Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=m38PwSgAKVa2lI75uwfkGld-Q_YIcnxqNUdFHgeF3oVFO209HrgGtmXxBBhJ4oTLsRBpB8UEPDAAh7JJ7VL8BzZNF-coSbftPeZ7ZwCAPpCFfmIN19WHSI141imtTd8G_iL83oE0yc-MRJ_HIXkZ3-G3oAYIir5e6Ed1VQu4YT-c1zLMYIwa_rt1IBlknwCaN_ECvDWSjeu7Lraka7d7jPla7wBxPu1I3I1JsZUkSb67lAEfenlZHflFW-YFcO3QcIcKHg9_z0bUVHTbjG7gXQKlRUj39vkEO656bfTSceOClBPsYY7BKrtDd2R2N08ujzlP82MOUm1wDloWJcC-Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=l8iiDGhVz5-EICqZ9SudzIK9xzUyDV0CsyYx-K9GF7oQmAIhpORaKG85qLdPJzsqcGLQ6Kk9D8Ynz5HkSP7ymsskrSl-z7HbefNRdsiKHWgMqCDLAsBg_65CqRbrT6wAzm1hagVADS29KlizQAs1du-CE_Snn4zBTD1RsoMEcxLyhzo_KghuWkqUjgFqkC-1qTLhWlw8uP9l-Gb_8cPA6zq23mFV4pYUyhy7UXPdn9gPjeRVu51JdD2gnQBCzKyoZzhe-ZbN5qR-3vRhS-fcwr-As5sQfJKMtWQEBQYJN-9hyCpnlupif_I3VEAFiITjJbUd-25d8GuJDh-ja_GgSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=l8iiDGhVz5-EICqZ9SudzIK9xzUyDV0CsyYx-K9GF7oQmAIhpORaKG85qLdPJzsqcGLQ6Kk9D8Ynz5HkSP7ymsskrSl-z7HbefNRdsiKHWgMqCDLAsBg_65CqRbrT6wAzm1hagVADS29KlizQAs1du-CE_Snn4zBTD1RsoMEcxLyhzo_KghuWkqUjgFqkC-1qTLhWlw8uP9l-Gb_8cPA6zq23mFV4pYUyhy7UXPdn9gPjeRVu51JdD2gnQBCzKyoZzhe-ZbN5qR-3vRhS-fcwr-As5sQfJKMtWQEBQYJN-9hyCpnlupif_I3VEAFiITjJbUd-25d8GuJDh-ja_GgSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfEw71ULP5RFWm_MFL4nVOJteOLRdk9T3RLgxafm0ADbA3f0Ug-x3lNGhnwVg6uniZgyc9BhoDDg20VbmsgGq3qd8X-tjnTiX4DNibN3FnXDLItQ5LDKXNHIL4aanoTL71L891hqcPNdoBOYlCBV9q-SeFRQAb2Po6dw8WK4l0jjS9gQqliSfEnAMB3011JxZlp0A41QEqOceanBozSZ64KL92cWsUXOeKaRiksn-qk9S1JejfVaINCG1RO-REdsMzogfmgdGByOEKn5Fo8Uka5LgUgorRm9ovIbD3GxdsbNHX4vgoqAMpjJpMBh_xKdzeAUPL8O6466W7q8gm8AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=FNvbTtATUMkl-b5-cKFn5JX6C42rSWdnf1ElMKNJun_yF4m1fZK-2JqdbVvCJZp3e7ljw1lP1AYF-56mZXBWvnk3xYrnJrE2IzsQUTrkptB_-wiEMvkXtLElUBPQetpGpSA9BtAKnsDmcO0ISs_uiXMMjBLEZqMHDSDnRiFBwJDKNcbT01mM2ZsJHo5Dr9kKicro8DSKUH9w0Me1uSfmFIhwBDA_3CAhETWANg-f3Sgps3nBWZ00tuuA-qOS6XZrJGfFEtnYG2KLld7h34A7wDIZpObs_a23n4Mbgu9rJlLhlIudpz372xazmkaAPczNbS3msrgqMMaOYEgCw6kF1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=FNvbTtATUMkl-b5-cKFn5JX6C42rSWdnf1ElMKNJun_yF4m1fZK-2JqdbVvCJZp3e7ljw1lP1AYF-56mZXBWvnk3xYrnJrE2IzsQUTrkptB_-wiEMvkXtLElUBPQetpGpSA9BtAKnsDmcO0ISs_uiXMMjBLEZqMHDSDnRiFBwJDKNcbT01mM2ZsJHo5Dr9kKicro8DSKUH9w0Me1uSfmFIhwBDA_3CAhETWANg-f3Sgps3nBWZ00tuuA-qOS6XZrJGfFEtnYG2KLld7h34A7wDIZpObs_a23n4Mbgu9rJlLhlIudpz372xazmkaAPczNbS3msrgqMMaOYEgCw6kF1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXLuIlqHTML_gRNbUke71jxWx_6N1vGdBUlk9PhKuHBZjIJ8XyK8_F5StvoSvf01XAip_ofpxdH-OB-oe4K52P9Ib0_3wvGXYZfEXXOSxRWPIIjzBB_9De46CJMO73SRjd966JvMcCF8VXEBKo3xW_PhhcT99pXVHJ4WP6cBWaKF-oDn-CnrCBqEgzq6ZMPzLfQ_-_9RWJNv0NFECAXvnNmb8mLcjk3hJ7nys-csNSoEJC_LRfZPzgvWfDmvuBIvMyJxpK57QiNKe7b-ZZRVj6N59A_zxxfXPOukHH8buj6U0CE9J96kKJ_nBNaT-m7lJQVFH54FZEzNVMrc8L7_aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=SSsHnXWHcxPc7pNiMr5eqpmMQDDJF20KMHMeDt20B1qhkzNuIecQdF3B9_dBwKvFwWYT-SypOfKP1xUMbiuRGzZRepTaB_Z4BTmD_4RnXRWJQgJZ0oEYrxDNE0S3jtnJcOFSl-9-jsgME54JkZKhkbddpkR6u_KR-pxf_TagW_0XLpdq66di4DlqpoEVt2aKtCq-dd5eIzSOHQh_vf4CEaSFqyPoZU_gt2GB-HNtpWUsupWd6tsP47lLOgBh23DBkmUV5-Z_jCBEW6pQCbxBnqDjxE5flOe2QuViCwsDouUJbfO7LdH3JjvJpO0VoJdjthtytNBylplo4mMPutMYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=SSsHnXWHcxPc7pNiMr5eqpmMQDDJF20KMHMeDt20B1qhkzNuIecQdF3B9_dBwKvFwWYT-SypOfKP1xUMbiuRGzZRepTaB_Z4BTmD_4RnXRWJQgJZ0oEYrxDNE0S3jtnJcOFSl-9-jsgME54JkZKhkbddpkR6u_KR-pxf_TagW_0XLpdq66di4DlqpoEVt2aKtCq-dd5eIzSOHQh_vf4CEaSFqyPoZU_gt2GB-HNtpWUsupWd6tsP47lLOgBh23DBkmUV5-Z_jCBEW6pQCbxBnqDjxE5flOe2QuViCwsDouUJbfO7LdH3JjvJpO0VoJdjthtytNBylplo4mMPutMYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LttzuVKUk0NAhPTvCFi9TOfRAHg9cYG-TxLM9FkHKFg9kX2OYhNj03SdCEvdgXfDTNzC1WlpZMD39BBAfLwJiA073iQT0tAWnV8IGYPd7HDeaekK6c58HnBATsBFhl3AkSjSFTixILP_LvFAO44-1AZXdqXs5Acd-bCU_UgUTwiNDVxE5QgBD4O9G0ZbOiyrDc1uMYuGnmdHOIh-aF2KJoxSDzJgrkS6Y-RlS_X8wfny8M2vrUiMWRA3zc5mgELiDg_t0FLA_rlzDS9Z8ktyFsjcHPDLQlnAuaYm96wqkvr9qyzmPqK-DIvqgmIp78UeCFT6WEstccRJUlpZ051mHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Doxjshbb9HpDUUEba-szqWlyh6duT-47qxxrfUHbKaWbtHkmytC0oAPynPm9qoB3Mi069m_v8Es9wArWC-vwz7bkOjZLm1_vjk06TXf7rPJN1qkbiqcCjV9RcKZMKr6vKGPNKZtYSaDR3N8wvfCBtX0p3U2Z0cm_WWw2Ehwj0oauTzymz6Wdt_Gte30gIqhw3of8PX9GgiUMRjTqT_xrV-tyAmtGcoBetWMqQUduwGGqKCkm4pFSVv4e8_XF9xXZulfPLNagOOMJNQ76GVc5p3CbtbxrkNBTzA3rwCRu43km-HUDduoh-m-lViw0n7Gg4VenX4CBrem_SS5Ae4Z_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Doxjshbb9HpDUUEba-szqWlyh6duT-47qxxrfUHbKaWbtHkmytC0oAPynPm9qoB3Mi069m_v8Es9wArWC-vwz7bkOjZLm1_vjk06TXf7rPJN1qkbiqcCjV9RcKZMKr6vKGPNKZtYSaDR3N8wvfCBtX0p3U2Z0cm_WWw2Ehwj0oauTzymz6Wdt_Gte30gIqhw3of8PX9GgiUMRjTqT_xrV-tyAmtGcoBetWMqQUduwGGqKCkm4pFSVv4e8_XF9xXZulfPLNagOOMJNQ76GVc5p3CbtbxrkNBTzA3rwCRu43km-HUDduoh-m-lViw0n7Gg4VenX4CBrem_SS5Ae4Z_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WF1LhL3gJ1T5EzAy2ns6fIj9Ir9rU_r64C0wc8wXSyjwRvA9NTd_FVhFC4nrflf9bGfhHg2sbjzmRK8Qot44V5n0knm4771ADUSaFrrOZz4FxcmsEOl_pdKjc_I5h_IS0-Cct6g-HMmzTAO5fgBEOaWU_CVjA-YjfutlDjyoOSI_s_e5qkkS0x9iYnqaZN3_rcoMwOZBYH-9TZbJCSwGkhZy_65bfG0_nS0AF6oNf1u30E2fq9RbnYzdSs4XuDpEQ0aJvsoygKDcI3HsASb6nI3teeJUvjTrr7vP-HhFYnJ-ldopiKeBJNqTuQd-Hwt1JJZt69nzZ1Dfk48ztWAqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfFeRkuFUBzvpywMDlSiGTKctUrfxTc3ACif4Gc1khHPxyFWQL_rL9CW2u_hTbAVgK3y9yUVr7qx0FC6dM8Qi7N0TMzVTKke7PnT6z2W6ZRq6P4Ds7Uvndtqzt6d11RR1F1CJ2ZMP3f4hZuwx678dMFVTjnUg5IZeK5u6MBvYHxXz3kAdgbvfKnueYb8PZa_1O4cPRc3YjZiKu_1Y1I8VcWbx64yuCVkkhTwu9NbU1SYM6cKi36AH9uUB9rYz5U1MpiXDtpbaVlnysloQIlCdDMK1lKysoltXSROcKH92btYDRCG4xwxTF9nTLr3RXIaVwioLB2DOFikTrJIlouqQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=HNOZL0V1Ggso3-pVrR2zeahUxc1hkfMbZbC8Ze_GtPCYbu9gGC2rSfuEkVZtyqioxtgpY0yF8rZbSsIVDYO84rTfzuSWAMv4EoJdBPRYkwSxavCnnM5-utedp9HvkD5OyY_EcAy2ndZb-DcU9ZKIBgVzjvxhhMCSl1NBjDxt3ZgRZ4L6ysbn5TyKB9o_5P-l4n6a2uoyPDm6WxTpq781D1gXlz-y3vnjB34rQy5Wi-yD1OT1r3SK6QL44WtDqGVd7AfSuH2Vb0___kWHSJDol3kmaAVNXp6Nu7CoxwmwIZ1a5gY-HqRwBHs3aA4heBpIxdof0Ugaia8PZlB3pdMkbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=HNOZL0V1Ggso3-pVrR2zeahUxc1hkfMbZbC8Ze_GtPCYbu9gGC2rSfuEkVZtyqioxtgpY0yF8rZbSsIVDYO84rTfzuSWAMv4EoJdBPRYkwSxavCnnM5-utedp9HvkD5OyY_EcAy2ndZb-DcU9ZKIBgVzjvxhhMCSl1NBjDxt3ZgRZ4L6ysbn5TyKB9o_5P-l4n6a2uoyPDm6WxTpq781D1gXlz-y3vnjB34rQy5Wi-yD1OT1r3SK6QL44WtDqGVd7AfSuH2Vb0___kWHSJDol3kmaAVNXp6Nu7CoxwmwIZ1a5gY-HqRwBHs3aA4heBpIxdof0Ugaia8PZlB3pdMkbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPKDniNUJCO22On9bdwo7iDQR1jGBH4m_jaHngmOE9RzKpJylTBh3Moy_encfqdDao_YQG0hxZ1K8i0k0hy6mOzkCmvd9OM3SSMq2O0xn1BNjT-a3Ka3AqVEzZ6AwXfHS6whna6Sc8qf40BgtKjOUQxOW-a69Ir2g4wYgAD1hFqmBKCu2VGcxV3eWwlyGWAqktR--kQJPaZA_oRJq3Z9oEA2sc7x11SURQysTFawQEAQThb9ehMQMLxJE54gehqssa2-lJhVwfVrqgZHsFGAUe6GPHOaAn5woaVaWp2qUQn-MbdfcCysY9woLvlj7pHwTpxrvdyOA4zP7_blx_5Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFjStDt5Yutf126OMQVC0YnF6QOXZuGfJ1XrilSa5-ZHzbSy83etPqfNAnePlMXMkPxC_vLZ7zy4sDa5YYBYDMBiDFxAaPrN7aeeme6O63AmaTocf1ZbEctvPHds4huyutcLumyEZhbLkIcCn1qGHy4M-EjMFlU2L52xAQWQpLTeSZ6thoiDV5-Tzj-SIuvcyRMy4k2MuuidbsWuyFV2xjGpAsL11STgTaik4mZ7mJfXbjJ3fhQd3CmaAOK8Iir5CYYhQ6xWJXr4M1_GPp93fDzc2DX1gdy0DS8Grl5OEKCIqs-rUGo6VRAUT5QgYjslz_6gHpgOSi6wBXHT_orGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKB-sAjZ5v5wRkOOhXdl5NqaxaKNp9MIAeaTjurrq52EqbTga6dH1F4qyJtC4nWBjs73Td-URVyB2tlX_YOLUmZbl9AWdmq62-IcHzOV4HA8OCQdEr89P-_CJQdiHRFuzB1Ly_sbCSiB8NmhO74PfxRzGmU4-Gyf9gFgZ1XpQyyTcq64-QLJzNSDFZd0UogVVClUSwijV4qUe_jF6th8nNvAWBFQgSY0mkl9xHwdepY79RkAe-MyNHv3Bh2bxynQQZ2jCfDZ4H_p4sX3CEzqrkKx93DwkInncqW-WY3Jppv5__t2KC_JBB8PHnP4rFpy4r5t9bigVBdS8sblCtNljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBkgvjFrBw1WqrVCbbVmzJjJx4PL9h3OoPN3t_ZVUrzuDKGdq64nJLtibBNwnKjCUpmZJoQVjVAyXGTPhHKsjc6-fZIInm3fo4fitgiSfBLMqcZJNT0iwjUlZ3YDXTNqwEe3CSid2L1qYYvoNshvdqkYLdAJUw2tL-GgSOJwK5sZeq63X63leAM5zuTIILIw_5FdNwAvMY2gN8c34xdnezDxruGv7ogIhtkbvsKaJqC9BzRE2RWLY0D3nUnbE78yz78dKQnH6szu7q1adjZz_kk4U1s-PJ91jMzlyQWvXaAFJdi8_jm05g_QGRDNsoCcljzGwszJPXayf7fR7zjgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNAvIokwysqzaNmOyMSE3KCOirwXAwRzA_7xsPNWEQ0s3-IuGNXcBoIBH4Fp4GHR33_pVsy9yCS4WJBG86lOGMvfUQY4M9BayTnA3oE2NcoptNBedBPNi7fgBCisNaJ4CefjSQ1OySVdOQdll4vx6y-1MIlIr2u4ArwfHRHSjEp4LbjwpRQTGrN3Qm0iLq-8FH4HCMMTOJVzCZqIcnw4uOzpbPVlBJWnuFBgaCuOmZNVxIqnE64lIIJRgE6sJWvQaVsehVZchoWepHDijqe16Z5Te4WtE7f0KOV52ac3BddJOt9gbaTDo-8LzbQJDSrKEYfzEfwUQgXY5U1gL5h9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=K_dQfREnaEEaZz_AbnSt7MOtY8d7v32H-42yExcMhGhUjVafPZMaDcKBmHbcak0uSyRYwOG2uBQqKP0kMHoZx0nv4LOcgsicaKJ3v8N6WEzSJf_bFVW1G5ktux1-vwjtskJJlXDfeh333n7-gj6X-yXEHhHzTaJdGkAhOhhxkmYEoTfRtjnoc9HdNMp7O0YJT1pLVZO4gLep3svp0jJAyXegnuetX20hmrekNCnZ1GKB1XccgWu4lQMx7zKDHfbZrJ-zC4QVymoxxvWys4RnspYgJNgSOvkePo9mgnY4lNRL8bLNDi9YjiL6SR48n2euTin4Jm6y44E9LX-muFgYUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=K_dQfREnaEEaZz_AbnSt7MOtY8d7v32H-42yExcMhGhUjVafPZMaDcKBmHbcak0uSyRYwOG2uBQqKP0kMHoZx0nv4LOcgsicaKJ3v8N6WEzSJf_bFVW1G5ktux1-vwjtskJJlXDfeh333n7-gj6X-yXEHhHzTaJdGkAhOhhxkmYEoTfRtjnoc9HdNMp7O0YJT1pLVZO4gLep3svp0jJAyXegnuetX20hmrekNCnZ1GKB1XccgWu4lQMx7zKDHfbZrJ-zC4QVymoxxvWys4RnspYgJNgSOvkePo9mgnY4lNRL8bLNDi9YjiL6SR48n2euTin4Jm6y44E9LX-muFgYUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=bLRtF6UzKEOX_FBEYJn6BZ0k2SchQxNolF5OkE_Mg2LAXwIUWg6lLYxIJDJ_GBJucwxnnoFIHMDHiWixDKVq0cN59SDu3PEH9c3t-SCQ4pc--Wh0fFM2QBaeZc05KnilPX8In6caXBM8q8ZJqvfdWZ4hjCpXIhVurN5rGDLbQlmnUG6Yrnrz5gnhGW_uEPQkJ_Ltl_y29NCl-jSW7m9MGJXSRprU0rRRX6WFwhYbhHm9PuTUwmAbZpo9X0VM6E9VrfEm-lGoyTKFoV62MyuLzkH7kl_v5gkJyWMbjRwdlZu4X_33gEOmeIBMhEK5arEDQsEE6_FLk91amyTO8_XJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=bLRtF6UzKEOX_FBEYJn6BZ0k2SchQxNolF5OkE_Mg2LAXwIUWg6lLYxIJDJ_GBJucwxnnoFIHMDHiWixDKVq0cN59SDu3PEH9c3t-SCQ4pc--Wh0fFM2QBaeZc05KnilPX8In6caXBM8q8ZJqvfdWZ4hjCpXIhVurN5rGDLbQlmnUG6Yrnrz5gnhGW_uEPQkJ_Ltl_y29NCl-jSW7m9MGJXSRprU0rRRX6WFwhYbhHm9PuTUwmAbZpo9X0VM6E9VrfEm-lGoyTKFoV62MyuLzkH7kl_v5gkJyWMbjRwdlZu4X_33gEOmeIBMhEK5arEDQsEE6_FLk91amyTO8_XJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=JjaL70ujnMl0cMGLnJX7apDVhGP8bFh_PnlYaN54dlftwUVfxsaq-qC0kCgFCJ6HzKyMUaoVE8MxtJ6OHNWC-tiZv8Y5pP0iD8o5zXxRvlGw1rHFEhLvBqyZ31Kx_iZdNkTAO3fh6jp46EHaLTy9nyK-QbIlO1OEcXjs9IoxV9QJkjwAFxTzk8hXxy2VQNct9xnu-3Rp3qeuzTTae63CoYH3t2bVEFaqCUpqRrJPCJCfnVwtO3AxLlQ9NbOBK9-GVRLxgDsTFg7V0RKx8ecZgpMM5oHbS1Elc3ubXFGZLvooVXVcW2vmOyIzjdEd3wpmPHOyoKu-AcaRo82FoDs9tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=JjaL70ujnMl0cMGLnJX7apDVhGP8bFh_PnlYaN54dlftwUVfxsaq-qC0kCgFCJ6HzKyMUaoVE8MxtJ6OHNWC-tiZv8Y5pP0iD8o5zXxRvlGw1rHFEhLvBqyZ31Kx_iZdNkTAO3fh6jp46EHaLTy9nyK-QbIlO1OEcXjs9IoxV9QJkjwAFxTzk8hXxy2VQNct9xnu-3Rp3qeuzTTae63CoYH3t2bVEFaqCUpqRrJPCJCfnVwtO3AxLlQ9NbOBK9-GVRLxgDsTFg7V0RKx8ecZgpMM5oHbS1Elc3ubXFGZLvooVXVcW2vmOyIzjdEd3wpmPHOyoKu-AcaRo82FoDs9tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=PtCwfp9jnAXvPSGQDtJqfo79hNFKJfm6hcQZikoBx9_MFhAWdNjNBCVZ8S8US_igj-e8k7DrcZdBs1NJ6BzZecQN6X5j4zqhOtR5w-cozd1kkGduONH2UTCUrGrT8Ub31QbWXjo-w_yNIDk01XebhpM7p6nMmCC39mJ8BCqLI2JcSzQl7VHZAsKmm1nZ_p6gMv_SsTlq6agmX3_lX5Q5KSSKzmzjfoORAhv342ch08MEjX-qQKa0vlYKwWVpkaIEifEP9g503Ql1jWB5bhZbTade5fsEp3l2fbNCWd23wWa3r2SXTHv9dYbGBwoCu7TFNp1FYk9mMXIrrBJ_cMpjng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=PtCwfp9jnAXvPSGQDtJqfo79hNFKJfm6hcQZikoBx9_MFhAWdNjNBCVZ8S8US_igj-e8k7DrcZdBs1NJ6BzZecQN6X5j4zqhOtR5w-cozd1kkGduONH2UTCUrGrT8Ub31QbWXjo-w_yNIDk01XebhpM7p6nMmCC39mJ8BCqLI2JcSzQl7VHZAsKmm1nZ_p6gMv_SsTlq6agmX3_lX5Q5KSSKzmzjfoORAhv342ch08MEjX-qQKa0vlYKwWVpkaIEifEP9g503Ql1jWB5bhZbTade5fsEp3l2fbNCWd23wWa3r2SXTHv9dYbGBwoCu7TFNp1FYk9mMXIrrBJ_cMpjng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzOCvHfpaIxGHDDcLwURH2c29urnbXyRtcHr43-KJFRLyb2hNgSkh2oCfgw4E7fxHL1oPWdiNBrKccDx1RIlelHqD97QpwrdFcxKAJpzRUWvxRhpaUgMtYkaqIEIGKX3W_E0paNl6KQa0tyKu-5q4u5DUuu2c8SOjkKQKNVvmDF6XYqpiBKcOOIRgkVcJ94Qhg631Iu2N7VoBL5aRtks6UMPcfiiRIjP15LD6uSQMXGIg_8JEJFqEwMEgBexu6L0BpQnt-zq_tM-lRclu8r_pquJIK09O1F_0GGf290dScrhapOE5IBXRfZyhE6DQLbqc4QnY-4qlIPRG-3KCde4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzZ-mkZOlMQwFglmFsuH-eYjdLTRvOx__nrXb-LuZJp-_XORLLeFyFmnruk5plPI3eR4g8lSPpJWlCarm1UHIg6Qj5eIvm3Q0rMDPwYSFXwY7rILLD2ZJVITlCtQpjJ5vQjDFqNaNQNYTyxpb7kWnPbDtfV_pS46cts4Oek1R1t38icIC3xxJlcrTqzuk33x0RJJ0PsjnYaZFN5050l5qJGowmc_pQsKTf3pSi4PB80FbUPQubf0vO53qtdE6Q4yS0buSj4DlHDi7It_pC_zUxcAZfYsh9T23pDavl-3NC-ebzYqu-4-fyy5TIXbwQXOUMKLTkoyQ6bVefF-yVax1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=cck0gCbmbmEKDxn5IYZBWbgjmlNYgCwxWPym_amRcyBIUunXN8Z-gbdG7a541qJ5XhZR530WBAPYz1msX--yR4VkLpMvbvl8_CkvbCPiMPY4NJO5Ic0honeIMTPvbaM7knsVdFV41zrUbAt6_RdSphukD6baXtsCMQErTrOWll-pMMzvYMh4fSZH3wsgUsfEaZI5nTf1NbsC_2uqDyoZr-OmkTWTScUe52yJPtyqEb_qbH82YpKcU7FD7Xvh5JY63pcL3-01CBeXeOQ1rWo3p6zCUlz3BN0B0h9jMp9RKTt3kSG06B1U_Zf33evGbcLXw4ALOoiOo6Dxq8hZlNM9vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=cck0gCbmbmEKDxn5IYZBWbgjmlNYgCwxWPym_amRcyBIUunXN8Z-gbdG7a541qJ5XhZR530WBAPYz1msX--yR4VkLpMvbvl8_CkvbCPiMPY4NJO5Ic0honeIMTPvbaM7knsVdFV41zrUbAt6_RdSphukD6baXtsCMQErTrOWll-pMMzvYMh4fSZH3wsgUsfEaZI5nTf1NbsC_2uqDyoZr-OmkTWTScUe52yJPtyqEb_qbH82YpKcU7FD7Xvh5JY63pcL3-01CBeXeOQ1rWo3p6zCUlz3BN0B0h9jMp9RKTt3kSG06B1U_Zf33evGbcLXw4ALOoiOo6Dxq8hZlNM9vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNOGFzv7IrHmhsWuvjiNCGlIEFJYqv7unA2zKoDMKeUNEOSURjABMksqwufi_9rsk5-OQWXgw_Hu6KPfB2EYNq_mjhU3E5-PIUDxooivYgbHhT4oXhwsxbmTa7l5bsajvr9B-yeN_qj6DYnfdSVZTWoxQMC9yP13j8_TIQFyaIR7VU6UtsezIoTgu5amwZUYIkoj7qfpq6T0ni_bF9_m0iPCP0svqLyNFc6hwfo0q8-WyZUzJQPY5_coEKwIHXe41KWCe_uMltlXuMW2wk_QPyGxjKYj4sEB2CA0JXAHOqXZiSjiSAWiZNndGJCnUwA6OGTtjh5sqqLJj3e5nZoYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=JMzhvvq7Sp29HuFsaYwM9d-Hae4HJfjvUxEO3xC8a_-k4APqzKxmWart5a6RNxYhWWt1bT-22yp0jKmGuADqLW-1DYIEQz_zqVJmGw2ULK0b6EQDE9iVMgzygaD6CHGt62Q3YoQn4CNdQukKO1rII-0Y-qLlMvYnKAajzlUtmfFQvUmUY3AzwKlEKA8fIGOR1idIdKaninou0eB3UnXfiMmD58VXD8RjggBzOGBF4J1KfFEb10dr3qxTD-uEQ-OGJUApBe_KoA6shqJhrXNzPbZ-KTK7ONikL6VUKZLRJ3CbWF3-5XGhqkZ91SrcVLEseVFEtZKmB0RmPZGzejBgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=JMzhvvq7Sp29HuFsaYwM9d-Hae4HJfjvUxEO3xC8a_-k4APqzKxmWart5a6RNxYhWWt1bT-22yp0jKmGuADqLW-1DYIEQz_zqVJmGw2ULK0b6EQDE9iVMgzygaD6CHGt62Q3YoQn4CNdQukKO1rII-0Y-qLlMvYnKAajzlUtmfFQvUmUY3AzwKlEKA8fIGOR1idIdKaninou0eB3UnXfiMmD58VXD8RjggBzOGBF4J1KfFEb10dr3qxTD-uEQ-OGJUApBe_KoA6shqJhrXNzPbZ-KTK7ONikL6VUKZLRJ3CbWF3-5XGhqkZ91SrcVLEseVFEtZKmB0RmPZGzejBgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d33EHNkBdDGt2nInYtH6N-5Q39gyF0rqw8TUffoBFiOSu9T06nMJY6sUrRTnogp2ndHhJqSxhf-anl04jKZzat29Frg0jHsfHoW9VejQ884XfS2gnrfLNRF-6PQicpNV5pLupEsXKhTOZoRj8btCFcwsQmUMzb-l6ZTrjAqE0YPvX-3t5XJNS19BdfAvbkCnevGQI2sjrpcWVZifnXB2TDldBoL30VdEi2YnAJ96m1eXcDM5vWxwr4SLUou8xEjZISdO6mZivzZvjeQZx0OmiHV24KuXOU0F58cWlBha209NWhvS7xZwAIyq2-_0jUuCRTfUcdkmt8TS64Xk96oOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxoiCMHBmadNcs9BG9yfQg8UmRSUHK5CwYISXyudZtngZB2weLrDlpy5tVZU1hOGP3gegZjPcxtRY9RT2wrq11quh_fX1AborZm-8eefuoP-QU9Xh7yby7OrJtq4bzK88v3x-aS2ztcwr2s9P0mfrIf_igQnhPBnTTHlK15_leUksQWEGu3sYKfN5pFlDsspixk_tRmXF-9dZf_4gO2cjPdJOvUZRc4VQxwTFPRuogG-m03D4XV9yRrk14I5PpSXBEv0MYHOQLbhYxI-PHMJUUEFaAuyA6tlo5IeSnHTuovrXti2dD7UU7z1aH3AcV_vD7ccTgr5-Iclbrb3hL47_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=cby2X_Nexj2ItEGOcoXsZTH1WP7SYcKwE-YSXoMxxsytUelgmnMbYEcnznRAou3EZQMIjM6XVrlZnBpeOrCD9iYtVV_TgTE4wBCSgfasv0y1cKS8h1seAtCnuUwJS6Erk67XGSJ-9O573W9ER6jvKY2m3cdMlVZ830cwxIdui5VGW_8YfU49mIAvH_cnR7ILTZyJgyjBWzFRsckXEkOVBF8kce2n8I0mR32ge2SVTIoMyFOGRfnEiBlmdIGQTIPZxsns3EQGeCLZBwyMZ0BP1hUWUqZPEQ1qVCm4dNIxxdqul2orZxy71PlVVqV6CXkgJY3d2OSwyLZtJOUZUUCM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=cby2X_Nexj2ItEGOcoXsZTH1WP7SYcKwE-YSXoMxxsytUelgmnMbYEcnznRAou3EZQMIjM6XVrlZnBpeOrCD9iYtVV_TgTE4wBCSgfasv0y1cKS8h1seAtCnuUwJS6Erk67XGSJ-9O573W9ER6jvKY2m3cdMlVZ830cwxIdui5VGW_8YfU49mIAvH_cnR7ILTZyJgyjBWzFRsckXEkOVBF8kce2n8I0mR32ge2SVTIoMyFOGRfnEiBlmdIGQTIPZxsns3EQGeCLZBwyMZ0BP1hUWUqZPEQ1qVCm4dNIxxdqul2orZxy71PlVVqV6CXkgJY3d2OSwyLZtJOUZUUCM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=OLHlWjXEN3JM76pAOtetWArFAwYRXlT2U8B5PGWybysXGwtGv5J9b8-nMeLwcPPmA3JxTNqeQARqxkxHJNk_n-zjtkP-9Yhn-wAxlPFO3XKAAsr-y_o877_fn9-yZLxPd_OMbE4T8I2QiwuoyWT772MCDDFevIm4CbnY3ExJrVrZ9gR7QepaqbSp0HXFMheZnQX4tJvMjDT5VSJcWJAO-pF0DbX63aEadhw2WMGgA7k60Mp3w8TeNXwBgx50crRnUmIKqY9m0bhEYgiwUn5Ybtn1-Ku2eWYmIcQl024enS7Z1ObMFGh3DC58CEic_TtEhnUpG2u3tZ4aYupYmUz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=OLHlWjXEN3JM76pAOtetWArFAwYRXlT2U8B5PGWybysXGwtGv5J9b8-nMeLwcPPmA3JxTNqeQARqxkxHJNk_n-zjtkP-9Yhn-wAxlPFO3XKAAsr-y_o877_fn9-yZLxPd_OMbE4T8I2QiwuoyWT772MCDDFevIm4CbnY3ExJrVrZ9gR7QepaqbSp0HXFMheZnQX4tJvMjDT5VSJcWJAO-pF0DbX63aEadhw2WMGgA7k60Mp3w8TeNXwBgx50crRnUmIKqY9m0bhEYgiwUn5Ybtn1-Ku2eWYmIcQl024enS7Z1ObMFGh3DC58CEic_TtEhnUpG2u3tZ4aYupYmUz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcNDobaY9iXyvn3VVdH9opeKfb358m7Oq1fnfBkBV7QsXwmMGK0S4Qzw07cDQTFyHzERvcoJcCxXvSQiUbSyNMZa7oRFJ2HT7tzUOg-dR6sWhkwvYwrVyBqWAwrEt9uXjA6yDJjk4IScR06YaLGpHAM5S_v5z6NIBHNj7F0AcOnl5i6W6oGakug-1sUV56lgk7M4qJVsL865wtCOb0RmdvSw5cziiXqcil0f1vrzAHnpTlNtGNvWmtMbbxx_IWqSoflrjsqj6mGK1OSm9WiIJ50Cc4gYtk5BPDSmekuFuDzTb3iOj990fuNV11KRbHcAAehoCycCB1MbwWjRHzsPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7L-ErMp3D3u5DoKmghsr6Tfi4_PqDCJXyCy8B-4uAjkmgQYordgfHIVzUTxQzA-i8d_zXpaFn40I8my94P02fJBsk21I5Co0tQHkYc1x1AvXH23TXGjkFLOe2aU14no6tlT6jPdkclKIXsAyzDcWr5dK_uC5Gh3EgsD1iLpXmolPRdUQLUEq41lavKhK3XylvyY5a_DZlFG8_4RtRlzzUfDXihzciXMZmHyN1Gm-MNOZR9pP7lKBpLQPBaClXLN92H4qtwtoHDsmNYC-5mHVpvM-6Zbo-sKBnIytnvZweT0_1jBRsECCvzw_tmJ4DjZaCUlLcCp2sUCyi3t796H4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8s7UYKE6IYkWCs8hu0JpQhCjTcCnOlFUL2Wx2t0Ue4LIAXMxoeP4zznF0qqCFkWovO05gGTuzzAYi7lDSFf4d__90hOSj4CUAvWu1wacKlKcz6bUSxbc2tjB4KI25dMfPAaKhH3tymZ3QGTu4CsZPoLPeKFUw8KUHdoRtC1jiEcZyMKjt7h-_xQhtZM8WxB8Rk-zdA7xvqE0eoqlK4Eo7ykJ09qI5cfeYafCJaOx3jdWHvgP0qHwOUTNEERf7LoZ8UeqyVvR5KR6m_BDNks2CcdQlSp2-lJSrE3kWCl_VqwUScFqNB5bD2WMYlwGGKopuI6_8hYnNCPYT6vHGeOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
