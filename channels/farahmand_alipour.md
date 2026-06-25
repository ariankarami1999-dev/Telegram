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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 11:10:51</div>
<hr>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTwd1PZgtxyk9gR0BeLXT4HH9NJBSEv-GoWmPocklLko1kaf4l4DSkY9gdhkW4GEPAsm579GvpZ9_dMnFvPFrVpeK1iJRhpa8vifE17BpLQfhr00rnK0v9UOaUoQx0Zlns4m_NNYZexTlSsx5rUDY8aQqpxlf5sA4oFXATASdDNmK2Y98zhpHZzBw4lp5UK___g91VDmTjZrzpCws2F7aCKct5QozVKtpMYQioNYpZ6C-NTK39I3tKuP4DiY7UNvire5mXpaJMGhznMxllPphfuXZt9XMFn50O2x4KQy8iMYXDSodh7H1RsaW6fBRE8fReRavSpm6NEm0AAXNKTUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=bfHtfbFkcZhEeNXQDX90Dj1WTs_l5DBjrTFbANLd0RfNw2qT1pJv5s7qk5RR0Qb2o6ua5uoYZuzFBBBLeZhjcYBbuyufIweb4RrTSRRGa3CjATpEHUgCTpvjDtPwVd3ZQ3zRKwT9m9_h28_HnRKTRQWORjwqYEsigmACNsrNCxsbbUfntuhULMTTZhduatEyRr9z4PwkElWasbNuzTigIKVK1Q79cnvRSnak1kZ9UfFumGfsZecxcd2OvkBAqowAyh2jmmZKz-02Vtf0pxDu4mb0J7LV8cwEBgsMxTu_-98kPfUC8AOUDwzhhYC51Va9GN_IsEngqdVBRtVue35HIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJiLhsVell-Bd420qib3ygSR-vR9PxXkWoxfvliQhvyQlqwo_foA2ZvxLDr7iapAlMgrWgFsbjddWV7DaJXvah9KaRZkPI9trVyS_-Zcf1hgUEHcnXgECjHjkw2a-SMq5yYOCE79rjZM3kKEHMQTxCvXHjbiik_FpWcfxI0uJpoAXBzgP2_MdV41Pfn0PMClx9Z0Hw5BPnRfGa7qfZTP75zE68_d9g3js_9zZj-5pqxrAkpJ5jv1c8Mlc6YKj4NnL647K9tq54sMcSBskKej-0lrz_1R2K8TMO60m-czke6F8uOv9wXsQ9i1oFrT7fVcqUaTGRzQ-pH33-fOE0hKTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=pZf4KGojMwFForvIq_PzHh9qGkGkFgr9ZWrSu3qHrrAjETBLpxIQoXe4arQGA5n-HNKDtrhN60zco2r95RGAjBAQhhZOF8cJNcauUW71R4t9ku6pIjheMWN7_uzJ2UElkby_f5i9R2xxXM_6rA_BOdj3xyaAX0oS4aJqQxtN01oBu-gqGxo2T64bATkvpvxxCIy4Qs0IGy_WLwRZz3K1_Pe8bwL6rDVTlM6fdaEdRtO9dgPlgKYnG92qcyUpK3-in8nTY5NZ7ffi_B81JnKZ7iHtyrZfeBmvoroYNSNtbwAWh-EuTYLHUwNwAJefIg_VBPhR7kLwLQmfamlsVKnfHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=pZf4KGojMwFForvIq_PzHh9qGkGkFgr9ZWrSu3qHrrAjETBLpxIQoXe4arQGA5n-HNKDtrhN60zco2r95RGAjBAQhhZOF8cJNcauUW71R4t9ku6pIjheMWN7_uzJ2UElkby_f5i9R2xxXM_6rA_BOdj3xyaAX0oS4aJqQxtN01oBu-gqGxo2T64bATkvpvxxCIy4Qs0IGy_WLwRZz3K1_Pe8bwL6rDVTlM6fdaEdRtO9dgPlgKYnG92qcyUpK3-in8nTY5NZ7ffi_B81JnKZ7iHtyrZfeBmvoroYNSNtbwAWh-EuTYLHUwNwAJefIg_VBPhR7kLwLQmfamlsVKnfHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=fjlzRJguP6AORE86-Vxp_Nuru0xwP5JTMmLpt60z2RVC45P-XIx9q-nU_n_-cRQPvdqX74o_2EeyMT2V7cF0jB67_YDLRjaWVLqwahFGgaPc1aGjoU16gGPlAzBZNhBZ3s6172U4-UXm0ebVpxIQOLDEEbj41eQgkR2j37umDnTurkDK3ajPPX8sHCdm1mQIgEgZr9eUp1SWEN0imDuzLFWybEKqp94QQFbkk0sOESK4YqVcQg9GrdxSSfAIFbYWJiZsx0mqZ3LGFHVSK2cAlsZszrtX5HJtX-x7Tjwreacoms5dO3aErbyAjf8Wf0vh8vNkDFShTMnB1GFhFcGRmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=fjlzRJguP6AORE86-Vxp_Nuru0xwP5JTMmLpt60z2RVC45P-XIx9q-nU_n_-cRQPvdqX74o_2EeyMT2V7cF0jB67_YDLRjaWVLqwahFGgaPc1aGjoU16gGPlAzBZNhBZ3s6172U4-UXm0ebVpxIQOLDEEbj41eQgkR2j37umDnTurkDK3ajPPX8sHCdm1mQIgEgZr9eUp1SWEN0imDuzLFWybEKqp94QQFbkk0sOESK4YqVcQg9GrdxSSfAIFbYWJiZsx0mqZ3LGFHVSK2cAlsZszrtX5HJtX-x7Tjwreacoms5dO3aErbyAjf8Wf0vh8vNkDFShTMnB1GFhFcGRmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUj3f2X-lSMmWy36Tz6t0Yw_y7NOxt8f3r3nv3euFbPSJxDTkHKtlMx0aw_O8vE9SEVWkt_QnNEvAmllpZAhcOdXTYq7WDjOMG2a34y9SXpfPX3TF6qbVTdML3OW7Tqc_-pXul-_yxzqtKBh67o6IvHdwq68pISLybl_kzJvUS_4VgJ_lHzUX5iCpefUWltM0yIVoWTU4BwPw3ibT-IC4h6ML1CtI5Pp5E2JIHgBtmSYIion5_kWjsRV72vL-ndPdxr0rH4P0oeJK_EsmibLy5PC-NZHUwL_YkGiCCgg8hHoHBtqwZWr1juDlUkJttLN_PxvXnJHUBrU2_SLVdgFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzQjTmye8sIj-OKrUT2n958KQtZ3P9krL4NCUmdL8CY_FUEXlhyEHILa2R-6_PHMVWNDJgaZ7UUZuZSH4VWfVpQqV1FQjMG5qHPi13rg2AEuH-YF2oab9D4Wef1V7wtocK0LVWC3t9EKfvdP57Gl12qKJtYJ7kCREnzmayvuxlnYlrBiU70gzLG0xGyxiB9JIsn_9P1OPbaVRDDP8O9AKGp_28yc0nq5ogMO0HakuHFtrZwIj9oih8X44z07aOnNtQOsnUf8LVOnVYv8WGGOkNUOn-0pvR9YGQcOyDe5iUW4Gjmm1vwNEDTOh_sIEbbh2lMH8yOUWOv8xCXzaP98XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2_NdcpUbxtp7tV8IBT5KaWWpiSx-mn3EGAyTuZFaxeFsTpHgLvOPTptVZzUr67f63DBh8tATZV8FzWuakNG4FHaI_P1xNFMFjv9xWWty8plsW12xSkTKGp-z6BaQY9Ngf346xLaVb6KXyYp1Yj2wPbBiF_BxNcWKHDNw1nCzlklDBoEb1TOBA9wDXtewLrYaUXywqap2iYKLl0okmsl7BS_8fUzuwrWtYHBJUxjklFi1xz6EBIrN0NanDxF7GfSxObQwNaeIA957XIWintjjMESk85kQ7vSW2qqJVgWr0fNx5cmSlxeQzQzMvWTfOBa4Z15uPghMDwJej2tdHo5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMYUVmya7xqob6UnvbaH1FAkz4VVaUBjdIbAnsVtsDrVod5jXcoKxyNoDVE5mh1N16lREgJY6mcYff14QyaZzEvDwtbP3ViPXw3qzk7yQ2uRdojZO6VOAB0XPO1wBez1FC_NOXujfmyS-RBgM_RqWixXX_tehiuVyMI5LJUR_G2ZNXNkVsvMNLGjDNvoXcLycJxo_nkyd5CDTkAzZE3PUnQAhJnibvOulfMFm4jZnudedtl4JILZD1RmyCozf4owei6d_ap9jEiySjgknJUY-YM2FG_XRQeEHIFQ-dQd8GSo3GP6g1851kBacwDtT2draEe5rlySzl4z-xwL3jRJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0AirCn3h2Ayb1D3zqsU9wgepiIKoBBZgP21rWNREXzF-bzTuqkTJgpEK-RYoa3aN9FyBDfIA-HM5grKsv391ulssyB5AMxVdNb34p0Xk1JZdCqmS8OtDW04bYEwtsbeMOnGzTlHbn3vw2JdYDyk0TJriC6a0dM5Kpi-I29QPCIYf_MltVZcxUI_G6xZ_nUZMK2IHt1AJ1okvEhYfDCx-8bGGNmKVkxtYzJnKPWXk-rMWDFPPVS6RC6hleqP7Kwgec9_n7MG89DsOcAScMRoD3JVnHYTciYAny1LwWwP7IxJNlOTIeibH_w5e2CNRxdx2X1B4Oc76_3HT-QHhqS5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxSUUcdno5q8Y4dp-tb9Aio-Emk-Zm73QfEGd_rJZyJFDtwCNpKO-0fa6bvmcvbM2hv2vELNsSMdG9zzY5fmc8sa6VOjco-viqgs430hSpKAWJWItf_SVMAURmlMTheL-H6Zzi5N_goRnxseS0WCGl5QU2QuNY8veTbpugCTtXbvQKER4BkQWOJkjYKGLvt0Yy9ilm7xD9t5JeugoEHNl7h6FY-Ll6ZCo77qizYyeSy6Gvq_TBGUKJdZBCsbIYRi6_k7LyKOmpxHkfOHRHnWcJ_rFv6Xn-ci0N-_tqOYFd_RVsJSkn0oHj__v-IwDKs_NeeEV6eS7Cvpa1FAxFrRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlnN46WTUOWy9hthk2wRKGmA16406xNWfWd47VHIxzyekiDj-nHsmJ7fGxEWGg2LcUyDoJYFOAoXeXM_r9_XNDtphmrZwZmPeDt-AqOmcYFY6mLiJKkhMEP907VpkaqYPPNzhiMrucs72hpgBM0dlbgKR1RWdwWpSKTERBZG4qGr2FYPmh0-rYOowmBIu_-nHWwg2mgYhgfmFHOtqYPhE6ww-mKMmOoSVKj_vJfWN7uwsRC6ua_9DUiItQc21u1bnyId59xIQADE7UoeCsh06PgX_GUyDiP9fSJW2GXw2mAmyepTbRFwiWufDAJHjMOJRpBvvKkBZm_vLWbF2_X5tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFA6P-OkHZ8DumAW7Uj8gz9qSqWVA60fE4xeP2gTG0rvygkFucpbokZZlFTf4OF87mljJngPZzCsDFAum6d0zN-laI6Pt4XAn86729m8itvQNZXCqOzrqKlVoP6epT9EdP0lO1h9Ed3HeyjZacGKJNg-IHFvznEw8Ceekr5SUwPnbKNFI3MXVsHHCp1ymihXtDIs4Y6SRrJLcvK2vCmVIisWPl0vrT0pt4RIJxyYhDMUCrpi3Kx20HQce46WDnn8LFutAONDN8HqMDXHs5IIm2tfwH3QmFXtARFrnzawK_voQSHP461JWIJFA52BcMI6biFpBWAhXtOBW7UG5BJVpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuieIjnZThzeUvWyVfs_z251UyF9_3tLYyskq8I-ff__lmJ3VmgRGoU16QoHGT1PTg3D4_z5FHipQHx5ChxbbuwxAUb2SYwZYlHBsxq0xCcPRe-dlQ6DGCAOE6xSd5qVHr6vxktbqzW7qUzFGpBO9lNmLVYb2fRrx2MuiJCvwB3dNlcrJMX4IEWcgNVSaaTa5Wnu9rVjSiaHykELfPKXjvmi68VzspXz_udKHzFV80fI2BYyZuY8qwXq_azXmQbVOjlpydt5AhNuUMDbh6sUDkf3ZYGVfcpQYyZ_XWjoKNKSn3J3k5TFg2dZ9fzwIEXxn5uiRO2zJz1zkUuqrzdnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKeF6BFz-u7EoxAgItmJSzDSkZm_LVByGoSBQO8Emzoa3bd04bPxIwG2093hdIibw4e2i8O-NVp0MoVRBRLAM-Dpu-SVFV5HQTyriFO-7HMFzrumjckMlK_9cdfzzLKXCUycV3ANxzQhMBrB6ylcOabNEQlPTZMv8-Iuk3d0Ayz4c_MSfayYOMxGTc2IWQ1nBb4v7KQEoQn4flxR6vWGflA-D3P3FruuRl8vkQEuq-s656YPuyqsN9a7VHh1RlcSX9luForfiqGCAwLHMAQ11rJ5Nby5fTfggle7VRt8ywpg1hYmfmEYhMlW5Mzfq2IsWaILruB9wDJP5uX9FiyszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcsdethKfGEmEcgalhCtpuAf0qdeqiPBLVkKtp-liCm_GLGP5EXB9pvstQ4YHoGxodMVayimOFe-BWGqCaJ4wA0YT-ySR3sRgz8sPA8gDXRSlDZ4a2uITO1aLQIsevYJbWPqpc0TGXEFEUsbTAxqSiMU3fyivwf1kHEwF0pvJMOYq4lQHVrDvDFAZnKCS0Mdqg5rYZ9vI8nA4QB0V16Eqp9lFpmA58g24PdVvhHgAfc7Pi5n4uNhq-rd6o53_GIVFsDeO68F9Uqk-lBN0ERi3LsDMXkZrGiLw6I5l1V1_KvqG3v7X2d98kWtBAeiVNILoOnSAEMnw8LDtsLmFLP81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCtVCDzygyx8f6_X40E_Q9wSnrNW8CCSRDN9wobnJiY3EUtjzlAY8cpPRdgqtTS7Co6pD3Wyf3IvGOXSthnKPJcaynBPzKs_SRv5rnLuHoBnqOsJlRFdTbBN_ypW0iHs9CasTIkB55E794FUv7E4IdB5VfBbnt3BcvYAb9f_IFCwNzoxDsE9gvaVzzKIkCGSRtpNj5JCGZVYMAvVB1pzVqxJPl82l4DhA3kfihSbo07Cz0QIwirwFoebkjAe3-FVLBaqrzwjzOZEhoMrt0eWYr-w_ZjfAVcTm_fKfmiVyWpzJEC9YpHCmWTewz09htBl4PJ19uSBtBRgTG5DhxaeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1zjaxNtlmu7Uhb2CNHvDpbLaK7_ib0eOmHk5uG3jXLmbGD_0JhdkXG05MAuMFe7qWN9fCp7sQGgGaInxOJQRDU7PaOrZfMBGPqwFl-r97SFFjbCf0FoPYg2ggmSTG_f75BQq2cq8cemOYH6WTXEnnCZ6_oQB4wiO72rpl6w2_cZFemrSrattz7gER8xNSWprtJLXqM0DX3aytT2hlO2rksPdbwdpzfnoQPHFIHG7L3dammbPXj4KYb5dOPMCShc-REnmOVG3gTY8vEx6xVWNNe4tME8hEijVXxjhC3bx8xQ5HkZ1okqXY6g4WvMpMDrdG2a0_ghxDU_y-tCmaatHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fct9hR6SzJ5msorzXT7FXsf8T4w2W7ujrPxd_2YBMXce1iGEbaA6HcPMpgdnjvBRYJFS3F9Op_BRyPszGyetzq4q2fANldO7O4TU1EnCqlWVmc4aCQQ5Avu9yxgkz6vzKGdNagVdbMZ_BeRQPJM_K26dZDrgE_nKxcMR7MZpVCikbcgh1M_nIhbkg8GjGUl1VcruspJ_-15Z5W6rL1KFgoj5DHytOXILvNtwdrf8aUIpPn4ax-kOiyOPqX3i2S6LwVfx_95WLgZ-ErhkWI_YHaoTQzlYyFQYBN5bo35pkOtUix6BCmM8CzyK6pHl4S3DNbVoqK7cKUMOyaYGWpb6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk-yrQ_V5gCIRpRRfbK86MhU6IaLKCxEgW2jnLg25BmIAmq-ZKEed67oKamhuFCnvbrcrKhVb9FfFodVdk4hdvq-bnqj_bZ8FA910KZyI3b92zyvDJJOFFWrRivUSSbpW8bvmoTGHoW6loIrlZI9S5nk1nhzvMNvBXCBEjBzNtl34mCOdNKfiP0wNz7p6Jrr41CyXzmNgUh02vioolJAmmgYPVPJaXfZ6BOOamB-2BP-17IPBuRA1mHO6i3j9s1oN1z4oJd-DBrf_nUEz_-X4lbe_sHtbuslNRV-mBvP2MyC6eHPIzof0LmZo8jekD5-t6ebBoM-z3RTeRYeAEWeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mFKp9Vn9ij7v-SWbDylvMVvlghY6YbwUcO8Uo43s-emXwa_9Qpmpv-BxVvOKqJplueMrpV4I89WZh50wL0G1UahSWzOLgcnKkxyZEq8ZatERmmkpv2sXEkPNSk4MO7KeqPpYg2IRN22pUJZ5evckoFwmal009dd88jTJoUpOU9sd8SxwjndNHJwbdiFWWJ3AIIjxbESK-xEf0EAk0HBXlYAsVS-A1qwuhtsZIz1VXSGFCqF09RkpHHAKDlXjuLlGUtSeo8fiqHoBVkBZ8MzRB8GoCxFzQDKYI3nCyqMBmQGwtvepZXVB7IcB8_wQI8SA7BPA1fylr037SyT9JKtgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=mFKp9Vn9ij7v-SWbDylvMVvlghY6YbwUcO8Uo43s-emXwa_9Qpmpv-BxVvOKqJplueMrpV4I89WZh50wL0G1UahSWzOLgcnKkxyZEq8ZatERmmkpv2sXEkPNSk4MO7KeqPpYg2IRN22pUJZ5evckoFwmal009dd88jTJoUpOU9sd8SxwjndNHJwbdiFWWJ3AIIjxbESK-xEf0EAk0HBXlYAsVS-A1qwuhtsZIz1VXSGFCqF09RkpHHAKDlXjuLlGUtSeo8fiqHoBVkBZ8MzRB8GoCxFzQDKYI3nCyqMBmQGwtvepZXVB7IcB8_wQI8SA7BPA1fylr037SyT9JKtgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3KEOEgU7xvncv46id5UZUiDkJoYeNhwjgBg-stiTbEl9r94Jx5lKO2H6YuCF8CD-TsK2usZ3wAXMEaj4dFDx6AqfwtTAFMM6kh96B0NpyogvMMhRCgGkOP6MspAVTc5g66lZUeZfQthv9GpFeLb7WxMKyCWyw4TYJsSwyJnrlTNEEuFfyskxwG6bHP1fp8lfnAzI6Za5D1IdbtABaL9JFOqZGU4Rc5KzVfq3432kYGdaaSI1ddVK-VwwHVO6gkIkPjgBVHd61R795uCBIfEaJDx2xr2MGtvm0d2ffWDU75Yc9fKbWRY6s-O7fUP4WwSpOhLziLi0GSkj45WhPo07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=v-yRT2jOVW2AmCryCE-9dEjUJbakdskVwsqF8gANHv5F1eVbvx55JSbpIz5yg33PfWYYyXoGAORbVAefaNAA6j0x8i-1YJR1MRfJA5RVsh-U3FGIZ2bLAxjRzd5ZwGNzxPcRoCrzvs62Zhm9PR0MFWsrC_ucV4VO54vKViWPvY4WhZjJOHzrh9X8acTjZ7u7qrGAtVNhr5mqFVaQLAUcx_hdBZgB3L7Oo8j-SctiGJcQ3dUcajcMC_jszfk7qBixoTXFuuDztqD-F8WmmVMsNGuNR_Qan6ZZQ1ns3QzzIEdPcmUMKTP1QWUMvsuzD_kpcNttqNhCU9cH1SqPFxmrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=v-yRT2jOVW2AmCryCE-9dEjUJbakdskVwsqF8gANHv5F1eVbvx55JSbpIz5yg33PfWYYyXoGAORbVAefaNAA6j0x8i-1YJR1MRfJA5RVsh-U3FGIZ2bLAxjRzd5ZwGNzxPcRoCrzvs62Zhm9PR0MFWsrC_ucV4VO54vKViWPvY4WhZjJOHzrh9X8acTjZ7u7qrGAtVNhr5mqFVaQLAUcx_hdBZgB3L7Oo8j-SctiGJcQ3dUcajcMC_jszfk7qBixoTXFuuDztqD-F8WmmVMsNGuNR_Qan6ZZQ1ns3QzzIEdPcmUMKTP1QWUMvsuzD_kpcNttqNhCU9cH1SqPFxmrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ZxoV-5_pFQalgCpdDGNull1CBUsh5kDd3bllvRmE_QLnHVus04wevi_fBe0SrT36XRQb-i-rM0-esEQMZ1dl6EdZnNK3Yl9qBEMmXEUDkJBcJQ5_Iz7ybPie1xjattzVWd-5dPEZaPObK5EBiBPFqDLBY1-z3PZ1aWPGB1KP7druSgs8ldtslIM1nEghMoNFT-kuNQpfGjisICZ3gQ7VA8WMSOUGJHfFFLf5ij9IaKBgzPrS3KbGhTuE4eSP2YuTKVGXs6Vsxk4rBe7TsTRsoRcqksv4PW55dNFfZzTiqD2xUyMAk42iI99YVZlVMaPuoY2W8ci14PfCPstivJZfeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=ZxoV-5_pFQalgCpdDGNull1CBUsh5kDd3bllvRmE_QLnHVus04wevi_fBe0SrT36XRQb-i-rM0-esEQMZ1dl6EdZnNK3Yl9qBEMmXEUDkJBcJQ5_Iz7ybPie1xjattzVWd-5dPEZaPObK5EBiBPFqDLBY1-z3PZ1aWPGB1KP7druSgs8ldtslIM1nEghMoNFT-kuNQpfGjisICZ3gQ7VA8WMSOUGJHfFFLf5ij9IaKBgzPrS3KbGhTuE4eSP2YuTKVGXs6Vsxk4rBe7TsTRsoRcqksv4PW55dNFfZzTiqD2xUyMAk42iI99YVZlVMaPuoY2W8ci14PfCPstivJZfeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7Kwvcl__zKh4YtNOtxx5d2plEuaRLcdo1qwDZU7ECrjEJLJQVCwRQLaTiFkneh006b4e-xGUo0ttizmLCWczA-4pmAK57Otz91XGZXImodnK8HgUXra1rr_52aHLmhU8u2DN6PnKFdRNQN7luhkj16LIGMdR36Zg2BuomHOXKG1zUHSohvZvxf_y22Inr8i6KhiBA2txHtILwzUsvDuCPdHrMCcMlqiFvXswpbZBFWE8h7zfnfPsyI0IG5DO4G28KtTwTXBJMs1Z52u42pbWQ3TpPzyvOl9i0RaUzNvYx3SFzaNA7RGrXAybFQ6RbmZrH8SSC6vvFpzjpYjKgSoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=H0DL8q9JYA6m5zV5C7yQUcS19LYsHpaxfP1We8FWKb4dVtTUUCLK7QXHzxAkmjcyGaNO19_maAr2G1PVwpQ2v-259zNj5aGC7LH2rZ6PZnhhA0bCqSaAyEdFXuEc6eIDJFFMR5JqRPTLTgk8ssjQQRb60WJdzM1PwGIWXRpuiOUvZzegdiOsr3iOHb32ORM_NabczINhq52xgPh6CU-SUKdvgrddcTgeWa3h_x9vOKYIV1ZR-6YrtjxNPGo9HNehSsbR5Xgm_jP2l3jQL_ZdETel43Qxn3bU84Ax6_I5Mo88AkX8j7GPru0qdFRT0o7BjgpZDZdBPIkHJX51QssLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=H0DL8q9JYA6m5zV5C7yQUcS19LYsHpaxfP1We8FWKb4dVtTUUCLK7QXHzxAkmjcyGaNO19_maAr2G1PVwpQ2v-259zNj5aGC7LH2rZ6PZnhhA0bCqSaAyEdFXuEc6eIDJFFMR5JqRPTLTgk8ssjQQRb60WJdzM1PwGIWXRpuiOUvZzegdiOsr3iOHb32ORM_NabczINhq52xgPh6CU-SUKdvgrddcTgeWa3h_x9vOKYIV1ZR-6YrtjxNPGo9HNehSsbR5Xgm_jP2l3jQL_ZdETel43Qxn3bU84Ax6_I5Mo88AkX8j7GPru0qdFRT0o7BjgpZDZdBPIkHJX51QssLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPtxXnmfEBVP2CQv7ihqpzXKvNiUCQvsMtyFYOyinVajW-uGkab3YpfPZFOE5KD8k40RIvog1_v-L0LvXIBbysI6Xg7KigwcpTalX_VhnUhpwJH8RL3clyUizN3BezRkuuNn4xpEF0LElrICMli-r5jrtzO5EZAtWeWYRZrY7h5DuLXnfC_LLIO_o9C9VLIfPld8Z8iKj9ARd-Wx6K0IoEGSvdvsm5ZgcXykioO8QffG5Cp68bvNXhHLc12caATKflIzHvnxm7TUOQR4w9zC-swe-jq1ERz-6ajyuEG8v8Lc9s_yAmCdBk5PPAuQsy-IFWaSCJLsAM5SHTPrbwVenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0E2Y5kKbSCeO_u1pOA0DgIu-fhip2XPBb-T2DFiLni8YUG1w4Ehtmkx_8a0Cm6P8FaDWVdLd2AspOpigMDxiP-tBj2OLRMB0yLPgWdqcZK_ooCJF694fIdl4YBv5D_6vlWA9kVawhXP_7TbO_GDiiy4TFjF3G-PqRHbKtSgrRepm2gZwGzqj1OOoea1twFxC5c6J-m88uGhtUtxVTaG7aQB0ObNvrToeoNY-9kNsNc8-GKEmAdvWcY_5EnhNS_CAhCHxsW7x5PZV9-AiLyQoP417kUsDPDyt3w-TtLJA-h_x3Mn3HE02c7F5fgr-YgM891_WTA8O8W5RQOHkjfGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYE_Mhh_6Atgh86qKcBEmY9_dnDD7BR-bYng085G0RtTWJmSpgEt1WT7SM8ZdyWgJl9r9UF43Ss5Wadg8QgcVf_8nTzwVIA4rqKfcXYfS_4y6hu7DLJtE7USCA7Uox4TVKPzwCQw2q0n8kmVYx66SGrnr6BDInJrNwGAkJRVAFQfx53j5CLerW6y01WAXBUc-S5rRqdNcBW5kVJcdLJgzjkMSkGRpFn5UEtpBR5Ra4oR6x6vDAdQlHP2PNLfpy0mFYJWP1LgDUBP-526Q2m2yjz5Xl29YMgNBJ8XKg9v7Unn_do3Op-oQYYj-HoGEQTVu_i3__8G7yjtT9MNJPqDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgtcMWsNYHdvg0f6d41bfRTCrgLP0xVEYR8lTf4W4oH9aF3nXvxCRuLq9DBt8gnHkgp67u2LhenSx-VQm9Su2jlnT4F6-ggXD86lmnfdGWjgyVXnkt7w2bUvrC4EfS4gh0WryFyTJ5EQ_c_fmpfgzo-R8bi5B-FkEmqqpen81vBpPpSfkTIj3VdgV-yv0amVKM1_wExx1MOJ9POOzqdquAKon0pglgTuL-qrEnt7LpV6jLZh912c2GHf6U96wEfXiZKpKyj-e88E5MVBZ_EviIwQOQ7cRflJQPqi1xS-xq8oEfkJmuhJXDSt71EuMHB0zRY9ZVAQNvCo5fHB4I3BtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=mAqk4GFHne5h4mYI9Yxzi25QszJEcGkRyzqHyPQxt6ITGEO60iL7kYOoKKWVr2PRJdb6Ycw-KSqJYsg4nUxeLkjvvegD4c2uplaQSqVZDxd9hFxmT799eljldxj6bdFSs3guAZZKQDLkYFkmZ4OacmbMGsb4HxIyaRADBaiqZ6VJYiCLSVnn_bA1qgoy8WzJvv6em79NXvU2C6syMquJHpsQVcvaaHKIF1Ec0crvXixzAeeAVPz1cpWitb5HqsXr37aX3sr21byypBV2ZhkplHnYmoMWAtup69zp-mZCSQvOTmDNUjdCa0zFFQhTJKOV7hAKNVpYYit4lDGxMWdKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=mAqk4GFHne5h4mYI9Yxzi25QszJEcGkRyzqHyPQxt6ITGEO60iL7kYOoKKWVr2PRJdb6Ycw-KSqJYsg4nUxeLkjvvegD4c2uplaQSqVZDxd9hFxmT799eljldxj6bdFSs3guAZZKQDLkYFkmZ4OacmbMGsb4HxIyaRADBaiqZ6VJYiCLSVnn_bA1qgoy8WzJvv6em79NXvU2C6syMquJHpsQVcvaaHKIF1Ec0crvXixzAeeAVPz1cpWitb5HqsXr37aX3sr21byypBV2ZhkplHnYmoMWAtup69zp-mZCSQvOTmDNUjdCa0zFFQhTJKOV7hAKNVpYYit4lDGxMWdKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=glQHWWFbF64KksWpMalEPkR6tg9R1PhytW3jbtAp3AcnVnAEUp4tqrBwBo6zMyMdL0lUi0l57g_aGjyG2Kstwpg8mg0w7vGWKdKr8n4ERseuvrBgFw8_qQVYWMV3dMclkObKlYxU_OXdwkGQYuXbAeC9u-giimo_2O7mca96WMK46yFiIa1fPu_-hxXP8UEBE5Ll8vLd0S5qiuI5cZ1QMgHYNwZS3RnJt9_sp0Vta3Gq7lED-QpAeJ3nxaqUMeaQ0v3C6LfwevFDAzOWPuM77gktx4zDqVQUGxW0kOTSZXSRMK8C3HW9CgXhdl5n27AOJGzQA3qMIFSrYLTsEg29zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=glQHWWFbF64KksWpMalEPkR6tg9R1PhytW3jbtAp3AcnVnAEUp4tqrBwBo6zMyMdL0lUi0l57g_aGjyG2Kstwpg8mg0w7vGWKdKr8n4ERseuvrBgFw8_qQVYWMV3dMclkObKlYxU_OXdwkGQYuXbAeC9u-giimo_2O7mca96WMK46yFiIa1fPu_-hxXP8UEBE5Ll8vLd0S5qiuI5cZ1QMgHYNwZS3RnJt9_sp0Vta3Gq7lED-QpAeJ3nxaqUMeaQ0v3C6LfwevFDAzOWPuM77gktx4zDqVQUGxW0kOTSZXSRMK8C3HW9CgXhdl5n27AOJGzQA3qMIFSrYLTsEg29zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=EM3L35oe0VFHOtLzysYjFzCExuYAn8dq_UZPJ12PVkx3GeW5eM07qRNByL7vPZNLD6AtaIxkB77kO7C5cd9GBgDWF6hEy_5EYGAU5F0Jlj4R1w8OhMJr5gZeDhx7yrBGSdxkuMAXLUKFf9dYLsah2Rjl-s_FG1pVVP4FzxtPYW0FDlJiQTBhm5PZ8ly9Wou61mv6fuA4AFw_0-xaUn7eKB-Mbv3vxZikStfaLEmOR6jafDsJGbowvcbfaDo9xmgNhAF8ymA3JeQA8LOSZVT5FHU4RnAH78FlAa4ztyQmTEXsyPZbYuZfaqoyRX891WWp_I-jowLgHWxH8f0Eo4MdhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=EM3L35oe0VFHOtLzysYjFzCExuYAn8dq_UZPJ12PVkx3GeW5eM07qRNByL7vPZNLD6AtaIxkB77kO7C5cd9GBgDWF6hEy_5EYGAU5F0Jlj4R1w8OhMJr5gZeDhx7yrBGSdxkuMAXLUKFf9dYLsah2Rjl-s_FG1pVVP4FzxtPYW0FDlJiQTBhm5PZ8ly9Wou61mv6fuA4AFw_0-xaUn7eKB-Mbv3vxZikStfaLEmOR6jafDsJGbowvcbfaDo9xmgNhAF8ymA3JeQA8LOSZVT5FHU4RnAH78FlAa4ztyQmTEXsyPZbYuZfaqoyRX891WWp_I-jowLgHWxH8f0Eo4MdhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=MfKDMWjBnqfRRIl-u9vT2jflyxYpwIDrL2mDP0vjw20MoeJ8YmKQ7Nxhy8S23LBerfXW_GiNeRLIbp33eFaYjjbfjkkZWS1K0jK-5y2o4j71eHY6O-FeDgVIGEJuJbFmFaZ19cP1nv5XVd4F0u91Y6ZA6hQyDFnbMJx0E-goFUiKrQcAoL2vNJuyWBjv20Nmu0ogYzIJo7sIDLkltSG82A4Y6kElaq3Tw1EccVrVG4Q83bhWORWQ1Yr6gRJy0QVT7IBXYJ0DN8OFbHUEnokd9neUjIsx3peq0cs2Q0hkcDGXoKrpBA883uRR44Mbb7sC2fVMrrMCmLIjBFIIxii5pxNJH_9mk6eaP7dZcfND3e4q-fRbcUYO5OYqOT6OS8x2CIDBltyOUZmgvLkoZ3w9zM0iv6Kgop4JBFv7NlBuVsuQwH5hI3sg52cZepQbMfUA3XeSARhdXThXiVkNt0vX8uMGlWAmgC4ffkPRrEKi-XmK0pRemuU25LD5nwxzhVnk73RF4kYDjgZL2uGFXLVx8OPOW4ox--UPXJ7WbqIpOCZP9hXIfe5DPN7mcGE0u962v9Ql3Gafs220oUDbPPAahFv_nrJI5epw_DvT3L6IzKMH7GXBmhomOuqEeD92uEHQNxseb420KZ4U3v7s9OUYTgf66j2ceVENx5Bpe6cDzTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=MfKDMWjBnqfRRIl-u9vT2jflyxYpwIDrL2mDP0vjw20MoeJ8YmKQ7Nxhy8S23LBerfXW_GiNeRLIbp33eFaYjjbfjkkZWS1K0jK-5y2o4j71eHY6O-FeDgVIGEJuJbFmFaZ19cP1nv5XVd4F0u91Y6ZA6hQyDFnbMJx0E-goFUiKrQcAoL2vNJuyWBjv20Nmu0ogYzIJo7sIDLkltSG82A4Y6kElaq3Tw1EccVrVG4Q83bhWORWQ1Yr6gRJy0QVT7IBXYJ0DN8OFbHUEnokd9neUjIsx3peq0cs2Q0hkcDGXoKrpBA883uRR44Mbb7sC2fVMrrMCmLIjBFIIxii5pxNJH_9mk6eaP7dZcfND3e4q-fRbcUYO5OYqOT6OS8x2CIDBltyOUZmgvLkoZ3w9zM0iv6Kgop4JBFv7NlBuVsuQwH5hI3sg52cZepQbMfUA3XeSARhdXThXiVkNt0vX8uMGlWAmgC4ffkPRrEKi-XmK0pRemuU25LD5nwxzhVnk73RF4kYDjgZL2uGFXLVx8OPOW4ox--UPXJ7WbqIpOCZP9hXIfe5DPN7mcGE0u962v9Ql3Gafs220oUDbPPAahFv_nrJI5epw_DvT3L6IzKMH7GXBmhomOuqEeD92uEHQNxseb420KZ4U3v7s9OUYTgf66j2ceVENx5Bpe6cDzTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ok-FqsuT_BA_PaSzDf_DJAQdB0D6kmBf_gY8LFdaxWvzs8_YKm2nULMTNoDuWTEb0-bHugA_E32n62o4xMsMozuM_04Xd1V6deoqM-2eUG-BhOE1kRgMaB4vaXvxfsOzwCLH-QPyAreR78vWglgAkHP4c1z_37iITW_RLPNv99vBX_GQ2ihbD_umjlRIYzFlWtGbtJ6JzzAqnj2E9h2qBdfe1cLCOkbwoKN1B2nYLJ1ioMkgx9f4sUqd860gpK0MfVyb_7tSaXPo362mTSVS5_IbE080iW-yMY9STLvVnGU3-FWEANXyTZtKN7SqAAG2kO5Ngiyv9h13ha45sKSCRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ok-FqsuT_BA_PaSzDf_DJAQdB0D6kmBf_gY8LFdaxWvzs8_YKm2nULMTNoDuWTEb0-bHugA_E32n62o4xMsMozuM_04Xd1V6deoqM-2eUG-BhOE1kRgMaB4vaXvxfsOzwCLH-QPyAreR78vWglgAkHP4c1z_37iITW_RLPNv99vBX_GQ2ihbD_umjlRIYzFlWtGbtJ6JzzAqnj2E9h2qBdfe1cLCOkbwoKN1B2nYLJ1ioMkgx9f4sUqd860gpK0MfVyb_7tSaXPo362mTSVS5_IbE080iW-yMY9STLvVnGU3-FWEANXyTZtKN7SqAAG2kO5Ngiyv9h13ha45sKSCRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=d8mNVgcLj-bOTb1YBAJB0CIzqw_Ege51PQJ2JCiLQ0LPS_aWRHgWHTulMvHQhEpjOSa7x2DD-Hh4EfD_FBcLbSs30gMPYbEq2mE-vzPpMo0fdYeN2jJICg8zVSL-oOKrKzCovbVq7fak3FY4XtkvJ9rEAvNike_xE_N1j-5A9Qs0D_mbz1bTINdLnk5S8z0YhRPEHoI_uSlJ40FehA75vDp23J8UafEyTV_cg1QPYnJawBiJHHc1YdkVjfljAMkVIhhA1as-3VA2CCQ-fngG-j709nrz6B8bUNME3pf6GMDDdVCb9aqwNZs94JA-in35xYspXHpha1CPzuqd4-p4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=d8mNVgcLj-bOTb1YBAJB0CIzqw_Ege51PQJ2JCiLQ0LPS_aWRHgWHTulMvHQhEpjOSa7x2DD-Hh4EfD_FBcLbSs30gMPYbEq2mE-vzPpMo0fdYeN2jJICg8zVSL-oOKrKzCovbVq7fak3FY4XtkvJ9rEAvNike_xE_N1j-5A9Qs0D_mbz1bTINdLnk5S8z0YhRPEHoI_uSlJ40FehA75vDp23J8UafEyTV_cg1QPYnJawBiJHHc1YdkVjfljAMkVIhhA1as-3VA2CCQ-fngG-j709nrz6B8bUNME3pf6GMDDdVCb9aqwNZs94JA-in35xYspXHpha1CPzuqd4-p4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgpEgx1uY6MVtmFfMRXELdV8YYR9mssBuOSP4UcXLCmz1g49geWZ5_YFwreXzJpcoU5pj81Yia7svv0p5Y3APV-X0UvqzZmhwo8GSLbELbFMBnNNqARPHAsFOa9yEtwGWPPKB6xL6_2p60Bm5T1Wh57ORq6LSQFOtEF-W-FdTAms7QGClIa6G3ciT-NNKSolNks32x_V52CBkZhZbgx7YLOBJVf34ukeMVUuDC-4uix7ujYE32XJnrcQTzVQ7-kw5hLLY2Zv-NEidsgnRe6UQfPluBK1Gt9ywfaIHzVskkh9qbEb9ZKWCM112xYnI6T7fd5Wtqrt6_OlitXihvnWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=QwYJzKWKn872SrLzyJXmB4KXruJ79Eq8QYLXZxfM0egGK4_KQi7A_sShfO8ERjfLB5H679JV5W5OPDBIyhcnMcNkvtFvdHT6L5O7DLJ_CTJwDV95z7SsMtO4N0dchI_Rk_nWLy16lsBxUr9rIELX5kcZqoAiLtv5Ph0nH8W9B-rgs_bYI-IQK7-GpcE9r4NpfHCpiqJiLnSWpmmI984m7NUKDU2Y208NWV1HE84Cjh8bpQfai9JcYtFwC8JRORoBFbsL_xd7OGL6AsY-mPkzAmzFzIVa8NJq34bCgMRuMYoqKbSdN_vzCMvOLaP7mk4vt_OvBQfwtE6tGR4VRrO-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=QwYJzKWKn872SrLzyJXmB4KXruJ79Eq8QYLXZxfM0egGK4_KQi7A_sShfO8ERjfLB5H679JV5W5OPDBIyhcnMcNkvtFvdHT6L5O7DLJ_CTJwDV95z7SsMtO4N0dchI_Rk_nWLy16lsBxUr9rIELX5kcZqoAiLtv5Ph0nH8W9B-rgs_bYI-IQK7-GpcE9r4NpfHCpiqJiLnSWpmmI984m7NUKDU2Y208NWV1HE84Cjh8bpQfai9JcYtFwC8JRORoBFbsL_xd7OGL6AsY-mPkzAmzFzIVa8NJq34bCgMRuMYoqKbSdN_vzCMvOLaP7mk4vt_OvBQfwtE6tGR4VRrO-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWGXjfjWizS0qNEyWCACjMI0stkYhUJ9aWKTaw67wC-l7fmzNS8od_VDeNFOSmx0fm1nahdd_GA66RoNgKqIc3nPGKB3iHdHsSActnW_yyMAKwP346twwogLnhI0O8qfxcDU4j7b6pdr5EwdHqT9YT1uuLCnyPTXKrTKpYskm_1wxLYI5kwWS2nism0-YzXkosDUP9tkvHmqbRcnLTsfVAVZmPtrSy1cf0TbrUgFIuTz79iinbwKoKqxC2zXa8kOWmXj2ZFYr-JEG8EMRycR4UDqVbFVI2GvlxDbKrRqwmk0mMpyWaG1Ia3WDUrs5enN39fnO69wx3cLWy6Km0EyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy77qN4vgCpUrsMI3tzZStwHbDn2oHWwIMBUIidzTmIj71o6LcI8uVnllFKkhrsjIN9RnHMGNOSBPlkxBQ0DFmelhM89PP-ItFpl5S_B4paZz03SKk5oc6RNDoZ2A_0BWVgEsv2ovjz2ZQy73L_IXB40BSxAJl2d2jHF4y3vXOy2uyFqki09HncFm7mk34kbbQyIplPgDbQcIgQfiNNtTAg8zxlO30QIMi1PzeLnsOm6TwYaEgmV5aB9gEUI8SmOn6AMUtyQLNossILPZISk-MafooehpPkAbXd_aIDcRenxgV3eM1u_LGRJLf0iCXhd5yH2gF0B1YEnM865AUr1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=KyEuHxh8p3j28YRZyVq-QqUAUfUW3KYJwfKhPWEI0wSIMh1ZcTHJngn5AWzwu_wZ1Jbpt5fMkm9wsOqzsyZ3ijiy-uHvxRYu0fVAnF8brU4kBXFChQsTEIQ_F-GJwweUB8KfY2L2D8QBPKKsCdLZbknpKSCqwlCX-Mpjeg9hmiNpR2JPN4E0xE8JGvgA6REkqXej4rtwbeUm1mddVOdu2p6gd16zIW5D2Xsn5FUJwLr8YyxxzcK7p1htn4AQK7Ia-BDZdP5TNGS7wbctJ67K0_I-lwe5LmovLu39MacQsnNQBfIRuUlnS6f5m9ZiZyg3A5AOowHgLOnYE9jnXkJc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=KyEuHxh8p3j28YRZyVq-QqUAUfUW3KYJwfKhPWEI0wSIMh1ZcTHJngn5AWzwu_wZ1Jbpt5fMkm9wsOqzsyZ3ijiy-uHvxRYu0fVAnF8brU4kBXFChQsTEIQ_F-GJwweUB8KfY2L2D8QBPKKsCdLZbknpKSCqwlCX-Mpjeg9hmiNpR2JPN4E0xE8JGvgA6REkqXej4rtwbeUm1mddVOdu2p6gd16zIW5D2Xsn5FUJwLr8YyxxzcK7p1htn4AQK7Ia-BDZdP5TNGS7wbctJ67K0_I-lwe5LmovLu39MacQsnNQBfIRuUlnS6f5m9ZiZyg3A5AOowHgLOnYE9jnXkJc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=kbxGyQyRrEUVizjFvIRUt97gtmLURutLu0iKJbP-I3BGeovn5B3e43wVWA7xhvbhkonQ524bXQhDQCYecolryp_-1lhNGWH4uWY3auH412EKCydgdCxUqSt3chF_yWDgACfgeowZhMP1OKWn7eF0O6wQEA1LHnO8s_8sfVbUR8BgLUPRQXRbRa08bTLPkl2GcAEpJ1RLCg9avRDAfFRWO-DamNO7cjkGdhkx21isf5JSy4Mdng6_rZQ98UWmnb27W6HinZ18J2VFHqEfhDfKi_JH9bIJZHtte20VZLTwJV2wFCdbVnbJ62geQLyfFzYaGOsLPgr3Fovg-OF-kS4Qhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=kbxGyQyRrEUVizjFvIRUt97gtmLURutLu0iKJbP-I3BGeovn5B3e43wVWA7xhvbhkonQ524bXQhDQCYecolryp_-1lhNGWH4uWY3auH412EKCydgdCxUqSt3chF_yWDgACfgeowZhMP1OKWn7eF0O6wQEA1LHnO8s_8sfVbUR8BgLUPRQXRbRa08bTLPkl2GcAEpJ1RLCg9avRDAfFRWO-DamNO7cjkGdhkx21isf5JSy4Mdng6_rZQ98UWmnb27W6HinZ18J2VFHqEfhDfKi_JH9bIJZHtte20VZLTwJV2wFCdbVnbJ62geQLyfFzYaGOsLPgr3Fovg-OF-kS4Qhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Y5FJjE7bjUs6AqN58hn0djaAuD8HI78_AV8HnF6x8NAMDbpoVL7giCgBiHC1NRMWe9fAZaaICJSU9lqoHrrU4H56zMRsfOL3LNUrDD_Frli8scAcxPXPMws8A9n316LjH6HiQro1rE1L791wCbNAV7KkHQDg0t29eQRBg4uO3DzeLROlNJ_HRapbrdTxKu57SIHAnkuCqqT3C9tkDABS-CTQK6fint_tvA2_vN5n87_mBk-9WJzEzB0f0zdPtXhMjtMuY6MV-eqOiNtC2MUd435cmx5gfTH8wNUSpo4mIJSr2ZLyTYXz56rvrOOaX8SnYVSd0WXzYwn7XkISh8IICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Y5FJjE7bjUs6AqN58hn0djaAuD8HI78_AV8HnF6x8NAMDbpoVL7giCgBiHC1NRMWe9fAZaaICJSU9lqoHrrU4H56zMRsfOL3LNUrDD_Frli8scAcxPXPMws8A9n316LjH6HiQro1rE1L791wCbNAV7KkHQDg0t29eQRBg4uO3DzeLROlNJ_HRapbrdTxKu57SIHAnkuCqqT3C9tkDABS-CTQK6fint_tvA2_vN5n87_mBk-9WJzEzB0f0zdPtXhMjtMuY6MV-eqOiNtC2MUd435cmx5gfTH8wNUSpo4mIJSr2ZLyTYXz56rvrOOaX8SnYVSd0WXzYwn7XkISh8IICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sja3heB2skHTDzIDKAVfXmBnEUkuhoT1wYEEm7eDPBjxIXd32JNUu_Sp2Aa86RapFdgKXE96imNnHoMhuT5geDLSAjCFuuwOEBLKAJ_ARck_SMDxlS-rtotPpmhIqy7rS_55BVMSx2bZBtScm5b7GVEQBSg_xCx-xYAqshUSbQjWANeSyDCZNEUKZhOnP9PqKILJUy9y0pFlW0sij-ak_pKga4f4Hw4CqTDX0x0xjPPSZ8mRf1xaQogNho6DtH5uK8zkhMsQUEVw3vM8QpqySO-L7WxVj664xj51P9hr9Td6sTFzu6Wd2Tiqt3TtpZ2tkpphNmxoCTzuhT3Fvjsm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=NM1K7ukXN2az3uoO-bVOWKSs671Id24Sj5xF4rsQ1ZQ-3gPRXEnAMqwoS6OKUTurMq4cfkadyHZb_EqtTrBFa0UyI0eM7l21-8HYb8qIAdQ_vJU0XBZFOT-tiLX8obWLZRjyksdjR9b8jNgDVJ0iKKacMyhBCcsTXdz-vVsupw6shdOqUD7GP0AlU1zscOt_9FmqIVQmOV4NkYy4naO8y1WhedCCwD3QS966Xf4vlY8uwFq0xYsJlG7Q1e2PTUeeZ8M3Pbg4KjK-uiUviNZwmKfpEtpT-HCG7ilm7pGvAkHdwMrioB5vHPDMyQ0Ifdh36suT6wQs1TZWYVmjcy2_lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=NM1K7ukXN2az3uoO-bVOWKSs671Id24Sj5xF4rsQ1ZQ-3gPRXEnAMqwoS6OKUTurMq4cfkadyHZb_EqtTrBFa0UyI0eM7l21-8HYb8qIAdQ_vJU0XBZFOT-tiLX8obWLZRjyksdjR9b8jNgDVJ0iKKacMyhBCcsTXdz-vVsupw6shdOqUD7GP0AlU1zscOt_9FmqIVQmOV4NkYy4naO8y1WhedCCwD3QS966Xf4vlY8uwFq0xYsJlG7Q1e2PTUeeZ8M3Pbg4KjK-uiUviNZwmKfpEtpT-HCG7ilm7pGvAkHdwMrioB5vHPDMyQ0Ifdh36suT6wQs1TZWYVmjcy2_lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=U_WP4R5rgdXB-RLnkl65UPV9T9dTX2vf56Goo0IsqLTwPdMwDySq3vQjfy8HOBH8taBYh5KCRtNSmWOz1M6Vms1Qaxnr87KXcX73rAnStnStZfpKn73iEZMbu5u8_8X6AVSq9nze9p2gTBDSLavroac4skBZf3s0IWn3-3L8iezRGqjRur68k9LK565MRSaxI6l5aOanZcrWgvS8C44tFX4YGMgaaJ1Lpb4qb0psUj57Z1DjLlGwk-UQp0GYPYs-TmmN71Mql5JFwimxYTwsN4MkxnhfoAWLQhguhYgLtIVLD29gxV_GxjNVc_VWWZoLLSa0fGNsar2L_7kXBPqmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=U_WP4R5rgdXB-RLnkl65UPV9T9dTX2vf56Goo0IsqLTwPdMwDySq3vQjfy8HOBH8taBYh5KCRtNSmWOz1M6Vms1Qaxnr87KXcX73rAnStnStZfpKn73iEZMbu5u8_8X6AVSq9nze9p2gTBDSLavroac4skBZf3s0IWn3-3L8iezRGqjRur68k9LK565MRSaxI6l5aOanZcrWgvS8C44tFX4YGMgaaJ1Lpb4qb0psUj57Z1DjLlGwk-UQp0GYPYs-TmmN71Mql5JFwimxYTwsN4MkxnhfoAWLQhguhYgLtIVLD29gxV_GxjNVc_VWWZoLLSa0fGNsar2L_7kXBPqmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=U2s0JvaN9vRxrGQDToerZ-SucoD-5vVzZY8DFNucFjQs3NURVh6uj1VZYTHEhWZ0LveISLX_ZpnZoIODNA5i2N_AiOpRJLGg1Pp5m2B1AoHmz3iqdGtSUy-SSEtfr0ZTZZ9rISKrHAzp-jmaVVBT6JKCRgvdTZZDHAoVJgXr5uwBNuFliEjs97xvrT2o86KXCqUElr6k69RDdacXqnjuFH-BeY4vTF9-iSSCFNvSM-0kCW3SuDbY6qbXDMbWBVR1-2wpmYFqTjs0J432yqOGM4vByX3THTjbYPuzDZixdj_7bzjr5veTIVfZUQ4ObNt_vUGCg1-CpvS7jv1tohHthg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=U2s0JvaN9vRxrGQDToerZ-SucoD-5vVzZY8DFNucFjQs3NURVh6uj1VZYTHEhWZ0LveISLX_ZpnZoIODNA5i2N_AiOpRJLGg1Pp5m2B1AoHmz3iqdGtSUy-SSEtfr0ZTZZ9rISKrHAzp-jmaVVBT6JKCRgvdTZZDHAoVJgXr5uwBNuFliEjs97xvrT2o86KXCqUElr6k69RDdacXqnjuFH-BeY4vTF9-iSSCFNvSM-0kCW3SuDbY6qbXDMbWBVR1-2wpmYFqTjs0J432yqOGM4vByX3THTjbYPuzDZixdj_7bzjr5veTIVfZUQ4ObNt_vUGCg1-CpvS7jv1tohHthg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbN96kMsZa2_QnLVh7Ov0cIHZvwVq4_2TqB0TfjMaYPy6-nCh-gmJKjdy0SMGoLrsyEQO2d2NtgxvXjwB3mfFAwHbZKXHSDs6g-Hq4t1pDrPco4vOyd-FFtAzeWaP3SsbtArsH49Y-95oVosLCRfsrwEkzmKFJDDHl21HEUgw6VOpjQcbkAbIxIfqx-aoq_8E5DMiqwFYAZIALJ2jfL92k5rAO-iU4tPqb2xGt9nwHP5oQ20YiLWzbWcu2YFAsrrcg1aFHJeaJzUcjoRXt3DhKcdxjT4fw5BMZyO9UDiEfcZs1_2lL6zOH-b58GL7HvnA4GeGS92VcoxKaNfeVNsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ckL_onuii5Gfv44-gH4m3HxYs3H1DXPcBWfx6n7aKDh5YuyauZk08F3tMgwMVOCYshAVQSApRbo8Izg0Gdeq8PaN1fVe4_ABuQEf1ogWJBg9spdWAgU0ZUprk6PIyEUxPrJt-hUDvS-2msoDvIGlyA86Gb7uT9KAew4Or9XaADRDlqToO8g86gOagpmVo3_gLF5Jy-iPWgrLA46RpoJgNIbjm2qcDAP6aZAG1vDiRmAn6IDos3tEC2tPImLCX_VyUDNh-vgzn08udCzEzpnKpM8MHK1bCrJujLsYtIX-u6Feg5Ol6W7saWgiUxk3p0KxJ6v8LZsTZ_maSYFomjL-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ckL_onuii5Gfv44-gH4m3HxYs3H1DXPcBWfx6n7aKDh5YuyauZk08F3tMgwMVOCYshAVQSApRbo8Izg0Gdeq8PaN1fVe4_ABuQEf1ogWJBg9spdWAgU0ZUprk6PIyEUxPrJt-hUDvS-2msoDvIGlyA86Gb7uT9KAew4Or9XaADRDlqToO8g86gOagpmVo3_gLF5Jy-iPWgrLA46RpoJgNIbjm2qcDAP6aZAG1vDiRmAn6IDos3tEC2tPImLCX_VyUDNh-vgzn08udCzEzpnKpM8MHK1bCrJujLsYtIX-u6Feg5Ol6W7saWgiUxk3p0KxJ6v8LZsTZ_maSYFomjL-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3ui8gbvEAfNnr6g8Foxn6PGTn9Vn-bVvc9-66y7BkREOA1cWdyDlX4mgQLtqwZmWyA8N7uL8Yf3kYJFQtLM90vhu1MXv3QRohKIN5H6kwp4LkF6Nx1ZECJtBq2ZqitNdms6FhOkuV1HMFGJ0P4pQ4FnIaStXwx7SJjdDb39PwfR05hh2NulyEI2O4Ba6sEg3MAIVA24KQyYrpkj4OxUHq41lvtj-b8N9bEvVV3o07YIlr7EQfiqj5VE1Fuer69z5iu4oyro0_Dn5pqmkLdIdew-FT_wGy3nWS0JE5KOBm6Dm1P5GicRx4JWjjxhj289bJuYWspEyjYD4iw63Xwhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ct0PeKay6SOdB7A1mK_liqwCDzaX9oXKkw8MtSKd0QJe0rimEkkv5SC84dKM1ywcT3aOWzfN9ieWwyxhzSiguwAM7Zulvxw-qwsa15nzWImnDmFrD230n1dxaPTVb9eQEzavO818AUjDXIMjJU2XrAwENw3Dry8dd1yRB5mgnMF9uycNcx9VXbISbI5-Lj6Wnaj67yEoRa_hjyI489sutJyXKDCnQL-VaSRJsTJ184xBiQ_u4SNXJrwVWZ7ggQ3XrpAnsOR8hwnRYsWB37Of_JvicCOy-3n8gCtoPh0FP6Y5tdmS9iAXrlWFSNO50pwtqhpu8Q69VxmBWevZWgpNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ct0PeKay6SOdB7A1mK_liqwCDzaX9oXKkw8MtSKd0QJe0rimEkkv5SC84dKM1ywcT3aOWzfN9ieWwyxhzSiguwAM7Zulvxw-qwsa15nzWImnDmFrD230n1dxaPTVb9eQEzavO818AUjDXIMjJU2XrAwENw3Dry8dd1yRB5mgnMF9uycNcx9VXbISbI5-Lj6Wnaj67yEoRa_hjyI489sutJyXKDCnQL-VaSRJsTJ184xBiQ_u4SNXJrwVWZ7ggQ3XrpAnsOR8hwnRYsWB37Of_JvicCOy-3n8gCtoPh0FP6Y5tdmS9iAXrlWFSNO50pwtqhpu8Q69VxmBWevZWgpNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-I_5Ub3Ozag3fdXzILI9M1ZzojcouBDwv4jsa9oDEttjefTgcqStbbgKjfBxs1Vqx-QEYNOrM3Gm3Xfywqypk-aa1xi8YtsS-1LBkeS5JrM6Av9sdbDtxKkqSq38BqkyGNxUW4k_UUpdQtl-e3_Itc5IRRxmhz45v7K4kr6ITx5_Fw_-RCvYdc7OJHd0snRMc4KaunsYRBHG202lttuV_5W7w_xQzPaHLwY5_39PDb2cuPdbsvKsawBW2DIclEnlCvp-2KFuXWpYqtKJRbCx0CIp81MC9v0YmbKVyEKUgkpLaBFC8DWyy4lA2yhcZ6nOfVEJ1pStvpwS39lLW5FhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=bLdAaz5-Mu7vTmQJnEOWhDiUuCskWiu28wSxlz5IeTLzoZU94UiAoMw1OTjqhbx9xvXwOmPKv3q9v66N52W7-Y1RlQVZ9_ef4p27t1UMQIaT2oBIBICwlVnTVhL3kDnQWyW7RbE_ZCtz_Svg-tbAaQz16ZX9EgMUcNJuAiN_mtGEkv4aj_wSNAkLZjfmbL2KiUcGYL0xNzGCozt0DkDDxDLs_u_s93-cc-dz-q0iC49AuebpKrpvA-j13SSALwJcWbn2joqmbh1ZQ0hhuE27fSBE65jneZaMKrWLt7Nrqr6qIH8UfYjCIAVeD_XmXG_l5YbddArVkROY3CGVd4GilA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=bLdAaz5-Mu7vTmQJnEOWhDiUuCskWiu28wSxlz5IeTLzoZU94UiAoMw1OTjqhbx9xvXwOmPKv3q9v66N52W7-Y1RlQVZ9_ef4p27t1UMQIaT2oBIBICwlVnTVhL3kDnQWyW7RbE_ZCtz_Svg-tbAaQz16ZX9EgMUcNJuAiN_mtGEkv4aj_wSNAkLZjfmbL2KiUcGYL0xNzGCozt0DkDDxDLs_u_s93-cc-dz-q0iC49AuebpKrpvA-j13SSALwJcWbn2joqmbh1ZQ0hhuE27fSBE65jneZaMKrWLt7Nrqr6qIH8UfYjCIAVeD_XmXG_l5YbddArVkROY3CGVd4GilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USG2rzrAHoLJADN6uWDh93dP8__QpW_4nG-xgXqIZN9WyIols5WfnvF6v5Cx86TyF-ITLxFE1YkctpvjKFlgXtUYkhWE9elAZVZEsoZ8sGAEzhWzRIQDv8rXcBJNA-5GvyU1RkpFuEu3H1NHP4kEzq-4r-4KDOOqTQoEJKxbpswC02JSDkgAIhvRV62qvTcmTKz1f5ssz2s9u15_NMvX2O2K3Khkqo4WxAURna0m2NWD_2ousVUNQR02Z3FRxT_V9AyIcpnnddXX_-SxLYeGI5NRENFHb06jX6ys1pLJU9LgfhSW8E8aMvmh7ohL93s2NwzHkCeG_D3aQMCpfsctcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXkoSW5Dy1crnczvc5QgUX0UIEtpwxt91dF86CLEceu5VLi9ikl3MVDb-_JX-mPq5s1tbaHk27qwA8X7DOIDLLF6Q-JdD5a7hdkuXTpQ52qW6xJJLgc8AHnztewAxsJ8qdvaT4JHujJRdeoUOl3jJCcDuKoJzwVskYbYsxgXMwNfydmAaNSxWVeb4jBR1OvVmUGCltQNAZtdGQkPHzlOeqzu69Xy-BFCbvj6nGPFSTasbUBqggD1hSLI3yPC76lqIP-l6-cIe-W8y4NLdmH5HyqX3ikUkPQ_FKYgWVLjFin41iktiU-53VUayBTliWWGrLFV3MKQDr_riStschzEAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Uaf5qttiGXjOWyYzb3DHKGF2rKpXXeDaOmMIHrzWwUc-tCNd0Uxelxb7IsUUvSoZEwRfyv8NCgcd-5t_9Y2kvwQN4D8m1qBaVHgKv69fD3V2F6BrlZU2NMwiWlEQfw0k0ntBJbMu6ahw98H-e_tXT7zjaf3ZUdcSXOGYQpUTAy8rBwOS660MJvJpwQE-8SRyHkZ0YDAN8kItyJ-tEoWmUVqF6dZIFj3Sk7_VvNVIID96CwiY101OIaFHoieIrLf6ke76UTeBQATQoisV8iWo5wfOQ9Kb3eiw39YFudVQvJnnT-kN_K1VoVZFM-hMWLTJTbbPwNynhiaLv73dkyz71g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Uaf5qttiGXjOWyYzb3DHKGF2rKpXXeDaOmMIHrzWwUc-tCNd0Uxelxb7IsUUvSoZEwRfyv8NCgcd-5t_9Y2kvwQN4D8m1qBaVHgKv69fD3V2F6BrlZU2NMwiWlEQfw0k0ntBJbMu6ahw98H-e_tXT7zjaf3ZUdcSXOGYQpUTAy8rBwOS660MJvJpwQE-8SRyHkZ0YDAN8kItyJ-tEoWmUVqF6dZIFj3Sk7_VvNVIID96CwiY101OIaFHoieIrLf6ke76UTeBQATQoisV8iWo5wfOQ9Kb3eiw39YFudVQvJnnT-kN_K1VoVZFM-hMWLTJTbbPwNynhiaLv73dkyz71g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IomOWHLyVNh-q3Wx6Ux0acMDbibnd5iYVhtWy-fFepIrivmDY7ZXtMdY9OFUEMZPUzUaYeBWtsqq1j6xGGwilK20uPFtzcO2JrqAo-n5sRB4u2nGgpXbiZ3myeQOG0OpEC59qONFzB08W3hlbON7sg52tCS3ZLSMpWshIPHFc-RJYDQXB4GNztsj-j72cTS3JD2Bu63H6RAtkJO9zd67aKgFsDbNsDvCggpyKOZDY5_vQXPft4tuKoej1u4snnMa3NL6rzKMheN-08mjsgjE0r9lQFxbuh2PgiqTEdSrH9wAnDP9Y5Hr2lfXuSNUBsPC2G34HQk30DLlbvJyAZps7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtQhxN03nP9HfXHUxrim66sLredkvMaWd_J88gfMhT_dbrZEKNug97aIXZh6yY8d8ivZhOGrsJixCLiLh7g5YTskarhrvCFxeWVyoAszdvGHgCEpdMdMENIPgBPiU1cYKSOBRGS0InntYxcCQo0txd-1nWTvQX9PAsEEb_jz29NaUgH4J5QYSf57ZXngueHN2Kfrr_1VaQM8ZW9_ieA9RGLtsD4vXHbH4QtPI4bkeXOncESjXHtsoRKw-4FAiZV_Oe0aaZD-AN0OUoMEbQNTAGi52MdYO5XV_BM5wAxBuebifGX7F3YoYohpMqlnB95_sC4BAZ23G6itmwQ7aD8tng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xpyx0m2eX3zBOqRp4K5ylYPtOhEkA04gvoFIzgoJeuIrd281_bj_6FYLzPtUIzubGYcYgq012yQx8kRV8TvhOmbT-UU48_i9JMYqO9ryGfzo3bcU_zYu5AOuvLkISGKBdaXaIKrlmThUM6I2N2jAq50oDuRj_Dg4pwI6UEVx-f3pYj5d1TAIix8m1E5RiHxTC0oPgToFtWkaZU610J75161QyWO4RN3tW253EyuCGR5LZMoxEg1M6k6H34CjgyFV1ScTM3RZw99n96OZ0mREG0Nr51pA9NYCwOeDkcFIllfhM47inooWjOjKGrofVgbH7pG_I5pH7EZ-guUnmGqTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oksYyD7ZEuSSu8FtRha05y-r6WG4RxOewfqsJj1zOOU66MueBksn_GKEh8wz9leJH6JHFkTY9LpB_ota-tTtcOK2PaCqb2s4zem0Z9PsDX7tHwqSyR9GI4sJGHu_XlrQdHiM3l32Xn3tNav2A-_Z56hhIVEz4vJlKVFV7GQDVak3UBH2_2qIZud1ev3dWyPxZuB7fHuZ_RZCDgyPOgiNfcMemlORoIpaGWvOqPWWvgEylF5Jg2H8GhwAgsEBm4HQskdAcOu8uPIggWmtk8KpPwOzPveVzVREPxijisPufnh_li2k57Unr1P3U3y7TyWguIYQryPShsjFet7uxpcfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZqhrIHXsPF8IehXFr7m7G0DavyFmjocPa6lYR7H_Zp7rNcDchVjQEGaqlLr0pT3y_NjnisyPCR9XrR99w8Y4eZlN1nkx4kJdc9s7cS9r-9ORkQPGnOQuizQi8awhmhUWCrYN1MZh3Qah_mK5ylRb10tPi7ZBmo6EuUG1gg37KGiqIjmVX5dhqmIkWgYPZp0qCyzq9p7vhkqWJFEFDzq72_l1ckN9CjbM2tKK_YPEqaLVb2bLHC5j2nvq5oWqPlhfGoslsUZMdN1iIZzaUsi9SCO5E37B8ueWPfg1dx8NdXr0SCqHLqh6WzteuDvnr0BTzqK7jqMTbE_s1o4bveQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=rPv5JRKwFBL8F5-mZxo3NTQY9nrbq33ZtsKzHdY3HI0EbpGdtNxVWAQaov10DXCsrj8rDEgzyv_H9r0nMXfsMC8bB7s3FgtZq15d620cCbcGpWRGV_ml43q3QN3JplTLu27ovKY3cZkHwnmFgdS_KGV1Kbx0tn5yJmL9MRg5ECqjanFDNpVP6UCmpyvRTKB1JVpYnmh9X6KWt9QGc8mRn-3mZa8CNsZmryEBFvrlXiAQ66VsElw_bWeqOsOkwhTRhnpazXpWXSaH_QKPiBX7M7tcyy_PKzZxYcnzGhz02V88L6hFHQZgefvyv8Ty5A1a3f34SCOD0BK9T7tpOVtznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=rPv5JRKwFBL8F5-mZxo3NTQY9nrbq33ZtsKzHdY3HI0EbpGdtNxVWAQaov10DXCsrj8rDEgzyv_H9r0nMXfsMC8bB7s3FgtZq15d620cCbcGpWRGV_ml43q3QN3JplTLu27ovKY3cZkHwnmFgdS_KGV1Kbx0tn5yJmL9MRg5ECqjanFDNpVP6UCmpyvRTKB1JVpYnmh9X6KWt9QGc8mRn-3mZa8CNsZmryEBFvrlXiAQ66VsElw_bWeqOsOkwhTRhnpazXpWXSaH_QKPiBX7M7tcyy_PKzZxYcnzGhz02V88L6hFHQZgefvyv8Ty5A1a3f34SCOD0BK9T7tpOVtznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VSX0dxFVQvrkMr6zmyWPYhaJVj0gIxc91TYlUMIF96s8OX-d7ll-EpRKTCtmINckv0T0rk9vZdNiZDjRtLocNxBKppCSZNWpTR9W8DA2ZVCu5KgzUJWx91cTwEKV9nnIKrIGzxEfWQwbgLqTFeWoKpT_ceU5qgYfhrnAZHUSWJjkX-SmZVjve8fcLsibEAdixnwCl202dBjN3oA2JtDiEjLVqZzI9Qt8iPUvKDQ8Kf4-OgzEdFXvneEh_01bSEcAPrsZ3iUbmQiIiTMc1v84vTxdLDc69UUanWeHOMNOsn9F20mz-skvoA2gqVpaYJfczn41awHsHEJFgYIoifVRlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=VSX0dxFVQvrkMr6zmyWPYhaJVj0gIxc91TYlUMIF96s8OX-d7ll-EpRKTCtmINckv0T0rk9vZdNiZDjRtLocNxBKppCSZNWpTR9W8DA2ZVCu5KgzUJWx91cTwEKV9nnIKrIGzxEfWQwbgLqTFeWoKpT_ceU5qgYfhrnAZHUSWJjkX-SmZVjve8fcLsibEAdixnwCl202dBjN3oA2JtDiEjLVqZzI9Qt8iPUvKDQ8Kf4-OgzEdFXvneEh_01bSEcAPrsZ3iUbmQiIiTMc1v84vTxdLDc69UUanWeHOMNOsn9F20mz-skvoA2gqVpaYJfczn41awHsHEJFgYIoifVRlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=EqRMIjAyja5ZEF4msKUT3c3eJH00XTJeJD4nvcEiPM07v49WG8dD33b56z9hY2jDUK703tBs-lZKONKNSxexXyIH6AwztTcGtcyDfmxocQ44_kabD4Fl_Dkek0lIeBhM6W6Xox_deUcT0m_5IRkof_D6DgI1hmz4DgXaf3BX7zQ-kESW79WNPoqkPJWtHapdApEE6EpfIVkfsEVdDoRKXKAj3BHvDEJIalSD1pPXSLDlss-Fsko04AzV0AtW56m9MjsnvU8IXh6WdOPRcm8wca_sC-ndp6Q8BLEjlHAZleWerNeuSLguvBXd406ugKG__-wiE9izt6fOZf22_TvGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=EqRMIjAyja5ZEF4msKUT3c3eJH00XTJeJD4nvcEiPM07v49WG8dD33b56z9hY2jDUK703tBs-lZKONKNSxexXyIH6AwztTcGtcyDfmxocQ44_kabD4Fl_Dkek0lIeBhM6W6Xox_deUcT0m_5IRkof_D6DgI1hmz4DgXaf3BX7zQ-kESW79WNPoqkPJWtHapdApEE6EpfIVkfsEVdDoRKXKAj3BHvDEJIalSD1pPXSLDlss-Fsko04AzV0AtW56m9MjsnvU8IXh6WdOPRcm8wca_sC-ndp6Q8BLEjlHAZleWerNeuSLguvBXd406ugKG__-wiE9izt6fOZf22_TvGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=bMFQkTDAmxcSUyLfFHZY_oCXwP4gO5YRij2hHVzzNsoqaem8Ia7CwyI_uavGi6NC0drNLY0GOM4IfZPgDc-H1yGZnzMZLu40yIk2JeN15k3uuODch3-Ga9uBPNbAgfCTLaWAewuJhZ-RDxgIeJ6v4Mep8kZcOV2_WjCReXTCWRO6JqOxU4e7GQ3T2jkmbKvskZr5SZSQTw_HP0X7gsy-Mt3OCqVwG4MD4pjjgkURL4yop08gdJ8GO_XQ3KVUIetVqLFxiXznSgx8mTrNA8iACLeXY8q2Gh0UZrN3VfFf9MZsC3sAAHCs8zZ-oK5IMO5j_ngEtwkSB9g-lNFGQ0QcyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=bMFQkTDAmxcSUyLfFHZY_oCXwP4gO5YRij2hHVzzNsoqaem8Ia7CwyI_uavGi6NC0drNLY0GOM4IfZPgDc-H1yGZnzMZLu40yIk2JeN15k3uuODch3-Ga9uBPNbAgfCTLaWAewuJhZ-RDxgIeJ6v4Mep8kZcOV2_WjCReXTCWRO6JqOxU4e7GQ3T2jkmbKvskZr5SZSQTw_HP0X7gsy-Mt3OCqVwG4MD4pjjgkURL4yop08gdJ8GO_XQ3KVUIetVqLFxiXznSgx8mTrNA8iACLeXY8q2Gh0UZrN3VfFf9MZsC3sAAHCs8zZ-oK5IMO5j_ngEtwkSB9g-lNFGQ0QcyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J39SBrihHmAXm_Q-Xh0M9vsMzfuua-0wuPXVVTsMuDwOvaprHxTyQrUX_qO0UMcp4L87r6OUzekxaFAC7tS7y2C-Rv6OM2V_-418cjE1QxufiMwezheZblEUHOQElhTW_D8Nw1VTd0vXd0BKpLovBWiH7kaAL1O7w7G5RbECKAgBB0DX3001Ctb46zxszMmSwEPMMUWeL3zucReujfPXXbHZ5zGHYxPPau3KLt8GRv_1a1tCDOVtQCrx-46F4nML4AmOqx-gQ8D36ESjEhrEZV-LA5meQlGzrPCzMaMkUuOIr8XwWW1mIfJP1pJw7d3cG6AeTQ_5bGUfn1py9U5dNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az6rgefQ2RdTkBe3R9feEiEyBjJIRBFjiXpfVFSAVg0xlj6ccfcgL4Pfl59ZnxrYYlBLSH1j9iIJP9YlKD3QedddHp7HM5NDe9AhieQcLHRxxwMG59BkmoOfssIP4d8VHC70OUZ0WrX411mP4sUIOu0dRvAw4qItq3fyIeEK4JOt7-n06Ah0xUey_pdfGDA81Z8RwHcN4wf85Ci7EIDZlFG3a6XAtf5I-LZem7echLmXS36p_S7Z4XznN72Hmsup87WxIB_UHkh2ajQoNmIAE7uRAVspalEQ10MA0PqWo1XMcyfzYBYeddWr6pdFXqPioPzdkoliDFVF_gGO47Cg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=lV1N3qPvwIXhtZs67YpI8zI-QWhMe1tDrl1NqmrCQHdiqcSemToTK7EyMETd7NAIjS7z-BNuUCQ3yJzDboEKac7ku49adnrYmzukIIXoRWqGHkCrp56zWLWRBgI5Or50dUawk_e05YZv6riw2k-bx12mH5IQih9j3fA74j2qD4kTUr97Dj4oXdWfEKKWUXX0Jiy0vraHDIvTnWqqrugCU2WMBAex9XsWcCjqq_FcRhEOAYGZHR-vx8doLW3MNaqblyF9Ax1AT4qsfr5nCYDON4np1Fo0WYo6SSrLlXEZmETyOI8XRNEsjiBafdLz2K4rQ5qw903t4DeuojeHdKik8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=lV1N3qPvwIXhtZs67YpI8zI-QWhMe1tDrl1NqmrCQHdiqcSemToTK7EyMETd7NAIjS7z-BNuUCQ3yJzDboEKac7ku49adnrYmzukIIXoRWqGHkCrp56zWLWRBgI5Or50dUawk_e05YZv6riw2k-bx12mH5IQih9j3fA74j2qD4kTUr97Dj4oXdWfEKKWUXX0Jiy0vraHDIvTnWqqrugCU2WMBAex9XsWcCjqq_FcRhEOAYGZHR-vx8doLW3MNaqblyF9Ax1AT4qsfr5nCYDON4np1Fo0WYo6SSrLlXEZmETyOI8XRNEsjiBafdLz2K4rQ5qw903t4DeuojeHdKik8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9lfg7Qt_e8mGRRulBZ292Gi3AVyBsXLV_hMYJEZxo3e6AoaV1_c_PpsWStLuq5tAoFwotcYF28AyXojAnIX50TExKuzHeISOg-NPlV15NuP6WGC-anD5UxQ-lJeBOeH7CMPcR_pmKc0qe3qe6MsESq77NUh8ZQhdSjWQNVf0nwe2RK8uEMCcFAcRkfeptKB8tZLYw2mHoqrrlR6vUdBXiXSZQ8DxfLqmaSWcK0OCypFtsDV_U_bNNtKAiszsvkVHskIujGMMhwapbgqP2i0ZLZqfQVQ4yYuJbi7fw-fWiEI45J-plIo-9z-0Lb4nSp0J_eFTXgCUYZd2uL8ThSs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=CvrFbwRekwsFgUEssTShEFb383rQPmGu_ecPiPHt1PzyN5FZWCC3eD18UdHRLWowjHpDEYxXxLTgZDlak-SMgvHQF2l9-rKn_su1rS0K0tX8CnZM--GFs7PoP0MYGHXyZG2b3aeDUdQ_TrekIUJFbnrJNwiyL2AFEq9jQ8m7pbDfg78Avhnq93vsB6bToUAnn6DWAGFqx7xw1G6Xy2W-ul28te4Hv6BnS8AmPS2X_z40Vnp29-Ndih-T_bNDCTCevJMl-ZDvJx48kgxrPTza6avUM0UzATlxfiXAlW0EeD4_hYFVFmRBG_u9PDnHaFv2HhrCp78L4yzt9WxOrn9Ysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=CvrFbwRekwsFgUEssTShEFb383rQPmGu_ecPiPHt1PzyN5FZWCC3eD18UdHRLWowjHpDEYxXxLTgZDlak-SMgvHQF2l9-rKn_su1rS0K0tX8CnZM--GFs7PoP0MYGHXyZG2b3aeDUdQ_TrekIUJFbnrJNwiyL2AFEq9jQ8m7pbDfg78Avhnq93vsB6bToUAnn6DWAGFqx7xw1G6Xy2W-ul28te4Hv6BnS8AmPS2X_z40Vnp29-Ndih-T_bNDCTCevJMl-ZDvJx48kgxrPTza6avUM0UzATlxfiXAlW0EeD4_hYFVFmRBG_u9PDnHaFv2HhrCp78L4yzt9WxOrn9Ysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOh7w4Ud5GinAHQ88bbpvvAS09hweYmME9qqYjZG2wN7dW7JZdbhu3m5sJNAgN4zC2dCKO4V8BuCkG6EQPECukbTIdWcgJfyAO8fYPodPoqg1GtXV3cHcRo-vNuXMcUh4GrdE8CAwmwJAdxXEit3BcZaYI9ymCKkHGQHNq6K8S5tm4XWfROzEigDgTjU6l_fZ0hAJBeOJeB-pEsb1puPkMHkmCKINhbOSJpFh3xCLgHjpTMQU55paRiT4mMRa3eJBrQwh9bdejrESUGsovr9P1K1TZFJFXwQAnzuooXmVQnroNd-38Xz-w8onCD5CsAVn0BIh3MhoNFV4VQl3OtDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJr7_uDp0TaHBo8emJK57emZncP8B-eNb-dNezUvedYN5JgPQ2RY24yQWXmOe8mrm0VlFcia2dgpdKNGC5hubDLz0-nCHhx8ifYFjQJ71hDWF4ysxwRIgpE8MGVq3mST9u4l_EHgUeZNi-OO8cbZ7mTrFgZKaYx5g7_mZ9_G_kbK44j7S8baYRb4-A6l5wXHmffOFnDszxFxkx7EcYMoXyuCxoiw-2ILiiPJTFr7NWWdaq8_1E9l06GF7vsL6FFEYYH4XWHJdJmVjCKrqK-fJp8C-Yom88l4V9jcILqVDlUdJr5kGFLIJQMSu47N3co-Rne2APN7kfzwuyyGEbg2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=XtH4_RqvoNay_YXQ91wZPg9WhpHjOAYUfgOkOSTPtzdmxbMCi-gnyKCEkwZzY3ShvPqsG0_tHeiPROdjnzIxzecg0cnCsTM7vx5O5Dnw336C92WBzqnAWd-MSPYunNqCMYMutVrJT1xQETWtVwl7spDG4VYCX-58SuAX5MIaVWdPNkoIXl0stsfETK4tJ4i5liIR0SzDPv6zSjNEghZZH5OgiXBrFFdO6IemGhN0GMwlhQY-M6F-9baPoxTzXiBCM-clkZLoZ_vYOHbpwraODbabxDNJKOSp97Xd-O7yosyTiAdK4ttB-sA2In2aKg5xj6wsLWmmM4I6twWo5hEflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=XtH4_RqvoNay_YXQ91wZPg9WhpHjOAYUfgOkOSTPtzdmxbMCi-gnyKCEkwZzY3ShvPqsG0_tHeiPROdjnzIxzecg0cnCsTM7vx5O5Dnw336C92WBzqnAWd-MSPYunNqCMYMutVrJT1xQETWtVwl7spDG4VYCX-58SuAX5MIaVWdPNkoIXl0stsfETK4tJ4i5liIR0SzDPv6zSjNEghZZH5OgiXBrFFdO6IemGhN0GMwlhQY-M6F-9baPoxTzXiBCM-clkZLoZ_vYOHbpwraODbabxDNJKOSp97Xd-O7yosyTiAdK4ttB-sA2In2aKg5xj6wsLWmmM4I6twWo5hEflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=FJtOP_UZklsQy2I0e6xBM2GnN74MZtCphTNIevUc9PqnH1msPxmfwz524TQekVRLgn7GHQvhU8htEfxO-Jb7JVO14G9Y6n4s7td4inDmnphMQM04Jz9lZ4UOZ59X-BDwwKhCL9drJTpqwAUq9f5XBVwQ-9mpAx7spkhM1eF_maymW4RmGATHDh8rDAXmPT1WS6O8emD8qPN6eONo9dh3VUllVrKXU1SF9cj_ufHbuu4AZH20zq8VtIxA7SlHKXSSx9-G-uJbQ0uLJ6-Spvxobdvh2tnqLzv5Z8pCFxBpTB-XnM8RN2sbcCeqE5gCt8knXMlPjfcBxQcgTHiRiKt8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=FJtOP_UZklsQy2I0e6xBM2GnN74MZtCphTNIevUc9PqnH1msPxmfwz524TQekVRLgn7GHQvhU8htEfxO-Jb7JVO14G9Y6n4s7td4inDmnphMQM04Jz9lZ4UOZ59X-BDwwKhCL9drJTpqwAUq9f5XBVwQ-9mpAx7spkhM1eF_maymW4RmGATHDh8rDAXmPT1WS6O8emD8qPN6eONo9dh3VUllVrKXU1SF9cj_ufHbuu4AZH20zq8VtIxA7SlHKXSSx9-G-uJbQ0uLJ6-Spvxobdvh2tnqLzv5Z8pCFxBpTB-XnM8RN2sbcCeqE5gCt8knXMlPjfcBxQcgTHiRiKt8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCiUk9RndqkHupbcJfBn3yyTYSh_gGaJcUaFaYVOWD3d7UQYM4yfpdAhEBaWnMJadQQwKHBk1CcGI05D2q9cvSF82F8MTQti9v_ib2Xdldh1c44Os9mNG03TVK61AKpeKKhyfoddXiscNJ2FqyOMP7AOESv1ME4p9sXLDbuPd7y6phggtQxOCSaTgy3cpKfSmaDY5zJITqswg-vx2PSvePn7CYmEQjxxIC7aeE41RphHub4zrMr7DkLryFzezK5qVgt3JlsTLpmj3khS8DxMlzvQgeWKhaWah6RAURNdwwAofjDWbJiBOm7uxzdYdhGAonmhUuQMhIFdJEYl129JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9q2WiWJ7BbL3bqUdM2AuSg0T6EL10mbouioSb_lwPLBcIK7bHpn2vpTLy0jdmpqnP1lFOYv3mDaQnAV7ajqkMe-ar-XzEp6AI54f0Gmi-RLyTP-MVS1RDdeG_Bby0haL5_R7aVruLXTbwKZsI3IwhHTzKOx6v4w_79m2pjTtr0pKKkYyoPxC-qtuqzaCtlFRm5a5VKrAhinjZ2fa65vFCtk8u8PHri6Hld1HQRqQm_pHc1I4WVAxv4GZf8vbAm-sNrDX4St_Xrr6nJnaHHLtvbes4k1Jw3Ljp8PX8qq8d5gD4mtf_0JClF7fg4Y3N6JLgqFovz0Zh3fIIJy-wpFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
