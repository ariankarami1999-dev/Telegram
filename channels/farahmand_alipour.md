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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 02:16:58</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMjZ4OoRUqn-V3pHQBGVmN897e85FyBI8k4AvIJuHoN5kn64UpMvIbYRY86ZmM1GX1mW5NUIBf7GbcfDzIxWQNxVTekhQHGDUaqYcU6lhUVwCpkShVx5k6eboffzUbyzqjHG_pNk6NDELE1IqoFft0fmspyUfAZwQWH2Qh1Oaxs8wjgGslueawP6Z3vtkI7VMTw1b04S-cqEbkLIGSgvdr5LueRsQVyTxecq-vhrMSBWlFngAfK7mKNSse3WNa5Cbtk9D_87fxgpc399blTuhAdY6j-X4A6tQxi7gMLYI6SWLLHd8lCXUkWt-iQ8VrCrvdJ5UZIDlMyz4McQKYMaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIoyIMFQUGeHYq2jpWwXKMZXA61s9MoEAjNSFSFJQ_wlm5VXKv_nh7SrBLbzlNS0SUlBEvCwfVWemBsU8rBdSdCNC3DSyhkOLadFv_YBCDgO5pkcnIxVExGwjBJqCiXPnw_FK3GyaHhWsPwWjvql-JVwz7b-yIzkWqiwphkkAtMRIH2gDle1OlsKeSxFs7nno_pMoJmTGVV4OrVXroSC49fS3B0uOIJcKSPXGiIpF93SD2LJW7J2h_CQ_HmgAI5tgujoswHNpjAuK8jtqg8nrSobSgYyaZo139LS_r8qQW_vq-eMyBAISjxjRJibohwmQUBYPeZSWrsTFT08G1pjmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbJ77U7SQSXhwxgCG5ZfT5peUlzk6ukzmi4jLANZAZDbGKNGNH7MiYfp_QB_eYWQ0TtRtxyKTtmeJIzL3wMftPkyV5wRQKodlSk1IztlPB9wjm94QrMQDZ7k3VCWg5Q6Gn6OdKVWxiLhiqJ4fpo6QFeDbticcC4dgu60xoAP_uRnFervovxXi928yO7JwROiZOMj_7gSsNVHg8Tv2WT5WDIKy6YRjYaQok1T_NSWEuD_QX-_s2GI2E66d2w_YR5OihcS1wHPb8H07ulyvHj_R6ED9SfeC1OYu0fh08Ytksr7j7Rw7claprNqS5LT3yqDXNnPv3_W3K1ZKkkAbFQq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plcyv1aD2jOYRdgGpN46SR2SX5jo_RDaUZSHvP315gULaRckOys90unz7DmcNbE3EokhfzPykVxWosuT28g1MWZPYUxUmGOAs6ny0Fpnx5Xg4lPgVojkgTMpvDLnmZStHvqodnlFPytFpv9OxvbYcMj0E609n8ZDgmTuxmb2Ie88cAukPHSRadPZY4AfJXms0-h0lLVbsjJaRazzYpKGc4fbG5DFnRmSDsS99Kr6lC4UNh7SvA9-BLw0owsRbDC5qJjo0NWbTlwCwOWzxymvd78-GU5G8VISDeVvfCEybQBSLLfDf5d7TFgmKigTvj6hH0J5BAE1mM_a1LOGUAZA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kvluqz9zN19CawRK72UBvkG-Hrh1W1TjGn0kIt0TnTgb8TiGlHH8krMI20iMKVpkCfMp7aApYI_lwSeb1f7TRxgsM0lrC15LRCv2LCe_GYx6FZ2eGpbHUH5vmmZjAH7Ro3d3HFjp74NSJBG64TkthlxiBRGpfeYlf4SdN5PnVfMHylVFRSbYLM5W8an7hrxD5ytJ1jjcIkaWEMUUjUcjnVXget5XWDV1qhHapbzpCI2q5AOdcvx-LqoUZnG-ARyPsV8xaI1Ul_mwcBmBiPB8nGwZXu4Fxvf4xlw61ecle0UU91HjtA5SYwWOi3oRi8sA0T5dHJSCKEryhEDrlBgIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YY2iF6b61Y66tDX3RCLVbZup07bb12Psckh93MEqnlj-c9sCj-J7x1dwm4ybXTOW8Zw24HuVRBguubhX59EvjK0iFY13_pqzRiwWjGxJdFX8fu3MKWagFAdxjQEAotmXemi53KFoaQHkJAHDUcR7fE78pEkjuleWkeX4lWPB5wc8kxUM0tasq8MNaR64K_qB87o84uof4JdRJJ0QsTa6IJlUiGgkkEAQ3x68t8cCbAwMPBrO3GSRiXJzBLVDgn_-rEKXIflVtQVwVu-7ze92gjJL8Is7SNDqUnjlY0g4lvrbKqauHmZcBusZwSJ5gkbCzIrDgQ4FsMbNI2GLElYuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlOOSMjwteofyMcb7L75okhFva2qqQA9HL7lRztmczTRfO9pDXL_m5MafJrS6gYW9bkd8otI8hihtv67EwAndvzcicYaK1s2EBmIZhRN7ahWZ3S50geEaCGx35k9k-ulLKUe8i-WiJwW8PGKW--f0qVotcNrX9lbDricq-Ne0Lzp_eRjVlFAaSeKSsi-HCMSmQdV89wWxwspEnCD00KCGK39dYaZlWCWAFUsyZHgNGWcI5GLm5QQKp36SrQgERGjOZxHBD6i9ZVylXRparz3FO_qeqQY46WTo3MXCzlHIm9AG6OYAnkJg9rr6OAUky6QUBDifxuRcyqWTu_PTukORg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC5CEQRXax6FJO0qMLvdIJ1O7wtkS7lTTj_5ziNA2KDsMxuAuBLWJUpjYNdP_xW1qXTlUL3zGIRqS3RQe0h_W3GJhgKCSV14Knzj9JRYafarn0G51aUDIFNH3dsbgkK7pkG1uSBqWja7zY3DlbRpDxhGHoF1-bN11-CvdlYSc_gNaf5Uc8jbDVST9pCx12mW-Pxrefe5DcSYbeHCiZjd0EwDAHes7rj4znzvbv0gV24HSPnwyJud8NWAVBFWzM_Hql2HkFU4TXr-2aIYbO2TBp719fvfaiiU_55bQm-K6Xq0BiORxZ1TVuPxaNVWyqb0Jd5ATN04b2Qz3Zdzg8yutw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtmlrnl_GzmK_C6MBiyG5TQw8NX1azvlqy9MSD3h1x_VHIC0-CHRQHfz9wX1avYGwRpMgpBCSiEzywI6eHEuYH9xP_7KPJYrmMfVbHtjTjEc528cABKrTDhjZ0kxP8mnicuDGbEo4M_fr9i0Fbk93oPqUcOHiE_gtCxp8EQcFAhC6DXb4jnst84dZQH_t4Yn5d9vwjjcAmhOhGpYd1NM2qf0GlhjqXB0il0ab2dnnOqAlH2yk8dr0cZV6fwYJ4nh-NiHJRBqc9Ms5Cdav5jIzfq2PrxLKSSGmJ5oC08U5otjl3Id6gd95F1qrfzRnl0d3Fueu7eXp1fh17cORoL4dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCdKtSe3KMvQKpNLvb-9iMOLGA4YGTPQYnS-ZmoexAqgNOhQc_yRTOWbaO1ycf8k2R4uQm2PihkWhSZbyM1k2YxhgKn0ttWKVT0E7uL-JivGMxYGiQr0Ufx4ABpf7QDmIIMDBSsQApLqAFCIwpyrFcZ3b8Mahyx6R8zGPYPJ5bFFmZcd_onlIxPQGaN5ID3eL2SfSAVuoeYqiRVhOqEFxvDSK7W2qhiNiuWfIjXWcopQBZB-GnxlB0wE6W_7U-1GtEb68FTM8orQourt4TaVU_iSt3-4lfxwyYQU3FS6DVOlnegAY-ikN4pBya2gawY5ck4f80JwTrcx-ZyITAJq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixGhUYjKUdTU7KOoTk8O9pdnp7pFA7Gy8rxEOKbIQqHn_w8-1zE-aOhreBz9oub_E5rphUbjzaEYyzSC0eCbfsAGIr-DEcwYkM1LXTK4X5qM69ZAILjK-UZwOOQfRe79OcPqbE53Ks23eQ1OXGswv-fsur2mdiIeJ-ndwYPZckoNPSe-81xiEoFeQ-OkX2R2emj75DHnkFEIul3lkfLBJe2zJq2LceHms4_Va0CecAqDxx-rGpBaPMBlA3JZIctYrSbaUp1PLJFdqZv05gKCbxWZW2r4VHxCUJNFwOpZUs1sOkZuA7qSE3uAWfUgQaXBETJBUDKxQJskPGESmKflZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPjB1kUdN-5UsJiNsW_pgRwsaAY0BoTYxXgTPcodQxH74g8QF9UNHyblL7n-TcCHlRcvJykfllKf2iz9ywzBRUUCG6iX4pnOgQJnzmqxiIJHwPgd63a4Pe4l3rQ3JfLf6yB_NOEUx_krmumWL6Cg8KXN4UXXsU5BuAeiSftkK82q2k1cyW16RiUI0t7ye53FYuL3qwYLg4NZgPGQ47h4HfpYyGE1Hk-jCX4pMcfIeXKqkucp55xltlhesgUZlE31F-FjyFpFm9sKpZvwh03OsxEoGpH2LjYBw4oNZRyR1RuLyWgb5duqPJIN5XowcCMqVhLl9wBsvPkrsTqtZjy_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMnFnd403q9ZtiKK2eko08IoFKibk25c8LTVJRuHPe0KffGDmM4MA0A3_ANIUUoKcjHwhPZGvd-g1ljUFHtvkhY6XWDCFw48RdUNmHt4Wb1IeyZPbNdyhktTtdEru5RPXm6EIeg5434nTTm_l1VGJeD-5nyqF7NQXgAE1-CT3YYJAsqtTKbsP7Nc1as-aVxw5nOQ5DlNkgkCyWUJeTbVn74h6FYzifHXSDwMyBnTaqQeeHijxrWm2x8ThibKoABRme4B9GoLbRM4lZ5wUa2HGMCNCVTnBKhpEjfiyihVqNSHgRoYgC_OmK2wAH0dLx1yASiHNq_y7ZjxOYVxJW2Kgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGkmfzhj75QVvV6VOdEwoes3v501aDE_90mCffOPrRVx_fMxwK1DYHFrAuuQt7hwTRb7w9eUfpbdcZOtFTEjCnZfEI1kxhN8Ianqjd16NzL4RUAvS-VC-aYl8W8D-zee7JaAWywD6LO34WbsMoemt91ilwEXUHMdUVR3diDhALExYdPmW2Qzb5iuYggotiIN-dydp2n2NHTVkdwPpTJ7NfzabquX7tLO3tXPOpYUcxir6R0zi4AGymXBqeM8ciC5TI61gf1ex2wwkt7WGSw7_DXT6Qyj37AUnoEKqOk6JnNauL_J8hsEGyAom1XaKoit3mEm6nqirqjxg8VO2Rnd9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAgnvuXTSpv6OA5Dswixvh6eLhWaHp-DkzduJeiGHv-OPLtr5qATnRMM_6begeLRSfTuL0UkZSKIjKYM8GWE9jkJ2OCVy7O5faAsAzvyeyeyF6rWUaq1for3-PTU1ZjvtZXY2HW9nhZ5P9utDBUMzi6LHgUeb3sA1ZcM77n7kElMTNfwAShgjO6f94UPkDUjpBn2OFLxHxH8xjIOPG6W02ZbKaEp0kDcscxQ9wkpc04zpeuX7w2wZk2K76yBLT3gFVVX-c24oA-Au-Zif3tzVUwjsjw7buJFpt0czQpWF4oBj5O_1cstvOjo58QpFWOjw9RebXdRRhMwhYmoxovo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ufVNxAUcChfjlBj7f1qk38r082pVWdpuuMWOZb52BNgT30V2gn7aKMkySyHYhfavcSGPAC2tePMyyWFCwC1-gLPaTsmxjb3603EGAg0TGFTy5xded_eHDAd8ZdIG9J9yeyeqUzPNWT6xWAemgMOveQTiOGZGYOwi3gQub_R2EJAvAGdKKevehyyal4tOafVX61ezOmRLehEnOTBjH0AdY_xCQe6GqJ7EkrnseK_0KvPHw_RLBkyrEI7Hf0HSAbcA3kAdvWXAtSSnsmA2Hr3KY01A3ZmK1qv3oX1jQHOzhdTj0DJ8SBlwkIFjqoSXyMNAEizwiSpz8XpxBiHTE9aNFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=ufVNxAUcChfjlBj7f1qk38r082pVWdpuuMWOZb52BNgT30V2gn7aKMkySyHYhfavcSGPAC2tePMyyWFCwC1-gLPaTsmxjb3603EGAg0TGFTy5xded_eHDAd8ZdIG9J9yeyeqUzPNWT6xWAemgMOveQTiOGZGYOwi3gQub_R2EJAvAGdKKevehyyal4tOafVX61ezOmRLehEnOTBjH0AdY_xCQe6GqJ7EkrnseK_0KvPHw_RLBkyrEI7Hf0HSAbcA3kAdvWXAtSSnsmA2Hr3KY01A3ZmK1qv3oX1jQHOzhdTj0DJ8SBlwkIFjqoSXyMNAEizwiSpz8XpxBiHTE9aNFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1Ma6dipmIqGNN87Cui9A0xEZweaXvJpDhotQfF7Id2A5j716HvlgzmxdTxjWAUc9d1PfT-EtTbRhPPCcr6n9t5oxIvNAeEEDYDq7MacEVBygiVqt16I2G6SwHSqW89QzU0ay9WYjFeJl37sRIl9Q_1NGpRfBFn1SbrJ14uOT_lDot_ad3niEeZN3O6Tn_5PzxPETLCvDI-HBwG5Ukpfkuha9v03qmdV95XRcB_-fPcqHcavk2L_9LoMhRrhJEMO87q2SnvzfrFDIA7tQtxZ9Ai9sNe6mJOC8F3Q8EUmDhuBWTJ4JFbFtDWmYgB78gwSuqajPCtxqnF0LLXg2g7Fog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=duVg2PmaZoolevT499LKMEBxkVVG6SA0HbnrGArtATOvHWTqa7Pjv6h2NVDMZS-wjIyrSmZs-T25xySDYlfGFSw9U-BKApnDy3CeCclTc6zx6uQ7UHTsgRzfFtQBUnBKUDA3ThYq5uvKgge9PqbYGj4b2lQSpelUEDv7JVhNnxPLuNxj7KUpSlsYZTjmyWik5coo9CpCg1zPwO1QMDEi9Ju1BDjUrX_Z8qjL4EpZlf-tC_acN6eMFiyGJ_O6fE6EO74FzTjhMVXSIodwY6ClhAkTCoM5ipFkIFLNUhua1URmSGfVTsBe9IDP9mtU3_6BceOOyTdW9fAqmRZaWBQSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=duVg2PmaZoolevT499LKMEBxkVVG6SA0HbnrGArtATOvHWTqa7Pjv6h2NVDMZS-wjIyrSmZs-T25xySDYlfGFSw9U-BKApnDy3CeCclTc6zx6uQ7UHTsgRzfFtQBUnBKUDA3ThYq5uvKgge9PqbYGj4b2lQSpelUEDv7JVhNnxPLuNxj7KUpSlsYZTjmyWik5coo9CpCg1zPwO1QMDEi9Ju1BDjUrX_Z8qjL4EpZlf-tC_acN6eMFiyGJ_O6fE6EO74FzTjhMVXSIodwY6ClhAkTCoM5ipFkIFLNUhua1URmSGfVTsBe9IDP9mtU3_6BceOOyTdW9fAqmRZaWBQSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=hcUjj713jWFKoqcT9p0vSCz9G6RaloWWoHnHjKU8OcTDvMLjsvcThodrOA4af-7EzAdK5RT9yyyNdyn2hQfQyexOEiYFY3edv74czrcMHNC3iRF1aEeIzTmui9DMfbcBXqnn6gq_WQtO0Xysn8yUg9fMT20eh6pPDXi86x0LMjU6eIbtdxHi9_y2w5F1ZdFsXZSEBPU9SwtE6FMoYdlqnlRKJFvxS8XtMtF5oOR1CgCmIWiRdQhQpbkwgB-gi7HUcwbVkdXDiBfUaLh1rTrulAv6DLnf0ouSbnxWn6rmI_ISj6ZZpCb3J64ZdMjxWsXdTNE9rnJlVo3esaicgDSMXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=hcUjj713jWFKoqcT9p0vSCz9G6RaloWWoHnHjKU8OcTDvMLjsvcThodrOA4af-7EzAdK5RT9yyyNdyn2hQfQyexOEiYFY3edv74czrcMHNC3iRF1aEeIzTmui9DMfbcBXqnn6gq_WQtO0Xysn8yUg9fMT20eh6pPDXi86x0LMjU6eIbtdxHi9_y2w5F1ZdFsXZSEBPU9SwtE6FMoYdlqnlRKJFvxS8XtMtF5oOR1CgCmIWiRdQhQpbkwgB-gi7HUcwbVkdXDiBfUaLh1rTrulAv6DLnf0ouSbnxWn6rmI_ISj6ZZpCb3J64ZdMjxWsXdTNE9rnJlVo3esaicgDSMXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXH88IYBL619Anqxk9wc_ArdaTYo0AVGGGlF0i5qflReavOm2FJ0L_rJLgBBiQXwFSUBz_40VPCEXPk7Y-QtHZ6SP8TzaEMnED0axebMcNHA58IoOnTqltN95514TbOH3MafeMjfyr41RFcOeAE_CiUizXxwmMHyjblcLh4B32gfMBmwr6tIrDwrS_IumCfbjB4n3KMh5BKjQUCibZ7jpNRJeEu800lS0SpHUHBpGHQZ1EgZTb-cMW0WcsGsro3Ez1H715DDh307nnatAKqfEHoGXbbhlBR_pmadgAwNnHsBVwQpoKErqZdmqoghpPWkrjhL6aa0McHtsoF2ldoamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=LmwLgbOdz7o88Ji_amIZ0UbBt_-2AjB6VehWGwIMMw_vo_s9k_ugA53Y2om4piSFUK4r2RnN5QMSKLZovbXV0aL6gPQO2PK0lc7UO1f90Iusv9qxvf40e3nNTkE6eJrPq8WbX-dF1UsmD9upMGfMiL_XdM-Uoq0ME5pZPJdq3e3Drs6aaaxAyi5sWjhKtbWWpTGTXo8yPciXOZ7L8UgMFuheSgmajGqe1WddMAnagRq_faNlthq1IRi9PueuJ0z_nd3Q7UirNrEmKftSciBWRvCBkzH7jpqnTb1GAbwAtQhCCP66CkzURAh_S0TMKkMFs_ztKaYS6bx6tR-hF8YCjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=LmwLgbOdz7o88Ji_amIZ0UbBt_-2AjB6VehWGwIMMw_vo_s9k_ugA53Y2om4piSFUK4r2RnN5QMSKLZovbXV0aL6gPQO2PK0lc7UO1f90Iusv9qxvf40e3nNTkE6eJrPq8WbX-dF1UsmD9upMGfMiL_XdM-Uoq0ME5pZPJdq3e3Drs6aaaxAyi5sWjhKtbWWpTGTXo8yPciXOZ7L8UgMFuheSgmajGqe1WddMAnagRq_faNlthq1IRi9PueuJ0z_nd3Q7UirNrEmKftSciBWRvCBkzH7jpqnTb1GAbwAtQhCCP66CkzURAh_S0TMKkMFs_ztKaYS6bx6tR-hF8YCjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-9Rn_Mc2nxY_2j-M7aLaMjrTIRqd0oGjlE4wuW-hgMUWGfFn0ZxP4aBV2n8O_zlbdvTfKSsJtl7NaJNizserkrbCw8czf4L77LX_c_Cm17HLBdUupydlWFNAtjte2Y7Upqz-6bhpv_UigehhDWIxB6uUhkZ20ipE9tw7d_0fud6w-0N-Fhfk7fZbr3oTOdBIxRxJT8961tqtjYqWMCu4umEvnJnyAEzJy9xk26MuUQA36kpAqs4rPUk0Woo6KXPfq4J03PdDUbOzBYFzqq2ErEorZcJMaF_QBhsemgPQ6M_i6XP6sdFv_O9EXn3oWHrp118HdG2sAcRs8YheJsw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXHpmT_wuRdwqXs1Lvhu30vcwSwnHhAp9_3FJLboxpI__Nrn_rJAwBk4INA0l3qtgHLRY-R33w2APf5Gq1GMv8n_TKA8JYFR6HhSAQLAtg2AAtQRoh0geb1wYSAOrY3djmDCBqYz5EB6zouFPYdhDXoMxztvhPQ7Jdw6waWNKKOT4-fedClLK0TdeUTHaSwuEhdlWwwAK3WmoBKboz9oL1XOW_U9xpXbzP0RujIdoRQKYcHmqiChDd9Eg-Rr1L7rFxZ6373lN0hFwWm6_7UJlwLyWeDBFSfvbj2immt7jCOjWJbSfmqwtvUXZ8vNBlDf_DY6VGJisnjQrwrVixzYEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfDLZYVdX5vHJ9025UZcshHEmgVdMc-hELE-vDqkUYahZGN4WyNOUKwzfxAX3v34rUIVElw3YrjCG-SiJp8stqaW0TiFzhmcsSQKd6jPz89EwN-FRb7WGwf24P6hW5RGXv9JYOkgPM5D-C8ipJmHntYWxe3z-K6J50gssj7iIYMh1EzTr4HB_Wa9AYjINNx5WzOYw8e9aiPl8kgzDhIlP8fv6XPjMNHo6Q7YUTu2yaqrNyOgnjenaXZ93pyXNMki2UKC5tjYDxvhJo2Hxw9iSWlTxYyjOajquqDdgvVuZgsoqUyWb7wPAcaObyAYByJhM0UbscXgKBeNjaQ3OBuS_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg24a6RyqmP4tp8y5GbvgetN-FdLozJh5Moxwt7e4_emr2zbdCyoHrcmju6IwB_Jv0efKgOY1OpX7T-PWcF6WO3pHktxpPckpqq1_zmcbZCqpLdeP0ZfNwbpA3MRd20iiSDcmkJek6UvMhwKW7Y7QBDZsQyVqjJvMYdjJadbkMgDK8VBpF0mmhSdpjVMwtCstZxZfXGjkwYwNBjf6t1h0fRcEkB2LJP1wtItgrpcMXnIibXyeSqzavd0T96N565NeFA8QvwCcm7uD93J-aF1bCe5WPOMwIWrgisKjXRDDlvxuJXbf06h2WLCEhirpff4Tnmw-na4TG5hHVNl6HqDSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=g5U5zD-tZKI9gu8L5Gs59sHuMuy8Ev7XPtMA5b2kYBozZbSSw9gYkLzFBijZa-cKSaa3tJHL6kNI6ryKuMTQWdQDDl6YBZ2WLHIfoJheYVThyb836UWhf3QPA2mPXzfuFvI1OyTxLaIK-wEBxgtEpeDzmkgdg6EGUNHPNnH9Mr79KvyywUg5yyR-DDFUkL44oBaCiBDqcwOm2w0sOQkSFeOrX_jYcMenJTucRIxNGWm3ga867fj6S7vT3xbPcwBQKIWTbBGrJeIX6mRZWl0vAW15oDhc5Z_CeSu1TxUUrPobvlzf5a0NSppS1C-c1qOYkKdnCR7DP_IUQ39MRTOCAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=g5U5zD-tZKI9gu8L5Gs59sHuMuy8Ev7XPtMA5b2kYBozZbSSw9gYkLzFBijZa-cKSaa3tJHL6kNI6ryKuMTQWdQDDl6YBZ2WLHIfoJheYVThyb836UWhf3QPA2mPXzfuFvI1OyTxLaIK-wEBxgtEpeDzmkgdg6EGUNHPNnH9Mr79KvyywUg5yyR-DDFUkL44oBaCiBDqcwOm2w0sOQkSFeOrX_jYcMenJTucRIxNGWm3ga867fj6S7vT3xbPcwBQKIWTbBGrJeIX6mRZWl0vAW15oDhc5Z_CeSu1TxUUrPobvlzf5a0NSppS1C-c1qOYkKdnCR7DP_IUQ39MRTOCAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XyxnScGreIu1Djwzdob0-hXxw4o9gMWXVFLgIMMFyfDvP7qryWaRqUzkgIjfayEtohCzDskotE8_HG1rzd1oTtd_HiUj_Gb9wcGXn815yciYoFAmUCqJ75C6neHmX9gTR_ttVeEe3AQEmV3_Jgwu4HRzdFpvRc2YrrYgQP6pJjTIZVPnMlQj5w8TRv-XCwIpJ86rl8A31Y0h3VAT9hBWBbICUL68zJkTKBuKeHQZoJseTWpfnqsyAls-ek8Ul3v1QvRsdukW46c0DwR7ilGgeZ6aal76VLCRcrJzFmEVC28ueJ4hA1klcsvnNdKAbzVlnz-o_69Pi7iF0e04E78oow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=XyxnScGreIu1Djwzdob0-hXxw4o9gMWXVFLgIMMFyfDvP7qryWaRqUzkgIjfayEtohCzDskotE8_HG1rzd1oTtd_HiUj_Gb9wcGXn815yciYoFAmUCqJ75C6neHmX9gTR_ttVeEe3AQEmV3_Jgwu4HRzdFpvRc2YrrYgQP6pJjTIZVPnMlQj5w8TRv-XCwIpJ86rl8A31Y0h3VAT9hBWBbICUL68zJkTKBuKeHQZoJseTWpfnqsyAls-ek8Ul3v1QvRsdukW46c0DwR7ilGgeZ6aal76VLCRcrJzFmEVC28ueJ4hA1klcsvnNdKAbzVlnz-o_69Pi7iF0e04E78oow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=juZ7jXjajQB2t_x3aU0ih0IpXcmjogkaD1zdvGXzGTOyb2an5QqJsIbaN8HuYcFUOUuZs5H4O2ifH2kKXI-p10tQhogIOLyUdwo3gfGWnwN4dln12XDil2uZsVRUx2EFxa4yWpBB8eARHnEdD0DTihJQWE1-DFehPkc0RHyIu1KaKRfYCmma1H91pXvxi6_g3_Z-ELehFKfI8iW44iJ-ZONDN7dtT7TFVJi29tKcMJK60OUsMHCr4J-BsQKVYzXmxjpml4q2QwNVwbuuukZLskMn-NFhkc_uP-u7z7mBPSUGmPQd8a5gBr9NbpuQ6nuE1C-9kGJvX8WklyKd0e_LEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=juZ7jXjajQB2t_x3aU0ih0IpXcmjogkaD1zdvGXzGTOyb2an5QqJsIbaN8HuYcFUOUuZs5H4O2ifH2kKXI-p10tQhogIOLyUdwo3gfGWnwN4dln12XDil2uZsVRUx2EFxa4yWpBB8eARHnEdD0DTihJQWE1-DFehPkc0RHyIu1KaKRfYCmma1H91pXvxi6_g3_Z-ELehFKfI8iW44iJ-ZONDN7dtT7TFVJi29tKcMJK60OUsMHCr4J-BsQKVYzXmxjpml4q2QwNVwbuuukZLskMn-NFhkc_uP-u7z7mBPSUGmPQd8a5gBr9NbpuQ6nuE1C-9kGJvX8WklyKd0e_LEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=E3gX6hTQXB646t_1TX88l8mK8rbf9Z8bYrQ6LP5VzPVLgcqLNiLht-3x1w5zVtJeD7Xeu7C0SoFloLDDcHIOp_S7zK_WKQB_w-9qJnT5BX1uuLGBhywAj-QeWIta7LTlvnyqGSWwcQLFUQaSjHdYfYeGRvuDL25DfShCM2hfw7epRUO0OiHr0MEhR31Vs96-J9xGrmhH8g70ZBMLhh2X8f6O7UcJScdaFsnIJyQ9UIYg38Xx6xFWjPPjSgKzFVzYdJeZ0HjbImjNhL54bq3raOmO6DpHygrPCYRpDpEgDBqVmo_aRtbEcaccNOX193ydEFwBbbylOrcthM6x9OVcZTb7Ln8h8811UdpOWNxGDKnL9p-0c5Kp9RdgXAr1GGIrtoP8pABqkqMwMMGW4Uj4Up82paFI6PUpkFB6rKOS01t8HQ1nq6lo5umWusdc5r6AwMmWILiOyaOPcW7q8YjnQTBvaIfKkjRv7TO590WiGegiEHWRziSkd2DfqiBTb1XR9t5dcvPlGi97J8Al-kOcn8onjL9MZWVGLRtZjgDyMl4LGLG-oSl0MJgOapn52uy_5Eq2msXLi08LF8fhDfBAQeqW-8uMiPunGfo1CnQfpbIznzkSI6LtPJ13fqjj6Rk5Qy-XF1siaoXii4SuKSSAn3L99PK_duVYF7HgnVsyovI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=E3gX6hTQXB646t_1TX88l8mK8rbf9Z8bYrQ6LP5VzPVLgcqLNiLht-3x1w5zVtJeD7Xeu7C0SoFloLDDcHIOp_S7zK_WKQB_w-9qJnT5BX1uuLGBhywAj-QeWIta7LTlvnyqGSWwcQLFUQaSjHdYfYeGRvuDL25DfShCM2hfw7epRUO0OiHr0MEhR31Vs96-J9xGrmhH8g70ZBMLhh2X8f6O7UcJScdaFsnIJyQ9UIYg38Xx6xFWjPPjSgKzFVzYdJeZ0HjbImjNhL54bq3raOmO6DpHygrPCYRpDpEgDBqVmo_aRtbEcaccNOX193ydEFwBbbylOrcthM6x9OVcZTb7Ln8h8811UdpOWNxGDKnL9p-0c5Kp9RdgXAr1GGIrtoP8pABqkqMwMMGW4Uj4Up82paFI6PUpkFB6rKOS01t8HQ1nq6lo5umWusdc5r6AwMmWILiOyaOPcW7q8YjnQTBvaIfKkjRv7TO590WiGegiEHWRziSkd2DfqiBTb1XR9t5dcvPlGi97J8Al-kOcn8onjL9MZWVGLRtZjgDyMl4LGLG-oSl0MJgOapn52uy_5Eq2msXLi08LF8fhDfBAQeqW-8uMiPunGfo1CnQfpbIznzkSI6LtPJ13fqjj6Rk5Qy-XF1siaoXii4SuKSSAn3L99PK_duVYF7HgnVsyovI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=osJ8FDn7VJf0cGhCGMUZIzONRXslH2HfkIW0TbTQjo6zA8HlRzpaOFsnCqR2s05mWo5bKqkdKzIfNKrafxxfyFLSQtboF17PtcY4R2cg5c-Q7m4d4q-cAFMO8lOAqZRvUgQQUZ0UJjtuSiCzDVK64bvewUSAsPeWemMS2mcT8Bm4FcwXrzMsJsah1X--4z59benWVn-Wic7mgn9e1FR0ZoQkliUXY-o0e8SLLJ02TZK6k1irJC3mXheQBcjLbL-K_FQF4vYE47-RUAJ4nIKA_D0Mion3NnTMVuUoX6f7G8WyNd4lhkbmepwllbskN24pOnDC7K5q1Ho9CFxBzhnFHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=osJ8FDn7VJf0cGhCGMUZIzONRXslH2HfkIW0TbTQjo6zA8HlRzpaOFsnCqR2s05mWo5bKqkdKzIfNKrafxxfyFLSQtboF17PtcY4R2cg5c-Q7m4d4q-cAFMO8lOAqZRvUgQQUZ0UJjtuSiCzDVK64bvewUSAsPeWemMS2mcT8Bm4FcwXrzMsJsah1X--4z59benWVn-Wic7mgn9e1FR0ZoQkliUXY-o0e8SLLJ02TZK6k1irJC3mXheQBcjLbL-K_FQF4vYE47-RUAJ4nIKA_D0Mion3NnTMVuUoX6f7G8WyNd4lhkbmepwllbskN24pOnDC7K5q1Ho9CFxBzhnFHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=AYSK6mctJxx8EoCtTC_W1PbILvPmW90tgwqQKShToPSvf3cbRrpA9-h8VYnmpQkiRTFd3SvSsTT0LxpSCPKDsym1Iv5YC_dyVH9_V_Stu3JErjY9dBU4cq2lPLM2Ia-Bcs8DTDmySan0nQZ3H6bdPWmlLb5qnlCF35FVg4M0cFtsfgd5pK25E_EQeofX73OgL0h8bp-Oumn2RCQvdH_xfJga-K45qzxB-9d4VWyPEXmQ3Ji-Yy2LDndzPhTPvJx6hmzJuQ3ybONt-33MTEFFKb4gA6a9JOuS8nzvno4wH8JFkEiLAn7ZhzIvs4IxIAdsJELsxu9_nTuTZWZATGxIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=AYSK6mctJxx8EoCtTC_W1PbILvPmW90tgwqQKShToPSvf3cbRrpA9-h8VYnmpQkiRTFd3SvSsTT0LxpSCPKDsym1Iv5YC_dyVH9_V_Stu3JErjY9dBU4cq2lPLM2Ia-Bcs8DTDmySan0nQZ3H6bdPWmlLb5qnlCF35FVg4M0cFtsfgd5pK25E_EQeofX73OgL0h8bp-Oumn2RCQvdH_xfJga-K45qzxB-9d4VWyPEXmQ3Ji-Yy2LDndzPhTPvJx6hmzJuQ3ybONt-33MTEFFKb4gA6a9JOuS8nzvno4wH8JFkEiLAn7ZhzIvs4IxIAdsJELsxu9_nTuTZWZATGxIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th_VQinFT1CYUNdxFp9vV-DkqpNa2yGQb3D9EQ8iDTWt094GkWxy_R4NFtKOr4R2Vws9x1OPsCIKy2HifKVpIpplyAFXsS0g7ccZu1yhAn757BJNfrSAsj6JL3UyVQZ8f7TMIGcVG-YeG_4UHVBnEEP1n_o6i722Z0I5xgmsf6E0i_SJ4rX3wjJMymVQI3rSroiDoBU2ky6tjKijPJCqveUILmcW0F_wfi7rsQdIv3na83OVprs45v1RU7Z2UOMrt833858g2zSGbtGUcEohaIp9jCDA3CoOhb9smF3VP7c9foRcGa2LBXNV6X_X_ni32ow4Kgsex-NtuqckRuqCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=H6wO4bBptkogwExZ1zwNYMrD2tDwM5kbiddMLNDSVT6_O7LDOHkf8K9QLfcGOo8Bc6btKrl_GzeoVqCcWFgcT4RBXkC1t2FNky6fi1_xxHfGYnxvQ13zGs7p8yOufRl6dml-vaCnh76esQfe1g2TIAgeGUSv9POJhXh-hgPPpC_XX6WbrPqPHULJzBTe5i-he2OXt0TRDVfYzCtNuGBLhtpy5Cd2bv-QsnT1lM1MP4Lf0qlDh5DTQuLuzYRRNBgOBdx0MGuWp3VQ1ziC3R3pRQBfNSGX6g34iNSbEi4DMjw61Nz2iCcGTaoM2yCoGF3fvGLebIJkBInCO_zprau7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=H6wO4bBptkogwExZ1zwNYMrD2tDwM5kbiddMLNDSVT6_O7LDOHkf8K9QLfcGOo8Bc6btKrl_GzeoVqCcWFgcT4RBXkC1t2FNky6fi1_xxHfGYnxvQ13zGs7p8yOufRl6dml-vaCnh76esQfe1g2TIAgeGUSv9POJhXh-hgPPpC_XX6WbrPqPHULJzBTe5i-he2OXt0TRDVfYzCtNuGBLhtpy5Cd2bv-QsnT1lM1MP4Lf0qlDh5DTQuLuzYRRNBgOBdx0MGuWp3VQ1ziC3R3pRQBfNSGX6g34iNSbEi4DMjw61Nz2iCcGTaoM2yCoGF3fvGLebIJkBInCO_zprau7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1lROq9Wfgumq7_m-miQoFhjUsUBBtC4jFnO5HdkuCqZu0jSOPbvaO9e7dU34V7i3dwi2BCOUjZqWelgpVIsj4mgu5Eyj5LOIr89HMs_4z33nzhy-dQu3YzEJRjq-ovNua5q4gTMYi-DJNASNIVwg6ZUCye12OkHyxGjQtfzTMvrg9SabiyCGGOSuKQ5bd6Vjvrfz_mUfyQ1KyJnP8zJ4mrWqoFN9gd4TNCmKHQ6grLnkRzKUBZ473pIbtWCzB0lZ7WgyWLqFytJRGWNq7DC6eVOtmmWkj5SVW2v_p2dvkX68l6lv2uaYb6Q7jYNiONaLdV5oN-TYacQ3TbunJ-dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwRvEUQey5VepPculjsipwqbsH-wRPggrXj3YS_BMhGasMHZ6llkhkThbGXPhabcgkL3ZyTUM8vzbQeFwejzKfTlnRgOalzEwA42buqT8GLp0dTUwhdZAgjG0a43dMso4rtcjsy9BWGg_ov11MS-WiQESXd73bLingUsp2c-qExwow1_c3AM3FyCd2hhq6y4Dv0Lk44BejZqpUBtbc-DEyUWMheerVVj4LF-MTCF78JVYZYYWaP9yJ36tLxUg5HVlzR3Nexpw0UTAatvtVLW3zSH3fx1ejZHjUCnttT8Lce7_LgwSsNPjegazZ9zqK2p-XBfuDS6BdinE7lfyLXdCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=OhtbcoO6C-h-WaBxT_2uNE8se_PsGBHWpLM1_HeRX0Bw_E0v4WwMfYTb-6SU2bMrta4svjvl1NuUWxa0VJTY7UrJSHunov641gewXIcvFshk3w5QW1HNDjrPXobUjUC4xzubikDRiMjF92lAfJ5iWWE64B-nK5H0ZTK9oR5HjnY3fcgJv0zn9t3dJIvrVG9Ltad7QWRuSw8YU9zR-qUBolj49SJwk9QYXqPmOOMq2mNofIOotz4dPLhPJ1iNVwzhk6yPghGKrAlEL_Rlv9RTPXhjO_zdDLXRBdq_goedJHuR29ChfNK5Eq3HWf0MDo4Ul_gf5kIMjcjjWPy0JeV_xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=OhtbcoO6C-h-WaBxT_2uNE8se_PsGBHWpLM1_HeRX0Bw_E0v4WwMfYTb-6SU2bMrta4svjvl1NuUWxa0VJTY7UrJSHunov641gewXIcvFshk3w5QW1HNDjrPXobUjUC4xzubikDRiMjF92lAfJ5iWWE64B-nK5H0ZTK9oR5HjnY3fcgJv0zn9t3dJIvrVG9Ltad7QWRuSw8YU9zR-qUBolj49SJwk9QYXqPmOOMq2mNofIOotz4dPLhPJ1iNVwzhk6yPghGKrAlEL_Rlv9RTPXhjO_zdDLXRBdq_goedJHuR29ChfNK5Eq3HWf0MDo4Ul_gf5kIMjcjjWPy0JeV_xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=uv33sOZm1dg2CvUMEJ34YsjHW_-VD1QbIRrHS1KWuHmwRZNok8JujvE4DD-npu6PUjc9sWzYUHg0ZkScpTCtkVcwBExFO6kiiBMQxs4T6wK9sFiiKdkH4BPgXCpmtTzw1tuqgsu68qQN48HlsYy0AsptdEuJo_rWCDk3eqJuGHQY7quLUTYGsKpP0cpIlmmtw26YJKVNjahGN6FC9WKfuNBNkZcun9PMigrfzWKTysCP0BgwwmoCPEPBQcKxUMM763_tbUPhcWM4wDw2ENXOJeJHnmVPql-EySMGIiTJKpE12pxwcQakoR35Bd0vi6P4gyurm2AXXbIXQIMhr1jVXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=uv33sOZm1dg2CvUMEJ34YsjHW_-VD1QbIRrHS1KWuHmwRZNok8JujvE4DD-npu6PUjc9sWzYUHg0ZkScpTCtkVcwBExFO6kiiBMQxs4T6wK9sFiiKdkH4BPgXCpmtTzw1tuqgsu68qQN48HlsYy0AsptdEuJo_rWCDk3eqJuGHQY7quLUTYGsKpP0cpIlmmtw26YJKVNjahGN6FC9WKfuNBNkZcun9PMigrfzWKTysCP0BgwwmoCPEPBQcKxUMM763_tbUPhcWM4wDw2ENXOJeJHnmVPql-EySMGIiTJKpE12pxwcQakoR35Bd0vi6P4gyurm2AXXbIXQIMhr1jVXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=miusTX7qooP7qP7MgY19Rv-_ZuKTxW5z-AUaV092MGZLPl4jcXQeOzIT6PxR8Cnu1ANrwS4My0W60yrlWgUePZLJILE075gecijeWUymBR1yeTgbsWN9LOXLgVR1VfSGU7V1gP0RxQPOudJ9k48B4YM5gzT2qEI7i3m_rjT7fhgWsJyeaczlQW3uDTO6_P6Vy5Oonfy3WYuSqK5KXr4k3uqECXJRzLeu3b9nzrjbfi9hsLYnJWeoGB4PBCN9zzCfR_HmdRpOQmGJw1JRrNxdYnE4z7AtGMxUHUcWhTjKb-gGUSS_UQXiRk-7kPrNttNRC7gSsyoqD0CG6AmFEa8ikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=miusTX7qooP7qP7MgY19Rv-_ZuKTxW5z-AUaV092MGZLPl4jcXQeOzIT6PxR8Cnu1ANrwS4My0W60yrlWgUePZLJILE075gecijeWUymBR1yeTgbsWN9LOXLgVR1VfSGU7V1gP0RxQPOudJ9k48B4YM5gzT2qEI7i3m_rjT7fhgWsJyeaczlQW3uDTO6_P6Vy5Oonfy3WYuSqK5KXr4k3uqECXJRzLeu3b9nzrjbfi9hsLYnJWeoGB4PBCN9zzCfR_HmdRpOQmGJw1JRrNxdYnE4z7AtGMxUHUcWhTjKb-gGUSS_UQXiRk-7kPrNttNRC7gSsyoqD0CG6AmFEa8ikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5kiJ1mkQ1CLvGai6cemkQyC_X1io9GTvmloohd2m1P-edTXvYiMQKDviwv2gWv2UdrnIUIFajQxm1RLwoplcMu_8ScTj_3LMa_N1Yo0ogGwzoxOcp5gxjQYbPLjOtTLwJm335F4E6oFhVCpA94p7t8ph_oUr-y4kS8UPyT6rUHYTJB-6lwBIotFp-zFiKQBzsPn7f1b0DJsZzONEIjmUegQOL-BO3pC__-tvf-sm3PUCobJ7OKgVuFQABPKdH8IuETPjklQcWM0FhHru-H3Az6i3k_DuGLVzZgX2OQmjRZN80g5VheGp56HL0OjV-ABDQ6CE3cPMSHBQuBtdObHMw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=moH6CbpGdmIzBUvVunOiY90y_4hRuEzmbMzCGwf4Sso3UbrRp4wyUDqdVEKCOCF1nz-ZlHageHkue5TssGnQfo2WJyK-zp-WaG-58Ry8tJ0rSO2JvBIT3PBpARWsz6x3v31Z0bEkngt8m3ae0fjM-Itc6d1j-sMtfoAnDntxw1NUZXxAPajC-2GJFu69n_Ivuz0zF643DWgjHTOa8ReMUGJvbgzjJVEHmU4Y25vYC-YX5IV7i804renZrRZNf1iSI6a1Z9ppRMMjGzU3B5R_GD0ea8rqDPC5KHMBcV4UXKqGwiwUCCToEf-bOhlkmjRugxMM-4X_qsyfCqKKk1w3yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=moH6CbpGdmIzBUvVunOiY90y_4hRuEzmbMzCGwf4Sso3UbrRp4wyUDqdVEKCOCF1nz-ZlHageHkue5TssGnQfo2WJyK-zp-WaG-58Ry8tJ0rSO2JvBIT3PBpARWsz6x3v31Z0bEkngt8m3ae0fjM-Itc6d1j-sMtfoAnDntxw1NUZXxAPajC-2GJFu69n_Ivuz0zF643DWgjHTOa8ReMUGJvbgzjJVEHmU4Y25vYC-YX5IV7i804renZrRZNf1iSI6a1Z9ppRMMjGzU3B5R_GD0ea8rqDPC5KHMBcV4UXKqGwiwUCCToEf-bOhlkmjRugxMM-4X_qsyfCqKKk1w3yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=mS-8VE3sXy5u2Mm62dGxuMvWzBZIQNOVVjsOtqVG9UO96Dl-kzO7TK8VIN2HwgzERJ8SLN3RWcWmLd8awZHzh9sExHfgimCLXpZvB79d3jwUMyQFQgDo83zKuH12siS030bPoBs24uyHxvsw1xQEEe3i4-_D6Azi43lZe4-dxNikwc0D5HvJHzEMIDmlrk54PsIVgw10gR4is08KiHJ4cXlBrmbRKK21MpjzxiTA9HWd_442XQdqqypwOZgFES1ncLrta_73AyBjl6muSu36d_jEyBW7W4Xct5D3-RIF2tJoacNTs4CosSo9R3-F85lNct5iVnwzNSh0kA73ldwwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=mS-8VE3sXy5u2Mm62dGxuMvWzBZIQNOVVjsOtqVG9UO96Dl-kzO7TK8VIN2HwgzERJ8SLN3RWcWmLd8awZHzh9sExHfgimCLXpZvB79d3jwUMyQFQgDo83zKuH12siS030bPoBs24uyHxvsw1xQEEe3i4-_D6Azi43lZe4-dxNikwc0D5HvJHzEMIDmlrk54PsIVgw10gR4is08KiHJ4cXlBrmbRKK21MpjzxiTA9HWd_442XQdqqypwOZgFES1ncLrta_73AyBjl6muSu36d_jEyBW7W4Xct5D3-RIF2tJoacNTs4CosSo9R3-F85lNct5iVnwzNSh0kA73ldwwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=PAQyb70d9VD6dsysjdcZwGawKN4wTOHL7h_NSR9vnMtmFbpZrEj7UL5W1SLLb6WZj0PSYSdUQ9gaBDhWXb_vTOfd0oZ1nyhxQykPCQyOdlT1WsgzoftaNDb4fAUEqhUg14T-j-YYRgZvdo4U96-TFPxEdFTy37grmu5LpjQ19KMMMdPAfqQzjOoDONH5N1Cqijyua3FiWbwq7kjmNzZPcIA3a5Ke_r8YfR0EVq1vQW97Qg5LbyiTr1mFBA_CukpTtr61s2fbnzja2gBwP6Mzw2qON7CzmiIUm5BvCm1XZs0oZrligR5lJFKzYnhU8vmamsbGYWJeppc6H8m_xHBlGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=PAQyb70d9VD6dsysjdcZwGawKN4wTOHL7h_NSR9vnMtmFbpZrEj7UL5W1SLLb6WZj0PSYSdUQ9gaBDhWXb_vTOfd0oZ1nyhxQykPCQyOdlT1WsgzoftaNDb4fAUEqhUg14T-j-YYRgZvdo4U96-TFPxEdFTy37grmu5LpjQ19KMMMdPAfqQzjOoDONH5N1Cqijyua3FiWbwq7kjmNzZPcIA3a5Ke_r8YfR0EVq1vQW97Qg5LbyiTr1mFBA_CukpTtr61s2fbnzja2gBwP6Mzw2qON7CzmiIUm5BvCm1XZs0oZrligR5lJFKzYnhU8vmamsbGYWJeppc6H8m_xHBlGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLLfgvwpwBsNg9SECk-Qp_F0jMH3yLmsXmRlwB_n1UfygR1LXS4rmt62tbd8I_mqREjehFRJJ7rxL1OIVYlNhCQVPaRQDU2qGeQ9Upc5O4W24sA3bISxCOC2pbhGtTI0AmHBGqGXbYD5olJMrv5-RuSAPhptqiig3lV11qhwvzlu5_0JsW6RyK4RIaKBDTuBpA08XnCG966ESkB-tiIRlnMML72ztg6BJyHPKhDR2bd84cnRxDypmecTJYJ2VBQYb9xk5MB9GbziJt3p7tf40PrcCw2WtqUrt9He6LXeKXBPqhADUy8hynws_XQ-hTp0JYV8uiLDf4Ldl2fAmoBPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=RzHp0WXiYF6J8ZY7akd8ipX_8xycepLpsWHzg2EcynqpEkT6d3ST2Ub-m7WgAVJ3ZaOGUhsieQm0GyVIASVxyNGtcoNwJYAUWwO5ZGCVRKo4VBhYAcbB7uBCdQxcNpT6XZw2u-sW9II5VEYZnmHylQGJMuLzg7ts9RLIqMtNvYkyE6v4jqm4gWfLJ9ECN8dxlr1LtochLs1NnN2BMDSvdK0Iw_5NxTf2JGjOgDDKRNj9LemIphgBDPseYgsXFsl6tsFNvybLGCs28C0R9MlpBMWQQpdOZzsKIW7BtBGvKCQRib870aKkiFotZKGgvgeiUAPK-VC8DN6QHzVBQK9PzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=RzHp0WXiYF6J8ZY7akd8ipX_8xycepLpsWHzg2EcynqpEkT6d3ST2Ub-m7WgAVJ3ZaOGUhsieQm0GyVIASVxyNGtcoNwJYAUWwO5ZGCVRKo4VBhYAcbB7uBCdQxcNpT6XZw2u-sW9II5VEYZnmHylQGJMuLzg7ts9RLIqMtNvYkyE6v4jqm4gWfLJ9ECN8dxlr1LtochLs1NnN2BMDSvdK0Iw_5NxTf2JGjOgDDKRNj9LemIphgBDPseYgsXFsl6tsFNvybLGCs28C0R9MlpBMWQQpdOZzsKIW7BtBGvKCQRib870aKkiFotZKGgvgeiUAPK-VC8DN6QHzVBQK9PzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbKBCatt4l_nyJFGlxDEgYHFnwO8pL3foft_Bhmepc5Lx-EPtdripiHZBCVrOWufclBkogTWnhz4zoZ4tEnUpdzD47Nm5Fanb_FxbnIw31uuL7diVoQggDDPBkPBxGq6FbhOKcVRkr6rpolwRZzbsuSq0NIIQ__TbOQGonKCpj9_SNrK7PGSnzAAIfm8yU4mo1f_AGyc6yPGuYp55Lj7nOckDWuho9pbUIFB7Z0yPnrkNlu6H4ynBDigX2_kFfmU-qMfCw3ckf5OSIR_mPFKet11Dl9NQB00LxgcB9nXJ_xyLsCwZN7RibG3JyIm3A5pE8RKxLphsdSbFqXCLjVirA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ebV9YphmRFHQsBwTlkW25bJYM17R2M-GL2nPoRBcvtXqK-SHldAFkR4yjX3Ox9MRo5lcSNPrhC_xufXZ1ruH5JGHIisb0evvrMuHtPusXURbfjRjfxuI1tYnJVOwnY_F2J8HkQ5ISEPdrPqjlljw3J2HzMBHUPFWsr74-1urDIYoMnChDTAkhOZvTF7OXyXbkXN2599JWuSllk0O3UbQR3XMUz4ee3b2IH6aozZC800ND2yoyp_s2tdeDTpFspnTl63BNFjsw4gC7fMSX3B7-g6s6EtWGK7jocWlThQyrG3S4Ki_oVEu_84t02mgiaPQcgDXcC1FtAG3Zrz7ajEmog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ebV9YphmRFHQsBwTlkW25bJYM17R2M-GL2nPoRBcvtXqK-SHldAFkR4yjX3Ox9MRo5lcSNPrhC_xufXZ1ruH5JGHIisb0evvrMuHtPusXURbfjRjfxuI1tYnJVOwnY_F2J8HkQ5ISEPdrPqjlljw3J2HzMBHUPFWsr74-1urDIYoMnChDTAkhOZvTF7OXyXbkXN2599JWuSllk0O3UbQR3XMUz4ee3b2IH6aozZC800ND2yoyp_s2tdeDTpFspnTl63BNFjsw4gC7fMSX3B7-g6s6EtWGK7jocWlThQyrG3S4Ki_oVEu_84t02mgiaPQcgDXcC1FtAG3Zrz7ajEmog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug55kHBOHCH9Yd7-Njh8HpIOvrnw3kA027RB5UyNiy7THAakptoV9et965OAbXIaDG6lbYfPUk4VY1p58fBmHOqDmQjE9Vy6Gj2sZkAGyxwJXFY4_1QmzqWyPitUlJW-LMGRylg53LXcf0EkSjYQ4pmGtHd5cgW5okJ0JpVG4GTyGsDcKekDaOmmjhRnB86ceO94ukSrC_xGUUj-SP_9FlJPTTyHLzQsJpJDJZOvEVNQsLb8GJnfbD1lBqR_ZPrMaZ-U4sp9MbgrW4zp8G5DxM-HpvTJyHpFtZm7kjyC_mzAUauXZboi-t-vXEZ0UxUUd3CYoMpV078SSOHuQ9QTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=VJlQ9r1PjTfFkCkjQdVf0LiWBR0BZExzH8kfLNIerkRFT0uowmAHOvn2B2jM3fYbQ_fSxORj-svQc9vEYP_cwCKvjVhgwUny6sTYNAWGvkR2LO7BnG0OmaFJB0pBuYxCrqrwfaVQpOjGustoIF678OdxT9LPvO0xh15oJHfAMY-VcdocWZmi5pFnWzu7y3ZGNR5oQFum7OZYUdye4U9qgRuUS8OeDvfhFngKdOtwtl0Fa4Opug0r0pcWkqKHO15xG0xX-3R75NvZO45HeHgzXLYbSeaowVfToxJG_dSpNpfd0qsdxcyAIebOZsoWm8guhZDqohf-5MIvWIRhzEZNpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=VJlQ9r1PjTfFkCkjQdVf0LiWBR0BZExzH8kfLNIerkRFT0uowmAHOvn2B2jM3fYbQ_fSxORj-svQc9vEYP_cwCKvjVhgwUny6sTYNAWGvkR2LO7BnG0OmaFJB0pBuYxCrqrwfaVQpOjGustoIF678OdxT9LPvO0xh15oJHfAMY-VcdocWZmi5pFnWzu7y3ZGNR5oQFum7OZYUdye4U9qgRuUS8OeDvfhFngKdOtwtl0Fa4Opug0r0pcWkqKHO15xG0xX-3R75NvZO45HeHgzXLYbSeaowVfToxJG_dSpNpfd0qsdxcyAIebOZsoWm8guhZDqohf-5MIvWIRhzEZNpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_j_BOGESaiG_JY1OtFvzP4Rj0fAGasSvat3qU0BRy--eVfiCI6aRCjcKSOWutM5kizsgFn6PE-O_ZpDtkXJheY6IqMLg_NEXS4MycM6agsscbeIiSuelMEcvbBuivksvGkBYLOc2CaGUaW_ho6-DYLGhVKajWkNCMMVRdeerHP9kljqhaA_6wWgMy50HpuJVritSUMxl7swwgugMnY-vkzIPllLq1QXL9VSklNx_NYXQb_l9GK1Tz0DqeOo8YH3oXMdAScfIFt1hQ-UIrmENrBfikC5HUcm6CWd6YO3MCSGtCE7gwvjhptjOtrv9e5_83Gzsdu_TkCsylp_516xdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2nd5wQNWnUpFw5JokYejc4PPjAmejm6snAFh6vhHQWJ0Idksh8dWavR15caTnZ-TAgkoo683TgVA4cCgoYyi-sjp-dtqWFHLWy0kAunrAHJsf1UPB0-50CTUt7ZPb3kE33hFrEcEWGugrGpEOjuO3jxUxxDAS38-v_xM43nuC6I0LdGABV0ScD5nOQZpcyUjRh-iwmh-ChPgTVXbEAeZncy8yJAAHmq60r30UqrhQ8I5DvtAOXhdgHgUlrs3wC5DNuNrRV-alG4-_YgXwZw8cq0E8oEJ2qI9ttTZu5RrYNH8E8sP-kGOS-s-S3hsXEANxN2jG4hC2gKOZFGsGgMSw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Tlr_avCW0AAtEDYe_y-f1TBOgqwarqo0Z2H3TSbUsyfdABftalfSWt9en5rPTY6f_0s_UfQkElTVIiDha0brmH0fzBoic59gBaZKd5lzpA6YFO-biquLvtglOc8rR2BdLRVo8V-upe1MNaEtpxYjxK44WtGQ7CBdJrC40KR0OxJjXsKrDTvjcDK5JDJpaQxiKx5MEx-kj8LlwkripbrAVJZZIwJd34N2PJmv2R-Zvp4N_OQ6EN3ip6ud5cRIty7pUQWZNYOzQirabOAVAhbeocvVjhgsbj_ll4LcRaZ3t6aO9IUjWKAjFh5QS_bgRJ8RhzaXf1ZISTcVD609mhmfdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Tlr_avCW0AAtEDYe_y-f1TBOgqwarqo0Z2H3TSbUsyfdABftalfSWt9en5rPTY6f_0s_UfQkElTVIiDha0brmH0fzBoic59gBaZKd5lzpA6YFO-biquLvtglOc8rR2BdLRVo8V-upe1MNaEtpxYjxK44WtGQ7CBdJrC40KR0OxJjXsKrDTvjcDK5JDJpaQxiKx5MEx-kj8LlwkripbrAVJZZIwJd34N2PJmv2R-Zvp4N_OQ6EN3ip6ud5cRIty7pUQWZNYOzQirabOAVAhbeocvVjhgsbj_ll4LcRaZ3t6aO9IUjWKAjFh5QS_bgRJ8RhzaXf1ZISTcVD609mhmfdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl6DYQ0xE_vPjzmvzu5uDjx0HhSJ_maDScKd94_ymqd-VqJFSz499wmHl6HErDJ8boHXRIviyz96iXId6F3KdplT9dZCwUttoso8tmL8r24xBd-VdwCfH_kWO2UNVLUEDJ4SLbwwFsNkU0Q06bXSCfYfKTz0tUPpBVIvuItj5Yx5Q2tAUo_0SnKcdLLtRVg01hicZLvY0stwe_P1MTtgcLsckc7pWGswnmPEJ42neaBE9R-xvDV7SqaynP7kSv0sMI9s61CgHdGIi3FE--zt0E4eyILll_Kyk4Sb-D1cxy6JHzVvcyvFZuqcy6YoaR4xJDokfplyGZDwXnnGP5H_4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSKwIFglFsPKBj7j7qNSfTONVS7G0BvKHhDtli8G6BKsmUTN12Q545LBstGoWZWFsbdLdergxHGhsZoyTU6ZfwPebZTiUgXqqujrQBSGLayofR1Jowk2cX0si2RBRQ1yBBpbthwkza4sQQf6P8KWbFJOYrTVmlVz5W6cCbwMgBthhHtcRj48kmzAq48aVX2k4qHoMTCMiD-SG9FC5BtD0l3RqTIG3xHPSqQUKJ-JwXpno57bu0FJNVDUhKkKlfsExNmQHFAKrvLqwQMSSIWmGHvZwOUrMzA0KsI_b-wczq-1vwqzVwyexDO0WH7UuMmBnPLOtBwWJzq53o4yHM-r_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFtsqf85SrP1yuhRPrwXB03J8jA9xIWmItHLC8ny0cbVnHzwLXTK1AvIWp0cHrmTXMJ0r0QKzg5tdXR5EL8XLHXfzHeacZVpzD0AlPT3VSb_9W69_2rV2JF9OdG4pRloemLPaKRIElzxajDk71RBOR-uwQTaSX6bBBZsbuptDtXSGw-wOlRWkIdZhBUi68H7B3F4ulb0TNFCxgX88LWgHGHmSSUfxy3FGGysEDdWy0Wr4fAMnpQ_U-EfSNeg0-OmYIlevUCEvwU2YWem2yS9k-APscmg7cpsUgVd-qu88oyJYsFpEGMjANp9HgDjaOFjydbpmKATLOAjdn9riZ3cZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9GLSPeRvX6NVPy-dEZR1EsnwZ5drIWYdj6kmahxZy44Dvmn8QIriQsN56Ey0emdd6O-XusXBtDfSIIeZaUXOya8FBSNrMkavFfxY3A5PxZFi3ENLMv4wf9x8B02xU0eWVexVfUdDWCqBQ1ggoC3ygwpdIrIIyaA4mU9dTNUi_scWsRDS-SIjVBSUEn5defKc8XZyYOCuCYNPfh9PhrhT16euVUjKqJQiflenPmvjcA9kIdpTxngCk_qEbgFwyT5GzxWs6mMMVGuTem88dsPviEnKgYCFr9bsmUv0sjmzqvq7XGIHvgWOfJmYTzSZmt2Xlasg1wu47gcmnR-IYR6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZROmIRb_ubjUd3kOObWPpIFcVDVw_V7RqtlwbWhouwJC2LdfZwDANPIfSrvjqjYIm4rKqHDPWxxvWudLjTT_L7q1sT2yIojtpzPPqJOVlfHevsWlfmkogDK00NlFJsDLnmxb7bgeJyZ6bQxf9dtjSFDVeTwqV25RQIBF-nzIJFYzJLI3yPaxP2yuZNOK2QueyCPdUBJy44AGcAQu5fHxdb4Jv8qaADaaaS9W19KZkh7XuFPGmmWFPVpyhO1it5EMou7W8PZWh86THnZjE8W_jV4UWIqvabOgsYv4f8FVpNulgtBZyXvJafAKffXcPnvdBzPKTrrsD7emUlaoEB-KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=gQdeAFQrhEhSRYznLSJ52aeQ1jDaiYzm34hkidxOWVQnsKMZ1B7ThXcK3vsN27K2oI96ZPKjAYU16wiiBxT9a7o53NyYdbLgfGxH44fYYwzNS69JW3gB9YoNLdmk6r881Pp-_4e9QeRb18XP0pGG4wolX21zFdx6BmJmjvjU-0UQfF3MhV8esFfyDREshDVKLDjEOu-g6eSRcIunvLVgkaUmqIOhYZbvtuiKRHkUu_Fwamsup8d0uZzZvMuCP2vfvHe8mAlo-aVsfX7s52ir5ZP3pi5iCKpr6VTRlmhJAhpSMcr2h1LVn7qDuN2WlDnZuUQ_djngp9Me0LJr2lan2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=gQdeAFQrhEhSRYznLSJ52aeQ1jDaiYzm34hkidxOWVQnsKMZ1B7ThXcK3vsN27K2oI96ZPKjAYU16wiiBxT9a7o53NyYdbLgfGxH44fYYwzNS69JW3gB9YoNLdmk6r881Pp-_4e9QeRb18XP0pGG4wolX21zFdx6BmJmjvjU-0UQfF3MhV8esFfyDREshDVKLDjEOu-g6eSRcIunvLVgkaUmqIOhYZbvtuiKRHkUu_Fwamsup8d0uZzZvMuCP2vfvHe8mAlo-aVsfX7s52ir5ZP3pi5iCKpr6VTRlmhJAhpSMcr2h1LVn7qDuN2WlDnZuUQ_djngp9Me0LJr2lan2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=LOwnFkP0hGqWvvb4G86CLxKMybMBL58ItJ-LKNoqfTey7FukxG1AFGwOrSSK7mOzqxeY1BZb-dykt2n2Lgym65XkQIrH_gnDBdwHJERNaj7MfFake2Bc_oqtxzVYI00XnA91-dVv3DU8E6H6f0FqlJC0DQ_kN_RxNce4yoPAhMx1X-GmzRjb7bz0P5vxF4kbwj2fyZ4JlQPKBh6aWm10LCN7lLSrrRzUcN7BwxyfPOPIEGhjzgSQM4BqPJVwP9v3JJy2-Y7RVWSiDrZ1RKc7bpcsvakfFY40Phx24ZrYKbkDHNP2KvBD9VJIexPiGKSNEsB_UkirV3C0CT8wh320Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=LOwnFkP0hGqWvvb4G86CLxKMybMBL58ItJ-LKNoqfTey7FukxG1AFGwOrSSK7mOzqxeY1BZb-dykt2n2Lgym65XkQIrH_gnDBdwHJERNaj7MfFake2Bc_oqtxzVYI00XnA91-dVv3DU8E6H6f0FqlJC0DQ_kN_RxNce4yoPAhMx1X-GmzRjb7bz0P5vxF4kbwj2fyZ4JlQPKBh6aWm10LCN7lLSrrRzUcN7BwxyfPOPIEGhjzgSQM4BqPJVwP9v3JJy2-Y7RVWSiDrZ1RKc7bpcsvakfFY40Phx24ZrYKbkDHNP2KvBD9VJIexPiGKSNEsB_UkirV3C0CT8wh320Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=POeBR54PQD_EjQeDixqgIryxoulgl7Uz8Shl0B35MT7EYLhj9ONplKu_CRne1GYLizi1tRDCCz-wC4woV2TKpcHhHadiPpoTzrbIuDlsNi5o1tqXsmQdCFovknEUT2TqBqrSBjbPzy56iiKIq9FCFAzrARglSKKU5ae-zE2-x9nmkSeje2hEgi-l6CeLu5N1uCYgycM9IEfzRaddN374hGG_8pW7pJw82B8wOEKLWH_z6cXpVtUmQWX6j8GxX0fOgvvvtkIb3LGGj_g83NTVnqfxrCfzk08ioeL0ZOiaMChViSm3x7LXRn48G8oIxdGIEcwgM1SnL93hAQB_9b-LGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=POeBR54PQD_EjQeDixqgIryxoulgl7Uz8Shl0B35MT7EYLhj9ONplKu_CRne1GYLizi1tRDCCz-wC4woV2TKpcHhHadiPpoTzrbIuDlsNi5o1tqXsmQdCFovknEUT2TqBqrSBjbPzy56iiKIq9FCFAzrARglSKKU5ae-zE2-x9nmkSeje2hEgi-l6CeLu5N1uCYgycM9IEfzRaddN374hGG_8pW7pJw82B8wOEKLWH_z6cXpVtUmQWX6j8GxX0fOgvvvtkIb3LGGj_g83NTVnqfxrCfzk08ioeL0ZOiaMChViSm3x7LXRn48G8oIxdGIEcwgM1SnL93hAQB_9b-LGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=cVPTObLGkCYVp7lQlKmBLDBMOZ1kvHRfMfLM2gN8T63efeUsu4dH2Cn1TXJ5fD4V08lK8EtJ87DF74Q0AItz2wrLSlBd29yhsEKf2CEyimXErOFfJQFEqF-9AlgooWN0t3rCZlaFytxx2vX4AK_qjC1BB6jXQiLgUIKxRvb-jQuc_YHlF7W8xLhfl4JgviDMFuCKlIzlQosjnCIlRH4j_jIlNICILSxoz2TVQVif3BQMyoFN6ewxM0th309IOcPBzeVNZeI8VtD88wic6nCuOHIjU9nlbdxKeUqKnzUruJa1zNkGNG3TqX4c_LIDeatPaX5Vriqc5one8UEEfoepew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=cVPTObLGkCYVp7lQlKmBLDBMOZ1kvHRfMfLM2gN8T63efeUsu4dH2Cn1TXJ5fD4V08lK8EtJ87DF74Q0AItz2wrLSlBd29yhsEKf2CEyimXErOFfJQFEqF-9AlgooWN0t3rCZlaFytxx2vX4AK_qjC1BB6jXQiLgUIKxRvb-jQuc_YHlF7W8xLhfl4JgviDMFuCKlIzlQosjnCIlRH4j_jIlNICILSxoz2TVQVif3BQMyoFN6ewxM0th309IOcPBzeVNZeI8VtD88wic6nCuOHIjU9nlbdxKeUqKnzUruJa1zNkGNG3TqX4c_LIDeatPaX5Vriqc5one8UEEfoepew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id1H8QLVO8XEf2ldtU1CBempOQqYZqBFBqO8E1UItKUgef7qkzzpvkDgxi2I_j_c22gQaNTu1sXNrbIB9VfsVhSK6a2SBprEO2k-L07BZDVj5X5-qo9ecQf1ikOXDegQZAzNM4lUAkgoiyVCHKxYGJAFHhjhPR-COr8gS81p3F0jgFW3inYNr_FwikAy-HPZKllIwdIZA72UVBBTF3GsfCF6DnIStKxwEwPizfG1u8qhjzLaWPPuUekhIBoMMhqrH-SjFWl2k74IZnsm5bgc6SZNujjRz390hJnbTNjqxtxbWgy4cEGseL97Doz66-Js82RztJmW0A_t11GFAI_jaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnISIGceQNVDCU3BFoQ5dmsod-rvGFeDFa-jtOu872AsGk6MvKFW5oNF0QH_Nl58cPVfbe7tOthtE-fKQnrj60VS5POfCpQq_K330ZHCb4ALuyTiQUvASq8xSBnGRGRzaLGcNIbU_HqE8kyd_G3W8IMK0nS8-XN4pVrfnJPAfsWHYPdKXyYqN7vhte_5SOVPLnAJ8Eng-IKoN9gF3CgWGX8CeJmdIE_2fc1UXcn42D5e0OSUXJilFdyyzeZY1sL0YZJhtZxUeMo3BYEub9hkOcmwGwf49LkQIAUMAQP9L4BWVqv0v3CKbJW6qdmoudO7KQvWAKFvUXtjr3fx1B0wEg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=pgxlzHOunG7KyJ9I-P6xM1xM6LeOUh4y_-e5pKDMLfXe0m2vcgoB7CtMc_oiVLsVQTJ2wLy29msS2D_2gwQTLL7puv0EJSBd2haRpJ6u-hEgrlQkztCZTnO6IkqNLo28qv4QdPk2OrKOK2OO3PLqWs8CXVLSCVSP6kW922b8jXUYk_feS1CV1Hxfr8UmvKlskmmGnYN4oy_ZQaJ4XX24kWPulr6qIVEFrZcet4JeDTuytwBVMRXRNTB3onzatBknlvrGr01kaT0YpHDvI5pYXQhWaT83N119BNtaQbjLNz9Vz0udLtoAWVWtNaTeeqpr2VqUNk23dyf2puwKZStK2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=pgxlzHOunG7KyJ9I-P6xM1xM6LeOUh4y_-e5pKDMLfXe0m2vcgoB7CtMc_oiVLsVQTJ2wLy29msS2D_2gwQTLL7puv0EJSBd2haRpJ6u-hEgrlQkztCZTnO6IkqNLo28qv4QdPk2OrKOK2OO3PLqWs8CXVLSCVSP6kW922b8jXUYk_feS1CV1Hxfr8UmvKlskmmGnYN4oy_ZQaJ4XX24kWPulr6qIVEFrZcet4JeDTuytwBVMRXRNTB3onzatBknlvrGr01kaT0YpHDvI5pYXQhWaT83N119BNtaQbjLNz9Vz0udLtoAWVWtNaTeeqpr2VqUNk23dyf2puwKZStK2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogm7mfF-3a8CmLZHbpBCGGr-jaSDwCCk_MMf43LBaEs65_Z0CoFfsKv05jgsvhSf35jAPIZA0jVHWHnPPC-5VyYhcFg1J_7G8UMRBzaWvUJVpq-_9IzzfgHmIR-GcYxmSpibYrtuRzproW1s1Cf30VT5pUi2aYEMB2OU0fgzQ6ChH728mOpAlA-A6m8GGmcKbxwtnpsvbQj1c0TjBikB_XM4IQ1604IsHxSrBVe7f48cmDKRhVRQelk0g9URJdrmGVjGX_eZepiGmSDN4qDRr_us5m3ZvsN0uEYkkwFxD-GzswdAiUEAJuNNvM9SaW9As9DEPU2XA05v32FBPOtioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=rROTbCzwv8ZsKI2ZL9dcEVyvqLqKlcR95KfA-ap6fvgAGdubeFg2xoGxXsjZbgbhTYZhhfcIkrn4btEYwXjJSLZG-_3yucRuPJIahhddT6avKztFZ_FFoxHHqmWg0CeqOR2qZp4KPzdi0XTSLJHMUruNivl8SOPfmCHRDSIIJ-jgdtFUmY3AtHeA9nfHsKwlysRWqyQVOtpFgxT4YLEjM9jLQrMf7HCqlHxa5_Dm8c33j00ZEuCDbprDz74IDOXGfJLBPVjEer-S2SeiCGDvLUVl9yn-m17c9oy8lflGmumgaxRlC9TPEQpSqMQbnh5wcO1RywH7mUI6wnccGGJ3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=rROTbCzwv8ZsKI2ZL9dcEVyvqLqKlcR95KfA-ap6fvgAGdubeFg2xoGxXsjZbgbhTYZhhfcIkrn4btEYwXjJSLZG-_3yucRuPJIahhddT6avKztFZ_FFoxHHqmWg0CeqOR2qZp4KPzdi0XTSLJHMUruNivl8SOPfmCHRDSIIJ-jgdtFUmY3AtHeA9nfHsKwlysRWqyQVOtpFgxT4YLEjM9jLQrMf7HCqlHxa5_Dm8c33j00ZEuCDbprDz74IDOXGfJLBPVjEer-S2SeiCGDvLUVl9yn-m17c9oy8lflGmumgaxRlC9TPEQpSqMQbnh5wcO1RywH7mUI6wnccGGJ3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDDopOjeNhrQyMCh0h6mL104S7D2lTUIaQjFhc07fbj-JLovhMm_WceSJy5Trdp5RzOdl8Owe2abP1fGKZrLcc3gcK4RnnlgoZ97GsV-jyiDvwaCe5AX26raGvvWLDb8kercAY3ZVGRMb6h4TR0noX7-XWxHuftci5iYGfygPWRraFgT1gCz5v1WaF2ShjwCDZ9hyGXcRIys_Vn7q54f4VNdrJdOiRhl5YlZyjt8hqVVmTyHfLklZtPpjK5UEvc_nSNxtF_DSb_GWJqRvnOjjkxWnnNbHoPTrIgn_1-sIyq_vYF5HWbiv3V5bYUbhGArJKrIA4joC05cokNuHiVRPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnJ63fPcpqPz1ujfCdgSPJFqMS1OnQWqDAy-ifwitqaoNQqja9ubgamTWlWeKKNHhAXDBqGf-cIrkusqsXdf5uF0s0LskLsOEaZl9jcuaLuOynnmICt3-k8jY_ZdxLpAlx6L4OFExy50KIHIxBYaoNtT8UuYHrG2s4OyHHG5yDL_XUe9x7Ylx4bhmgcpJjJjxqXRCpVG34rYxftTqx2tUYXtSpObUvRvMVa2NSGx31tfAvqyk_s5MKWtU3R2qkm_t7ubC8FA-DC2BAf9wj4JhKhDN5aa9wj9LCMMSEB30eg2fkUEMEazPtAvB2OcXhdzfjbVC5b91MeLtiSVCIT_vg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=BH3Ro2jUgsmc2KBtJ0oagoCp9eo4hK1EQy055zhbuCYTsbtKh0WGYLLLz1HlzfPC2KofcSGIWC1zc_8sLHGSGkyOtQiL1l-VWhfA3ImGAkuEDxKIBJk8T6NgqDKCWYS8mZK0mSi6MQhKkIMPFTdN5A4SJh3mJvtl5tMdRtsGYVopnb74HA025X-PwgYRMBJj3eG51Zw1xMankqaQwB0-V5pGqe7iiw9km7nRoC9A-4dh4xB0oB_-ww2Sm7lGBTX7QkNk5_yhbgu5hTpuAZN0_tWa4iy97c4Ax0JY_8x5jn6f4EXWaoJzuGMXXvbcrsBXPQFn38he93lcLffd2OwJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=BH3Ro2jUgsmc2KBtJ0oagoCp9eo4hK1EQy055zhbuCYTsbtKh0WGYLLLz1HlzfPC2KofcSGIWC1zc_8sLHGSGkyOtQiL1l-VWhfA3ImGAkuEDxKIBJk8T6NgqDKCWYS8mZK0mSi6MQhKkIMPFTdN5A4SJh3mJvtl5tMdRtsGYVopnb74HA025X-PwgYRMBJj3eG51Zw1xMankqaQwB0-V5pGqe7iiw9km7nRoC9A-4dh4xB0oB_-ww2Sm7lGBTX7QkNk5_yhbgu5hTpuAZN0_tWa4iy97c4Ax0JY_8x5jn6f4EXWaoJzuGMXXvbcrsBXPQFn38he93lcLffd2OwJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=FcKnZqF1mHqWjsf5dOKicXTRzWnZIYsvA-j3gTU9C0EWBChnx6ogj9c1weEx6uvtOTxuOdQO_1hlPlNqTck99JMqFOXxKKe6YcIThAexb6qgPBqJbRohNpbx7WZxJpMofLF0X2FJCdjzkvaXPH4jMtehR9sT1X-zPjerpD65ynyjWXxek6Qt2Gc-DkMMtkMoWXqznZTvjup1XuFtaHbu4x-ZQ_DZW2Vhv7sZIIje7yb8ZzO6g4OS0u4fnWgWZDZrzbrdeXmKNXGo2su4FKgUDBeHZxzA-m-U_RWYgNLI3mdgQ_TLumBwJzVbVGZSyAjCHb_v4SOpAcLafykad--G3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=FcKnZqF1mHqWjsf5dOKicXTRzWnZIYsvA-j3gTU9C0EWBChnx6ogj9c1weEx6uvtOTxuOdQO_1hlPlNqTck99JMqFOXxKKe6YcIThAexb6qgPBqJbRohNpbx7WZxJpMofLF0X2FJCdjzkvaXPH4jMtehR9sT1X-zPjerpD65ynyjWXxek6Qt2Gc-DkMMtkMoWXqznZTvjup1XuFtaHbu4x-ZQ_DZW2Vhv7sZIIje7yb8ZzO6g4OS0u4fnWgWZDZrzbrdeXmKNXGo2su4FKgUDBeHZxzA-m-U_RWYgNLI3mdgQ_TLumBwJzVbVGZSyAjCHb_v4SOpAcLafykad--G3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOxddZ07fwGA-Nn4uX0Jh3OAsD0PCcWkX8JRqSRFRaC9phU4weltgeZN2h18IFhHZgK26dIRv1zf7EoWBGG209QjGstR0lDN54LWW9yzRwSQzlw5m-YExMDodHPXG8bmfSGy3qhD4h-Sd8GKoupCWbs8aNZMvPFq2lQch0ikwor0FrUKnWKnjaUmRkQdoQEwfPGxkrp__Q3Fd6rcGX7B39ibDqJ4WR7IxoNp8Wkstafhc7nB9Hrbek3bIQK1qP9BjGLZ47wSbepAKD4UcNaNoPQeYHBbcoAI19vrQdC0NCtl4yfLsfZ0YFKmYc2JGGrKLjUaddTLL1O1mGGnsvwHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIdY4A5haZt1UPEzLHPcu0cexp_ooNmFPhFKZKu6VhnF-IkkozGTqF_S76vHoPFtQEqwxzsnsrNW3M0_yELGiLXuIEYiq5FLfUKxgjYOSwpSakNJqybA6ETwbSv_38XeRY-GqtVBLsjk9V18gVkh5x1i69O5nJmDSUkcnuov0xlVQe_B-d1rMjihjgtIfPRwOaSrdMvoWm9LAhgSzVAFWmcC-qW9fHB8i7y5A2RqZ8qQyd1IN8znFSW7_5CiKrpVLvfluPXR9-YdKKQkSAyp6UcllTr0Nv0ni7CaPVz2X17imUWB_YLIGzYWtJMgKDwQpEx01GvgnY0exW58qFruvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKXWhEa-04ZUhH5AhaYxu4L99zwJCeofvqguHe-sPVZHVnJE0FzYZ10q8PuxjwTZ7qdmXM7xhHcRDSQEwjOUT5kAnCmEig-6mGvanb9FwsfMLJekAv5-VsSBgerXu-XeWtduipyoPXn7mq7-_UylPYdbbAREp0pe54XGvXZGNhtoz3iBGUhoGEJd88Hc5rLPUhG_S5QFViAObXr4dvCAaQ9PhVMt5QmA_ctg09cf9Zaz5IFK1xmUFfXkX3w0ZfxbzR6L9zGTrnm3U2HYptFsCQ1oyfsMl7x41Nb_uqHS2townwVriyIvJwPaYlwb6mteen8fImPb7-KJdMMaKy5KKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
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
