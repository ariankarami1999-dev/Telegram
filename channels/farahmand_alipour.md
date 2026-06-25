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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 07:27:51</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa5qiA9m8oU_ib8m_H5eYZl1IHLauoZo2-EYpgAKjfZ3wpiw10ca_qUgRoKTFXt7tEXSQf-3miMO3ocHbdcHpCwpSrHkTDUCOiZqdM4Ta3T7pD2hFAH5SHjWKY0-suRz7RObOwIqwZ6YnrGQI7-YEB7EEKUF_NmDuF3JxykilFpSaK0kQvBDQO_-JgYrwI36sC9M1ZvKrC-r2BcdCkmGod4sR90FCzA5OptXlG22KchK51FxzmQu1oz3c7Zddm_2KBQ-fmp-zFCdh9iXnroD-bzv1n5GPzpcmtCwejRXbtV6bpGQ2jgSY1iji7H_PiTPfpf2sVqLk7JPQXuThs3-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkGf1V8W3zgtbmMI5rlwqNx6um0lLquzPfsvq10XDC3e0VbaZe15e2HPqVmNu3sphpGDrE5z9Y9gDVKnHZKNJx6gG2k433fyO5YGr2Dwb300hZNmFobp9mqtyjb1AfStyzDDNurenQb4ujmIblei27ZcKzK570_k2M8HkjQSty_OtpAJS6a0VE1ZalnzLCnpsdG8NZbzlO9ccLbQpUKsqYEeVlCB54FlCAgByBSEuWtftU1WjSqPe949UUCTrTQsbffz-7-MKDm5kLY9tjdDWlcgiVZsMntAIomgkGInir1tQ5xKXoJCPdKQoAlL8XKMl8mLQwpPlhfPIGKolLBcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpoUA7w4fdx_oepbp70y-J_tmGlfg65yDB2vZ7JwaLCMs8_FKlkVJM4jKJSss9xJDkT7bzVq6jukb32ep3xowHn_I5Wl5unCZ7qbNsP0dggJwKfhur3T63vSVkago18Oa1h4x0Km7G1wCB399L3vpfIhurV7RTWxIFBqpi6Vd8e2sSTBJl9S5agHvJO1CtHVmIByKWcjF97fJYStbVbiQXBBvkScsVl7n2Nt69mc2eQJwyFExVsQSxrnSWE_ii2mr29XoRBITUfqArCXn4dkcbERrOWM8Ma0Zl0qrD2zteXM7Lwrdb6fHMqyTSHCNUL_FW2To-JzM6rsRoPWIPBRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfBdx9H7qtb9xso24kovTjnDbZmSIqq1DVHXM1COHi_AOzWzAmBZuc-TUE12aPoUURjNz4zJ0R-CwRkMx0KSKM3xdgAiOC6vQZpLPqr2a0AzKy8HmaQzgEC7WCTCSjJH5M8uWkt9jPYLnGq5du8ubNKRS1ZScmflvy9cK6a-DEHVXIX3LHP0g_ka4JsGHJoO_rGicw-cBPkAET_ZIhQAeRKZ8e-vsCAAhtln3SRqk8LD7cHz3_JNXOFoh8haFgEsTqTylUT__a2pt-4IszbDVIXu94PfIloNs7Mygzz9hjUEl6xf67cxwSiydjRb9oHCr_p2ELzpn6q1an1TRrDT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kvluqz9zN19CawRK72UBvkG-Hrh1W1TjGn0kIt0TnTgb8TiGlHH8krMI20iMKVpkCfMp7aApYI_lwSeb1f7TRxgsM0lrC15LRCv2LCe_GYx6FZ2eGpbHUH5vmmZjAH7Ro3d3HFjp74NSJBG64TkthlxiBRGpfeYlf4SdN5PnVfMHylVFRSbYLM5W8an7hrxD5ytJ1jjcIkaWEMUUjUcjnVXget5XWDV1qhHapbzpCI2q5AOdcvx-LqoUZnG-ARyPsV8xaI1Ul_mwcBmBiPB8nGwZXu4Fxvf4xlw61ecle0UU91HjtA5SYwWOi3oRi8sA0T5dHJSCKEryhEDrlBgIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YY2iF6b61Y66tDX3RCLVbZup07bb12Psckh93MEqnlj-c9sCj-J7x1dwm4ybXTOW8Zw24HuVRBguubhX59EvjK0iFY13_pqzRiwWjGxJdFX8fu3MKWagFAdxjQEAotmXemi53KFoaQHkJAHDUcR7fE78pEkjuleWkeX4lWPB5wc8kxUM0tasq8MNaR64K_qB87o84uof4JdRJJ0QsTa6IJlUiGgkkEAQ3x68t8cCbAwMPBrO3GSRiXJzBLVDgn_-rEKXIflVtQVwVu-7ze92gjJL8Is7SNDqUnjlY0g4lvrbKqauHmZcBusZwSJ5gkbCzIrDgQ4FsMbNI2GLElYuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBd0zYool6LRd-QvMaeSDGZ0gl_Ag2IAX5kVTAfdlWXqdVtSReLF1c3SIFBoDQHWocnAvg2Jk4VK6SfDu_NN2IbFixICzIVfqmPn8Dn9ZCiTeSr1iK2L6cudKNbz8RtMhMSethB10FuuWt2ciriKmURTGskcNxjeA1MYjS1oNiZCrqhAwvfjAWQe31JfcA_3EtQvr35ZClC9re6wL4m1T0U8qYLaLFjPPfohC6edkj3lRDUJzGvy22ZB4iX0h7GxeZKojT7CyZalK30A1g36246sMDRcGYHg08av6EVYN-tvmUaI2HM-89V1sG9ZKYABWoirfX51xmZu2ZR9p-VMng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7QG6QV2i6UvV3B8YGIYUqY7JZvUeg0BIfUqwrucImXUrjt5yLmUVqW0ZgkM58iifX3g58js0uKGyVtqKMrycm6JBhnMo2S-sZQoicJ11cjqEcu06c6jW5p-5VD0r7MwphWD7fx0K5A0zTvJuET9DtwYfK1mfaGKp5xreG2LmiVMdAX1F9igDXq5p3kBMPPC17j5BH8gRT0KjFWmwAoTBTisHc30MDwqDIgwRDReK6Zi_YWk9jwabCFRIqauZoW2g5k3Y3qC1JiP9x0OldWtgYcv1d1HDSXwn3RObM00Vx1HJM50qeVoIMSmtwgsEP5Hs0aUB1ISFtr92_jTihaYQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq1zqNn2eCiTXwRnGnKZBqq6hA6Ww9gV141cGKjwPZFLaOSoSoBIBGjPkPDFNuMVBnFDtFd7O0jlwq4Wlg-V6qgqmGR6hFgSTqaj1mPxmdV7K5kCRvctFIgLwhov2Y18EVt-el4ehtTRzPGw0rUF-aGVc0ZBearzSnR161GKMPAXljK4jYOLTX6RN83dIWTugfJmLBaYpu5CPizr2gBspou0yyQoSotoxQOnPE_My9bcC-0PAlPDuPWZsClV_ebAf7B_wvFKosfJn4y6XpNQr-5r7vCpJl80putiSO8XtPfu4PLdHavekVPLx7ja4RpgsRqCEASmJItHX0Q-RWh9Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZDZrvmqk13xyPptBfhzWHh_RLVsGjmNECGsmsUdxD1rai45GsQnTJ_yNeG3-q_0APx14jTku2OZNdgeFrB1ZyU6hzv6NtbZay0jnREUnAsjRkyh58KyjV8_MpIVNB4T6rtKZ14B20BASAsKa6UMSjOpV5sDnjAcA3URnXEzsDG7lkoRmRffFuZh6B6PWJBQZ16xWm0roMpoCzgelOeUw8Wr2bAHX8S8PMNFDLS4sqCytWLKU4j28zaxpvffpQo6fLfqoX9QD-kkUnLNyi2y2nIf0AdFR0tOk7MZJQYUxl1Uk-Sl9pOXzZjZmnRoTP1jZ4CZKg5PsKN8lkp3_PL3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8dZHsTqmaq5TAfplTvTmkG6Gjx8VlYgvaZeAwSER1KaSpYQz3fR37jD2bfx7QWI7OSnu0U1hJN3A5JyaznEPLyiEgpyQy173gygcwD33qik18weFLVM6gY4xYO6PESzN12fr8tllCO-DT_0JWTXZIvEKmrwl-yKlSMthbiDn4xK7rq0ciDoK6wqjOvMOLQXUK_kuh1xOothxIQ23HfdzXWV20Pwb1sAya-7B8Hx4aCirB_ny2sJHQ5hevimzGpgMgymLf3OuVEvoOKLDtHASOWB_53UvwHmN56JFAAdg8JM2E_0rPe8nWDL2VqKazFvx3AqdVLnxwRs-Nqd4ov8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPjB1kUdN-5UsJiNsW_pgRwsaAY0BoTYxXgTPcodQxH74g8QF9UNHyblL7n-TcCHlRcvJykfllKf2iz9ywzBRUUCG6iX4pnOgQJnzmqxiIJHwPgd63a4Pe4l3rQ3JfLf6yB_NOEUx_krmumWL6Cg8KXN4UXXsU5BuAeiSftkK82q2k1cyW16RiUI0t7ye53FYuL3qwYLg4NZgPGQ47h4HfpYyGE1Hk-jCX4pMcfIeXKqkucp55xltlhesgUZlE31F-FjyFpFm9sKpZvwh03OsxEoGpH2LjYBw4oNZRyR1RuLyWgb5duqPJIN5XowcCMqVhLl9wBsvPkrsTqtZjy_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-yy9_zlUbmuSB9W5VV6cI0MlI4Q1x0Jvh6YPMuPC9pYbc7x6Ywk5ayZu8a1P7xnTEmp0N1Dc20JQ5lopLB299ZjLR0_pL5LTPYQIFL7pTBPPBlExDgtLAeLaiHJckwrpKFxZKmhMCSyB58_rcDBk6hlzWLzeOBX2dqlCL9S-wX0bSD9jhFmVQtyQPoRHNaLuXtLITsAV40vMF-i8htM9zxqgPMrsSvXk11E1Tg13363SqB1kFIYu5vTgd2UAwsV05ZQ6Kl1N-0GkF8SlrNEhe_hUe3dc_qpSkF0RiG5_3BpJbChK7YaJHrLvQY2ZfCmlgsTEs3doLVYnXYZoXSeYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGkmfzhj75QVvV6VOdEwoes3v501aDE_90mCffOPrRVx_fMxwK1DYHFrAuuQt7hwTRb7w9eUfpbdcZOtFTEjCnZfEI1kxhN8Ianqjd16NzL4RUAvS-VC-aYl8W8D-zee7JaAWywD6LO34WbsMoemt91ilwEXUHMdUVR3diDhALExYdPmW2Qzb5iuYggotiIN-dydp2n2NHTVkdwPpTJ7NfzabquX7tLO3tXPOpYUcxir6R0zi4AGymXBqeM8ciC5TI61gf1ex2wwkt7WGSw7_DXT6Qyj37AUnoEKqOk6JnNauL_J8hsEGyAom1XaKoit3mEm6nqirqjxg8VO2Rnd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=NuQmSp8uDawcJ2WSIK-WrHZhtlNlggQRf4HIR4H4Zszh-gRhhxxsm6R8exHVhombaDZAI81GRQEyU63SrKDDJQPK9MDRzqrDekUf6Wn25_uGzYmxgTPfxoQ1il2QoCifTk5DdqvJcdbGBZzHtMMOSL7B8XbuEkWIHdRvk4tRY71fjsHPaFNKsPUqeirpvKBtcYHi8l22YKOasoqw1uAYzM0dZhgG1Qp4d6Lm8TzLzxr2uU3TY9huiLRVXO4eFHQ9Qsq94Juy-mBxLU5TWTcEWG5ejLyDv2WTRK7Rf4Soc9haDfx1idUh2IsL5rUgttpmQPe-PwcF1hzsYUs1jvl1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=NuQmSp8uDawcJ2WSIK-WrHZhtlNlggQRf4HIR4H4Zszh-gRhhxxsm6R8exHVhombaDZAI81GRQEyU63SrKDDJQPK9MDRzqrDekUf6Wn25_uGzYmxgTPfxoQ1il2QoCifTk5DdqvJcdbGBZzHtMMOSL7B8XbuEkWIHdRvk4tRY71fjsHPaFNKsPUqeirpvKBtcYHi8l22YKOasoqw1uAYzM0dZhgG1Qp4d6Lm8TzLzxr2uU3TY9huiLRVXO4eFHQ9Qsq94Juy-mBxLU5TWTcEWG5ejLyDv2WTRK7Rf4Soc9haDfx1idUh2IsL5rUgttpmQPe-PwcF1hzsYUs1jvl1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVqtYUuJ7ivnP9B1Xs7JH4xEUZ_3ArPmQsKcZdYS1MrozhRE191-ZwmKJWsmQqNaHzoiArdv9hlLYTj3WbF93VfCMJ-K5cH0j0H4JCyWvvLGENJlJcLyRc8Z77svodu2exIJGU8xwHnf3NKL1YH94AYOCE0E8CW81EREXfDbU49WLgF9vwUW3UlLyAJgfDLVSJyowgCiQFhXNL9KjIFk1PqrrMiPgBCxliRy_A4RCduV56c9Wl6Q9Vt9R_jY3YgELknuJf4mJT_n1xUOtsbkeroTbtwQDxJYIdp3kvvkHPpwRG3uSVrl3zhfZI8x06Tuw-c72phspT8AjTXxlWAk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=cFPmeGELpNQuxZKtTfnN-dDpfF_Tr8JA9seJJf5pZ2NNvsy8QSkGLEs4dLDhWNY6UKclgCndTibvgSW_QcfJRQ7Dzs5cav6ci8fEFHdtUUYdYz0UHTlxoTOqpkox-wrak4KkXPMypAn7GpVO0aeze9lENwyoChkSZ2RmLgD5sP-JCIGQJerLk9WzCwtR9xR8jK9v_w9AxUS0yShMTxtWCgjAixntZUZJ-Ri7XZ3iPqR3Fc_covOQJPsVK20U6XxJm8rJ9tlDJDDcRFvii-TkWdX3dAXA28DvRC4u2LjWPaTwhESwtKqxSR4t5DIghCa3LyVK26PfI9bJcw6LmvDlog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=cFPmeGELpNQuxZKtTfnN-dDpfF_Tr8JA9seJJf5pZ2NNvsy8QSkGLEs4dLDhWNY6UKclgCndTibvgSW_QcfJRQ7Dzs5cav6ci8fEFHdtUUYdYz0UHTlxoTOqpkox-wrak4KkXPMypAn7GpVO0aeze9lENwyoChkSZ2RmLgD5sP-JCIGQJerLk9WzCwtR9xR8jK9v_w9AxUS0yShMTxtWCgjAixntZUZJ-Ri7XZ3iPqR3Fc_covOQJPsVK20U6XxJm8rJ9tlDJDDcRFvii-TkWdX3dAXA28DvRC4u2LjWPaTwhESwtKqxSR4t5DIghCa3LyVK26PfI9bJcw6LmvDlog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=RZN_VjvCHRw48gp4zvPT4uE4pJe_a4AQ8vaQ2wVIGegq6Tg2bx6njomyrOlWYvnpd703NC0BzQbRFYASgOPCMjgHbesR16R6zkcMiqXNNpEeHrg7O-v-DO0RK8-ejURhYPteu5V-KYZrZJ-B5YMe44IwXk346HvDO2XzwRJNZZYpQX0zp6NuMXE04sQZvNGnDGEuqTL00amSV4Tw2o9_f_yaJqR7ZK9ooo2RO8fYhKHoW5j4L8c4aD4dt5-uZb2ARniDWFeX56_Y2E563G39kXAx-kFZ22BE4Ti0s31TQkvQSmCGizT2Ic4UDDCRA8QRgja1F30BaLlJtSjfSt1VzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=RZN_VjvCHRw48gp4zvPT4uE4pJe_a4AQ8vaQ2wVIGegq6Tg2bx6njomyrOlWYvnpd703NC0BzQbRFYASgOPCMjgHbesR16R6zkcMiqXNNpEeHrg7O-v-DO0RK8-ejURhYPteu5V-KYZrZJ-B5YMe44IwXk346HvDO2XzwRJNZZYpQX0zp6NuMXE04sQZvNGnDGEuqTL00amSV4Tw2o9_f_yaJqR7ZK9ooo2RO8fYhKHoW5j4L8c4aD4dt5-uZb2ARniDWFeX56_Y2E563G39kXAx-kFZ22BE4Ti0s31TQkvQSmCGizT2Ic4UDDCRA8QRgja1F30BaLlJtSjfSt1VzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcAkBvIbagSm_JgPG0JFLeLaKabs_uFjb5BusIufQ7DfL1z2LCN8dtZQfloU7a9gb9G7RDmvvaX1Bsery4S0h6WPBc3UBX08FWhRNPPdQabKVVVOsRq7uz3Yw0rr4vO7z9PU6q8PfPGYg1hmqhVzHaMpkWAwAxcUDfdQo4srHQje_1nR1sIzN77AvrRruIGOlgkwPUs4iy_rbHldVP8By_M4CvJWff8t2voEl4xrZaNEhAfm-edTnLLhyXQBjMMZGbLUaySKa4Q-qr8ufKdTJwla8E8Ld0pl6DmTL_P0MNtgem2516S84qyLNf658SOTvXXzS3mJUKSQ5Ngd03EwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yq0lupXXCg1NXssgwrV0bZCsayBUmUWhzBgK06GTBhx9Iv6aykCCQsCu1vBTUxMUF8nx6RqWe9mO7P9qj_rzAQnxyLtWHI49tReHHCebre5pTL-O9zn_g_9ciNLmM9bPQKK-aM6qws8Z8DQxQoL34EEiRtWYuEyq6jGCTNzSGLNAgGn1AUsZ5hoYWOQNgTzxKuDrynZuvP_37aZmzmOZ068c4jAQ_weLFtT_Um6iYKCw0f46UQojq57d7CXqM1MHbn_vhDY9-2LcGczsd64OONuVBFnMbfArWja-6DxJH2gReCOuXrHYlTCZ9DaIN_YFVXRMcpnElBmQhytYFnbk5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu22euJr1TLw60ujGFwTSDy0Z8veyKj4gdk3Xaiesm_Gm1FzjzyvBE5r0nAgj0W5Gt-i2CCldx56SXg72Ee7iVC9cjU1E_zDOPU1NUS1seUE-Zu5Zld8q0ogJnZ_qc80gIyYkwobtVfyy9WqvkMuOQGrAnh3OOGjHwm1nGeVkCg2ILOLzxeBQ8WJrgJ9qzy_dhmqBc7zeCGecYTzxpDtmuFflVoyIPRZlPh9xkqya5eoqkSf3q_oz6_t1qQjexBEqMGF9wPPUrHr_8RmoEhC6E0vOmV1psqDn0TTtOwhnQHU2-YjdwwplfhAEluqZVXYbMkkvss0j-DRsiPgWAlmvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO7vEl7ceEB6kniw1WOdQLxRtl2QQMJ6dBSJaeeELyGS_6Qr8MyBUWuPj0L9Zs9_4Ur-yrPXjBWyotZa-hrsn6OmEFHAq9CswHF8N6cHORego3Dc0xMgZGYuaXRoNV-mLj06HgBuQ2ujvu0-Q-Pc0Gv_bZ-h6VSYJzSSHGPY_2Pir7d7QKtOgOf9hFw9g8JJayShgVBGog8LUcVhf21dW4t6DaIzKLf_XCaVCmr_YGVMFtrUjmvRTPaQz15nh2k8fFYaw277gswmcjhDHq_Jo-0x_vaafHvuYslEB6ArLmoYw-r4n7faBCrO8mGLVf-fzjUCTT0sxb-tjB0gBxMlBQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=MKL9dMwjJjQ3cBJJe_0oK-0B-0mWtUbLQGoIBX9OJY4LIbSfDkWE6Tn7DWVTWmW4jfotJE22TmMWtpMtFCNYCyZm8rdA2DBQzQ9eTtv61Dx9J-rP_5Hjvhs-BCWxS05F780vavEaJJcZfCcGOYEIz8_E4AtVZSTHZhqSEpSMPEUJQulYYEHBKj116o_f7OkyoyL6FSfobWGLDSv-AjX2qMSH6Wy5PWBDIgtHw1RwTU5XU2Xg-0H2iXs8uYgPaAmbWSzGLvm7Y25QtCaFMsMVKdARssTlnsAJYmb-MyqlxJ5ez53FA6L9yxnMUkiS9xliVaecVOj2hTAIbByNMm2n4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=MKL9dMwjJjQ3cBJJe_0oK-0B-0mWtUbLQGoIBX9OJY4LIbSfDkWE6Tn7DWVTWmW4jfotJE22TmMWtpMtFCNYCyZm8rdA2DBQzQ9eTtv61Dx9J-rP_5Hjvhs-BCWxS05F780vavEaJJcZfCcGOYEIz8_E4AtVZSTHZhqSEpSMPEUJQulYYEHBKj116o_f7OkyoyL6FSfobWGLDSv-AjX2qMSH6Wy5PWBDIgtHw1RwTU5XU2Xg-0H2iXs8uYgPaAmbWSzGLvm7Y25QtCaFMsMVKdARssTlnsAJYmb-MyqlxJ5ez53FA6L9yxnMUkiS9xliVaecVOj2hTAIbByNMm2n4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=r5u5696oxfVnq42oPUMdCKh_qy3SAOzkPpE6GJOeAASe8naK4T0XrkyV2OOx5VB-vE3UdZeFK5DyysGN1nF2FJKRf09kwjqoR6QjwaRqGRUUdLeoAi3oIC9wW03MmqXGcAHUZgEcvBAVLHvz2X1wLiBVM_gY2u18qKprtrU1UK8NmRMb_vqD79oKfWQVkVMzmWc0MAWz9dcHbemy5PVTW5qlsZg0NZie6uag1ySLx3WGHERGzePurLmhDVM0C1amhDcAhZII7qTs0bxytte6WNVzbDb4pn4vYGja8jJb7pAz7o1PbhCRXqgcB7eYRP0opmJG65x_9y1qAmNe918KVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=r5u5696oxfVnq42oPUMdCKh_qy3SAOzkPpE6GJOeAASe8naK4T0XrkyV2OOx5VB-vE3UdZeFK5DyysGN1nF2FJKRf09kwjqoR6QjwaRqGRUUdLeoAi3oIC9wW03MmqXGcAHUZgEcvBAVLHvz2X1wLiBVM_gY2u18qKprtrU1UK8NmRMb_vqD79oKfWQVkVMzmWc0MAWz9dcHbemy5PVTW5qlsZg0NZie6uag1ySLx3WGHERGzePurLmhDVM0C1amhDcAhZII7qTs0bxytte6WNVzbDb4pn4vYGja8jJb7pAz7o1PbhCRXqgcB7eYRP0opmJG65x_9y1qAmNe918KVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=rtCev_cGnTBVft2T1luJrZCRjebEwc2hf5myCulGTfdTwhj2tqlSd9PbKdW5cnT_s57bi_0GrKdqQMXUBqKtnoMQmQfoYDxLP1r2mG9PUfZCSMp0Wgr9JFntxM_D-MRztUO_ziX2eUfs-QGUZniLL5qU0VX28yYk7RYfRx3zHrWuqNMkVb2S72DB2iLK7ItD5JqGRWH9Kr0ly_p6tCJxMv5pdDHb4YfAfuXxXWiRAYdptcqXbo0y_ZUaViv5N0Mf2XPoAsdugMDwK1gqIixAf-8A2nWmoahYcrJ3QApR9dq2qtgbavc3vAuOYw_KXolIQKVpRCX6EqD_GSyzgUSD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=rtCev_cGnTBVft2T1luJrZCRjebEwc2hf5myCulGTfdTwhj2tqlSd9PbKdW5cnT_s57bi_0GrKdqQMXUBqKtnoMQmQfoYDxLP1r2mG9PUfZCSMp0Wgr9JFntxM_D-MRztUO_ziX2eUfs-QGUZniLL5qU0VX28yYk7RYfRx3zHrWuqNMkVb2S72DB2iLK7ItD5JqGRWH9Kr0ly_p6tCJxMv5pdDHb4YfAfuXxXWiRAYdptcqXbo0y_ZUaViv5N0Mf2XPoAsdugMDwK1gqIixAf-8A2nWmoahYcrJ3QApR9dq2qtgbavc3vAuOYw_KXolIQKVpRCX6EqD_GSyzgUSD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=feUVkTrNqX4K-7cemPzvbFvyw_J-vqhzCIN5CWL9Ym9jNNS1n2H5qnjGyDWsqulaIksLbQdb7dQ-c17Wn9ZopWK_bZP_avrfSDaR0LLbQww-ayOdK4UoordnuVjJTQfvqLdaWqKVDVaj653ajPkVpcOjnOLzRi2w3g_EFC3B2IkY1-4c0p6XjrCXQQ8b2VcsXvkUqfbrpm-T3IFAlfkwAntjES596D9YW5mpW6PzfXTkKyAt5m1H1G0SfU11TNymz9OgN971k-k5erZjWsFMcKzpAy8KmnusksfXQI2WlQO0_E-ySRWxsMfzwbh2BKROCz8eVA2GNVzWc37DVr4vy1e_j_1g-lYwCJtnVgZ-UcPc6hf899zOsrolhVpNeStErgkZzKC5fMG_9nkNSfQDliRJTPcFdJmv5tpeqGgidDalIH7j39aljwr_pTPXEieWO5wODMKvgHc2Gxl2vGNMbdgRI2YhCojcF-dKRYJ0hwjQjUdABbd_TlesL64zq4QQsEQMkcbd8uWrf4HWgc_3aGyUEZ1EYlyfer8j54WMZYyXgDvejP3E734QQvSmvNmUPnLQdLFLSGJLqeUVwDomPA0pPKfE96iTAxi3WQMNLVlkwwQAQ8GTZ432voVwo_a0dcoQJQ_ccwzZ4VmwapXh7Ck-sCL5sguAwAJId6fiTwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=feUVkTrNqX4K-7cemPzvbFvyw_J-vqhzCIN5CWL9Ym9jNNS1n2H5qnjGyDWsqulaIksLbQdb7dQ-c17Wn9ZopWK_bZP_avrfSDaR0LLbQww-ayOdK4UoordnuVjJTQfvqLdaWqKVDVaj653ajPkVpcOjnOLzRi2w3g_EFC3B2IkY1-4c0p6XjrCXQQ8b2VcsXvkUqfbrpm-T3IFAlfkwAntjES596D9YW5mpW6PzfXTkKyAt5m1H1G0SfU11TNymz9OgN971k-k5erZjWsFMcKzpAy8KmnusksfXQI2WlQO0_E-ySRWxsMfzwbh2BKROCz8eVA2GNVzWc37DVr4vy1e_j_1g-lYwCJtnVgZ-UcPc6hf899zOsrolhVpNeStErgkZzKC5fMG_9nkNSfQDliRJTPcFdJmv5tpeqGgidDalIH7j39aljwr_pTPXEieWO5wODMKvgHc2Gxl2vGNMbdgRI2YhCojcF-dKRYJ0hwjQjUdABbd_TlesL64zq4QQsEQMkcbd8uWrf4HWgc_3aGyUEZ1EYlyfer8j54WMZYyXgDvejP3E734QQvSmvNmUPnLQdLFLSGJLqeUVwDomPA0pPKfE96iTAxi3WQMNLVlkwwQAQ8GTZ432voVwo_a0dcoQJQ_ccwzZ4VmwapXh7Ck-sCL5sguAwAJId6fiTwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwpwvmoqIQ5LDlx7tnyyIrOUQfrl_3dvs8qboDLskDQ8H5nraYUzgJiYrHOJnTIdM2Qu9QNXqfiYRp8iM_87Qin0z5pHxpar8GrLChE1R0TtKx4pFmD8hKLGaR4wk9gb-hhSNtnZuiONUAqPPDXYB373KnZ13kxMI8z4aSwUXPD3AyXLJ19E7kSjk2t2TDr2B8O2VYKlDhYpHkjFrXiu0x9h0Vgz9zB4eq2XiIY-bQYGkwFgijgfNb6YpUy8nAZBOdMjwAEyroGtRkXuLawXyeBpxz1u5zLx1NNEhbLeWG1GVSz3u75loUMsGNLuFN_BIQMmAegH0IYTS97bu3fF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=TxTJeQquT3t3PxHuCHfCfciPkHYmn5E1F2vUt01bUNhiUCaK9iTk4O08AzdY6ssIuBF84YGhKiPbGPAp-AMz6VtiMmerEAzWK8k9Tt5C6KE4Z5_-dxM1z7OHdl-JwLtx7Xepmn57j_k5MrDzxBA2uwj76cGAtRhPEVHt7pJLX92f06tO376DUIc--I1rgzDYfvhRgjF3Af5pL8PtEKoA52NpHEmJAyZxVALdN4Jp8l59vBchQxqtoK1-mvPZHDFTwNQBpbXP4ez1XF_gHCUWO2N6hXr9fWaZUFu5BmUPsIfowJbV1TPwObRqr8UjxvvqrFunZtduTJrxulmYBg4rTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=TxTJeQquT3t3PxHuCHfCfciPkHYmn5E1F2vUt01bUNhiUCaK9iTk4O08AzdY6ssIuBF84YGhKiPbGPAp-AMz6VtiMmerEAzWK8k9Tt5C6KE4Z5_-dxM1z7OHdl-JwLtx7Xepmn57j_k5MrDzxBA2uwj76cGAtRhPEVHt7pJLX92f06tO376DUIc--I1rgzDYfvhRgjF3Af5pL8PtEKoA52NpHEmJAyZxVALdN4Jp8l59vBchQxqtoK1-mvPZHDFTwNQBpbXP4ez1XF_gHCUWO2N6hXr9fWaZUFu5BmUPsIfowJbV1TPwObRqr8UjxvvqrFunZtduTJrxulmYBg4rTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdneqbmXlVgtlARhxO2W-dRL0yKjabVzWwEc7Y_8ZhM3NYQoCJktlD7zTrAUThozhEB6hlUGhIy5fhj_h4AUtq7vZtVyNQdRGr5xvw1BEwjGzB2zg-C_yHYNrXh_GsdiM2zruNt0v_8Rm90O19gO2zQFfqeBGRedQCby9GaIvPz6s_fnx_n_ClfNXloVcreFS5bXzkIB43qA-sDgiSTwMGfRSQZHwjBE-uwNu1QwsiEuybRpR49w13GaWzVU80Rc0VlU60yl-AK6mt1sfq4496jZx9CjIlWBuBDifWqrrnMVo0OJAmJQW-IWnaLmVdK19EzaUxZHIYXKD2y2rFaogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVqbS0rxnt6HU02yIwqFt5clkz8T5J-CiDQAHdUF64ghQ-3gxPZNJdW9hD713UaQYGnxLp8-2cydJDXCJYKQ2iPYt_wOaTK4XkvmhhOmABhErT8Wh8_k2b_T8yOIH1O66b0oOPCwmSF2JK80cEf22M0heP2ZvZ03A9D9hHkzay7joRVdV69Ca1PMf1SW02QdYet8G84WlyrvKqD7-x7sP5ut5AI3iY1LOLA6U1zQDAeyjf_iju2dxk6p4NSc6cdUudiITFXKXBY4cdTdQlyMTas6y04hj3GbzyTGvgbGPavAhEdGETqE5_8rZ4uFLIciRgmtZMgElMC7gf_rUoswGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=ITELW0Eft9ZyzgyUjNB7ihKV7PZ1OomPGKxPVorRSIcxv25rqZ48L5Z8_SJUDjFB8IxnxmUuRpgAz4GZaBgBlWcyTqrHwCpjjwydMWPA5JB7-oaUCKFlJPpGFrvZOg-9u4Wuu4p_XyfXD7LYcqD28Jf4SiQZnhtTU-iwDaTPzWnKbw1vIy3PG0CvVM6r3E4N_04u65pgOTQSL4HmpyFQJFPsO8v1uP335wUgIGf-VUCxParbeWPg3vD0OlBngYmOVilhvFteYaUszlG-k8L4aH6SHbpHLDA-_yuEct4hqbSL3DFpr21D545i1ulB0gGirWp-6gQzK1GAjQncovAN6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=ITELW0Eft9ZyzgyUjNB7ihKV7PZ1OomPGKxPVorRSIcxv25rqZ48L5Z8_SJUDjFB8IxnxmUuRpgAz4GZaBgBlWcyTqrHwCpjjwydMWPA5JB7-oaUCKFlJPpGFrvZOg-9u4Wuu4p_XyfXD7LYcqD28Jf4SiQZnhtTU-iwDaTPzWnKbw1vIy3PG0CvVM6r3E4N_04u65pgOTQSL4HmpyFQJFPsO8v1uP335wUgIGf-VUCxParbeWPg3vD0OlBngYmOVilhvFteYaUszlG-k8L4aH6SHbpHLDA-_yuEct4hqbSL3DFpr21D545i1ulB0gGirWp-6gQzK1GAjQncovAN6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=YNJa6XwzrGhOxS5GL6ITd28MLjp36aKgrchnROdpCz3TXtLvc3mZdeiO1AJOdWv2vxFJBZ4s-wMxZyTI12tkTCfJggSx9mUF8izs12mbvrEe9RAJtQpaO4kPb9L-VVLK2dUiTNg9-hB1lCr6GA4_xqeFwTpsLgxFPVZUhSJOT6SmoriUh6BewZGlERNs4F-HyF79cM8tP6rIfvpEXQsoVUGZNowhds_5P1mwDWdB6nRYm0KzblnzL0Q7QTylsiAXBgMfQuu3VryDxb7lJ0CcF04RlzVo2WnyUOBVeIBkwFIhPfNoU6aighu1L3dRQtquMGGc_8xuNAO3anCe3LCM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=YNJa6XwzrGhOxS5GL6ITd28MLjp36aKgrchnROdpCz3TXtLvc3mZdeiO1AJOdWv2vxFJBZ4s-wMxZyTI12tkTCfJggSx9mUF8izs12mbvrEe9RAJtQpaO4kPb9L-VVLK2dUiTNg9-hB1lCr6GA4_xqeFwTpsLgxFPVZUhSJOT6SmoriUh6BewZGlERNs4F-HyF79cM8tP6rIfvpEXQsoVUGZNowhds_5P1mwDWdB6nRYm0KzblnzL0Q7QTylsiAXBgMfQuu3VryDxb7lJ0CcF04RlzVo2WnyUOBVeIBkwFIhPfNoU6aighu1L3dRQtquMGGc_8xuNAO3anCe3LCM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPywef2jS7GNPpDauG7cMOfJBEdgIdTgKpc3D9MSzQxKyvqqhtnNB5K1JFZ1tiO11kzzKfiNgOq0fm-dHDTUsuxBc5fhm6rHO6BZh8Vr8TDY5P4vCQuf1a_ZSfydr5yzLHvCqCEMFZnOeWSqXUMFX0SpYrQ47bMe62PtBWIGX6ITmlOF98IweLPOyRgy3kkpwcbjHCCQ7mban_Xo-68m9k86AOltK9SmhnKKQLCu6FRofLO5LV9KYHElmfwd-2FWJiJYWp5rq3yM-bupVmOkfm4eARZIYxcZWguWxZyHeJAuuC5C-rZx0muhfsb_asrYn0uac0C-YBNsNlNS0yZwyg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=jrQldHQFYX8XzSvRKa6cvImPTwXz32SE__zTU6ATcueyRp-VfZWPl1lMEeAysijPopORmJpmeiTNfWeOhemhsfPPVLw88shc7tvFXoU9PlG_gg97aDBy0Zb_xePdYuio4nJmZ-ESbVs5LzygoIDPT5XOVs0SllyQSm1OeGcUURqkkj1ez-p2zoxcFaAqMJToY5UY0i1hn5k7Sdu6Rxj9USnxn-bBzbCTwkAndacUkD_lgESri3WCnpQwhREhDM5-MqPjHDHmyfn5-eWPPmrhfQlP3RyUpM5KaUhdvKgS7jTi2XLZEyy3nPwSGATN5WmsPDNIOpt0aRE3_Blh_0wvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=jrQldHQFYX8XzSvRKa6cvImPTwXz32SE__zTU6ATcueyRp-VfZWPl1lMEeAysijPopORmJpmeiTNfWeOhemhsfPPVLw88shc7tvFXoU9PlG_gg97aDBy0Zb_xePdYuio4nJmZ-ESbVs5LzygoIDPT5XOVs0SllyQSm1OeGcUURqkkj1ez-p2zoxcFaAqMJToY5UY0i1hn5k7Sdu6Rxj9USnxn-bBzbCTwkAndacUkD_lgESri3WCnpQwhREhDM5-MqPjHDHmyfn5-eWPPmrhfQlP3RyUpM5KaUhdvKgS7jTi2XLZEyy3nPwSGATN5WmsPDNIOpt0aRE3_Blh_0wvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=Q1vWzZpN5lmZIIAaO208b-L5B8Bi8goCZO5WdQJzkiZqrAeeqjSvaE8DINkwxSYhCOTH57US9AERUYRqxndDML-oCZNN8aloFK5hYOBM8Huloq3LV8XD7-APJZfDrMAkBdQgplRgSzOzbWzXFtDBS42SBFgvTENnfvHx2zwch9GAMBnFuD03CArqBbwN1y4Jzo8Nv1qM87ViKdCBk7YboCaBiWS-Crc75rAP_yXmta7zmawj7U9qWKPMwb5WisbvJpxYtZZe2_Rd-KHgaNnGBTUzIlffMnHyBwXMYTeuyW916iNaRtisKthaTh1HfVtU5XaJwHwrzwhUtPrmmROuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=Q1vWzZpN5lmZIIAaO208b-L5B8Bi8goCZO5WdQJzkiZqrAeeqjSvaE8DINkwxSYhCOTH57US9AERUYRqxndDML-oCZNN8aloFK5hYOBM8Huloq3LV8XD7-APJZfDrMAkBdQgplRgSzOzbWzXFtDBS42SBFgvTENnfvHx2zwch9GAMBnFuD03CArqBbwN1y4Jzo8Nv1qM87ViKdCBk7YboCaBiWS-Crc75rAP_yXmta7zmawj7U9qWKPMwb5WisbvJpxYtZZe2_Rd-KHgaNnGBTUzIlffMnHyBwXMYTeuyW916iNaRtisKthaTh1HfVtU5XaJwHwrzwhUtPrmmROuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=X_Dows0o9LoB1HSENGyWEkdMtuMQCeXBNxl7FSzCE1vEFLj109s3FlFXi5To56Auu8-GH1Cj2h03xVNu1Py9JmsB_MdPe9PKMF7QDDAO9V1DDEbt54iXJhS5Kg2S-_TJzpN97aTglc2RaiNLltvEmI5-vXDa09LlxEIMnCD76CgV2LolqsPpa0_2TJV-EwUYBvadBcmDIkqRbeJ9jFVee-w6okqtX0LNQgeekcCi6HVF6RybpCCHtlHHxEsQXbYbOCEIFKWI0wCljrxaK80OQ9JGvv4kXlRlCiYOUKWy0bND2p8YWsvpOiDIzqTcqY3y8HkcXTeup5I7ipXOtsV6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=X_Dows0o9LoB1HSENGyWEkdMtuMQCeXBNxl7FSzCE1vEFLj109s3FlFXi5To56Auu8-GH1Cj2h03xVNu1Py9JmsB_MdPe9PKMF7QDDAO9V1DDEbt54iXJhS5Kg2S-_TJzpN97aTglc2RaiNLltvEmI5-vXDa09LlxEIMnCD76CgV2LolqsPpa0_2TJV-EwUYBvadBcmDIkqRbeJ9jFVee-w6okqtX0LNQgeekcCi6HVF6RybpCCHtlHHxEsQXbYbOCEIFKWI0wCljrxaK80OQ9JGvv4kXlRlCiYOUKWy0bND2p8YWsvpOiDIzqTcqY3y8HkcXTeup5I7ipXOtsV6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYndnK4IM4KQLBtGF_1X5z612TQs-PW5kHogH4ymtEtbQRvbsAjiYv7uEtsOOklNXrTd-JWrJ05nGWhS5HAEBLK-EFj6veTezjDV3VPleW3TNWoWL_-MlU-OOHDzYPv9onY_eQgu2-qJ893lqQ2w2Y6gKrIzn0SIejs_NsErWcMwpH5voUeWUx2P5ESNMWXxscD4zSHUUG3RU3GkdR-SohGFYZ_1y53jERwk99sMjGtYSWM5kX7qknirev3ZAxO9h1pY2AWFIHKpSPcQ3-4L7DwraWBQrPxi1eSTNcMhYawV7W8-mbO4JFkZanJ_XhSXmYg-e2NVe2Kdq-u3P5y1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWF1_lWjU6Dn0dZYBNIQ-K0KJHl7Gld5KAAcC3T_8FjLNKWUh4TnaQUJDksB-1xRlbvBFyq8HFeSY_KRGD36EtppO10KwUJPtiWMvb50GoSVpdCPTTAhlvJjQuxms7mMYghcm_HIC3jkTfdBpvBz77r4qp5pSL6xwfyZ_OpcAcSAC_tgXoqTonQ0abnRR__AxEeoFU1SsqVHGOfetc-364gSuLLoAwN27o_GVqaqG_U8bgdnhiN5iR4qYtFkDFynxW3YCfaaPuj4iGJqoZg9aky-WLpSQ2rumxOzCr7aFT2sTMjB9O0WLzuo7NRvMb8JCzpVI6T2v-V6wsXBP48-Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYLrXL8QFIgKyXMZBKa0mJE3tOxpTa_wh0zvJFKa5pvUJbo7aMT-jAifXyprmLzYDtpxcPyN43KX0yf-j6MloaI1HSrw1x2LUJAABJGormOk6RUJdCtxnsWIdrhDf5Decc_g1xSeerGSLswFb181C6bIy8qWlMhHdnGWNqJefHFHYmVCK4cG7PQ0OvKAFrnqsKSlQIaRKvuw58T7xw7rzgrPkCrmxua9xszD5Z_WuN8Xwg-iKkZFaQPea1XlLZUFPNrrSCI3bqWWlmupio77oQ7EzV6i5UfU8NRW8xRnGMdoqEm1YIgt6Cg4e_Cos3KoXDRBvkcCl7ffu0pxVa5p-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh3lTK8_1rvrdwOjsoin-ufMUYfxs7QooWJbNJw5Auy4lCBwp0mvePrfI-o7zzcDRD9eVvKh4dQ6xr_401WfSi71JW_nEOIjm_q8Of6rcvpQK39_pwaOcU06j01D5A8mZsS3AFctmaNBIO66lbFqjUv6PywYe2lT-OH0ZQ5m3gV488MSo17QkCnEwA7WMAiqWNbBhbip7s3mJoXQwZfnV2694tg5sEJ3iHlF61LKNPbRPGRAF0yjk813iTgl8qK9HG4M5E2K6fyF9USwPlvvAkgNnvWUZBWRtc57zqSAgyaaVv7W2lVjOigTeBVuRmOWz5a_A4mqlCkqLSq80IM52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkfCAZ2XdTO9BQaZ0YAWpHvyc4TM_IGz-dohyZbWpI8WvEcagz7Rg3N6LPa3c57bjrq-6UNWgv9p3Sj_c2ATX047eOyey0ezUircNYPxCzKvbBc7I6iomS7lOicFla7CWpH7oMrp7aQJ0JZaO_5QdbphMGRzhXN8oJrpoyg_OFve8teFBYMQWqPW51xOXtAWY-v58jBCx1Exe2wcvvD4hwcgwgYB4-Hgh-eoyaCQVirrGuzKDXjjE1If7RO8-7vhXqeJXDEKPYC-fEGD4oKfJPdRvhbOuEn8_l5cNXYCX_mIgH0VkOkWahd96dQWMewuz-oSi0ymDhUv9jWovTPAEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsySpxDbIWcW7w8AlgyBgFqMwOeBAlWDeWAzm6ok8KzZo80A6A55UgJq9U8Fsgy7i5i11GkGxcHpSbgJMtotDfbjk1hWz6ct7BkJgRFwesWGACjIEIvZzizGEkWtZWkdcayr57H8-_HdiyRqfsnUlVSfBApkGIHL5sjBGSz-nKFqR9IsJjXyg8x4k91ZH9c_XuZ4Rw9Pn6a_k6pgXaATvIHp-JsKGUSI37geI44w1esbG9JSso9jCClOBQtIjNegOnBhw3Mj0QQQWtSslLpd-n56AO1ZJ1UOCMQCS-Zh3hdYOAfWPk2c-7db06v_Cb1Mi4JROnx85iP-DvrU0qDqPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=jwRoXKg3O5gKsy_eiC4nYYR_iT3xzNfJisR31LnKwtyGmL16TA052HcztWGD5PwqnHdnncojtFVHbAd70jmTdlF8JQRKO76SnqxBsogJH-LZjy5CySUFWqZgIhwn-ue5_9I1TgsFr6onXhdGOOKT-FpCOjcYLuOppvq6Qj-dc-7ff3f-t5HlpPvtLpX44IeR86fD3L2sA23XYqiEvP3CuiK2d-9Nkz0yAJPGiZJeDaO9MMMRgMtrH0yHxZbcAKtvifjbr6Q70obtFy7I-YuMhEI0X2Qv9x-o0i69fSbYHam3GZQGQvj5d9GGC5LNrAjq6ryEgWKaGoxriDoVSSpBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=jwRoXKg3O5gKsy_eiC4nYYR_iT3xzNfJisR31LnKwtyGmL16TA052HcztWGD5PwqnHdnncojtFVHbAd70jmTdlF8JQRKO76SnqxBsogJH-LZjy5CySUFWqZgIhwn-ue5_9I1TgsFr6onXhdGOOKT-FpCOjcYLuOppvq6Qj-dc-7ff3f-t5HlpPvtLpX44IeR86fD3L2sA23XYqiEvP3CuiK2d-9Nkz0yAJPGiZJeDaO9MMMRgMtrH0yHxZbcAKtvifjbr6Q70obtFy7I-YuMhEI0X2Qv9x-o0i69fSbYHam3GZQGQvj5d9GGC5LNrAjq6ryEgWKaGoxriDoVSSpBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=ZJSylS5XkJZJC0jY9oszJLRIqi1sKq3mxuEK1Oct7eyTxm7oAe_-F2XQNsSfpuztPhW2yxOAczP67PCrWSEIZ2V1bgIz75eUFMlt5nUU_iWI04Sh_86kdD6ZjYF1wyl01t2xUtGHTbJn3JAwvVXcnxdo009JeWmwMdK-vtq_bURdh88yFW_5gts94c3PGUGjMuk3G39Ep21rHDv1Y1U0sk1dCbdvK_Rsp3agc7n8CBFEFm2Mg5yrjZzPrXcwHW60usv8XLLVCpr2yDQ1CsPD_PHRu2y5ZA0M5XUNYDtaoMVC1ncf6jy8kBLcUSLoHcvlouLA5AClINgYF4v9yTBkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=ZJSylS5XkJZJC0jY9oszJLRIqi1sKq3mxuEK1Oct7eyTxm7oAe_-F2XQNsSfpuztPhW2yxOAczP67PCrWSEIZ2V1bgIz75eUFMlt5nUU_iWI04Sh_86kdD6ZjYF1wyl01t2xUtGHTbJn3JAwvVXcnxdo009JeWmwMdK-vtq_bURdh88yFW_5gts94c3PGUGjMuk3G39Ep21rHDv1Y1U0sk1dCbdvK_Rsp3agc7n8CBFEFm2Mg5yrjZzPrXcwHW60usv8XLLVCpr2yDQ1CsPD_PHRu2y5ZA0M5XUNYDtaoMVC1ncf6jy8kBLcUSLoHcvlouLA5AClINgYF4v9yTBkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz3sXbjCHdES8lbIYuQ2lfw8id1lrxGr1ZihqOmJOaJ1t5k-5o92oSuhF1dzoxpNEfzVnjM8g2oi__TDZeiMl_UVE41ofg3FMGsqHeLDttpGoovc6nU8VhA0YO-YbT938Pq4jphH2kqSV-GAgOBOWyZqlCLwIue74BeHfcselfyx9nn0jNXoRGN22hJZaaOo3WuQzHzp3SROzvIJTU1BZwhz_UGNWZUoBEjkdsnKER7eSd6hRefMWnjB2NQQ5Y7sRh14gbOLHes1LYUxjca0_wGK29DrropxjIAxG8dmY0ZJSRnAxfzVc3avifYfl9ysHSq4JyKIaKCBFsl9lkB_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUtyR_7y2E8kbqactJddNr6HkZ2CuWA5FQrqadshG8pjaXfaUh9velyc8bCZHRmYR-CX5SD0VtvvgH33zrdPy9tjzhd7e2g17NUBB6Ymhd4Kqt79pftGtzf6qH2ZnJVrVzCxN3Q8Q4M4PHFY50ztRGtrZoNGmg7kZjSU1GTxUN5WtvTlNn6G-e_WkyM_7BXOIWd0u25-eTiFmcHxRriJqZZNkCvePfprARblWoXyati2Y1MGYvjgxp6ycFv6C9reS0yPWJuTydJhD4A-KCHwB3a4047JfSGSQxmSWqRkIay8B4oV5PDt564nLiRlttQ49dvp0HyUOQsHFyY1AXI7zg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=aH3JU6fecRKYOXAZbXS-KtSCIkAMeOZftb-973V-LkAwU2RhWtSiWiEENrx7xGvM_M775SLP9ONNSHHwESnbD0dG-ZyuD2IhABBx8DIiMjYWG4eXuetZMUwc_fCiBF0Popz15hJL9N1waHX39ySl3-dz64lnvIRZ78NnAW4WNT2scJGAIP9U4bP_5_38zv58b5j_iuJa134vN7b31-tpohJ07R1Ge8HNbE_RwReUT2I8F-jZzIDktKuT5qOdK4j3mtjZPqTd-jiOcYbNsYY2-Fp9L8vlI0ULM6KYIu3ZEXZxeLaez4hKe9XyQKD00DJcRNjlvGPHckQOXyNKi2eO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=aH3JU6fecRKYOXAZbXS-KtSCIkAMeOZftb-973V-LkAwU2RhWtSiWiEENrx7xGvM_M775SLP9ONNSHHwESnbD0dG-ZyuD2IhABBx8DIiMjYWG4eXuetZMUwc_fCiBF0Popz15hJL9N1waHX39ySl3-dz64lnvIRZ78NnAW4WNT2scJGAIP9U4bP_5_38zv58b5j_iuJa134vN7b31-tpohJ07R1Ge8HNbE_RwReUT2I8F-jZzIDktKuT5qOdK4j3mtjZPqTd-jiOcYbNsYY2-Fp9L8vlI0ULM6KYIu3ZEXZxeLaez4hKe9XyQKD00DJcRNjlvGPHckQOXyNKi2eO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Y56mEn6agsrlqbUikQSBTS40G9vHE-IQxKbW67xQE-cnyAlhnlfLyzanMTfPm0pfF8OFdAtGxhfwZ7fnYZHOjbjGl7fY6TbiaOz5tZkhhGO7LThVIvm9Iee6w4VSsalsPKv6BP6KJEzrOnbN7DZbbPVHH3EXn7hV89wZymX8-Dr0VKHjkn0LYe6MRGLbgTxqDMEGJExNckCsXjfdHf9wOlMcjkP_36lgAJzT7Mgz5wH2p_UKa5XantgFMwajRjh9YwoFA1_IjmrCTMbE4SX8nnrAQvtm-6jaU1c236OXKC6qNJ36aaCuGVRuKrMyw0hmpL2pfa01ZCMtB-M7ctNCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Y56mEn6agsrlqbUikQSBTS40G9vHE-IQxKbW67xQE-cnyAlhnlfLyzanMTfPm0pfF8OFdAtGxhfwZ7fnYZHOjbjGl7fY6TbiaOz5tZkhhGO7LThVIvm9Iee6w4VSsalsPKv6BP6KJEzrOnbN7DZbbPVHH3EXn7hV89wZymX8-Dr0VKHjkn0LYe6MRGLbgTxqDMEGJExNckCsXjfdHf9wOlMcjkP_36lgAJzT7Mgz5wH2p_UKa5XantgFMwajRjh9YwoFA1_IjmrCTMbE4SX8nnrAQvtm-6jaU1c236OXKC6qNJ36aaCuGVRuKrMyw0hmpL2pfa01ZCMtB-M7ctNCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oia79c7Rbjlwfa-uYWH8ar1o4pJVAhtzj3C-aBe_IuiZXyKZqASgXVhXOXWNIDvHf9JsyZdOodF8C3GIkoE_-XGTofc2G2VQMBXdll1sPKyLnoBs5ogqQXn0XfrLpRqoYa_gXN2OrI5dG7bxuRqYjSOnYiA7VTbLyxXrCcbkYuH-TD5O26B3SyHaB5JkKGKPSwEEsLeEAtdxVrSY4C70D9KGOPGw8t-IN68oM91zTia20Rst-LT93xCoeOfZlqyL7KGR6VqqkoZcbtwWeNdwhJagLznfv3JmiMP0pVMlsrzfWoA67-7NcVqzeT8oCtF0PRBeAlCeTQ2GrMIS_aPzug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-vd3s7xvecFwgF_ujALfaiKlNKPsMZEI1-RPjcLVzX91zCMMJxKO6sYrpIND4h-I1osnTHEKWsvtsYlsniRqm22FiSVh3dQsf7xdl2BFPro-VScqHTlyucP-d_65efUXxbqPtRDacC8v_iEoH_J8y8P7I9mvSBpAGGjNWq8xmjyVOU9O3tbg-Ozh48CNtw70c63kGZ5T7NLKT_To_CsXu3Fkmy2e308Jt265qJgURToQsCV3UitqWWI3F9uF9i9IGUSJG2yZoiAs0mqASeNzakwYTlTzAGUTVPWMhVhdZhFY9Q89liStGORokZ63fIpvmc2Edgvc0f8EXvjCEIMQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=FN5J_9O3-6DiSq67Qdf1tlL1zJmNGPUNlNeloTItUM21Pncw2n0CcggnCU3813j4HNMB635J4gbhJU1uvq8p_IeSt1aslUy6i8Zlu7oVJkj8Xdg80bq1B9Bh82LBTQYIbJzJrMxuoIy9U_zd2UtX7fAzl7Uc0XZstSByyDerZw01B6chKBBMLwu8IcaInfkdXUZiAYbK-ui1bFCYQnT7cdn7fgB8VGbOqo0Fr9NTxIyMloFY8YRAyYBlvLhSYobYXIFMFIxJZAmgJWSL_N-TGpnBIS8YAsYBloRJC6tlsgOBTPQwpLkIpzsz97wu-pr4CvoErkBMOOZOt7mOy-jwiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=FN5J_9O3-6DiSq67Qdf1tlL1zJmNGPUNlNeloTItUM21Pncw2n0CcggnCU3813j4HNMB635J4gbhJU1uvq8p_IeSt1aslUy6i8Zlu7oVJkj8Xdg80bq1B9Bh82LBTQYIbJzJrMxuoIy9U_zd2UtX7fAzl7Uc0XZstSByyDerZw01B6chKBBMLwu8IcaInfkdXUZiAYbK-ui1bFCYQnT7cdn7fgB8VGbOqo0Fr9NTxIyMloFY8YRAyYBlvLhSYobYXIFMFIxJZAmgJWSL_N-TGpnBIS8YAsYBloRJC6tlsgOBTPQwpLkIpzsz97wu-pr4CvoErkBMOOZOt7mOy-jwiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=ezkvX08cFHo3ONkBIXekj-XwMeVGg7HLAA9HCHGdq3twJZ1rzjTSbuZsOA0exDrqqRkf149nLJ62Nbs8IU02GSRD76yNQEuDgvgUROZc9zxR9m31D1KNzGlei2ONZGPYeo-dSKbDZjt7SucQI-Z6c1DWAePWC4wchYVOWeEnYzpPsuzTQ6i7_YemjxlCd5CK9499YKVYQvMh8-l4d1rGgM-2ct1ku0weCiTuv3Kv-oH4n3jggvZqFQbDikxZJV9h0AIrKilz1_zHXcBC6LkfnHZPq1Jgg9k6ShIX4yW9xPfjNTZ_kxm-mxvlHd-wgJXg_1Glqbjr16oBUdRKE2dIEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=ezkvX08cFHo3ONkBIXekj-XwMeVGg7HLAA9HCHGdq3twJZ1rzjTSbuZsOA0exDrqqRkf149nLJ62Nbs8IU02GSRD76yNQEuDgvgUROZc9zxR9m31D1KNzGlei2ONZGPYeo-dSKbDZjt7SucQI-Z6c1DWAePWC4wchYVOWeEnYzpPsuzTQ6i7_YemjxlCd5CK9499YKVYQvMh8-l4d1rGgM-2ct1ku0weCiTuv3Kv-oH4n3jggvZqFQbDikxZJV9h0AIrKilz1_zHXcBC6LkfnHZPq1Jgg9k6ShIX4yW9xPfjNTZ_kxm-mxvlHd-wgJXg_1Glqbjr16oBUdRKE2dIEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c43f4nb9qof6mUY_6SdbpFvYiLgl9G05HONsCbo0DBAzNKQRaIpfdvlGLHOEartpvaL8NOCqJakz0GXo8ejp0E1qnrQvwTNKKHa1sSK_5VN8AkLle617sHqsSc_hdTpsKxqVpgOzTOo36SO541ACUpWJ-lu-0cvjwO8YNjpOIat-MFdje2q11QD1Dwb41a4L0u22cGvyTYTUhZsHGxDKIVruBY5SbEfdIErG3daFIiCAO6J-as1X7sjDwMqFfyw4k8Go0oi_GaqpwHfVE3bj2wFtUcKsyohI_08Kzx59jnoslU5pcHfIvrNX4UwzGoH5DDXGfvLk_pGmNzaOPT3rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnMJRJmZsXgmtwMX76RYso_IXeVRjV0kE8XOo5m_6ELgT9h56W6WF1QrK7cDLk201AmXj1R7hIJfq4ZW_zDjSRrjsmdl8YHeGQJsQwY1v7Pi4KZp-HmcVlY2YRpIa6Fdq9LhWlZsvkBaC-t3U5gHzB1PtL2psydTA_w4Kl4Bk0Qeh9sReGRvoF93BG4esdfeYiL3ELXcxBfN-G7fDso3F4mKb-ZCQqS9qJhNjMb7yuKi4l4JnrhrJ98-M-W6UYZVvpzPerB0pEkrDB9R45JjaR7pOfS3y9026bNXoHMo5QJCHkk0ZeOWMKoZ3GhoQVFU0msebfalmFPjtX0DNIyLXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEMd7r47duRcyeQIPv6mE0MgFxmPYT06Ci0QF5bsRoYRD9-SSVHbZFSAaUbo4FiSVUXjNgq38RALA0MCPOb34oL8hg1lshqMgPETuKYbiEyUyJXvbN__c7xQd-v9Ut7h2KpkS9p6SM6zOuN7RLpBOeRHVsQH_N_H5yi7yqL6U4-DJ_iHA7uAKK6g5hrOCJquNr4uqfp3l7biffxAV37Su7cZAn1KNySU-ALdRVLeyBULCKm6PIC_cRFwBMcczAqrmzoOrjposZ6gfNqRfSEgTkjMWoelTIXZ6rsQUF5ve4RqpFHIE-wu8Z3pI9roS5jMHsz6GQIuU-Wf9QQ6lb4cMA.jpg" alt="photo" loading="lazy"/></div>
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
