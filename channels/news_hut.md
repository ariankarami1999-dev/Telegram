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
<img src="https://cdn4.telesco.pe/file/KVJmVVMvGxE_cIvCwsou34InN-tKimzrVg4jeze_6Z3DB2NGfPLzHAPoSlndf3vfKL6zIXWCHfIPh3QFeeI_yyGC6N3jB0_gh1rVdnS3EmufVZ4K2cVCK4CSJR5mUtLGZe_Uw4rT4KqkX8WJrEr5Ol7s5drh4jAh_odA9jJnekMGlNae0q9N4euogr3yTkAlg2Q7R6ZCC5pnYjhLLHjD26WnDKwUs0jirs_l0PpWrRxCaD1imNcDsfnHcqeSbhJLjdz629xi1hgDgx7mFBzq9uxcadwrIEJnDp_m8C-3q22Td0X7lj74pwAtH-GndMkyhgcDkMwJu8UbGyJYRZpmKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 08:53:36</div>
<hr>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=WlCmUl4pjBnlJX2Tp4TotCghqP1FRb-dPvxCyS_7xle1v58OX4_Vc6nbdBckFeqFUTQFaoqzhVTu-41TU-8a283NPLYDGsfBztDIie4xYzk8Oc6V2v4a5m_6rlC35EWq1dZgWn8xAU68k2g0LU2jwWDNomkCQbEEIHyqFUZ3-2tlIz2gOwhqozbyryehqBCIm20vWeaOZeXStZTgVDkPx4hS_vJV22H7W02F47AZfb5hwYdkV0Ws2JlCAN8jwVQla0NbDJA7-mzMnvwxtrDcSzeiXX9YYX0-KE31NKfhugxhKz_mjddy_yHT96s6PDc7G5iO9G-EvqIu9fL97nHvYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=BofmLe1kvbMc_bvBoMrA8X7eZ_o_Umk53KoHj_U16QjNPX-dx52NI0Jq5YfO_oBwvR1Uqg3w9NwUQYzUYg7-7V4b4EyHzbz_sTz2UCZk3Nsl-bQLI99aqY5O2AUBpRAPzKYSqp5XVe6S6sdZC6NBUBUyjMOHLRIr-NSN04WFXTs_KyX4DeWgv95dLKbeNl9L8L-3dg-4CB_WQ_P6dfhnK_Da7r2wI2tC-5Ba5jdOWKTXMbJPYi72a9g9wOFqqAA4sWfgbleL5Navjtygc1lVKXdhuU11I9jKosZXeMCQBhhDPoGJpElZe7VwlqBAjvuAcIJQHPO1SPdpdUUq-t_Ukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrOY9lWAR46FQimYdFuFuN6sPH9hJSMuNdI8haVYDzgAfwHxhG3K9SukDpLf389mEZ8gJKO96_AxLXPKl4v-ehlNqbSu26qDxB0y4yq9dcNP_VdgTrX57juUL2RR5h002BuLYfCl4AUYXvWJmXgyLKcqV5Fwl0iMSN2bi_lAkB1v9C6AGvH5h-Y5_QqTRg7fiaKLsQ49RpAUZL-bUR-E6mIU6oE1BSmX9VUAz7UB-cpqk1GVPi83uL2QDZVOLUZPNCXDNFWoGn7YLOqB0kSz_xWfnT4H0sMYYJqeH5tZa-BBl1PkvmrL89uTH8TtYNTLKg8Dvnct40TNopw_GmUEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjYjFGnGC49Hw0a8CusGDqcAoPT8AJo1Ey3th4Ej7T0pBLGXygL0nN0u5dDjF7_FABud29XvCMbx-ya0TIzGaSemdImQ_dalvVqp-pzK63_XVWbbaad3WwaMfsLStYSpffcAxK7ovkP2pDjYmtggYt35ku0tnkel7jM8rhX0ThqhsyjUTmbVzG0g0_nEFvdRNMdL2VxBBt5PGYiONDdYSSDjcouqnh98qEid-5beqfs9gglQRQF4pIWg0L7_S71-_KEaRaBR5ycRqn-l4Ylgk-DGB2RpMiUx11rQrj3DPCHGHwmbX_6cK9-YmkaayAjyAgoymC7xBqwNANkmHnfalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Tn8AsIflYbJyNin_DihPWP1CoGyxpynEVIKT46etUaQirs9yWc1fDarZjtCF_-4gU4sgJx9RbvQSFxJvr9Q4pOWQZiolg9rf4ReVPvaDLhJoMducmWKVJ0Ps0D05MeIDq_Yedrat-plAOWTs_XwOwAXlQc0zRMpNoWkEAelmd8WL9VyPWXzGjWVphxSqrQ4EYeaeYOQ9s65WnCFkjQJWDM-r36386M8bqd1SYvIkQkWWsX1BvrgwFWuDfUEg73WHkgChYMXwKxQRYf4tk2zYtiaMkLke4lSbIg9hRQ1DEg0xl64mTMvAeb9fgo5KQo3DV63o7Rwx5ZWUc9gy2g98SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2-m1rfZwPXJfDZ5jBwP1N76mCWCdXfy2KLov8CNYLplyEydn7uzQ9RCbgMmDI4hyPGTjDI7eZeFR6gzOuZ2OJcvYhARFVn1Q-Oc4Nav_dTta3hndyjqNAmF9f_k-LfAwLxEeutA20QO8vrsb0F7e7DKrJBK_rBRDiMjciRoM9PcD2T8evpBHrX06oybCQJowfTtqv0fs6l848DFpNA7_VKaBAcP5cM4Kkft2wWfK1Aj8TDatC4FLBRpOq8ZeUoIY5QZvwiXqedpG8aMZSKz1wo5IgsVAUuF324_RRWG6MpGkIZ1Y0cNVn7sVwReHpkf5LD1hH-L-uwp_uVmnF6Hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=OM3wLehK32NL9cH7mxvTc3OfPMZsKUvdqy8vt_5GTVddor0cwzfcavEtKZIRzVrcIQGyKb_YPOZF64kcK_k6RUJsZUOPJK4GefFd24iUeIrkU9fKmONoVPscbyfHPUX6CTI8S4AtzkOw250CJYM5PJC_CdQChZx7tcWNKZbCmvEKphCo1ZoJTM3KD62MudV1hpU2UwUK29qc2vOcgy9ezqrgu6XsIdIgxQkDnDhBLUT5SgnfIX57hVyzqb8OYU9dYPkSkBDbaAc4G7QUQ_rNn87x408gV6aPlsBcuVOwu4jjR1j1alC09qDANuvvAhYWxgxGER3FfdnHEPhunw5Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=OM3wLehK32NL9cH7mxvTc3OfPMZsKUvdqy8vt_5GTVddor0cwzfcavEtKZIRzVrcIQGyKb_YPOZF64kcK_k6RUJsZUOPJK4GefFd24iUeIrkU9fKmONoVPscbyfHPUX6CTI8S4AtzkOw250CJYM5PJC_CdQChZx7tcWNKZbCmvEKphCo1ZoJTM3KD62MudV1hpU2UwUK29qc2vOcgy9ezqrgu6XsIdIgxQkDnDhBLUT5SgnfIX57hVyzqb8OYU9dYPkSkBDbaAc4G7QUQ_rNn87x408gV6aPlsBcuVOwu4jjR1j1alC09qDANuvvAhYWxgxGER3FfdnHEPhunw5Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAXLkpXxXHHtUOo-wyL88_Q2FEJ7DMHZTDsNgaibsXufjIsHrBtmND865ui3xaT0Xccg2DxoWXLv2SP-sdvGPr8d5p3QX_OnzaiBPQ9quep5J-VmAeU4G-2RN3IRca_lBB3zafZikXsThhbvtJzSifU9900AgPjJ0-zD6PfRhdw9OqFWvSWoJSzqSwdI08rl3PlAaKWmg38F2XMHX4dvZRgTrB1Lzb992AGcYfdNacP0AXGrZH3g8BDOIPj4FCC7VZlzrro7UiR444c08aESssJj-XLcywDKKl4h6XIlx2MI5LsSxbXNKYZH0INPnCeTfeRFDbwkIPhDkZZ_6vs3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qG1z0C4DLELw528v3rviRdvWpmPopzjMqKjeRZFdmjuwKtRUldrM4pUoHZKWvI1d-lhUpCCMckwI_4liw0BRCaWOyvZw0xKATvUWUAF1mkLM_mKXe22XvDAa4ZI79AV_8uSe-tTqSysIYtU-0RzrB3Gv2bK3J4VQg6iWxAkvQYCkcdmUtuHPsUvnKTiqvL2uPAFpE8BLhrzLsSCXTImoNba61gIvA_-HMzkX7EWJ3nGXoNR1w09jHJVPx4YqYe_QW5XnIq40UduySFom86V7O5vAjBRuUBf1YwsZZC5PD4puZN-mYg41cKOI2nIn9vechLTQ5S0j9ZzKOUf0iSu-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qG1z0C4DLELw528v3rviRdvWpmPopzjMqKjeRZFdmjuwKtRUldrM4pUoHZKWvI1d-lhUpCCMckwI_4liw0BRCaWOyvZw0xKATvUWUAF1mkLM_mKXe22XvDAa4ZI79AV_8uSe-tTqSysIYtU-0RzrB3Gv2bK3J4VQg6iWxAkvQYCkcdmUtuHPsUvnKTiqvL2uPAFpE8BLhrzLsSCXTImoNba61gIvA_-HMzkX7EWJ3nGXoNR1w09jHJVPx4YqYe_QW5XnIq40UduySFom86V7O5vAjBRuUBf1YwsZZC5PD4puZN-mYg41cKOI2nIn9vechLTQ5S0j9ZzKOUf0iSu-cjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=uBPkQABiYy8MOXqTUhYmaymdJDAa6tTXiDVR22pzcnmhcpgu2gDLvGmoy3_ne3IPomA9uFycSMqMftdkatb-Dkp8tyd0ZokivYaZ_1B7ShmLwKdoU_nXUD5C6yw-8LiWmbWstcfE4TEO0vJW-DMnOz9agFyeRer9k1MSLtVQn-mq2BFaAWTHM33hKpawzkFWQXqmDcOZiAJ73-W9uYWA4axXeUNKCCg5jD3F2jTmykQuK9HTD8_dBQNcOO8UPQFrhiQOX3EtU8SgJ3Zg46Nmzvf7zTzLC9tuz7uVD3QyXqFCiv1c5GhVEcwSdf7WUPE1RRuNeSOHKjTbD7jiujvfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=uBPkQABiYy8MOXqTUhYmaymdJDAa6tTXiDVR22pzcnmhcpgu2gDLvGmoy3_ne3IPomA9uFycSMqMftdkatb-Dkp8tyd0ZokivYaZ_1B7ShmLwKdoU_nXUD5C6yw-8LiWmbWstcfE4TEO0vJW-DMnOz9agFyeRer9k1MSLtVQn-mq2BFaAWTHM33hKpawzkFWQXqmDcOZiAJ73-W9uYWA4axXeUNKCCg5jD3F2jTmykQuK9HTD8_dBQNcOO8UPQFrhiQOX3EtU8SgJ3Zg46Nmzvf7zTzLC9tuz7uVD3QyXqFCiv1c5GhVEcwSdf7WUPE1RRuNeSOHKjTbD7jiujvfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qv38W8J6N36sBSWLRO224qrgDJtykUzQnAm_KuGsR5VvQxLII41IRbHwxoVuqOfm1FlK1Cwvw2rPPEq6rNIE-hsPycR-Tk9IbagVs-qBchkCjJx1KGTmKq0VJ8OxoRcKStowc6wkfX18IRIrypHIU-6F8-HBmjIFqDY8PTunV6dOOLVTDbDmNt_f9ko4YFJJBAjA2T0fKiHYGDW_u929jSIly0t9sWHeZ4A5VMXo4IhKvOrIN6JgA0YvMTBYNZyJ11sQhYdSfyCpnCOFr4em9hlVanLQCeu_hip6l1uAkx6I23pNHibJU4CGk0shjyHua5STbSxmsDyMRN_9EpY2YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=qv38W8J6N36sBSWLRO224qrgDJtykUzQnAm_KuGsR5VvQxLII41IRbHwxoVuqOfm1FlK1Cwvw2rPPEq6rNIE-hsPycR-Tk9IbagVs-qBchkCjJx1KGTmKq0VJ8OxoRcKStowc6wkfX18IRIrypHIU-6F8-HBmjIFqDY8PTunV6dOOLVTDbDmNt_f9ko4YFJJBAjA2T0fKiHYGDW_u929jSIly0t9sWHeZ4A5VMXo4IhKvOrIN6JgA0YvMTBYNZyJ11sQhYdSfyCpnCOFr4em9hlVanLQCeu_hip6l1uAkx6I23pNHibJU4CGk0shjyHua5STbSxmsDyMRN_9EpY2YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Oj_P81WtOVAVy8BXdyhV4ZgQaSa-M1gt74O2suNebcfvo0JNTFUL23TXJ5vDstDiRHSHx-b0EhEmM3gXpk_J7RgHHg6wRk9mFVkmeddQLSmec-yKiLWUslAl-6EWil4U3AOAEhOvf31Qo9o0WWzdog4be5PwUcGus-Acq0fgCCiTYOgbHwrt-8mvrgk_AzSP-haVCjpTtu9TGvv0iZzGRUePY0FDzX7Aj0IALsoXW0DHlw2og92_6lntMvDSf5z49-4Zho0RVSIj7XmKuAy9isjue3reUedklL_CDn7gS67-FF1g_y4tMPnBr94XCGxcoGmxXJO-ZfrO2v7Sb4_QlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Oj_P81WtOVAVy8BXdyhV4ZgQaSa-M1gt74O2suNebcfvo0JNTFUL23TXJ5vDstDiRHSHx-b0EhEmM3gXpk_J7RgHHg6wRk9mFVkmeddQLSmec-yKiLWUslAl-6EWil4U3AOAEhOvf31Qo9o0WWzdog4be5PwUcGus-Acq0fgCCiTYOgbHwrt-8mvrgk_AzSP-haVCjpTtu9TGvv0iZzGRUePY0FDzX7Aj0IALsoXW0DHlw2og92_6lntMvDSf5z49-4Zho0RVSIj7XmKuAy9isjue3reUedklL_CDn7gS67-FF1g_y4tMPnBr94XCGxcoGmxXJO-ZfrO2v7Sb4_QlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=jSSjzDBksvlELh3HSvXS3HheSY18Dl3FGGndeVImFY-8FN0KVxovTjrq73iHzejgVt0jR-m6rht9wQE8LQetdtW2PPRb1fpUe7SU7F8LFIcxGmDwl9q0jVsbq0NA7eEKsEt0gmRuaDNR-rA7LZcGsokio8jMLblxkzEQG3Rj4zhDR5SJ3_IWHi6xIOnUbBspQ2FeoxAA70UOTC9neIqT25YqRHJs6J1OnQ5t88S3y-YcsU3QKz3dflQL13ZMq92Wsl5P6C7RUQ9Q6xpXCpXmqkvkoWmK3RZzzydb4Fy7MDs4N2OREqcrD4Ipn2pF7xSNfPfbcYVrHkFy71UofMIPtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=jSSjzDBksvlELh3HSvXS3HheSY18Dl3FGGndeVImFY-8FN0KVxovTjrq73iHzejgVt0jR-m6rht9wQE8LQetdtW2PPRb1fpUe7SU7F8LFIcxGmDwl9q0jVsbq0NA7eEKsEt0gmRuaDNR-rA7LZcGsokio8jMLblxkzEQG3Rj4zhDR5SJ3_IWHi6xIOnUbBspQ2FeoxAA70UOTC9neIqT25YqRHJs6J1OnQ5t88S3y-YcsU3QKz3dflQL13ZMq92Wsl5P6C7RUQ9Q6xpXCpXmqkvkoWmK3RZzzydb4Fy7MDs4N2OREqcrD4Ipn2pF7xSNfPfbcYVrHkFy71UofMIPtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=Q-im6TuXoInUoYoBcfQIkM7mKOWGbduV-kr1YqDfDLj8ZVunuDLTcEAf9OWCOOYwyd3Ybz2ALhX5c6TlmhAu-P9QVrQwNjpkJ13ZbTWCyk-dUjNTRW7ICmPAw5UhyaXI_vmojDYHzQBUNvb3-ktGmpLmyL_8jY62tzH7yDHpbAN6C0tP1zBRr_9fAM77x8IXK3EsOg1ZO3Dn5sqn9HaGpgcp6mekUuta0Z0E7AEstrGojYkZ3U3Hd4uImFen-e3ssur0cbv-PxjGm8qIsC0u9t38pFLP89p5Fyr6rTgv4D8gihmwupSLE9pwaJqnBRat1sHAfLV76RDl6OitShSU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=Q-im6TuXoInUoYoBcfQIkM7mKOWGbduV-kr1YqDfDLj8ZVunuDLTcEAf9OWCOOYwyd3Ybz2ALhX5c6TlmhAu-P9QVrQwNjpkJ13ZbTWCyk-dUjNTRW7ICmPAw5UhyaXI_vmojDYHzQBUNvb3-ktGmpLmyL_8jY62tzH7yDHpbAN6C0tP1zBRr_9fAM77x8IXK3EsOg1ZO3Dn5sqn9HaGpgcp6mekUuta0Z0E7AEstrGojYkZ3U3Hd4uImFen-e3ssur0cbv-PxjGm8qIsC0u9t38pFLP89p5Fyr6rTgv4D8gihmwupSLE9pwaJqnBRat1sHAfLV76RDl6OitShSU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=hjyfN_ljkiXT4SSgpohj5Yzj46IDaRuJLHy0IEzrrqJZz8XuAQdixdUi2DMsrYJAUN1H7FM5lLb0lXyXcbbvKyA7zU_Rv5i3W4W73wzM-yuFclsaOYJx3a9jCW2n05QSdMVoXM4ODhVUZblgGEvnKRxOnDQDVZ_ErHSahSn_o8bxpmuxkKhG6e8BqvuzRloYtOB2b3z8VwXPZ5QgOzZh7l1izFN4EIDPpR6fRo8IoO7lZIahBol2o-SG55tECW8cIWMw7AhU9lVi4Nwe0cy_JQCoPjOIzA_RXO5RIZn7ZxXwtqcUVUpwcjIQI4MHUUfws_pY21EVjK2i44JnF0fxOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=hjyfN_ljkiXT4SSgpohj5Yzj46IDaRuJLHy0IEzrrqJZz8XuAQdixdUi2DMsrYJAUN1H7FM5lLb0lXyXcbbvKyA7zU_Rv5i3W4W73wzM-yuFclsaOYJx3a9jCW2n05QSdMVoXM4ODhVUZblgGEvnKRxOnDQDVZ_ErHSahSn_o8bxpmuxkKhG6e8BqvuzRloYtOB2b3z8VwXPZ5QgOzZh7l1izFN4EIDPpR6fRo8IoO7lZIahBol2o-SG55tECW8cIWMw7AhU9lVi4Nwe0cy_JQCoPjOIzA_RXO5RIZn7ZxXwtqcUVUpwcjIQI4MHUUfws_pY21EVjK2i44JnF0fxOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72076">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=JeUZIrpaK8vJ-zINo0gaoob2r3NQDEcHjv5-xvGEwlrioMeYlpjj4-5tPMU7QkHaNJmcACg-7-Px7tF5ml23H9GtIRat9Tvih_rP7Vy9Kt3ajqPQpNlb6ku4dUdvosohTVmdmjt8nNfNFpFnKTcHt5ISSb8lWVDzzTiW9ktBwr-rPoqfzM3Ducowcwibi90IVI8hGvbNMTETkOA8frOLotaodhmg-qayxkB8yhDEernGncc9k-R7uEzybNQ9AiyhbUElc6DGZnOfa76vhWIhD9WYlazqJRCmjuD6VQpQIDvmHuh9hOXmXmtp7VSO54njHhfqM5vHqNmLQzVoWXdatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=JeUZIrpaK8vJ-zINo0gaoob2r3NQDEcHjv5-xvGEwlrioMeYlpjj4-5tPMU7QkHaNJmcACg-7-Px7tF5ml23H9GtIRat9Tvih_rP7Vy9Kt3ajqPQpNlb6ku4dUdvosohTVmdmjt8nNfNFpFnKTcHt5ISSb8lWVDzzTiW9ktBwr-rPoqfzM3Ducowcwibi90IVI8hGvbNMTETkOA8frOLotaodhmg-qayxkB8yhDEernGncc9k-R7uEzybNQ9AiyhbUElc6DGZnOfa76vhWIhD9WYlazqJRCmjuD6VQpQIDvmHuh9hOXmXmtp7VSO54njHhfqM5vHqNmLQzVoWXdatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیداری بسیار خوب و سازنده داشتند. دیدار دیگری نیز برای آینده‌ای بسیار نزدیک برنامه‌ریزی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72076" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72075">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847d96020.mp4?token=DFZv5iQ78kzdLMj5nIliqDxmv9MvKNXZpSGJumy1xXpEQPuj2WRcapy2TqjnrPwzbxcP2fTZI9R0ZHvhBPojPoj4AVG79A1NEh0IQaKwH9aUp6uYh_CKwxqOHs2gna442OQspiql4pP-hLrfzU50QOI1iPVm69hZpUAoTT_SrxGHJk6z3Hxqe7whtnY1Whm5Ko0mBut0g4QjD8d7TykZ7Sm-scqVQnDEVN1DlSDt3SYknJYOxuKwloNLc93UCya9N-OVt9CLjX0srC15wIOZ89Lm-ZHK6CybB5799p4djygpGOEDtgVuBCEOY9OSqr5Bhoso7nOBC6nbKPWYH5Kd1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847d96020.mp4?token=DFZv5iQ78kzdLMj5nIliqDxmv9MvKNXZpSGJumy1xXpEQPuj2WRcapy2TqjnrPwzbxcP2fTZI9R0ZHvhBPojPoj4AVG79A1NEh0IQaKwH9aUp6uYh_CKwxqOHs2gna442OQspiql4pP-hLrfzU50QOI1iPVm69hZpUAoTT_SrxGHJk6z3Hxqe7whtnY1Whm5Ko0mBut0g4QjD8d7TykZ7Sm-scqVQnDEVN1DlSDt3SYknJYOxuKwloNLc93UCya9N-OVt9CLjX0srC15wIOZ89Lm-ZHK6CybB5799p4djygpGOEDtgVuBCEOY9OSqr5Bhoso7nOBC6nbKPWYH5Kd1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز، حدود یک ساعت پیش، گفتگویی انجام شد. گفتگو بسیار خوب پیش رفت و یک ساعت پیش به پایان رسید.
این نشستی بود که سه ساعت به طول انجامید.
مسئله، عظمت — یا عظمتِ بالقوه — و یا نابودی است.
در یک حالت، صحبت از نابودی است؛ و گزینه دیگر، عظمتِ بالقوه است. [ایران] می‌تواند کشوری بزرگ باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72075" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72074">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=egX7S5DB1ExaPc2rHm4bXWHFJpFLcRLfEpTvklg06cl6_fVDx5Fh17yvN1rnvjOJYoaqIwQvWBE_WykvKcUXYTHVQdWl9MpdmfHHf28HMDTxN0Z_ojMssgwQrfW3UnC5wafcmTMEpAFL6DxK_uLq6wFEOylvtQH2LtsdXZqUp-CvAV4bdI2DKvQftPbwFFAhX85P4F84SH4iDry-9V3QceranflAlFd7Pk8i946Q4aHxD1H-kFJBOiTI2xRWe3vAplLYZK60bvExWSuaIZ5_7VoJ2oNXNPbQV72ssq3Foi_YQEV4mdu7KrHOxPyhDANsKEasTWdty7s2xPmYtFeWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=egX7S5DB1ExaPc2rHm4bXWHFJpFLcRLfEpTvklg06cl6_fVDx5Fh17yvN1rnvjOJYoaqIwQvWBE_WykvKcUXYTHVQdWl9MpdmfHHf28HMDTxN0Z_ojMssgwQrfW3UnC5wafcmTMEpAFL6DxK_uLq6wFEOylvtQH2LtsdXZqUp-CvAV4bdI2DKvQftPbwFFAhX85P4F84SH4iDry-9V3QceranflAlFd7Pk8i946Q4aHxD1H-kFJBOiTI2xRWe3vAplLYZK60bvExWSuaIZ5_7VoJ2oNXNPbQV72ssq3Foi_YQEV4mdu7KrHOxPyhDANsKEasTWdty7s2xPmYtFeWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گفته خانم دکتر؛
مردهایی که به‌طور مداوم رابطه جنسی دارن، طول عمرشون تا 50 درصد افزایش پیدا می‌کنه و همچنین خطر ابتلا به بیماری‌های قلبی هم تا 45 درصد کاهش پیدا می‌کنه.
-در زنان هم باعث میشه سرطان سینه و کیست تخمدان نگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72074" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72073">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=SBbSLJI8rKS-2TCaTjvu_DN_poMfhgHFj8t4di9WpxW9LEsfuAlvaiYgTyYHNQfOKFtr-5CCJ53jX4KQ9cNJBtqCwPkAHP--rZLmkR3yV7RuqDOOxUEdOb8OVH8vGg1yNLJJIF-uMQ6gnkWCxmYlJl9uGKNupIq2Wx7R-CdvssoC-BQpIeU6EzYikJ3Ns8fIN7kUV-5G75RDltOb3T8sxZoGjU-ezEx6bCkdAEP84al9mhmcD0XFLGKSUvoNlQNTTKeqOTYw6qfgjbLaissnZNLhu_3tAOMi4tsqz9YD1hn2xFZeaawPP9XIaA3NgUmnMGv5uFig0q7lVaTqkhzb9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=SBbSLJI8rKS-2TCaTjvu_DN_poMfhgHFj8t4di9WpxW9LEsfuAlvaiYgTyYHNQfOKFtr-5CCJ53jX4KQ9cNJBtqCwPkAHP--rZLmkR3yV7RuqDOOxUEdOb8OVH8vGg1yNLJJIF-uMQ6gnkWCxmYlJl9uGKNupIq2Wx7R-CdvssoC-BQpIeU6EzYikJ3Ns8fIN7kUV-5G75RDltOb3T8sxZoGjU-ezEx6bCkdAEP84al9mhmcD0XFLGKSUvoNlQNTTKeqOTYw6qfgjbLaissnZNLhu_3tAOMi4tsqz9YD1hn2xFZeaawPP9XIaA3NgUmnMGv5uFig0q7lVaTqkhzb9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بانوی اول ما کجاست؟ یک جایی همین اطراف است.
ملانیا:
👋
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72073" target="_blank">📅 20:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72072">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اکسیوس:
چند کشور عربی در تلاش‌اند زمینه برگزاری یک دیدار سطح‌بالا میان دونالد ترامپ و مقام‌های ایرانی را در حاشیه مجمع عمومی سازمان ملل در نیویورک فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72072" target="_blank">📅 20:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72067">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=qQKuMoVss8wHA75JOhz5U9zO1We8TIkfStGXUNGdEwoqBsPDkM6K6Kb39nrj-7zEQXMWqHfT8jfVwUnHpfhRBdGO4gTzek1dTOaG44fo2yIf3Yl5s3BOa2orRTy7cIxCnhAqGSkluDY8CAEXOl6T7_HquprHHxhEKdqFrDBs2khxuk7JrrSV149HadmzxTLawcPAfJN-w5PVcLJt7rNamZvjCaUb9Ri0sIOowtUj5a0p8ALQ4IeET7iF77Sodltr44mv39KneZy5MPcCStNwdp7Hal30kE5DIbiEoNcMv9JGDUM1FKuxPwwrznpJtWFSIW3DoNcjZoauOZt0EAKDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=qQKuMoVss8wHA75JOhz5U9zO1We8TIkfStGXUNGdEwoqBsPDkM6K6Kb39nrj-7zEQXMWqHfT8jfVwUnHpfhRBdGO4gTzek1dTOaG44fo2yIf3Yl5s3BOa2orRTy7cIxCnhAqGSkluDY8CAEXOl6T7_HquprHHxhEKdqFrDBs2khxuk7JrrSV149HadmzxTLawcPAfJN-w5PVcLJt7rNamZvjCaUb9Ri0sIOowtUj5a0p8ALQ4IeET7iF77Sodltr44mv39KneZy5MPcCStNwdp7Hal30kE5DIbiEoNcMv9JGDUM1FKuxPwwrznpJtWFSIW3DoNcjZoauOZt0EAKDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در پایانه لجستیکی شرکت «نووا پوشتا» (Nova Poshta) در حومه روستای اوساتوو (Usatovo) در منطقه اودسا اوکراین، پس از حمله موشکی.
علاوه بر این، ممکن است انبارهای متعلق به شرکت‌های دیگر در آن نزدیکی نیز دچار حریق شده باشند؛ چرا که مجموعه‌ای کامل از انبارها در آن منطقه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72067" target="_blank">📅 20:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72066">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMsq8NYHcmFgBd4L00ZV08IkqxVzenm5jaG_z9lO7fDHr0VEJIsS71GI26ascQ5GnchsiQhL16iqNIuppYzdWlatVsX4ynYb8LUbmwABGc3AwriXY10x4nWzOpR_4zd1NEwC5uPXIezJuZiduPiH71d4vqpN5UlvCTriaQz9Ssjtea3r-DIabFT9SXiE6jQL5wvUx5SSU-4O6aFdD95ZrH90arEV7dfX1f1w2GmamH07cZ9ybPOndkzgF3l84Pgr7nw61hHvwlrWwmqhXAw3Mkdiay-8IufvPF5FFth1vCnDsnzuEeFvwmeSgl8RpTsVVoOQ8KOSh7CRHJdaQB5UBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی وارد نیویورک شده است؛ ایشان قرار است در «اجلاس کونکوردیا» سخنرانی کرده و دیدارهای خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد داشته باشد.
با این حساب دونالد ترامپ، بنیامین نتانیاهو، مسعود پزشکیان و شاهزاده رضاپهلوی هم‌زمان توی نیویورک هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72066" target="_blank">📅 19:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72065">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد؛
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از مجازی شدن فعالیت آموزشی تمامی مدارس استان در همه مقاطع تحصیلی از شنبه به مدت دو هفته، با هدف صیانت از سلامت دانش‌آموزان و حفظ کیفیت فرآیند آموزشی خبر داد!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72065" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72064">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72064" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=K5G7kKOEMd_Ea9uqA3rzl3RbtVgGc6S-0ajuO_CPON-ZFvIXXjn8-w9uGP6_HpvsOetvTadxY78kyuO1DtmYKA1Mz5w57hxIh0zu9y1kWfGrDYq2AIpzDbi_TwYWzJzTAoS4gQBeRewkaFGEcQaonHRHeuRY5D9J6qTVP4F0_3gS6TGhIcwSEMhSwFh46nQUnAUGhU1Wmse6N7k081n39u0f2kDlcDUAnZF1aMH-HyvvmSHWYaiPoFI6sCsN0eV0A2EZyxUxbrRZ33SSuF4Jotw4trWM-1ntO2lCyQWPkNJ_idy6G7rPi3eS8xzYtAYNFyS80ZnXN7AYsYgfz2NOcnnuy0cEUgq0PR5YUSg3pz1Q1sCDCcbgl-ZI3xdYfgPFm4U-AYvQep8lYGjOmBCrI0ofCaY6GnR_lqG2KATI-Ayuo0rRHvrqrVrSfa1IeMORlhPu3M5cuzZ2VngjO__VCQjt_rD25axmvffcdj9dg2hbrC_299ytWumE0xjMW1M9zlOtd8Hcowy9tSVpBRQK2By3mwakZEVPi9ACWhNe8YUOejn_a4UgGq2OvlkpxKb_YC0Ha_6LSquv1omnpoUdlVeSzSUtkdWE4KxnMcFqvjY6-SKrw0co2y4-kYYsZVGD7NTkmznBbZf8CRld5sncPrxLDrwqPKOPmzBEmv1cxBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=K5G7kKOEMd_Ea9uqA3rzl3RbtVgGc6S-0ajuO_CPON-ZFvIXXjn8-w9uGP6_HpvsOetvTadxY78kyuO1DtmYKA1Mz5w57hxIh0zu9y1kWfGrDYq2AIpzDbi_TwYWzJzTAoS4gQBeRewkaFGEcQaonHRHeuRY5D9J6qTVP4F0_3gS6TGhIcwSEMhSwFh46nQUnAUGhU1Wmse6N7k081n39u0f2kDlcDUAnZF1aMH-HyvvmSHWYaiPoFI6sCsN0eV0A2EZyxUxbrRZ33SSuF4Jotw4trWM-1ntO2lCyQWPkNJ_idy6G7rPi3eS8xzYtAYNFyS80ZnXN7AYsYgfz2NOcnnuy0cEUgq0PR5YUSg3pz1Q1sCDCcbgl-ZI3xdYfgPFm4U-AYvQep8lYGjOmBCrI0ofCaY6GnR_lqG2KATI-Ayuo0rRHvrqrVrSfa1IeMORlhPu3M5cuzZ2VngjO__VCQjt_rD25axmvffcdj9dg2hbrC_299ytWumE0xjMW1M9zlOtd8Hcowy9tSVpBRQK2By3mwakZEVPi9ACWhNe8YUOejn_a4UgGq2OvlkpxKb_YC0Ha_6LSquv1omnpoUdlVeSzSUtkdWE4KxnMcFqvjY6-SKrw0co2y4-kYYsZVGD7NTkmznBbZf8CRld5sncPrxLDrwqPKOPmzBEmv1cxBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
هر کس در حوزه هوش مصنوعی پیروز شود — باید این نکته را به خاطر داشته باشید — و حالا می‌گویم هر کس در حوزه «هوش برتر» (SI) پیروز شود، برنده نهایی است.
آن‌ها همان گروهی هستند که پیروز می‌شوند.
و ما در حال حاضر با اختلاف زیادی نسبت به چین و سایر کشورها پیشتاز هستیم. ما این وضعیت را حفظ خواهیم کرد؛ مسیری بسیار مستقیم و موضعی بسیار قدرتمند را در پیش خواهیم گرفت.
من نمی‌خواهم مانع رشد پدیده‌ای شوم که ابعاد آن از انقلاب صنعتی هم فراتر خواهد رفت.
بسیاری می‌گویند این تحول حتی از انقلاب صنعتی یا خودِ اینترنت هم بزرگ‌تر خواهد بود. و ما بسیار محتاط عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72063" target="_blank">📅 18:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=qWPQXmV7F96_FUtuFBIDOPdyhINf5fsZYQ0zVMkaxQCzv1U_Kb24YtgJli_gkRsQCDuZmwX-rBQZg9Zz3vMc1pKSVLjapnUG9aGSWce1Tult28Ef3nl6r1Jaxr4Lj0O3JpWLjvywBy4wowF8nWo2HUB0CEmgGMLx-HhDqcgZziAWVA1hBh2Htq06AdC_lDW3Ghr6SVtlh_8h_pgHf-yto3rklUWOG0Is_xNsUesQwDzGveKt6bNev7ZhtrvgG4vI3WGyVbhibIdL8gvPQS-7-0pTdrNb0XKs7CwT9HDAby4adbcJJBuU2LeMqdgerSwtePuutB8KDiKFBVOs9SyV_pauFBxlQqaUygh5h7Qbwdxy5rpIgHV2jrbnxSXXV4iBftTGEl9v1Uyg1gYuhl_nnB1LRb7abRPsG3--g65nllxFeG511sts7jsERMMjvn9DLuDZqrbqX9OvFLyeXMgL8B4-vp2MW6IobT2Vhe5Cgn4mSruVQjEEHKPp6Dp3I2pIK2koeCc84B9YIIEB13b4XTL4wIzFpyn1ALJ4frHH1Ir7OIbnKZEQ80zTaNnZUDnAhgFwlf652gYn7tMQwuR_4w4aezwjpuCqlwMbPY7mLuJc7T4-A0izPonhXGAiQip9MmjEFSPtHwxspfFs0fXWQ_kcNzWcPigresVTFOJbZnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=qWPQXmV7F96_FUtuFBIDOPdyhINf5fsZYQ0zVMkaxQCzv1U_Kb24YtgJli_gkRsQCDuZmwX-rBQZg9Zz3vMc1pKSVLjapnUG9aGSWce1Tult28Ef3nl6r1Jaxr4Lj0O3JpWLjvywBy4wowF8nWo2HUB0CEmgGMLx-HhDqcgZziAWVA1hBh2Htq06AdC_lDW3Ghr6SVtlh_8h_pgHf-yto3rklUWOG0Is_xNsUesQwDzGveKt6bNev7ZhtrvgG4vI3WGyVbhibIdL8gvPQS-7-0pTdrNb0XKs7CwT9HDAby4adbcJJBuU2LeMqdgerSwtePuutB8KDiKFBVOs9SyV_pauFBxlQqaUygh5h7Qbwdxy5rpIgHV2jrbnxSXXV4iBftTGEl9v1Uyg1gYuhl_nnB1LRb7abRPsG3--g65nllxFeG511sts7jsERMMjvn9DLuDZqrbqX9OvFLyeXMgL8B4-vp2MW6IobT2Vhe5Cgn4mSruVQjEEHKPp6Dp3I2pIK2koeCc84B9YIIEB13b4XTL4wIzFpyn1ALJ4frHH1Ir7OIbnKZEQ80zTaNnZUDnAhgFwlf652gYn7tMQwuR_4w4aezwjpuCqlwMbPY7mLuJc7T4-A0izPonhXGAiQip9MmjEFSPtHwxspfFs0fXWQ_kcNzWcPigresVTFOJbZnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
از این پس، تمام اسناد ایالات متحده — و به امید خدا اسناد سراسر جهان — تغییر خواهند کرد تا به جای واژه «مصنوعی» (Artificial)، از اصطلاح بسیار دقیق‌ترِ «اَبَر» (Super) استفاده شود.
به عبارت دیگر، به دنیای جدید «اَبَر-هوش» (Superintelligence) یا همان SI خوش آمدید.
باید دید این ایده چه بازخوردی خواهد داشت؛ هرچه باشد، خیلی بهتر به نظر می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72062" target="_blank">📅 18:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72061">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=XQM3Xzub8fb0I1Jmsq11xnsCJAq2PRSUIGQDc5Yg8czVG8FaFP50g41ozffEg8_nu60K_iUWcOvvTEmt0NJ-DAhijy1WLyjLDUsCwFX6huzWnXgS5-VdrrIUAAo_y8c0AWmwMNWO12UNL84pPfBl7ds0ffHmABatr9j7DEeW2EY43DogCLkoULUW_JSsInc8UV-G6ShuV9Ex0CtrpAtuukVh8JGg8axwj5qL57JaMCpSfv8EYsaQzpE-zxo69V_4UyFE0axqcUrWtxRhBq9BORCDEQdgv83Gn0fZBmOtWdM0ib8J5FQN4acLCtUydrCTD0_nhqA5p6I2TS5Mcfbzsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=XQM3Xzub8fb0I1Jmsq11xnsCJAq2PRSUIGQDc5Yg8czVG8FaFP50g41ozffEg8_nu60K_iUWcOvvTEmt0NJ-DAhijy1WLyjLDUsCwFX6huzWnXgS5-VdrrIUAAo_y8c0AWmwMNWO12UNL84pPfBl7ds0ffHmABatr9j7DEeW2EY43DogCLkoULUW_JSsInc8UV-G6ShuV9Ex0CtrpAtuukVh8JGg8axwj5qL57JaMCpSfv8EYsaQzpE-zxo69V_4UyFE0axqcUrWtxRhBq9BORCDEQdgv83Gn0fZBmOtWdM0ib8J5FQN4acLCtUydrCTD0_nhqA5p6I2TS5Mcfbzsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام «هوش مصنوعی» (AI) را به «اَبَر‌هوش» (SI) تغییر می‌دهد.
او می‌گوید استفاده از واژه «مصنوعی» باعث می‌شود که هوش، «ساختگی» به نظر برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72061" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72060">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156037c15c.mp4?token=l3wYiHvpfgGCrLBm1NnHwWiTlDAh0Z3x71l5EpIah1l3Hlvo6vo2Zg1LQVveU2Hx69bvPOVQN2m-nDEScw7P4qKJ0hFBVB3lJ8TL44ISOaUN5bZbNHeJrj08LCvOfK4esSYsNMVRQO6MpOiuPf37KNw4U1AczwjXjeajLFq0GFOcFurnYHsmCPmO-tYGLbOKSaBB2sRuID3ygQlU8RGZyZkHzDNcb4QOCkunXHUGdG0UuKLFK_mRsMAptq_Hymb9PWY7_MYoNfDrEmVmfXJzV0vkhk_wa_HvcO2u02S1BQs8rAtK6015m-nNcAPykKz-9dXuTfsWjX2X1aH1CpO4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156037c15c.mp4?token=l3wYiHvpfgGCrLBm1NnHwWiTlDAh0Z3x71l5EpIah1l3Hlvo6vo2Zg1LQVveU2Hx69bvPOVQN2m-nDEScw7P4qKJ0hFBVB3lJ8TL44ISOaUN5bZbNHeJrj08LCvOfK4esSYsNMVRQO6MpOiuPf37KNw4U1AczwjXjeajLFq0GFOcFurnYHsmCPmO-tYGLbOKSaBB2sRuID3ygQlU8RGZyZkHzDNcb4QOCkunXHUGdG0UuKLFK_mRsMAptq_Hymb9PWY7_MYoNfDrEmVmfXJzV0vkhk_wa_HvcO2u02S1BQs8rAtK6015m-nNcAPykKz-9dXuTfsWjX2X1aH1CpO4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
نیروی دریایی ایالات متحده اخیراً بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت و عبور داده است و حجم نفت در حال عبور، بیش از هر زمان دیگری از آغاز جنگ است.
ما هر روز و هر شب، به ترتیب ۲۲، ۲۵، ۳۰، ۳۲ و ۳۷ کشتی را [از این مسیر] عبور می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72060" target="_blank">📅 18:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72059">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=PuT3UTR-1IopihU3u7Qykuf8mQaIs8f6hALE8xfx7OWI_J7Z5e-lZVrVLYh25cTfFd_BYpYDzQwgfjyHpQVF3PC2xy3d_JtCTKAO3dkTSwqpoRdzQEKdmLVM6oST0R4QmRO_WEXsi8yvsD0wf5NYcWxU5WJ9Gd3e9Kahk3D5UjmLXbhtVAq69Zg_J7j1XtsfORbdkC9Wb02SdtoM7oYOnDp_oCtG_RLr7a2hklVotw7NvIiO5JoQWODY10JCL4BQcQtiW6u8CJErCMDdAUibevXBwqrdKVrtocDLO5Jyax8JC9A5_Ruya_K96W708CL629ds6NZ3eJPrUW98FF5XtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=PuT3UTR-1IopihU3u7Qykuf8mQaIs8f6hALE8xfx7OWI_J7Z5e-lZVrVLYh25cTfFd_BYpYDzQwgfjyHpQVF3PC2xy3d_JtCTKAO3dkTSwqpoRdzQEKdmLVM6oST0R4QmRO_WEXsi8yvsD0wf5NYcWxU5WJ9Gd3e9Kahk3D5UjmLXbhtVAq69Zg_J7j1XtsfORbdkC9Wb02SdtoM7oYOnDp_oCtG_RLr7a2hklVotw7NvIiO5JoQWODY10JCL4BQcQtiW6u8CJErCMDdAUibevXBwqrdKVrtocDLO5Jyax8JC9A5_Ruya_K96W708CL629ds6NZ3eJPrUW98FF5XtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایالات متحده و ایران قطعاً این کار را به سرانجام خواهند رساند. ما به هر طریقی که شده، این کار را انجام خواهیم داد. این کار انجام خواهد شد.
این کار به‌سرعت انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72059" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72058">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=L2DVCunqOUlb6b7W3QWqgTajUlht3wlzELbOuDWl2TmVyGMFW3rYi4ux4b1eG2ZZaiifnZYuqg9NWVySnsNjoVbuHJaIOJN0ZLe4EAKZVU0h-QuNpoiFre_9SZ7nLh-7ppSRM5Eglrc6yQPNlfvMlH1ZRvjtGVzCAHqCNEN3veHOggMrvo65XKVqhZV33oKsl0nR7joiTqfyOf74XbXp_h0ggiJuXP8nfeIORh7gE-bBerbgT9GN2xUASvKh94bpIXvkt_Wiq2XssQBUFneHDr58UQJm6WSlE5p9-mBTP2I7QoJg41qnbX8l-1WjmE8Rb1kVkOw8VNMyS6cGViF2B4mCKj3CuUE2fcJP1OjtXlq76xT1T7n3a3zZM2tUxDMttrdSr4qWqFg9P6XnJBmZ3tIsA6jOWOoctFO1UTA67WVtPmRzjo5e_BxxVF_sdeBD7OxGtqr3ZDtHxh9MCsiGzXkW386ScRoTU4fXujlHjcPnRFaegks-vyZ1wTB8KVJ3e5aK8I0g2XJ_eUNjIjLw8gQdGCauUoLJaHxQ24fApFtVvrptx9tmTaymt5vH6E_Gch5KaqtGjQ4TENBMhlZLgM5ldmw0DsDFgdJPIUz85qxJF2llxgjqsnSKW63GJUfsDX0S3-4nESxqpFrY9KkGTXfHvVe_CUxcf0CsaxdufVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=L2DVCunqOUlb6b7W3QWqgTajUlht3wlzELbOuDWl2TmVyGMFW3rYi4ux4b1eG2ZZaiifnZYuqg9NWVySnsNjoVbuHJaIOJN0ZLe4EAKZVU0h-QuNpoiFre_9SZ7nLh-7ppSRM5Eglrc6yQPNlfvMlH1ZRvjtGVzCAHqCNEN3veHOggMrvo65XKVqhZV33oKsl0nR7joiTqfyOf74XbXp_h0ggiJuXP8nfeIORh7gE-bBerbgT9GN2xUASvKh94bpIXvkt_Wiq2XssQBUFneHDr58UQJm6WSlE5p9-mBTP2I7QoJg41qnbX8l-1WjmE8Rb1kVkOw8VNMyS6cGViF2B4mCKj3CuUE2fcJP1OjtXlq76xT1T7n3a3zZM2tUxDMttrdSr4qWqFg9P6XnJBmZ3tIsA6jOWOoctFO1UTA67WVtPmRzjo5e_BxxVF_sdeBD7OxGtqr3ZDtHxh9MCsiGzXkW386ScRoTU4fXujlHjcPnRFaegks-vyZ1wTB8KVJ3e5aK8I0g2XJ_eUNjIjLw8gQdGCauUoLJaHxQ24fApFtVvrptx9tmTaymt5vH6E_Gch5KaqtGjQ4TENBMhlZLgM5ldmw0DsDFgdJPIUz85qxJF2llxgjqsnSKW63GJUfsDX0S3-4nESxqpFrY9KkGTXfHvVe_CUxcf0CsaxdufVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من از همه کشورها خواستم تا در اعمال
انزوای کامل اقتصادی ایران با ما همراه شوند؛ تا زمانی که آن‌ها حملات خود به کشتی‌های تجاری را متوقف کنند، از جاه‌طلبی‌های هسته‌ای خود دست بردارند و به حمایت از تروریسم پایان دهند.
این رژیم تروریستی نه به این دلیل که قدرتمند و با اعتمادبه‌نفس است، بلکه به این خاطر که ضعیف و درمانده است، چنین رفتار نامناسبی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72058" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72057">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415b898f05.mp4?token=vNdlcEKQR-MyUhSXBJKXaq0MOEgKdBUm25rH7RZ4RDhL4i1pcS9LrBOVw7rvWCjf4d8Vu2H42gajn8LjDJW2FGMyWIk6-fB3OT3OJuCAuk_c-qxjTdroVDz4yvseAfOas1hGaOXtdlxn7H91eIa4evTvD-dG0_88mc1BrvIZ65dlQaQ0mntCIXeM3StWM0g_XNVBRmGRboZTYfkWyn8gsomaHoIpxKy-mz5CK7WNCGVU5lf_oe43YsFgbgGjFyt-_sEHySHVQALeqL9Hw9C1zNYywtjrTLLQwCGvaoi75bNngWuPuYio04IFpQ3M1RoY6dwOyyZgpyw6G4eDu2bjhFq6ilvaN4B4LK-DAPDkD1fGYEGd59czXJH3jLK2qeTmdaqwrxD8Wo2h2L8mPk8GxuSgSMEZ-w_wEo5qgogMP2GV0StOoT7kVmiecSQkLWFcc67BS7KPfNFOWkg5w6Uti_-68SfDkZDp4j8ldGbd3kU76NaTAbJuoXWtVPlcjnSHktkf31xKEgQ0forjmRD0EfGAPK_4Au_HRkfofj1wiZzRZMnvmLnE8VHCHX2-pA-FTgweayYKD_RIgUeI1PKwxdtkSPfU7QFBSTQy4P8OCHJUzRRPE4qCfYGJSP3s1fzuialmx9Y8pscAligHAML_hW-2IdQcYMI9ktIpc407F1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415b898f05.mp4?token=vNdlcEKQR-MyUhSXBJKXaq0MOEgKdBUm25rH7RZ4RDhL4i1pcS9LrBOVw7rvWCjf4d8Vu2H42gajn8LjDJW2FGMyWIk6-fB3OT3OJuCAuk_c-qxjTdroVDz4yvseAfOas1hGaOXtdlxn7H91eIa4evTvD-dG0_88mc1BrvIZ65dlQaQ0mntCIXeM3StWM0g_XNVBRmGRboZTYfkWyn8gsomaHoIpxKy-mz5CK7WNCGVU5lf_oe43YsFgbgGjFyt-_sEHySHVQALeqL9Hw9C1zNYywtjrTLLQwCGvaoi75bNngWuPuYio04IFpQ3M1RoY6dwOyyZgpyw6G4eDu2bjhFq6ilvaN4B4LK-DAPDkD1fGYEGd59czXJH3jLK2qeTmdaqwrxD8Wo2h2L8mPk8GxuSgSMEZ-w_wEo5qgogMP2GV0StOoT7kVmiecSQkLWFcc67BS7KPfNFOWkg5w6Uti_-68SfDkZDp4j8ldGbd3kU76NaTAbJuoXWtVPlcjnSHktkf31xKEgQ0forjmRD0EfGAPK_4Au_HRkfofj1wiZzRZMnvmLnE8VHCHX2-pA-FTgweayYKD_RIgUeI1PKwxdtkSPfU7QFBSTQy4P8OCHJUzRRPE4qCfYGJSP3s1fzuialmx9Y8pscAligHAML_hW-2IdQcYMI9ktIpc407F1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به اتمام است، اما این حرف صحت ندارد.
ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و با سرعتی بی‌سابقه مشغول تولید آن‌ها هستیم. ما با سرعتی بیش از هر زمان دیگری در حال افزایش ذخایر خود هستیم؛ آن هم با تجهیزاتی که در بالاترین سطح کیفی قرار دارند.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. هم‌اکنون ۱۸ کارخانه از این دست توسط برترین شرکت‌های دفاعی جهان در حال ساخت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72057" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72056">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=RMh8M1azmZg8m95SFfkIgaQQ8GGSm1nW_FKy0SENupU7kntd66Qgzow46KLD7uN0zKYlYPaCv0Ha0O9eLBhjYIi8qYviYA-TM659B-nAgnrs4RtDOUWoKmHbARId6nEeKFFoD9EIUUbJMy84E2gVWEYBF9ndBhceevSP0Q1LZf4h9juJtMOzfRikEbFUGUWnZVS9YMQLID3zLWiZR1ShKw4DxxvDuhHj2yFRpWleyHG_5YW74u0cPI97dcRvb7Qs_0m4Zvwr1fn1bq2M45FrdbBTneJ7mzauXa9LtYJ1pEtWHkie3ZN-ZAZO576QUySo-O9kMCmVW8yhnYpJ_In6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=RMh8M1azmZg8m95SFfkIgaQQ8GGSm1nW_FKy0SENupU7kntd66Qgzow46KLD7uN0zKYlYPaCv0Ha0O9eLBhjYIi8qYviYA-TM659B-nAgnrs4RtDOUWoKmHbARId6nEeKFFoD9EIUUbJMy84E2gVWEYBF9ndBhceevSP0Q1LZf4h9juJtMOzfRikEbFUGUWnZVS9YMQLID3zLWiZR1ShKw4DxxvDuhHj2yFRpWleyHG_5YW74u0cPI97dcRvb7Qs_0m4Zvwr1fn1bq2M45FrdbBTneJ7mzauXa9LtYJ1pEtWHkie3ZN-ZAZO576QUySo-O9kMCmVW8yhnYpJ_In6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من برای انتخابات در مورد ایران مطلقاً هیچ اعتباری قائل نبوده‌ام و نخواهم بود؛ این موضوع حتی به ذهنم هم خطور نمی‌کند.
تنها چیزی که اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72056" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72055">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:باید تصمیم بزرگی بگیرم.
آیا توافقی با ایران صورت خواهد گرفت که به آن‌ها اجازه دهد کشورشان را بازسازی کنند و کشوری بسیار بزرگ‌تر از آنچه پیش‌تر بود بسازند؛ شاید حتی یکی از بزرگ‌ترین کشورهای خاورمیانه یا حتی جهان؟
یا اینکه جمهوری اسلامی را نابود کنم—آن هم به سرعت—و هرگز به آن‌ها فرصتی ندهم که دوباره دست به کشتار و ویرانی مردم و کشورها بزنند؟
آیا آن‌ها را به جهنم بفرستم، بدون هیچ شانس بقا و بدون هیچ امیدی به عظمت در نسل‌های آینده؟
اما معتقدم که بلافاصله پس از انتخابات به توافق خواهیم رسید، چرا که تن ندادن به آن برایشان منطقی نیست.
آن‌ها منتظرند ببینند عملکرد من در انتخابات میان‌دوره‌ای چگونه خواهد بود. چیزی که متوجه نیستند این است که من اصلاً نامزد آن انتخابات نیستم. من آن کار را قبلاً انجام داده و با اکثریتی قاطع پیروز شده‌ام.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72055" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72054">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=hfPPtnUsaVawchcPTM0EDqGxs1ek_-2vgyqWf8b3vWEleqwbiJ8RnH1EXLi2Z2EnssORr3PjYXejLq3rrRuAWZBAHKqadXhDEL9AXJ8P_tSU3ReFXQNPrAM7gx2hbq55YpY6pXtMLbVJlnsko_ywTPVphRHcJ4uvEmAsRQu8vQIhoakgx7_ta_IFf7RzZadMgHUmmPYx4v1Mqj5XnYoXXVZKbzNdXtAzTKJAjLB3--8QKP8bF2eofLx7DBIw6GcBMQS59feTd17GMMa10ORdCcYqUi_l2RAGqPOZs5Fxski2uboueJDDxHHyjRWmvvKzl6AllpYEshLTPVqfhHuuKycLmU5LsAL-G8gVkSYvQzit_DKAyI4vqFuYW9QABNA2Isbdw07VBmsQn96Yg6Zg1gU-jbpHF-uBzv50A5cIaK7-OJ45bFMLktdGmd9nZvjHEgOPvxx0bRjPeeEbP6gb9pZKOtKcRniU8XMroqZi2k7m2j9_dzvW-KGVasFc4E55SdKXK7YR6bBeTVEK3VR0mRJNAv4Qe-yaUgedaaMSdDgIJKmwovXV5z4JAvC5Vv9EiFOPDNQHiPM62EK5ybujtSAiSo1VbNWu3-uURODC3xUhWRLIoMwyTB_3GbONc58Bkp0Dcmwf5bS8oWFYus3rzBabbYlcFf7SJlyPj3eudxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=hfPPtnUsaVawchcPTM0EDqGxs1ek_-2vgyqWf8b3vWEleqwbiJ8RnH1EXLi2Z2EnssORr3PjYXejLq3rrRuAWZBAHKqadXhDEL9AXJ8P_tSU3ReFXQNPrAM7gx2hbq55YpY6pXtMLbVJlnsko_ywTPVphRHcJ4uvEmAsRQu8vQIhoakgx7_ta_IFf7RzZadMgHUmmPYx4v1Mqj5XnYoXXVZKbzNdXtAzTKJAjLB3--8QKP8bF2eofLx7DBIw6GcBMQS59feTd17GMMa10ORdCcYqUi_l2RAGqPOZs5Fxski2uboueJDDxHHyjRWmvvKzl6AllpYEshLTPVqfhHuuKycLmU5LsAL-G8gVkSYvQzit_DKAyI4vqFuYW9QABNA2Isbdw07VBmsQn96Yg6Zg1gU-jbpHF-uBzv50A5cIaK7-OJ45bFMLktdGmd9nZvjHEgOPvxx0bRjPeeEbP6gb9pZKOtKcRniU8XMroqZi2k7m2j9_dzvW-KGVasFc4E55SdKXK7YR6bBeTVEK3VR0mRJNAv4Qe-yaUgedaaMSdDgIJKmwovXV5z4JAvC5Vv9EiFOPDNQHiPM62EK5ybujtSAiSo1VbNWu3-uURODC3xUhWRLIoMwyTB_3GbONc58Bkp0Dcmwf5bS8oWFYus3rzBabbYlcFf7SJlyPj3eudxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
ما در آمریکا به‌تازگی بیست‌ و پنجمین سالگرد بدترین حمله تروریستی تاریخ، یعنی ۱۱ سپتامبر را پشت سر گذاشتیم؛ حمله‌ای که جان سه هزار نفر را گرفت. درست در همین نزدیکی‌ها.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های تحت حمایت مالی ایران، ۱۲۰۰ غیرنظامی کاملاً بی‌گناه — از جمله ده‌ها آمریکایی و بسیاری از نوزادان؛ نوزادانی کوچک، ظریف و زیبا — را شکنجه کردند، مثله کردند و به قتل رساندند.
رهبر عالی ایران آن کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72054" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72053">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9289304.mp4?token=GPCJlyIrY6_PX8IrrGkneHl_a2Mlp6cVDIK0A2PONxcB6leSt6oUy-q9XH7KPqGc-RKhS6P2GmjEp4NTfX5XXkZuV73F1KC3tU9GB0G8er_ll4gHBG7XIUlYlPQIths8almQTXwld8ETgjAVA0qpz9kiR0Ilq4wkxYGQ7684NGHodtQl50bcM5SB9mlaEGc4_-NaVl42mhyUvaWt_jlZy0MipafLlI5kNFcXTpujrMg4gFHN7GnVEhcP5XRxX2F094GNenS2TzBXcf6rWGTcyftzeT2bb9vgfn7YegYzwSXPDLFpAZuBYH4CeGq7uMwc2Z9JY895hjz2BlZDm-TzAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9289304.mp4?token=GPCJlyIrY6_PX8IrrGkneHl_a2Mlp6cVDIK0A2PONxcB6leSt6oUy-q9XH7KPqGc-RKhS6P2GmjEp4NTfX5XXkZuV73F1KC3tU9GB0G8er_ll4gHBG7XIUlYlPQIths8almQTXwld8ETgjAVA0qpz9kiR0Ilq4wkxYGQ7684NGHodtQl50bcM5SB9mlaEGc4_-NaVl42mhyUvaWt_jlZy0MipafLlI5kNFcXTpujrMg4gFHN7GnVEhcP5XRxX2F094GNenS2TzBXcf6rWGTcyftzeT2bb9vgfn7YegYzwSXPDLFpAZuBYH4CeGq7uMwc2Z9JY895hjz2BlZDm-TzAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این رژیم امسال بیش از ۷۲ هزار تن از شهروندان خود را به خاک و خون کشید.
تصور کنید چنین رژیم پلیدی قدرت آن را داشته باشد که از پشتِ سپرِ هسته‌ای، دست به حملات تروریستی گسترده بزند.
این واقعیتی بود که باید با آن روبرو می‌شدیم؛ واقعیتی که بسیاری ترجیح دادند آن را نادیده بگیرند. همه آن‌ها آن را نادیده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72053" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=KyPbXRnKKoHPDPCcdC1bXnO7ULfaGYpzLNOr7rMhmwrOBbGsvD1vWErdIo923Ie-tG9G2YzBGh3CJEtp1DwjCWAqnahD8UrNC_Gt1W8rUxEc0MotcUSed8XRLNnqEwmjrlwT5ulNUeIRidybXtIKzmHEkrPmD0TXoG9snFYKqj-zsOdJ_UisJZAWeNjJeBy6TgvpoMRQ-AJh-QHLlaf58gVP9st_B3_Q6YxRvlMAhZG3GduBAwvZCZUFqqRsYXXyJiPkhz6RUiTISSGla6v4alH9fHitoWTs3NIoGdqlJACKc3bfwCQPPvKMjy2qlcEaQ4TjMb5QA3zoYNW_I6Zhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=KyPbXRnKKoHPDPCcdC1bXnO7ULfaGYpzLNOr7rMhmwrOBbGsvD1vWErdIo923Ie-tG9G2YzBGh3CJEtp1DwjCWAqnahD8UrNC_Gt1W8rUxEc0MotcUSed8XRLNnqEwmjrlwT5ulNUeIRidybXtIKzmHEkrPmD0TXoG9snFYKqj-zsOdJ_UisJZAWeNjJeBy6TgvpoMRQ-AJh-QHLlaf58gVP9st_B3_Q6YxRvlMAhZG3GduBAwvZCZUFqqRsYXXyJiPkhz6RUiTISSGla6v4alH9fHitoWTs3NIoGdqlJACKc3bfwCQPPvKMjy2qlcEaQ4TjMb5QA3zoYNW_I6Zhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها موشکی ساختند که قادر به هدف قرار دادن اروپا بود و به آن بسیار افتخار می‌کردند. امیدوارم اروپایی‌ها متوجه این موضوع باشند.
هدف ایران این بود که در پناهِ سپرِ موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.
اگر آن‌ها موفق می‌شدند، آن رژیم شرور آزاد بود که تا ابد به گسترش وحشت و مرگ بپردازد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72052" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=ry8rLstH0ZNU3HY31Td4p0ugy8S6kv5IQP8kdh7x3smZTlBcduqB4Q1jMREUsEXZL__6kofdSBdZ7evwlJP4Ih6hXE3cfuB_bVfMmdrMv-uGJaBXhAvN8rSv6D8GLar-8IQ46E2ZDll0O8MgFB51A1mHfbkSxxwmyCiqehxwkPn3w-v4VZj3iN-yzCN2xzmvbT-5I1oc6pUpOVjPlBlLR_hUCjgOpZVoWTJm2wjaZsfIBG7-thv2j44Kbup1cZqHMTqHDtBYu2fqMUS_a2QyWq9L0_71qM2w33YptVHL7gnJMPKdey_q5BidHTRETrFVi-5A96nV4soSGIqjiorkDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=ry8rLstH0ZNU3HY31Td4p0ugy8S6kv5IQP8kdh7x3smZTlBcduqB4Q1jMREUsEXZL__6kofdSBdZ7evwlJP4Ih6hXE3cfuB_bVfMmdrMv-uGJaBXhAvN8rSv6D8GLar-8IQ46E2ZDll0O8MgFB51A1mHfbkSxxwmyCiqehxwkPn3w-v4VZj3iN-yzCN2xzmvbT-5I1oc6pUpOVjPlBlLR_hUCjgOpZVoWTJm2wjaZsfIBG7-thv2j44Kbup1cZqHMTqHDtBYu2fqMUS_a2QyWq9L0_71qM2w33YptVHL7gnJMPKdey_q5BidHTRETrFVi-5A96nV4soSGIqjiorkDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
سال گذشته، پس از آغاز به کار، مذاکراتی را با ایران آغاز کردم و به آن‌ها پیشنهاد دادم که در ازای پایان دادن به برنامه هسته‌ای و حمایتشان از تروریسم، از همکاری کامل اقتصادی برخوردار شوند.
اما آن‌ها نپذیرفتند. این اشتباه بزرگی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72051" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=fuAJIG3Fhau-_cC-1pqATamGwsU5PslXmxIrMo_dCxiMucfdDYW8Dh4CuF3-QYrDAcCp6F0IGDNe_Sq79Awu-4NHv9ibBe1gai3AgEBplJiuzaA4l-2MwJAwfuCcvTUgYO9hOriIbDbkK2bUPovJUX17-0eOx7ncolDb3eSN93psoxCXUuxZ903sJ3LKwvdQNAENgMtY-wM8MqrXwF3XCHuhqsCCHiz6YYS11ZnEwI0W-3hjbvo27Dk0FpunY0bdn8XU2Th9jbA_LsPM3-GvQ5AeIjOW67ckvM7ojczy_g8I4ZeMdxqolabMGKh4bVVjYXNYMpJxlsTxdNESOQR0IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=fuAJIG3Fhau-_cC-1pqATamGwsU5PslXmxIrMo_dCxiMucfdDYW8Dh4CuF3-QYrDAcCp6F0IGDNe_Sq79Awu-4NHv9ibBe1gai3AgEBplJiuzaA4l-2MwJAwfuCcvTUgYO9hOriIbDbkK2bUPovJUX17-0eOx7ncolDb3eSN93psoxCXUuxZ903sJ3LKwvdQNAENgMtY-wM8MqrXwF3XCHuhqsCCHiz6YYS11ZnEwI0W-3hjbvo27Dk0FpunY0bdn8XU2Th9jbA_LsPM3-GvQ5AeIjOW67ckvM7ojczy_g8I4ZeMdxqolabMGKh4bVVjYXNYMpJxlsTxdNESOQR0IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند.
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد  ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72050" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=Bakn_gn2Tc7jvZRZJdW5NHQTDpfGNEnCCBEyhzSJbvS-utdzg5EEjn3HlbiWBRnXwNFjulSGhmcu2AnHYup3dS8mwIfNyZII_8HY9QE-pgKeNTGv2P5ujPRayWJv3WdQw5Q_vVZqPQ1AYcTkQCd4payJT5W6CmJseHmJuml04qc7yW3W1VRuvQUCJnKBrn_e8-Or3WUF5pgCNbtA_MqQhRKcsH3p9op3owzqRV-CfW-5_ZtmTtVdfOC3-J_gCGMwzrOXaecyn8fvY-KYeiLcm37J9Kaxkz6sXJqs9HAVneO3BLRtJZGDA0CmpvVU004SYDkdDSw38RYTv7oxWFg7Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=Bakn_gn2Tc7jvZRZJdW5NHQTDpfGNEnCCBEyhzSJbvS-utdzg5EEjn3HlbiWBRnXwNFjulSGhmcu2AnHYup3dS8mwIfNyZII_8HY9QE-pgKeNTGv2P5ujPRayWJv3WdQw5Q_vVZqPQ1AYcTkQCd4payJT5W6CmJseHmJuml04qc7yW3W1VRuvQUCJnKBrn_e8-Or3WUF5pgCNbtA_MqQhRKcsH3p9op3owzqRV-CfW-5_ZtmTtVdfOC3-J_gCGMwzrOXaecyn8fvY-KYeiLcm37J9Kaxkz6sXJqs9HAVneO3BLRtJZGDA0CmpvVU004SYDkdDSw38RYTv7oxWFg7Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من هیچ تمایلی ندارم که اجازه دهم خطرات، حتی یک روز دیگر هم رشد کنند. من به اینکه بگذاریم مشکلات وخیم‌تر شوند، اعتقادی ندارم؛ چرا که حل آن‌ها دشوارتر می‌شود.
بنابراین، در حالی که دیگران حرف می‌زدند، من عمل کردم.
در حالی که دیگران از صلح سخن می‌گفتند، من صلح را محقق ساختم.
در حالی که دیگران تهدیدها را نادیده می‌گرفتند، من با آن‌ها مقابله کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72049" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=fVFzvZCceiJwPphXzM8nTDQ4h2X03DhIFwjrKxkZOx3PFory_YraQlr4jH6VD4z1T2oo2UVYGg5LgizOFlNDEB5hpBR8Tvi6snMbiixMa9-E2fuhpscaN4FglsLBu9qj0ad0sCS77oS483gM3-75tjezK1e0rhNLpT66cxVWAgkCPRTpV5WpjmHzFiM_6Qucv7wGZ3YbADev6aYXCEdsZLaM0jwxDhRhIALBCKLc6P98mfYkvGJr6BCbW85ZoEfEXDAwZyUXOkphNX2A-Ol4GxrMp_rtm2CFlTNqHur9CdoK0ul1vUt4tmzZdqZjUCedFJ1-IKEelx1q7l_K6d427w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=fVFzvZCceiJwPphXzM8nTDQ4h2X03DhIFwjrKxkZOx3PFory_YraQlr4jH6VD4z1T2oo2UVYGg5LgizOFlNDEB5hpBR8Tvi6snMbiixMa9-E2fuhpscaN4FglsLBu9qj0ad0sCS77oS483gM3-75tjezK1e0rhNLpT66cxVWAgkCPRTpV5WpjmHzFiM_6Qucv7wGZ3YbADev6aYXCEdsZLaM0jwxDhRhIALBCKLc6P98mfYkvGJr6BCbW85ZoEfEXDAwZyUXOkphNX2A-Ol4GxrMp_rtm2CFlTNqHur9CdoK0ul1vUt4tmzZdqZjUCedFJ1-IKEelx1q7l_K6d427w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
با افتخار به شما اعلام می‌کنم که آمریکا بازگشته است و کشور ما امروز قوی‌تر از هر زمان دیگری است.
اقتصاد ما مایه غبطه جهانیان است. ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما بی‌همتاست و ما تقریباً در همه زمینه‌ها پیشتاز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72048" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72047">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنرانی دونالد ترامپ درمجمع عمومی سازمان ملل متحد در نیویورک آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72047" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72046">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دیدم که مراد ویسی گفته احتمال اینکه پزشکیان و عراقچی رو تو آمریکا مثل مادورو دستگیر کنند غیرممکن نیست
آدم می‌مونه به این تحلیلگر چی بگه
😐
🧠
#hjAly‌</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72046" target="_blank">📅 17:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=ccAqNg67yKIH2AfSmq8HmhQgOPqLW5aMIBI4qOGxZIA6OIriuQXjnVWFtX5LQPdLf1uOupUVGFUXwT0FZw5Ke9GKaWP0u39zHZy6v2rVj9bVUhdVdj56u1aL0DFwMJUncJIVnqcIbJ65qQlgd7g7e1C9vRPxO5cDqQnC9piQLqVn1iZwz7iD9HmXqkY_slyMuHa7z48RHHcBFrB-edU7NMlQyzgPiafGK87nzWl3iNHROy8BPjhMupmFxlMcfErAC8hmx4S6Bxr1nv184742kQp2_o-opBfn7wMH_2S_vZQYFafAaTqkJDbPt9oIFiKbJsER4uLe9D83rE2U8Fu78A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e4ea7a67.mp4?token=ccAqNg67yKIH2AfSmq8HmhQgOPqLW5aMIBI4qOGxZIA6OIriuQXjnVWFtX5LQPdLf1uOupUVGFUXwT0FZw5Ke9GKaWP0u39zHZy6v2rVj9bVUhdVdj56u1aL0DFwMJUncJIVnqcIbJ65qQlgd7g7e1C9vRPxO5cDqQnC9piQLqVn1iZwz7iD9HmXqkY_slyMuHa7z48RHHcBFrB-edU7NMlQyzgPiafGK87nzWl3iNHROy8BPjhMupmFxlMcfErAC8hmx4S6Bxr1nv184742kQp2_o-opBfn7wMH_2S_vZQYFafAaTqkJDbPt9oIFiKbJsER4uLe9D83rE2U8Fu78A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:پیامی که می‌خواهید به پوتین منتقل کنید، چیست؟
ترامپ: این جنگ را متوقف کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72045" target="_blank">📅 17:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=vZEGyoVhIZ8VkN-XFXfg-09XIyv93VzNWVvaSU_MwAehwUhNEDqJYNIUhgBNwGXr9k1hMKmpOtPD1tZDwui-XLeXR2uqwQ1d1o7miXxvbjvXY4d1lHX_d_hP_I81pQN9Ew5xGRIbfyPo9LlIDoKfGWbk_gbiN6prti7YPbGGm-RMkUbWUt3ZIilPGOc8A5Hu-d4SgThJQradfJk_G8YVYBY0MO1YGi0PJe5HOxJAlcw5I3heLLblw5D7doNxjM_GidYn8t2KqkXVxfen6k_fV35c-a7ruH8kXmkOM3nkVhPWnYnkaUqvL1ZiQr1tvG9yfmmQGMP4cjGLo90syg9l4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7aa5b4a7d.mp4?token=vZEGyoVhIZ8VkN-XFXfg-09XIyv93VzNWVvaSU_MwAehwUhNEDqJYNIUhgBNwGXr9k1hMKmpOtPD1tZDwui-XLeXR2uqwQ1d1o7miXxvbjvXY4d1lHX_d_hP_I81pQN9Ew5xGRIbfyPo9LlIDoKfGWbk_gbiN6prti7YPbGGm-RMkUbWUt3ZIilPGOc8A5Hu-d4SgThJQradfJk_G8YVYBY0MO1YGi0PJe5HOxJAlcw5I3heLLblw5D7doNxjM_GidYn8t2KqkXVxfen6k_fV35c-a7ruH8kXmkOM3nkVhPWnYnkaUqvL1ZiQr1tvG9yfmmQGMP4cjGLo90syg9l4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ هنگام ورود به مجمع عمومی سازمان ملل خطاب به سی‌ان‌ان:
تعجب می‌کنم که سی‌ان‌ان اینجاست تا اخبار مربوط به مرا پوشش دهد. شما نباید اینجا باشید.
شما گفته بودید که قرار نیست اخبار مرا پوشش دهید. نباید مرا پوشش دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72044" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72043" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVaviNcNl3xr_6VMThFKotT6NZwF41NtKBmYDJfx-X-659XiCJBzgNCR84zbuxOeTHegj4zkpOha8R4n9FcF2XpFQvHPsi9z4w46fBOCyiSDYDRIxT7vX6PgzYY9-66C5zG10RXqK8Jfay7ICnWB3JcByuRog86efn6If58pVyMSwwsZ1yL-94xd0n_9R4nqBti0pQ3m34mGGQNlms68G60ew34MF1OLj6ahpTUvXh7h_BZJKUJTokyY8wnzMd-EjFU_-IobgN-DOhX00-pwFlxyYN3Kbdam6nIDmG_cLbcbYpe-VfXt7Z_VZlWQb319Kvi8q-nxIwNS35JhD7dhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72042" target="_blank">📅 17:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=HDeaieBU9_ftkxHsx8le6WZ8wRmz5wNU2TT_RK97M7SW1v52u-HsWDV6NB1hEizwtT-dC_UXojidKzkz1OswO3wQbp76KRTxOf7lO0BkePIgc3tR7_-iTl4Lf7judcn3bH5t0jH7jXGY6irFd2l6NW_MtUkeEFnfHhkP0mH3DpxJwjwM1nejPwz9L0SXdirMXdd5-oMXR2Ls4Z5zWDQtt1pzEXTaqvcQpy_BIursjXKQ1ehZCap8vmIlTzNyqnboZGgOzv6RzDMtmuj8x2XDmyCdOeMxt3ypZNsRp45JqRwAmCnelvixLwyu5mMbM2RsCl7-xfpYDBH-yiWdiuL8uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05f244ea4.mp4?token=HDeaieBU9_ftkxHsx8le6WZ8wRmz5wNU2TT_RK97M7SW1v52u-HsWDV6NB1hEizwtT-dC_UXojidKzkz1OswO3wQbp76KRTxOf7lO0BkePIgc3tR7_-iTl4Lf7judcn3bH5t0jH7jXGY6irFd2l6NW_MtUkeEFnfHhkP0mH3DpxJwjwM1nejPwz9L0SXdirMXdd5-oMXR2Ls4Z5zWDQtt1pzEXTaqvcQpy_BIursjXKQ1ehZCap8vmIlTzNyqnboZGgOzv6RzDMtmuj8x2XDmyCdOeMxt3ypZNsRp45JqRwAmCnelvixLwyu5mMbM2RsCl7-xfpYDBH-yiWdiuL8uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره چندین دوس پسر داشته ده ها بار باهاشون رابطه ی جنسی داشته حالا اومده پیش متخصص زنان تا گواهی بگیره به نامزدش نشون بده پردش ارتجاعی بوده و سر اون پسر بیچاره کلاه بذاره.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72041" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=vmJ-XfoUBiLXbd1NFGGIRNue46WU1_hOSb8T59r4Lv0nu6FAeM7h1U0h3nBscEuP77cskyP_9F38MjPBbMZBleEyimt5mdVP5NxVA3sF3OTmUbXQOvBaxLlxqy56xAdPY08yECBHGXAVSqRsEF-MdAfHoN02RvfHsWRPuyCTeB_-7x8-BVq9d8gem2JHwBM5Gb9vH1WIe8vt_uOewcTOfEYHW9OPqK7tPGNMBMLvd6IfGB2yUbY4tEqSIdGiHKsDNjzOuiYIQxyz9oMfxQRqPhZPFlTIN-X8Su3StGD8_LURUOEZkc8PTi1yrB1WMi2fiQI1zYX0oMqU3aNs7C70aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/396f2961ce.mp4?token=vmJ-XfoUBiLXbd1NFGGIRNue46WU1_hOSb8T59r4Lv0nu6FAeM7h1U0h3nBscEuP77cskyP_9F38MjPBbMZBleEyimt5mdVP5NxVA3sF3OTmUbXQOvBaxLlxqy56xAdPY08yECBHGXAVSqRsEF-MdAfHoN02RvfHsWRPuyCTeB_-7x8-BVq9d8gem2JHwBM5Gb9vH1WIe8vt_uOewcTOfEYHW9OPqK7tPGNMBMLvd6IfGB2yUbY4tEqSIdGiHKsDNjzOuiYIQxyz9oMfxQRqPhZPFlTIN-X8Su3StGD8_LURUOEZkc8PTi1yrB1WMi2fiQI1zYX0oMqU3aNs7C70aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو تحلیلگر و افسر سابق سیا؛
اسرائیل با پرداخت مبالغی در حدود ۱۰۰ دلار، هزاران شهروند افغان را در ایران برای فعالیت‌های جاسوسی به خدمت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72040" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تو نمایشگاه خودروی تهران که تازگی تموم شد، تنها کاری که مردم نکردن بازدید از خودروها بوده ؛
جکِ ماشین رو برداشتن، با خودکار رو کاور ماشین کشیدن، با مشت زدن رو کاپوت G700، کارت استارت ولوو رو بردن، شید سقف ماشین رو خراب کردن، خار دستگیره در رو گاییدن، دوربین جلوی ماشین رو کندن، جکِ کاپوت رو کندن، با خودکار رو صندلی ماشین خط انداختن، دکمه صندلی رو شکوندن...
‌
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72039" target="_blank">📅 16:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=szdrFjO_Aj6zM6oQwFPqzRO0SjVPB--zOdvprLSLO9k9sC1WFSE27C1cdByKptVe18dibIe3AxWKVlcs-gpQfsQ8u8_zKx4lRb6zVECWXXtiMGE91KDZ89hEVTA7wYwguOH6IeW2bFdbI9dNwq83NPVFsLhd-C9a6Tkzl9ThUt9btGXH5WPbqfGTgdBA5A5Di7ODlP8lhPL9OolrtMNXSrsq8laV-ZDkan89DrNBiWSc8_PgmFUnfjOlz7NJfUcMiYkTBBuCyfvYkB8NfBZHNBZepX8jHYYM8zq5CpLSRy8XRRBcpwsbLGLiSzWOKQ4uTnjw3yzRZTlKFmFC5_vt_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1637ed0d1b.mp4?token=szdrFjO_Aj6zM6oQwFPqzRO0SjVPB--zOdvprLSLO9k9sC1WFSE27C1cdByKptVe18dibIe3AxWKVlcs-gpQfsQ8u8_zKx4lRb6zVECWXXtiMGE91KDZ89hEVTA7wYwguOH6IeW2bFdbI9dNwq83NPVFsLhd-C9a6Tkzl9ThUt9btGXH5WPbqfGTgdBA5A5Di7ODlP8lhPL9OolrtMNXSrsq8laV-ZDkan89DrNBiWSc8_PgmFUnfjOlz7NJfUcMiYkTBBuCyfvYkB8NfBZHNBZepX8jHYYM8zq5CpLSRy8XRRBcpwsbLGLiSzWOKQ4uTnjw3yzRZTlKFmFC5_vt_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
پیش از سخنرانی رئیس‌جمهور ایران در سازمان ملل، کانال‌های رسانه‌ای سپاه پاسداران ویدئویی مفهومی و ساخته‌شده با هوش مصنوعی منتشر کرده‌اند که تصویری از نخستین آزمایش واقعی (انفجاری) بمب هسته‌ای ایران را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72038" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=op882h7LBRhLz1ii_cSXCtlfuwSisnAJ1GxNKZQPiN6ihw_DOCS8hF4wHd1bWQL5Lza90XDDfaQLcl6kEfgXho3bCKOIdgds7UwBdrz6L_7G97ZJprmGLirTR0H0pH_zRXjGUQbXaYZWMkzGn_IrcaP56fV8tpT8-h7H-LZppdcMk67EFg1wMtIBQ6k84LLYw_Ga8sTXNs6HrYh6CtCWLr24jEhjrcbtuZH7qoee9AHlyUaZsNsoXsVg8Ff_QL6VaDv75BqfFdRwMBRQ9Bat2GV5QcwKSb1YvKf538oQTyKLRQrvcWHUUMCDP68-u22w2Yj61NYwFtfDYdJTo5Bi4V1rHVOF2rNI6InV_UKc3INsGIHphVCnSeBoarq3bpsmx1TbGMKO1nzsuiv3K-Y62CAHDGppMNP_XCfO08EUaKu0hwFO2nstf6vNTsjBXJxcHC_NYfbpSS5HgUITqHV2E41cS4wIRTdLdsxecIEWDPNf6zjuifEoyzrpATNHRFNdlfgACi6kl_6L8LixINKiMIgVOaSWlgX2h-kLbp-H0AkUrIfvSucbQjhe0YPlCITaArGatfqwNnC2dLHaRnuZVT4uuOTAt0Jn-X5vMgVGijJvf9Xbn6AWEBxmgVmarkCl1M88FxYjFms6PcPPGMozN5vSF-MS7MVBMJl5PWzTt5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3d6eda575.mp4?token=op882h7LBRhLz1ii_cSXCtlfuwSisnAJ1GxNKZQPiN6ihw_DOCS8hF4wHd1bWQL5Lza90XDDfaQLcl6kEfgXho3bCKOIdgds7UwBdrz6L_7G97ZJprmGLirTR0H0pH_zRXjGUQbXaYZWMkzGn_IrcaP56fV8tpT8-h7H-LZppdcMk67EFg1wMtIBQ6k84LLYw_Ga8sTXNs6HrYh6CtCWLr24jEhjrcbtuZH7qoee9AHlyUaZsNsoXsVg8Ff_QL6VaDv75BqfFdRwMBRQ9Bat2GV5QcwKSb1YvKf538oQTyKLRQrvcWHUUMCDP68-u22w2Yj61NYwFtfDYdJTo5Bi4V1rHVOF2rNI6InV_UKc3INsGIHphVCnSeBoarq3bpsmx1TbGMKO1nzsuiv3K-Y62CAHDGppMNP_XCfO08EUaKu0hwFO2nstf6vNTsjBXJxcHC_NYfbpSS5HgUITqHV2E41cS4wIRTdLdsxecIEWDPNf6zjuifEoyzrpATNHRFNdlfgACi6kl_6L8LixINKiMIgVOaSWlgX2h-kLbp-H0AkUrIfvSucbQjhe0YPlCITaArGatfqwNnC2dLHaRnuZVT4uuOTAt0Jn-X5vMgVGijJvf9Xbn6AWEBxmgVmarkCl1M88FxYjFms6PcPPGMozN5vSF-MS7MVBMJl5PWzTt5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
رئیس‌جمهور ترامپ برای دیدار با پزشکیان یا هر کس دیگری آمادگی دارد.
اما اینکه آیا نتیجه سازنده‌ای از آن حاصل خواهد شد یا خیر، دشوار می‌توان گفت؛ زیرا تصمیم‌گیرنده نهایی در ایران، «رهبر عالی» است و رهبر عالی، یک روحانی شیعه تندرو است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72037" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=D4bnDjLlwRUyVEuqMS0XBQBYWYrReTFYzsGce9fprzC2yCIiqr8ICjCjC0HPue6uUkpkCvtjpRwAXpy4AOwYcvjCbgU82C8rbBBRTX00Gy7preyc7l9eDgk8PZRKBYK1aRW5I1txBbC-aUtbAfQJ5624BtieGODVI46XGttZi87zHpx6oa6Oq7gcAe8PM-X3rim-OKiRrDFGQi5LyVjLQg5NdiAOCLO_coHBX6sqIHTD2Ht4oHhZDqN2lVwmApuEJrjaKsNuQ2DQknbS0amY52CpU_xxRmN7coGgxlzbti7tjjZdcypsyhK1X1L2_3mPA8fy0Ju38GnXgn1Hq2S7yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab0515ff.mp4?token=D4bnDjLlwRUyVEuqMS0XBQBYWYrReTFYzsGce9fprzC2yCIiqr8ICjCjC0HPue6uUkpkCvtjpRwAXpy4AOwYcvjCbgU82C8rbBBRTX00Gy7preyc7l9eDgk8PZRKBYK1aRW5I1txBbC-aUtbAfQJ5624BtieGODVI46XGttZi87zHpx6oa6Oq7gcAe8PM-X3rim-OKiRrDFGQi5LyVjLQg5NdiAOCLO_coHBX6sqIHTD2Ht4oHhZDqN2lVwmApuEJrjaKsNuQ2DQknbS0amY52CpU_xxRmN7coGgxlzbti7tjjZdcypsyhK1X1L2_3mPA8fy0Ju38GnXgn1Hq2S7yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
مسئله اصلی این است که ایران توسط روحانیونی دیوانه اداره می‌شود که دیدگاهی بسیار افراطی و آخرالزمانی نسبت به دین خود دارند.
این افراد هرگز نباید به سلاح هسته‌ای دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72036" target="_blank">📅 15:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=dcgJpw6K6f5qqmwdM5AKMC85NGGLVSwmDADrCL1SLt2bTZODsZIStRjqKxwGGxqAFCPOoSphIk8vj05df-Rhs69NLTzqZYbqiLsraJtsNCU-zBK_pyafZGlS2F9mPzfsNdGR7UilMjWMx2D0JPvJ1RcP3SskNrLmhSJZ83IGQuR2V3iVOvAN09aZIDzo_aHBJnub5Vy1KiNseveyoaMvTBPAcB_qy5sMMishLY8eZZbwx49UD3bzlWssrFolgrb8LfUCNrR3wHntMm2lyC0Qkf-TRwu5WYuwSVQECDB8hKUJqn-0OixKaxM-128FuM2tF62hZMCpYJtoFE93kylYkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb195e4e.mp4?token=dcgJpw6K6f5qqmwdM5AKMC85NGGLVSwmDADrCL1SLt2bTZODsZIStRjqKxwGGxqAFCPOoSphIk8vj05df-Rhs69NLTzqZYbqiLsraJtsNCU-zBK_pyafZGlS2F9mPzfsNdGR7UilMjWMx2D0JPvJ1RcP3SskNrLmhSJZ83IGQuR2V3iVOvAN09aZIDzo_aHBJnub5Vy1KiNseveyoaMvTBPAcB_qy5sMMishLY8eZZbwx49UD3bzlWssrFolgrb8LfUCNrR3wHntMm2lyC0Qkf-TRwu5WYuwSVQECDB8hKUJqn-0OixKaxM-128FuM2tF62hZMCpYJtoFE93kylYkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
ترامپ برای دیدار با هر کسی در سازمان ملل آمادگی دارد.
ما نیز برای دیدار با پزشکیان آمادگی داریم.
گمان نمی‌کنم در حال حاضر برنامه‌ای برای آن تنظیم شده باشد، اما قطعاً از چنین دیداری استقبال می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72035" target="_blank">📅 14:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شرکت‌های هواپیمایی «ترکیش ایرلاینز»، «پگاسوس» و «اِی‌جت» (AJet) تمامی پروازهای خود به مقصد ایران را از تاریخ ۲۱ سپتامبر لغو کرده‌اند و امکان رزرو بلیت نیز حداقل تا مارس ۲۰۲۷ وجود ندارد.
تحریم‌های ایالات متحده موسوم به «عملیات طرد اقتصادی» (Operation Economic Outcast) دامنه‌ی گسترده‌ای دارند و حتی هواپیماهای ایرباسِ دارای قطعات ساخت آمریکا را نیز شامل می‌شوند؛ موضوعی که شرکت‌های هواپیمایی ترکیه را ناچار به توقف این مسیرهای پروازی کرده است.
شرکت هواپیمایی «ماهان» نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72034" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_iawI-Usj0GVjqD1f3zs0zgy8DTWWUHO-rXin-LXQulrAJ0MX5Fp73WgUBDtANB4Kp1wuszdcpAbNynjhxfrZXv-YuWUOwlWaWJocjKgOqrGyErNKm5YnNFzzfTvloyi9mvzOtbSX0mDQ34OG33n8GA-LDNxYBB38EjD5jlZ1rPime3zVlM67JMZUYPIjpDwk_FlPIooLB7O2pnj2sxM5IDGlDE6AOzajY774ObA-wCeoPWd6yQ-bbQlqyXwzGGUNVdzJ0TqD4slAe8dDqT0mQrG_hfLX2yKAUBkGpSLt4vvSto3p3xJtyEcLX4kypUvtqZZiK8TBl66fuBKotsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری ژاپنی «کیودو» و به نقل از یک مقام ایرانی که نامش فاش نشده است، ایران پیشنهاد کرده است که در صورت برداشتن گام‌های اولیه از سوی ایالات متحده برای کاهش فشارهای نظامی، تنگه هرمز را ظرف هفت روز بازگشایی کند.
این پیشنهاد که گفته می‌شود از طریق واسطه‌ها به واشنگتن ارسال شده، خواستار ازسرگیری مذاکرات با هدف پایان دائمی خصومت‌هاست.
این مقام ایرانی اظهار داشت که دستیابی به توافق همچنان امکان‌پذیر است، اما احتمال دیدار میان ترامپ و پزشکیان در حاشیه مجمع عمومی سازمان ملل را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72033" target="_blank">📅 14:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPc8osDYHn3jbAucrtLJoLVv93zKe4FdZpCdgzcYCJcfe4OAOiqmDeef9fNLBK9klKXjMgzB1ANn89b0DxaR39ibEI-LlYPrdL2o53IrGTS6KE2oK8mNKN4qd66UfC4wjzq4Tl9SI8n_vS9MGhGpPDC-Q_pX97wfqPorsqFQ1lhuNoGh9pfH6xtcRI4EVbEgXLUZ9pAL9QG3rjDLt1frt7YXUCtAfuEWjWlk82IodAOt64d9ePCkaE1Tev-eK3F7LZ4OVXWJ9moib-Mz4qddnrYnepJ0orUXPzNoqT7OAG0KxXx-yx2u3nOKSylh5Aiog4j64hqgv_kwRfaUQUPz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72032" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=gjL07BLfILxaXUs-uYwV729f7_kzQPKvINB0muFHd064A4JxBFGugDslWmZPQS-KimFehh8yc9xG6vCm3mh1Kt23xpWqpRDR8iAk6-FXwUTq1FfGkk6csNXMZEanrbpWzoPxrOgJDPG6RykGUC4WE6x6mbEtH3Gq9Dkrhhi0nhWg6pX3-uqkcJ-Yf1S22hI4csJRSU-JuUtBmHKQlR2khBVCfNwx-8cr1t3y69WA1dhyoMJGyh3n6G_MEhpw5zytKYxDWOqCRGTl1IUyxEM7erMTm15692RbRvxxDfMqEiX2_u7NuH-K0OIZxz1-0YVng6V18_K0MeFJVRFMNxVeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=gjL07BLfILxaXUs-uYwV729f7_kzQPKvINB0muFHd064A4JxBFGugDslWmZPQS-KimFehh8yc9xG6vCm3mh1Kt23xpWqpRDR8iAk6-FXwUTq1FfGkk6csNXMZEanrbpWzoPxrOgJDPG6RykGUC4WE6x6mbEtH3Gq9Dkrhhi0nhWg6pX3-uqkcJ-Yf1S22hI4csJRSU-JuUtBmHKQlR2khBVCfNwx-8cr1t3y69WA1dhyoMJGyh3n6G_MEhpw5zytKYxDWOqCRGTl1IUyxEM7erMTm15692RbRvxxDfMqEiX2_u7NuH-K0OIZxz1-0YVng6V18_K0MeFJVRFMNxVeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت عجیب سربازان روس که به بالای دکل ها رفتند تا با استفاده از سامانه های پدافندی دوش‌پرتاب(MANPADS)با پهباد های اوکراینی مقابله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72031" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72030" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOyFH_TnOznpDw8o-vWp20R7GMYGokAfwoF4s5FwGiJY_q3VoEnfrcZT-MEUhF7EuwT6yixkRblXyjzdcDVJCLhW0r87ZJNDBWMioEeNJ5TWzOsZGgOof_BpnO5fVVGrURjwm_6mscYP4QVIRNiNYHyp4LlIfvr4TcnsFK3x-JPUo1ZgER-Bya0q9jiww28V8cPrlO6oKcCqa3KKdDJXq4iG-HMvFlXiyA6p__kuq2KccpBrYgf3ww4-oWONHJfS1zQs8k2XpJThP4Wo7MVVXEeL27VHhJ4fHxlKDAm8dOC2mBKXGv2yJQnMEmr_bWbAxp6-Eo7_-rUnsHrq1g4UsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72029" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCAxwowg34yv5T1dZ9cQ7PM0UE6CefyC_ERtRGINGV8sVmskJTHYP5RVOuRy4miFYtlwkjSGlCiyATUXVsOtRXM6SJzSsmbZgVoEtqYNS9egyug2t71BsEImHqWMRCnZCULtCAmCvvBYWprJOkgPpFLkxRKrJB8xgL7WPRIwGwJbKezuuRNdUxeKo3-X-oUTFI0EtFzWrkKY2o5z1Z34XBkZXzQac9838A25_VM6ODbFhf0TBR4V2eCExfmLUtBg49gQw8k2VdotZ_XG9VBzbS9BGwI76rtKMp57qKtp540OTNblKq0RiofF2e8FiLKduogl22C5xM77ZWzdy_ELMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست وزیر، گفت که بریتانیا پس از حملات پهپادی و موشکی حوثی‌ها، پشتیبانی «سوخت‌رسانی هوایی دفاعی» را در اختیار عربستان سعودی قرار خواهد داد.
این پشتیبانی که انتظار می‌رود در روزهای آینده آغاز شود، شامل یک فروند هواپیمای نیروی هوایی سلطنتی وویجر مستقر در پایگاه نیروی هوایی سلطنتی آکروتیری در قبرس خواهد بود.
مقامات بریتانیا گفتند که این استقرار «محدود به زمان» خواهد بود و احتمالاً «برای چند هفته» ادامه خواهد داشت.
برنهام گفت که این اقدام به دنبال درخواست عربستان سعودی برای «حمایت نظامی» و با هدف حفاظت از ثبات منطقه‌ای و منافع بریتانیا انجام شده است.
«عربستان سعودی حملاتی را تجربه کرده است، به دنبال اختلالات احتمالی بیشتر است و ما باید این مسیرها را باز نگه داریم و از این رو با این درخواست موافقت می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72028" target="_blank">📅 12:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=EYFeG_tl8WOY4AhVHJViuiD2T3uywAYtEJ4aLJBrKOwzf7GCvHz_NPuN_GE5de6rhKoLTFE3Fw3dg1XkNLw-9CQhH1dOAGNnYY6nPIfB3IMVjSHmWpgYD2beSecdUUzJJUSJTPh8BAtEYZnXfSMRKUFE9p08pJx2-Z9A9LjMR8WQ9m4SsU_GrUABZsp_Z8L_54WdgHIkQ8SoweZ7HzzH61e6rAlMEIGZR-y8cxVhc1x4e7X4AfrR2lXOd_8PU05aFmMPEqoNsyModjJywJwZWb4e_AnV2b7fz-r6W6hrhLEHwCWdk5TwzNN3mM1B7diF1Ccz5YGL6sdE-a3j1IEqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=EYFeG_tl8WOY4AhVHJViuiD2T3uywAYtEJ4aLJBrKOwzf7GCvHz_NPuN_GE5de6rhKoLTFE3Fw3dg1XkNLw-9CQhH1dOAGNnYY6nPIfB3IMVjSHmWpgYD2beSecdUUzJJUSJTPh8BAtEYZnXfSMRKUFE9p08pJx2-Z9A9LjMR8WQ9m4SsU_GrUABZsp_Z8L_54WdgHIkQ8SoweZ7HzzH61e6rAlMEIGZR-y8cxVhc1x4e7X4AfrR2lXOd_8PU05aFmMPEqoNsyModjJywJwZWb4e_AnV2b7fz-r6W6hrhLEHwCWdk5TwzNN3mM1B7diF1Ccz5YGL6sdE-a3j1IEqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو صحبت کردن این پسر با یه پشه که تو اینستا خیلی وایرال شده
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72027" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/72b152b531.mp4?token=FlWoSxGBEj_MLvGTUmcMwDdZnEMEdRbr8CZb5wYP4u_5TXVwvZOmeAks5yLAZhf5VOJb0ENfdqmWDq6H018goW0XgHPQQ-NMkAT9pEFmwazhtkBZFmaOP_BnSzcpdFW9YJVduFpvaVmLkYOQWzusl87VZM1o1HQ5HtOkjNRrZJw3T2OviU8BHp-uKIvujc8cDakJRUvh2IIx7863JW0tDBzPigpEcGstaamPnFnG2b_8eH-PiX5aR0mCjByxqzuV6PeTj03GZqmdoZO96jgjWvQxB0Ht0WbjOSqbOvJfBZlFVWDkvY2_TzbcSVz0842HP6_Vo-2-8Hukvio3CJ-qTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/72b152b531.mp4?token=FlWoSxGBEj_MLvGTUmcMwDdZnEMEdRbr8CZb5wYP4u_5TXVwvZOmeAks5yLAZhf5VOJb0ENfdqmWDq6H018goW0XgHPQQ-NMkAT9pEFmwazhtkBZFmaOP_BnSzcpdFW9YJVduFpvaVmLkYOQWzusl87VZM1o1HQ5HtOkjNRrZJw3T2OviU8BHp-uKIvujc8cDakJRUvh2IIx7863JW0tDBzPigpEcGstaamPnFnG2b_8eH-PiX5aR0mCjByxqzuV6PeTj03GZqmdoZO96jgjWvQxB0Ht0WbjOSqbOvJfBZlFVWDkvY2_TzbcSVz0842HP6_Vo-2-8Hukvio3CJ-qTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی عظیم در دنیپروپتروفسک؛ صحنه‌ای آخرالزمانی؛
پیش‌تر، وزارت دفاع روسیه اعلام کرده بود که نیروهای مسلح اوکراین از تأسیسات غیرنظامی برای اهداف نظامی استفاده می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72026" target="_blank">📅 11:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=A21dZAOjir5KoxXlD1BvljSYhOg-9zqs7giyuBqmMoEAnZdUsDKzxM7Fp5ceLEEpLAvu7gqZlaxvwOchzEhtJ-cq35Vk_7GlDNwRMbWs11KOT7lIvPsUMhq7qUlhI9H0VQVq4_dwn80ey81D5DuW8-nWSDt3uLYCDDDfJ7QvjXBaANAofF8vc_K7rkYI5U6gGIqmyWWZCWiWkImT5tupKl97ezBCIp72W08oYvyd6pPcbyel_CCnHN5bDehrgP6cKNaOvo-G_fQlr6J7z7aElzdKBL4xsTf51ShQkewIndzX-3HCLyGsQfpNRyPirsehLxyLGDI8lyDsMvedWR3xqHNbeF9POWpiy-uaU8FQt3uR9qMeu4ye9WOt7w6sILqLetOreepCut-ZibzLpvhVmoKoTh9YEJB6FYJcTA-5SpiElPmE-w66EnV8QPScf2o2wMVNhp6vHoP5kDTrEFztu5h3K_pKrl-KnfRpK1wvjSakqAfRfxvlQtUtXYRoDEFaOKuSemuPpNLFmuoKR2UiJXx3F_MiEb4UCD9k2K2yUXPwh0PEKSMhToJHNRmAuO2MrF1PxCRazP1nMwUsoPJg3UflzmpSkS2Ac0xOI-txkVt_m-LT79Qt-FWCkbZqCT8vLr2r9K-1Lvml9IqRzaDaHkUU0AxL_UrC5HxBbvAeIaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=A21dZAOjir5KoxXlD1BvljSYhOg-9zqs7giyuBqmMoEAnZdUsDKzxM7Fp5ceLEEpLAvu7gqZlaxvwOchzEhtJ-cq35Vk_7GlDNwRMbWs11KOT7lIvPsUMhq7qUlhI9H0VQVq4_dwn80ey81D5DuW8-nWSDt3uLYCDDDfJ7QvjXBaANAofF8vc_K7rkYI5U6gGIqmyWWZCWiWkImT5tupKl97ezBCIp72W08oYvyd6pPcbyel_CCnHN5bDehrgP6cKNaOvo-G_fQlr6J7z7aElzdKBL4xsTf51ShQkewIndzX-3HCLyGsQfpNRyPirsehLxyLGDI8lyDsMvedWR3xqHNbeF9POWpiy-uaU8FQt3uR9qMeu4ye9WOt7w6sILqLetOreepCut-ZibzLpvhVmoKoTh9YEJB6FYJcTA-5SpiElPmE-w66EnV8QPScf2o2wMVNhp6vHoP5kDTrEFztu5h3K_pKrl-KnfRpK1wvjSakqAfRfxvlQtUtXYRoDEFaOKuSemuPpNLFmuoKR2UiJXx3F_MiEb4UCD9k2K2yUXPwh0PEKSMhToJHNRmAuO2MrF1PxCRazP1nMwUsoPJg3UflzmpSkS2Ac0xOI-txkVt_m-LT79Qt-FWCkbZqCT8vLr2r9K-1Lvml9IqRzaDaHkUU0AxL_UrC5HxBbvAeIaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اخوند توضیح میده چقدر رژیم جمهوری  اسلامی پول خرج اینا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72025" target="_blank">📅 10:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=oM3JTz_kyIPjhe5NORI33M5wuqxU21ggEr52Hzk6HYS5GxX7hih9gpM_e8yf2RZ3FGM1Qu2D6fcYSJ2iMb-f5Vr9RKV8cJfbT8n6AquC3i1V9QDfVQGvU2a8dQLTWJw2khKR-zCwcCE-5t0_5-GHpuyz4u-PBZXtEI1jiPxU6leTRI2V_fYTq1OoxyjuYsJbDpg1IwFloAwpAS0VvDBUA7dnlBdA9L-lECmKiqh4y4obxh-wSK719UxNvFJttUa4GsDNOP0TkjKQoXUOsWf8OkIzksVggO3VvSU5f-MPQ-WVjBf7Me8GbibgbulXsb3mbs9E6b1jKKtneV1vBtCcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=oM3JTz_kyIPjhe5NORI33M5wuqxU21ggEr52Hzk6HYS5GxX7hih9gpM_e8yf2RZ3FGM1Qu2D6fcYSJ2iMb-f5Vr9RKV8cJfbT8n6AquC3i1V9QDfVQGvU2a8dQLTWJw2khKR-zCwcCE-5t0_5-GHpuyz4u-PBZXtEI1jiPxU6leTRI2V_fYTq1OoxyjuYsJbDpg1IwFloAwpAS0VvDBUA7dnlBdA9L-lECmKiqh4y4obxh-wSK719UxNvFJttUa4GsDNOP0TkjKQoXUOsWf8OkIzksVggO3VvSU5f-MPQ-WVjBf7Me8GbibgbulXsb3mbs9E6b1jKKtneV1vBtCcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال گذشته مردی در حال قدم‌زدن با سگش در کامچاتکای روسیه بود که متوجه نزدیک شدن سونامی شد و با تلفن همراهش از آن فیلم گرفت.  لحظه‌ای هولناک و در عین حال شگفت‌انگیز از قدرت طبیعت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72024" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu6kGSs11XPV9GiVqyVG5eFIs9zGgzvlsKJsqIEx7u12THaHgfXOiE0xUR4EllgPo9Xk3gKoYIOs7rb58rlkCn7wSb0c1al7gBK3D5EM9JABAlyreZu-xunwqHPzl3uR-a-flCHJkfcLxQ4NTcSs0Wwvzbmmk3Erp1rG-ScXBn5uCgrUO-leN6uWTRq-8ch65CiC16EPHLJrc8JIM6m6VEIGBxIUZ2xua71BNuxzKOtbZZyKoIXC9QAMcj_orIddgpz8VQsrZaGCHO9gAoe1mbzzy7-jkHHzbXOMglMRf0c4QVoutokCsfD1-uKr4f8aQgnZJ9T0vnqeZ88utTuZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پی درخواست مجدد عربستان سعودی برای اقدام نظامی، در تعطیلات آخر هفته احتمال صدور فرمان حمله به حوثی‌ها (انصارالله) در یمن را بررسی کرد، اما در نهایت تصمیم گرفت از انجام آن خودداری کند.
دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، پیش‌تر تمامی گزینه‌های مربوط به حملات هوایی را آماده کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72023" target="_blank">📅 09:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8969619843.mp4?token=vS8bv56mcTdM_Vd3P0_WQeb08gp46hOHmkusKEMXdEfCrBXmcL5c5pwYYOoM3hUlao2leSpzjQ3SC0wBgbpGUyTm2ZrbTvVbX2KJ6cr6nV2yr9t7r-MUJtuXeAS0zm1Eu_EppSZLS8dFlwP6FQkRCvg-lpdgj8Yxz-JS5WyRK_FTvgn8X_IxiMmE4DlGeTmCjR1BAG_tLKHYAmFOlraeft-Vn_Gj4AqlccZioAB8gCqECuBlT8JsMkKziUY_VlB1i0CVNUgPzIPfU1QEcqzNraJ5OlzsBAOsj7v1Lb25aCOI7yikNVBzcgPqwb_9iABY3j8VDogtz0BQZfZvjYcysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8969619843.mp4?token=vS8bv56mcTdM_Vd3P0_WQeb08gp46hOHmkusKEMXdEfCrBXmcL5c5pwYYOoM3hUlao2leSpzjQ3SC0wBgbpGUyTm2ZrbTvVbX2KJ6cr6nV2yr9t7r-MUJtuXeAS0zm1Eu_EppSZLS8dFlwP6FQkRCvg-lpdgj8Yxz-JS5WyRK_FTvgn8X_IxiMmE4DlGeTmCjR1BAG_tLKHYAmFOlraeft-Vn_Gj4AqlccZioAB8gCqECuBlT8JsMkKziUY_VlB1i0CVNUgPzIPfU1QEcqzNraJ5OlzsBAOsj7v1Lb25aCOI7yikNVBzcgPqwb_9iABY3j8VDogtz0BQZfZvjYcysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود: ‌دونید شماها گوهرید یا نمی‌دونید؟
دخترها : بله می‌دونیم نه نمی‌دونیم
مسعود: می‌دونید من اینجا الان اسمم رئیس‌جمهوره؟
دخترها : بله
مسعود:  می‌دونید من از یه خانواده معمولی به اينجا رسیدم؟
دخترها : بله
مسعود: یجور این مملکت رو درست بکنید هیچ بیگانه ای نتونه بیاد اینجا شماها بخواید میتونین دیگه من تونستم شماها هم میتونید دیگه
خنده های وزیر آموزش پرورش فقط
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72022" target="_blank">📅 09:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=iG4PgUDikauynloIZx1u5AII5r9CngJHJrI9gUEZmvTI-CVOn5jqBE1BMRLsPfqhfHN0WukmbQIH_6pglsfpdNOoi0J-cTSSH0NSBF2KEetEiq2RT4mth9heUA1eOX4L1RCMrU40Ju6fO4EVJm8feCMSzClRvw3zIB-zdIgKupEanFghgpFUumxkaFqvGSZTo5m3A_GNXMmrW7MdabT2hAFZHU1CJ-_b163xlBteYRY-aF9BoHOVYVwOz2X4KayWYjYRGnTVQqZiKuGy2pVGkLbFv1R9haePJjh77_8bBIB7zNC3LaL90WFOfjfiPOft7dcOe8jaiB86lSfd9ho2tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=iG4PgUDikauynloIZx1u5AII5r9CngJHJrI9gUEZmvTI-CVOn5jqBE1BMRLsPfqhfHN0WukmbQIH_6pglsfpdNOoi0J-cTSSH0NSBF2KEetEiq2RT4mth9heUA1eOX4L1RCMrU40Ju6fO4EVJm8feCMSzClRvw3zIB-zdIgKupEanFghgpFUumxkaFqvGSZTo5m3A_GNXMmrW7MdabT2hAFZHU1CJ-_b163xlBteYRY-aF9BoHOVYVwOz2X4KayWYjYRGnTVQqZiKuGy2pVGkLbFv1R9haePJjh77_8bBIB7zNC3LaL90WFOfjfiPOft7dcOe8jaiB86lSfd9ho2tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو رو به خاطر «فیک‌نیوز» از کاخ سفید ممنوع کرد.
فاکس‌نیوز + ABC، CBS و NBC در اعتراض، پوشش تلویزیونی مشترک (TV Pool) رویدادهای ترامپ رو متوقف کردن.
نتیجه: مراسم‌ها بدون صدای زنده پخش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72021" target="_blank">📅 07:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72020" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDdPZVtDBfpr3BZeTGLu6zQo6vu7E6aNJ8VNd5y01f3X6YB_Vh5h_MVbQ3K7p_2wlC95-xygWz0LC-zEL-e8oa2Xfi4aytZh761zUiiscswcGij1j_kXMSJ34CeK_8CWY_Upyoez0q-6dpeuKIZrzAR7LMXglHFfuwBynByhSdKW-ORB5OYX8NCsSF5zZ42RmLqrldQm6wuP5JFlpmm-DoFKcmAGS96BtWSw_k50Qz9N3J1pVi7o0fisUuJxc96VfWZG7uch_yV20TgTqLPzqwoYwcZLpSEXjr-Oe3XQQiig8QvEj8lMNg_dzYzuD2qaRNPPfsdJfvIhfrSOI3M8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72019" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=M79QZmkcuV8s6164JNDMjWeyMTPFFaF5epAx2uai9s8obNiaY2w6P7uz_mDVf4ItvEkg6cwPupuUr59GU7cHSWiff_76kXw4q019P37fAF6BBKui4PU5Ni6tFdNJwxLndihjfYE47zITorJQhrAq6EyGvViUlEWsMSiJhG6fvWTfn0jQvxzHYh1R0ZHkYnlNyxpR2o699M7oRvIP5l1yJbKl13m6mWl5GbvnavWqjPfvazHjXmHOBKgKio-7uZaMGjjFu6So1yfZcXELWhfpc6ci_-139IUGKUc7Oi_Qf-Nw6uBbdyVztZ2wEHegO33ROldFA0BuMPPZ8mIAx5ZR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=M79QZmkcuV8s6164JNDMjWeyMTPFFaF5epAx2uai9s8obNiaY2w6P7uz_mDVf4ItvEkg6cwPupuUr59GU7cHSWiff_76kXw4q019P37fAF6BBKui4PU5Ni6tFdNJwxLndihjfYE47zITorJQhrAq6EyGvViUlEWsMSiJhG6fvWTfn0jQvxzHYh1R0ZHkYnlNyxpR2o699M7oRvIP5l1yJbKl13m6mWl5GbvnavWqjPfvazHjXmHOBKgKio-7uZaMGjjFu6So1yfZcXELWhfpc6ci_-139IUGKUc7Oi_Qf-Nw6uBbdyVztZ2wEHegO33ROldFA0BuMPPZ8mIAx5ZR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72018" target="_blank">📅 01:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdV0oul2-HGQRY0IvS9NpTfa8KFYzmKpJU_rOl5yoq2DTZkDCH_NLGo9I77_1awxwWNRhqjjmMo0NZfdx17MW4cJOBoWIND2D5_sioFomK_2NgTb-g8qsfmvvl4RHm6GibSALjjnPPZAF9KHwl8YWBEdklH6Qz3t3-_jbAsaGaBjeyeraOa-vh_GbQYwxBE0tvh6IhmSNcPr96d7YELR4nMRtdE_nNJmMEZ68xYI8WM0OOYItAj9aG6yqTx7uhQKf0LbpE4NzwAwwcSSJy2XzkQBdVfeh4SNNpDciCiTY4b4Oy3AYNKivTEDFzfHXrD1kodvUKIInQH_r0t1nlU1QIPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdV0oul2-HGQRY0IvS9NpTfa8KFYzmKpJU_rOl5yoq2DTZkDCH_NLGo9I77_1awxwWNRhqjjmMo0NZfdx17MW4cJOBoWIND2D5_sioFomK_2NgTb-g8qsfmvvl4RHm6GibSALjjnPPZAF9KHwl8YWBEdklH6Qz3t3-_jbAsaGaBjeyeraOa-vh_GbQYwxBE0tvh6IhmSNcPr96d7YELR4nMRtdE_nNJmMEZ68xYI8WM0OOYItAj9aG6yqTx7uhQKf0LbpE4NzwAwwcSSJy2XzkQBdVfeh4SNNpDciCiTY4b4Oy3AYNKivTEDFzfHXrD1kodvUKIInQH_r0t1nlU1QIPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبری فاکس نیوز به نقل از ترامپ:
«در حال تصمیم‌گیری هستم.»
اریک شان، خبرنگار ارشد فاکس‌نیوز، گزارش می‌دهد که دونالد ترامپ، رئیس‌جمهور، در حال بررسی گام بعدی خود در قبال ایران است؛ آن هم در شرایطی که برای دیدار با رهبران کشورهای حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل در روز سه‌شنبه آماده می‌شود.
ترامپ در حالی که گزینه‌هایی همچون اقدام نظامی، تداوم فشار اقتصادی یا تلاشی دیگر برای دستیابی به توافق را سبک‌سنگین می‌کند، به فاکس‌نیوز می‌گوید: «سؤال من این است که آیا و چه زمانی کل کشور [ایران] را نابود کنم؟ بهتر است آن‌ها درست رفتار کنند.»
این هشدار هم‌زمان با تشدید تنش‌ها در منطقه مطرح می‌شود. ایران تهدید کرده است که در صورت انجام حملات جدید از سوی واشنگتن، علیه منافع آمریکا دست به تلافی خواهد زد؛ این در حالی است که حوثی‌های مورد حمایت ایران نیز به سمت عربستان سعودی موشک شلیک کرده‌اند.
ترامپ همچنین می‌گوید که برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در هفته جاری آمادگی دارد، اما در حال حاضر هیچ دیداری میان این دو رهبر در برنامه گنجانده نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72017" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612f18036a.mp4?token=ZVkDp6n4AqVRznrtc-79OhTEo8wspXtRSHyaOyJx5Lvi-TSVIgles-ET0YhqrJvO4QTaWmQZ6Z-sUDlNRGic8ACZlkBGxe--sxoIOO8U008s7MyojXoZE8_tpZFV8orIsxva0xybe02azkf_5RqJXHBVkVZ9evgnb3hc44HcPSTf-ZrbvODEaKX5GhW79ELbnYrpHTBVUYwvsNo4K_-HbQ82TZ9xgzRJUgZlbySFDc16f_XrDb89HJKKSJYXi9-wGeCHkPNfVNToNWgUM9N7B9AVCxJp2X-7wjK1X5gX3PjH6j3nnbvLt_aDsXbYhIyLr5cuPY3fHtqMxVd7yT_mvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612f18036a.mp4?token=ZVkDp6n4AqVRznrtc-79OhTEo8wspXtRSHyaOyJx5Lvi-TSVIgles-ET0YhqrJvO4QTaWmQZ6Z-sUDlNRGic8ACZlkBGxe--sxoIOO8U008s7MyojXoZE8_tpZFV8orIsxva0xybe02azkf_5RqJXHBVkVZ9evgnb3hc44HcPSTf-ZrbvODEaKX5GhW79ELbnYrpHTBVUYwvsNo4K_-HbQ82TZ9xgzRJUgZlbySFDc16f_XrDb89HJKKSJYXi9-wGeCHkPNfVNToNWgUM9N7B9AVCxJp2X-7wjK1X5gX3PjH6j3nnbvLt_aDsXbYhIyLr5cuPY3fHtqMxVd7yT_mvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکردشان بسیار ضعیف است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72016" target="_blank">📅 01:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72015">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0z_2PAzUAjH1k6lm2ZMOgnGy7WVoOdcwjk0v28F-LMLYI3Y8uR6WnFTrhcMpCG562iTF-pgRj2HIBlKeFxCrJOIxIOsMEKGyN7djXx9jsTdmjO2jX64O6nh2_J5bl4AvwGfsfsRL_ylBmdUkYSOqU_U8cuFPEnbPkTVKQXk2f18LtP9C7Ijr_hPqJi60OT-oNvK2MuOYD1dXkgEFvJDets9Oudh0b12J4kbc3lM_Vh5cKEttQ66ZlwrWPy_xYCfT37ZyLoZO4xPxIIr3DOmlheVVduSwDvuZtaaTd9paydRdwNpoYDFHqs4UqjTJHryheAL8km-dXDNkw58pllVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امجد طاها، روزنامه‌نگار و تحلیلگر اماراتی، با انتشار پیامی کوتاه نوشت:
«اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه. آماده باشید.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72015" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72014">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترکیش ایرلاینز پروازهای ایران را تا مارس ۲۰۲۷ متوقف کرد؛
یک نماینده شرکت هواپیمایی ترکیش ایرلاینز اعلام کرد تمامی پروازهای این شرکت به ایران دست‌کم تا مارس ۲۰۲۷ در برنامه پروازی قرار ندارند.
این شرکت همچنین اعلام کرده بازگشت پروازها پس از این تاریخ نیز تضمین نشده است.
این تصمیم در پی تشدید محدودیت‌ها و فشارهای بین‌المللی بر صنعت هوانوردی ایران اتخاذ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72014" target="_blank">📅 00:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72013">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyJuopKfEPBX__k0xa7sC3FgQUKV8B0rXFMwq2cVFtaOD2g0CiJUPr1Vmhz2Owayluyvw1NnnrDm9k1xDMrnPGTtIhFXdTPVbO_D_fP-JCNfR86aMkRftRmKM-Ys_DMhkljxG5xoZN1cZ5hHBlc6uqLJO3zPxtwwr0on0O0i-rPjUc8opZytcU4BMxoisxl7eF4kf7DZEaePEUXx_EkpnCUSEW5Jwu6PRfvK1r8ndKEvTe2U_NSN5CU8HgAo8ekLIOuZO7AwqoR9W3xBKhbmsDB6lNrBKhVZh6Q1sbfcYyHc4acOpFSQf30xEwcnJddsBbmn09p9DVVPC3CauAuacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛مقامات استان لوبلین لهستان در پی حمله هوایی جاری روسیه به اوکراین، هشداری مبنی بر احتمال بروز خسارات جانبی صادر کردند.
هوانوردی لهستان در حریم هوایی کشور در حال فعالیت است و وضعیت تحت نظارت قرار دارد. به ساکنان توصیه می‌شود منتظر اطلاعیه‌های بعدی باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72013" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72012">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">#فوری
؛حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی — که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است — فعال شد.
جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72012" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72011">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxkfypU0PtI_Qqapxf6WJCPrIvMKG8V9LLhLvykXx9KqUrISFPuSkDqLTesDkI4EkdmkNyuBTOasZwix4oMWRhgkq2KnNtaJd9rW5JGEPdufvtIEtgeOzwUo8R-kznuWYr39en3iRmTq-eNd8rIWfsRmUG0bfH2ScUkGiNx4LXb2bH0oj9dWvsmbRxlOYsgxts86MM0duqTcuN43SrITHne7cpQLytoHgtDKkbtkqBVYRNfKyykW-ZQFn2BDNdKb6op2gxSDG6HDVUV7od4Pi73KNsUCRT230vGx4iL12dStiWBEO8_fHGKgc4QvAF6hOkDSNyzTFtegWWfD3EUdBnWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxkfypU0PtI_Qqapxf6WJCPrIvMKG8V9LLhLvykXx9KqUrISFPuSkDqLTesDkI4EkdmkNyuBTOasZwix4oMWRhgkq2KnNtaJd9rW5JGEPdufvtIEtgeOzwUo8R-kznuWYr39en3iRmTq-eNd8rIWfsRmUG0bfH2ScUkGiNx4LXb2bH0oj9dWvsmbRxlOYsgxts86MM0duqTcuN43SrITHne7cpQLytoHgtDKkbtkqBVYRNfKyykW-ZQFn2BDNdKb6op2gxSDG6HDVUV7od4Pi73KNsUCRT230vGx4iL12dStiWBEO8_fHGKgc4QvAF6hOkDSNyzTFtegWWfD3EUdBnWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلندی ها به این شکل پرچم فلسطین رو از دیوار کشیدن پایین
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72011" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72010">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=bNiDG-rHoEvgdLxlbOpAb7JLAKRYUT0wdYsZ8uUdzdDgfY_ksWjN7TZ-lYig7LolJZlTA1opjt581Zq0vYBy7tQvFcG7sG4ss42hx5P2gAllonnxzfTuW_dD6hFmImzXB1BFI7qpQz6QFjM_fZQ9-EdqPtgXNF9qtCVxZbdRBQfpZc9M_h1Mgd8J_KRNzL0MDSMn2oZvTr3xUtB4BQvTYBFMdSptonK-Q5fijuvTdvTGeny6yFECD0wD3SRP3vGK6gKAvQJfPc5T4hnNtc3IHDXPE4GRjaz5hVbnFwH5U5-JVIWAlGMB0Dc9djzW08afMLbHHwrBcAX_oE86rIb8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=bNiDG-rHoEvgdLxlbOpAb7JLAKRYUT0wdYsZ8uUdzdDgfY_ksWjN7TZ-lYig7LolJZlTA1opjt581Zq0vYBy7tQvFcG7sG4ss42hx5P2gAllonnxzfTuW_dD6hFmImzXB1BFI7qpQz6QFjM_fZQ9-EdqPtgXNF9qtCVxZbdRBQfpZc9M_h1Mgd8J_KRNzL0MDSMn2oZvTr3xUtB4BQvTYBFMdSptonK-Q5fijuvTdvTGeny6yFECD0wD3SRP3vGK6gKAvQJfPc5T4hnNtc3IHDXPE4GRjaz5hVbnFwH5U5-JVIWAlGMB0Dc9djzW08afMLbHHwrBcAX_oE86rIb8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر این پسر رفته تو اتاقش سیگار پیدا کرده
و پسره هم این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72010" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72009">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ مراسم افتتاحیه (بریدن روبان) پد جدید بالگرد کاخ سفید را برگزار کرد، اما به دلیل غلبه صدای بالگرد بر فضای مراسم، سخنان او اصلاً شنیده نمی‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72009" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72008">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=KWbDLlaSVboXN-NJ_OzeBaBN7LB8_dS-sl4PuhYy11FAmHG0kEddVph9ivFYjVaAYJemizt6658wqBJ_OQsTSReV59hQJmwBI8riezyJ-ZMi4SFH-XEZGKH8bcp2YNrd7ISauu0zTvxiQ30Qasp7Vsuc4LB_pddhDBGmPPGGAhQioauVwyNdWL1EI6AVqzi12Bxc4YRHeok9MSoqlSvTSa6E3Afrnz8dnovwZBdtp5lEzhWb4M0awlK-6q6eXskQd6EOTll6zdZeFdHHdWf73FJxSMyG0-RmKAil-zqV3tkfLbnlHTpFv-gdPtYb56kIxqEHIQLhAGLfE_Z85KY_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=KWbDLlaSVboXN-NJ_OzeBaBN7LB8_dS-sl4PuhYy11FAmHG0kEddVph9ivFYjVaAYJemizt6658wqBJ_OQsTSReV59hQJmwBI8riezyJ-ZMi4SFH-XEZGKH8bcp2YNrd7ISauu0zTvxiQ30Qasp7Vsuc4LB_pddhDBGmPPGGAhQioauVwyNdWL1EI6AVqzi12Bxc4YRHeok9MSoqlSvTSa6E3Afrnz8dnovwZBdtp5lEzhWb4M0awlK-6q6eXskQd6EOTll6zdZeFdHHdWf73FJxSMyG0-RmKAil-zqV3tkfLbnlHTpFv-gdPtYb56kIxqEHIQLhAGLfE_Z85KY_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس:
ماه نوامبر پیشِ رو، لحظه‌ای سرنوشت‌ساز است؛ یا در برابر این دیوانگی می‌ایستید و یا با آن همراه می‌شوید. و ما قصد داریم در برابر آن بایستیم و با آن مبارزه کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72008" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72007">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=t33ueVOJiAl5Gt33-tO4ende0UBrCLcDEs95aXTp4dFdGpHRA52rQ41T72b9MDt-VklnvnHWZ_F-ikKa9R5lPK220ia9fwQmicVAL7SlUdNgegXAXI1YFOo8moLvjHd-DUisZoR84noLiZzsPbLSZUjSxFM1PtUmrk2uL48bpdCpEypqSkaJMpIPS9JrrisGyI1iH6OLqVTVUlIXRgyIUM-3w29S22WyXfc3hvq9BLYOsD63CNkXbrBrponqTW_e5GOP2s7pOsbNLkMjoYeZK-0ispK2hgpnhIB08QS80Bc0A66hUb0ci1OKgECDVfZNtr7leNPtKpzlx1p4e2sQQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=t33ueVOJiAl5Gt33-tO4ende0UBrCLcDEs95aXTp4dFdGpHRA52rQ41T72b9MDt-VklnvnHWZ_F-ikKa9R5lPK220ia9fwQmicVAL7SlUdNgegXAXI1YFOo8moLvjHd-DUisZoR84noLiZzsPbLSZUjSxFM1PtUmrk2uL48bpdCpEypqSkaJMpIPS9JrrisGyI1iH6OLqVTVUlIXRgyIUM-3w29S22WyXfc3hvq9BLYOsD63CNkXbrBrponqTW_e5GOP2s7pOsbNLkMjoYeZK-0ispK2hgpnhIB08QS80Bc0A66hUb0ci1OKgECDVfZNtr7leNPtKpzlx1p4e2sQQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس:
این انتخابات میان‌دوره‌ای، رقابتی است میان کسانی که معتقدند این کشور باید آینده‌ای داشته باشد و کسانی که ترجیح می‌دهند شاهد نابودی آن و بازسازی‌اش از پایه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72007" target="_blank">📅 21:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72006">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=UAHe2PNesvSwBK3KTm3gemW4h0N4Y09jXNI7AhWHlA3ZC_U4dDqmFmhA7zhiA5dyOxGO2XJXpHgwvoDS8f13dHEmiqe1CdbuGQJq3Z5uFLidAgvyqRoMM_p2-YyAgIxpPZil3FYECEtJA8pniwmiPJwcMA5tJnAOFQAinGaXf6viUarl7ETl-28rPMmHIURcD220_y-rulponD0dMZguOn24RLV4R0Px2WqpXa1AcDtS_QtOTRqkedSV4D0DoMeZTF3-50lolsxpcFr7uNAC7QfxoPOFPratGspR7jCaWt8gzb6RTTt5XWdmZ8eLO6mdB2ZCk0F_PsIGGhsyXLXg8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=UAHe2PNesvSwBK3KTm3gemW4h0N4Y09jXNI7AhWHlA3ZC_U4dDqmFmhA7zhiA5dyOxGO2XJXpHgwvoDS8f13dHEmiqe1CdbuGQJq3Z5uFLidAgvyqRoMM_p2-YyAgIxpPZil3FYECEtJA8pniwmiPJwcMA5tJnAOFQAinGaXf6viUarl7ETl-28rPMmHIURcD220_y-rulponD0dMZguOn24RLV4R0Px2WqpXa1AcDtS_QtOTRqkedSV4D0DoMeZTF3-50lolsxpcFr7uNAC7QfxoPOFPratGspR7jCaWt8gzb6RTTt5XWdmZ8eLO6mdB2ZCk0F_PsIGGhsyXLXg8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از آواز خوندن یه مرد ژاپنی خیلی وایرال شده به اکسپلور ایرانیا نفوذ کرده.
و حالا کامتای شاهکار ایرانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72006" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72005">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a929447dff.mp4?token=Wd3g32J2DyGKI8c0A3GfCAXJB-wrGuaar_WKQNfmuXdX6eZPI5iDrZ2ZBf-H2534PP6qKnQy-QOG-lq8WyvjeqDNM8b1FfOiDY__OfIjFZIW-gyn7cn3b3jbGajBdOm0rG0dRIGLeb6jMKDOiJwdlml-jpDAy-aVyBZvE8NP_tzlg2YeCjcqXNJboARf9JSfu93ymRmJam4Wr9UctqQ7Gidxfne6-iO8u_4C2LsnclW4pBK9w20gjP3jMJABl0vUpZNd0NlBFWSTKo83F0pwOBKRQwu8H7cgZLx6W0JXynKVdKbgNM9HeFwRVVMVVNsvXVwPUHCDoOhJfMkqIi_-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a929447dff.mp4?token=Wd3g32J2DyGKI8c0A3GfCAXJB-wrGuaar_WKQNfmuXdX6eZPI5iDrZ2ZBf-H2534PP6qKnQy-QOG-lq8WyvjeqDNM8b1FfOiDY__OfIjFZIW-gyn7cn3b3jbGajBdOm0rG0dRIGLeb6jMKDOiJwdlml-jpDAy-aVyBZvE8NP_tzlg2YeCjcqXNJboARf9JSfu93ymRmJam4Wr9UctqQ7Gidxfne6-iO8u_4C2LsnclW4pBK9w20gjP3jMJABl0vUpZNd0NlBFWSTKo83F0pwOBKRQwu8H7cgZLx6W0JXynKVdKbgNM9HeFwRVVMVVNsvXVwPUHCDoOhJfMkqIi_-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید حساب کاخ سفید در پلتفرم ایکس:
چیزی در راه است. منتظر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72005" target="_blank">📅 20:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=cQeJUxB-UtcQOeNyDPvBNK-4MUfBH2kNBSAPrU5g-AwEuKqGqmzRmuGHT5r_BIrxgx0BHS59gpUtkshRvZW87Dexm5FcWadXaw4PgV1sk9D_eWaFeL9Hkf43lMzzYqubKgYxBTWru4s1YBvg1eKSytdqOF-r4FGhl9qCVeipS0IH20I9IHyFxulM2utQGvF81BUc3EqBBNpmNVu3mltjjZaGnCraWUR_jqCnC_P_48kL7hla3N0gokJq5vzA8lEUPbYO02_yV_0mZKNK9wmaohfwP-rbGplNux1Z4-fuUMMFH-fPILht-whqymfTUkUnMqAca9dciVJkkj05lxzJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=cQeJUxB-UtcQOeNyDPvBNK-4MUfBH2kNBSAPrU5g-AwEuKqGqmzRmuGHT5r_BIrxgx0BHS59gpUtkshRvZW87Dexm5FcWadXaw4PgV1sk9D_eWaFeL9Hkf43lMzzYqubKgYxBTWru4s1YBvg1eKSytdqOF-r4FGhl9qCVeipS0IH20I9IHyFxulM2utQGvF81BUc3EqBBNpmNVu3mltjjZaGnCraWUR_jqCnC_P_48kL7hla3N0gokJq5vzA8lEUPbYO02_yV_0mZKNK9wmaohfwP-rbGplNux1Z4-fuUMMFH-fPILht-whqymfTUkUnMqAca9dciVJkkj05lxzJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای حداقل ۲۵ تانکر نیروی هوایی ایالات متحده را در پایگاه هوایی العدید در قطر نشان می‌دهد که بزرگترین حضور تانکرها در آنجا از زمان آغاز جنگ ایران در فوریه است.
این تانکرها در ابتدا به دلیل تهدید حملات موشکی ایران از آنجا خارج شدند و حدود ماه ژوئن شروع به بازگشت کردند.
برخلاف پارکینگ تانکرهای بسیار متراکم مشاهده شده در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، به دلیل اقدامات احتیاطی مداوم علیه حملات ایران، هواپیماها همچنان به طور گسترده در سراسر محوطه پایگاه پراکنده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72003" target="_blank">📅 20:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72002">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=MnD_5h6hf9qc1ohO8MXdzsSK53AjX_Vxh1nfTHETFX_XqwuSFhLqDgeDvQH-45LmwPdDst6KlxNM8SS9j15T93Iy9SMiKKoZJG92iCen9cB7vPvvCWBnNaIwE7cx5N-JAFu07LpcGms0damq2o9a5ZJEI96KGzfU81d4gBfcu1ps30M85w2mJbqZSmeNaUdspuoZApkOAtXuOEAfRCDOaeL6qGdRSPoeALFUSLxb1P3xT9LCLA8zdMwZ1IPN820rEbOtxAHd0ovzutm82D4JYfBELcFkKJByp_WOkiW2SAd6l78EE2ps3nFXlOhxyJoc-hOOSB-ylnMIO-rxg7EhJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=MnD_5h6hf9qc1ohO8MXdzsSK53AjX_Vxh1nfTHETFX_XqwuSFhLqDgeDvQH-45LmwPdDst6KlxNM8SS9j15T93Iy9SMiKKoZJG92iCen9cB7vPvvCWBnNaIwE7cx5N-JAFu07LpcGms0damq2o9a5ZJEI96KGzfU81d4gBfcu1ps30M85w2mJbqZSmeNaUdspuoZApkOAtXuOEAfRCDOaeL6qGdRSPoeALFUSLxb1P3xT9LCLA8zdMwZ1IPN820rEbOtxAHd0ovzutm82D4JYfBELcFkKJByp_WOkiW2SAd6l78EE2ps3nFXlOhxyJoc-hOOSB-ylnMIO-rxg7EhJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مربی بدن‌سازی:
خیلی از جوونا هستن باشگاه ثبت نام میکنن ولی تو تایم باشگاه، میرن پارک با دوستاشون مواد میکشن
وقتی هم که خانوادشون بهشون میگه چرا لاغر شدی و قیافت اینجوری شده بهشون میگن رژیم گرفتیم و طبیعیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72002" target="_blank">📅 19:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72001">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=FeTCeNtNaXLvXADeWpdItislh7L-na7NI8lmlMQmIH6fF_JGjIS5HoYtlE6IFPQIyIfLnUGoDRc9ovql41IWyBeE26WzePwG5OX2twNIsSFlqgAyWChMtzc_gD3S_ERtB0v_7p2cf2QHPDzk2HB80e6e4hUTdKd5RIWwDoucZ6IN3AbRYHZc9fA_tn2vS4MjeSKbAlAEl7exA-nolhFzB58b7hM7LNLdxYkc6R7ZZZYyZT1VuuJdwOGmaY3NKffG1G4QeHjOU8L5ACZ9Rah4JHl3z7ll8ijsb6JBpd6INh6Zk_lL2YnIxeq4ZEeeVfLR1VlEsgWOgy5QxSLeP5qJkYZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=FeTCeNtNaXLvXADeWpdItislh7L-na7NI8lmlMQmIH6fF_JGjIS5HoYtlE6IFPQIyIfLnUGoDRc9ovql41IWyBeE26WzePwG5OX2twNIsSFlqgAyWChMtzc_gD3S_ERtB0v_7p2cf2QHPDzk2HB80e6e4hUTdKd5RIWwDoucZ6IN3AbRYHZc9fA_tn2vS4MjeSKbAlAEl7exA-nolhFzB58b7hM7LNLdxYkc6R7ZZZYyZT1VuuJdwOGmaY3NKffG1G4QeHjOU8L5ACZ9Rah4JHl3z7ll8ijsb6JBpd6INh6Zk_lL2YnIxeq4ZEeeVfLR1VlEsgWOgy5QxSLeP5qJkYZR-VwAyCmly0oNvjRqMupUAzMrPsp2OEGp0TeBYmFmSm-oHiegkDOkf6AIOUlvMPoReQKvHixc32RHodWOYoS8SpQm-SiiwjlaD9K-IVGNQqDZ_bB_B8kHeFDjk8Rzm0JWYjjStSVzRbcAx0TZp_GqE5e3ZWTOR6gYPIU3c_rDfMQvZ8SgKxRoiMcjowZrv6OfikRulDvfUE0Hso2-SFEKiav7GSGOdNpHMMxSqtHjQEEEWS8I0NiHGYuiJP-Hkv6dE8_HnSmVyuh3ShSX6AGcz3x6HoALzQtDLjEmS75P6A1ghYwn0uYcZqeROxiwjIGm_gv5N8wOIrpbDWduLNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
ما کاملاً واقفیم که قیمت انرژی به دلیل اقدامات تروریستی ایران علیه کشتیرانی بین‌المللی، افزایش یافته است.
ما تمام تلاش خود را به کار می‌گیریم تا ضمن مهار این قیمت‌ها، در این فاصله باری از دوش مردم آمریکا برداریم.
یکی از اقداماتی که ترامپ درباره آن صحبت کرده، تشویق برخی ایالت‌ها به کاهش یا حذف مالیات بنزین برای مردم آمریکا است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72001" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8571b32102.mp4?token=hRJnTP14WGUyxpU6-4zWDzQbKZzPQ_rOmXYDU9vP4u-fvIUgn2Chp3fNOXgyWn-PUkiP_i_yM3drPiNxlnKflP2bMQIbmMIWnC7VYk9CCCfW-Awx_6CuoG-dMlGwg4072VZdn8fIMjNP3atWFbUqpZSX8IvZmpcYPlPeZFG-R_dhK4aTLMMbghyyQsKVeiTvzW5_8SZxjVdcGS1wQUt4xOEpcYNAXks770Qv53NtXbLy4AmBzZzk-WnpnRGty8nmBB_bm9lNnUJ8q91OZM7Tmuh8BJwquhiFYLSnm_V49kgX14rl5Rg5TXh4CMA-Cu34qjQbboD8BgXAq3CaZk1Fqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8571b32102.mp4?token=hRJnTP14WGUyxpU6-4zWDzQbKZzPQ_rOmXYDU9vP4u-fvIUgn2Chp3fNOXgyWn-PUkiP_i_yM3drPiNxlnKflP2bMQIbmMIWnC7VYk9CCCfW-Awx_6CuoG-dMlGwg4072VZdn8fIMjNP3atWFbUqpZSX8IvZmpcYPlPeZFG-R_dhK4aTLMMbghyyQsKVeiTvzW5_8SZxjVdcGS1wQUt4xOEpcYNAXks770Qv53NtXbLy4AmBzZzk-WnpnRGty8nmBB_bm9lNnUJ8q91OZM7Tmuh8BJwquhiFYLSnm_V49kgX14rl5Rg5TXh4CMA-Cu34qjQbboD8BgXAq3CaZk1Fqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
با وجود اینکه ایرانی‌ها هر روز برای کشتی‌ها ایجاد وحشت می‌کنند، ما همچنان شاهد جریان حجم قابل‌توجهی از نفت و گاز از طریق تنگه هرمز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72000" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYuEIQ_wMgTpE8CXtGE518xWrDEqWjAyies42BZhhpwlq0Ijak6UauK5GmHfzD1hyLGwutrj57Fy59TMpeT2_k-P2ogR_-SPKTFyfShUvnNGkgZ-cfaTfk_Lm76aCru6Sk6n4cpJ1aJnEwkW1emxqEzFllZknkLUjvJUJoYR9jd3l9WTj5DP-00EvslPSBH9JX_V_w0VZNB09yS-r9jBSEHxWV7p5s_-VnkYMSU8Xnf4k7gKtM5ygafkcmZIuuLwt0nM2ENk3Wy_jMPGOI9UfOEQLtzi9JM0FAz7B9SqHAIWPzLHiEVAHED8LSNyvxO8pQQ1wejvfQLRKx6J9wQ1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71999" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=ZObZ_hTYQNFmjKev8tmx2QSvxtlSn2xjYNRjsqOxth3e7WWmuLY4zo6xwRUoS98mykuACvDB7hPevaZAhiapJguIwd6oL0MQUByKvLbq1gr_d9_hKF4iuPn1LrsF89KH4WX3o5SwDDea5iIQtkZUAP9vlh4H6s7iTr7wMfDoFS7wqvQ3oWeOMnylRz9QcJkot-yc5ZEGIJQ8oQQp6pUlzuc4lTOcNri5HSXWl5K6KT6C2gXf35KeANmv1Sw4SLWrzWngyRM4o6gVu7KTthSkOn9pGS1XaCXVrcUA-uLbcBl_dLRAZHhGnL71ZO_pMJuShQWij5UEkiAdODEwIjYpUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=ZObZ_hTYQNFmjKev8tmx2QSvxtlSn2xjYNRjsqOxth3e7WWmuLY4zo6xwRUoS98mykuACvDB7hPevaZAhiapJguIwd6oL0MQUByKvLbq1gr_d9_hKF4iuPn1LrsF89KH4WX3o5SwDDea5iIQtkZUAP9vlh4H6s7iTr7wMfDoFS7wqvQ3oWeOMnylRz9QcJkot-yc5ZEGIJQ8oQQp6pUlzuc4lTOcNri5HSXWl5K6KT6C2gXf35KeANmv1Sw4SLWrzWngyRM4o6gVu7KTthSkOn9pGS1XaCXVrcUA-uLbcBl_dLRAZHhGnL71ZO_pMJuShQWij5UEkiAdODEwIjYpUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران ویدیویی منتشر کرد که مدعی است لحظه رهگیری و انهدام یک پهپاد MQ-1 ارتش آمریکا در صبح امروز را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71998" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71997">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71997" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71997" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8wmGei3fZvU8HCjvL8nIRbbeu9JVz_IprEGy1MkoNTKKcTBoeVpyVa8QEOBYz_laprB_LaHw5t6Q70xUjhNQRz-gj3h4qw0Lfzkv68VhOB09FLN_48Npq_EEF9e0HgNr5N84_5kz9rdLhQHKYlT9apqOYUruIPeUy02pJtmJbGyuMy7iefS6SsSsXQKGgtfAJb4rnHPonhO-o0jEveJjopn-CbsnTF7fBcNsrmIdAn6T6UYWS6ZGR_Efr64yrC1OCNL3EQxeyuvVioX2onMqQMvISu9snoH8QsycVgrwCaSo8lrcYamqdwKORDPrudg8_0jkz7Zg07emle8wfQukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71996" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71995">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=gnZjbHGuV3a_Unr4mUEYeI8N9Mx_MOPKeq-Z1bG1dJpXvlaG-srpGjpJC7XePYyz2vRpfyvwyPfZFddYL9XEx1_WczzL-Yyo0PZzBMf0-TCol9HJfdeM_L6D4DvFi1GmTJFpCAbRPQVM1tHnCBdAl-_Wdnbj_Ld0Eok-Mf4-GEwRYr1GgRFl1FFzOhyZrcyL-un42iEo_5icXs8UZpftrypTgxyRKsD2rjtSXZUHzOAjYfs089vz8SWs0fSTklFxrZ8SVfin5wCtppzjhIwd4KW9qZKIAIq1zDdnOR6JqqFde6s3iN2D0v-dP64uGtzUN7kWkDzu7QoguMuUXHKWhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=gnZjbHGuV3a_Unr4mUEYeI8N9Mx_MOPKeq-Z1bG1dJpXvlaG-srpGjpJC7XePYyz2vRpfyvwyPfZFddYL9XEx1_WczzL-Yyo0PZzBMf0-TCol9HJfdeM_L6D4DvFi1GmTJFpCAbRPQVM1tHnCBdAl-_Wdnbj_Ld0Eok-Mf4-GEwRYr1GgRFl1FFzOhyZrcyL-un42iEo_5icXs8UZpftrypTgxyRKsD2rjtSXZUHzOAjYfs089vz8SWs0fSTklFxrZ8SVfin5wCtppzjhIwd4KW9qZKIAIq1zDdnOR6JqqFde6s3iN2D0v-dP64uGtzUN7kWkDzu7QoguMuUXHKWhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک: این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد
ایلان ماسک با انتشار ویدیویی آینده‌نگرانه از تعامل انسان و ربات، فناوری‌های پیشرفته و سفرهای فضایی، چشم‌انداز خود از آینده را به تصویر کشید و نوشت: «این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71995" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
