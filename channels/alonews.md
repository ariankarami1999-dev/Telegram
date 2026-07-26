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
<img src="https://cdn4.telesco.pe/file/o9dZy5nQlUhSL222gtmk9640dRbnHsLVsUe3zxCjFF4TFWKqQp_lbfEj83AuxWBH7F-bqSoDBg3e_aDofWl_3soe6FsX_GxsDmhNyJ_Q_jggjpBsbNHt4jzZzrWlRAmqAKErtRZNKBGHQHrFr95JhJa9tTKvKOY75kUzqsxsdqdJGgcnH3lmm57gESSR1gmZ0P_LPjh594PNKQoFHInAmXSBTV5fPLgDhlq0kzxPopyHEh39las_X5QQu3vylqKd0-iNwwbiHrA8csi6qnfUqkBDRb-mo7R-TDkGG37_NxRr1alp4pXBtszy-gx6HL5RjPvvPSzu8aJ1RKW4Zi8NaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 947K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 13:21:19</div>
<hr>

<div class="tg-post" id="msg-137651">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی اتحادیه صادرکنندگان فرآورده‌های نفت، گاز و پتروشیمی:
ایران روزانه با نزدیک به 20 میلیون لیتر کسری بنزین روبه‌رو است.
🔴
واردات بنزین نیز در شرایط کنونی به‌دلیل محدودیت‌های منطقه‌ای و بین‌المللی تقریبا غیرممکن شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/137651" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137650">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwspjOYe7WUJf08rBJNBU9stD4d86NE7TKz0DviCCRb56cRz8mi7b4HhzvCo8C7p32_IHGXYbMLW1_lF4aj_LpTUDzn8Ox3lvF2KRB2azMXoWSetzobUw2FbK_Tk9nz-HMNCIJzbbjT3nLqRk1veHsbT7VVUrudpkIjK5KAKb6MEX6wwsFdHJ2pFD6ET4VCk6mlLRYbXyb1-RO9UfZU7kgGO2Q01zjo1OpVi9UUhg0s97KFvOYYgk3rCqrR86dC0ddRGSTTPRhkkZUxbi5lSplXFzArteA3-d9WpKogQQFykgP06WNM3hvqAVdPULIkpIg8n07Vk7PTuGEt0eNYn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس با رشد ۱۰۷ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۰۰۲ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/137650" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137649">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqStHbMnxuHiJEBjacLhrw83WcKoF6piK9RzIr6ttrA7cPvcvWq5F1sk3gN5yNjsc6Yh2tLpv2_oqp6_I-wdAJwSRBGwQhDd9NdZ5xGl4cocRXaP1Exui_GNhEDiuz2uV9kWnMpadkOV4uf9H5UJPcpOj3IyqqA17vPanh8f1IDIA2p6AGaV5foaIBEVUmtA8tqTADbvQSS1TmRLXbzUkIsFzY3gtOyju6ts-gIfS58q9FsoDzoY79yaaB1Y1TdNDMTQviObGJPw3pkx1xZYWGUFbWaDjtNVCaToTnpYjq4X3SfDBma0tM6er-KR_CWNxUHMv2AICme_NbHwVXsS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریایی بریتانیایی: ما گزارشی درباره یک حادثه در جنوب دریای سرخ دریافت کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137649" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ، انرژی هسته‌ای را ترویج می‌کند، از جمله توافق با عربستان سعودی. خانواده و حامیانش می‌توانند از این موضوع سود ببرند.این توافق به ثروتمند شدن ترامپ، خانواده‌اش، مشاورانش و سایر افراد نزدیک به او کمک خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/137648" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیروهای اسرائیلی اطلاعیه‌های هشداردهنده‌ای را برای ساکنان منطقه الیرموک در غرب درعا منتشر کردند و از آن‌ها خواستند که از هرگونه مانع‌تراشی در مسیر پیشروی نیروها خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/137647" target="_blank">📅 12:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy0hNKDmpp9N-Qko91Kpm8v0X0d36jcuKM0X2MUc5yAnBpAtKNeeNYUOCXx_UIfi3ddt77fWDGLaiJ874G3zgISPzZFqN1JcoY9UblW8H6rnR4SD9vrY5mctgGCBG2SwWgut8x0lu3G7SvIyS3M7nk15nZNd3ZkrdO5B-vEK2jUzwmfY8LK_3DmCDPAA3OUahD2gEY90zFBe19-nJVuLv-K5ce4xB6kCFvsCZ_FRyFoGWdJhBgWCXHHn3-1yKdNkinZw5Jpid8QK_rgUu6DyK2Z5r2_iizQuX45Po1kfcYTdzG5QoiQa2Tye5A28R4EGeYBJCvxcDUVYbep8qaHo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پروازهای ترابری نظامی آمریکا به خاورمیانه همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/137646" target="_blank">📅 12:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/137645" target="_blank">📅 12:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
غرق شدن یک کشتی ویتنامی در دریای جنوبی چین/ ۴۵ نفر تاکنون نجات یافته‌اند
🔴
یک کشتی ویتنامی با ۶۲ سرنشین در آب های دریای جنوبی چین غرق شد و تاکنون ۴۵ نفر از حادثه دیدگان نجات یافته اند.
🔴
تارنمای خبری «گلوبال تایمز» با انتشار این خبر افزود: یک کشتی ویتنامی به نام« KHOI NGUYEN ۱۸ » پس از بروز مشکل در آب‌های نزدیک صخره «یونگشو» (Yongshu ) در جزایر نانشا واقع در دریای جنوبی چین غرق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/137644" target="_blank">📅 12:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137643">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی ارتش: با توقف حملات آمریکا، عملیات تلفافی‌جویانه را متوقف کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/137643" target="_blank">📅 12:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137642">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
یک آتش‌سوزی گسترده جنگل‌ها بخش‌هایی از منطقه مادرید در اسپانیا را فرا گرفته است. آتش‌نشانان و نیروهای امدادی برای مهار حریق در محل حضور دارند و عملیات اطفای آتش همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/137642" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137641">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مارک اسپر، وزیر دفاع سابق آمریکا:
بر خلاف اخبار فعلی، ترامپ در آستانه تشدید حملات علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/137641" target="_blank">📅 12:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137640">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شایعه مجازی شدن سال تحصیلی کذب است؛ آغاز حضوری سال تحصیلی جدید
‏
🔴
وزیر آموزش و پرورش:مجازی شدن سال تحصیلی آینده کذب است و متاسفم که بعضی‌ها شایعاتی پخش کردند که آموزش و پرورش سال آینده به صورت مجازی خواهد بود.
‏
🔴
از همین الان تمام تمرکز ما بر اجرای آزمون‌های نهایی و پایان ارزشیابی تحصیلی پایه‌های یازدهم و دوازدهم است.
‏
🔴
تمام اهتمام دولت جمهوری اسلامی ایران و مسئولین دولت و نظام تعلیم و تربیت این است که آموزش و پرورش به صورت حضوری از سال تحصیلی جدید آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/137640" target="_blank">📅 12:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137639">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279c2568c4.mp4?token=dS3shC9ANhwkSH4c09is-8l7bG_7fKmHz8sMR2n5BXhaVut9ugLPx4yEpR6PNRKex1t4vmI9WKaTyEnfVwZCCzMvLlRpDZCi-gzeKFuM9EyWLv5kyh2XTDd8lcI5XkE6V0GbP287fbzWGr6HZByAR-mvD7EIqBQODeKeNoINP0GsrArdKPWAExBrcPlX2GQNO-Ny64exl_nMac6FwHWU9JntpRlbaaRPjDbBuMepfQ1p0h8rPorX0G-LbIlbecQ4iueikbSsLrDWGkyM2rtvLBJHWMPxK8JUK2CfAbmB4Qogh_LI5hvOnD-XEBH7c1q8zrWTm7NG1bKR6AWHOYOsH4Opv61RkD0_Y8JkMpwB_d-McjZseQmQeuPHeYoqZIFBc8wgTpbkfPIJdxs4G7v7XDSn-ojw5nOf_FPJa6jxWK_sR7qunJGhM2jNaehiCsDG1CezED3P90-vk7urtjuprF2b9Wqo0a_uYx7H3-WC5ndOOiH3akYN-U2RI7QGDZKBRTrAS-mDj3x7yE4fFiVGhD1XJsaJzzyBC5NCURENYeWb4EagGXKVIRLAwDizxD6JlMqU9zLnMHjBcGfZUPxSyTkEmnFprdBEym1ugQ21wvhV2nRXSd1YjfexyGeaIUzGXJTp6T4oFd2Lnvtmh0ZKiTpQorJ2ZSPHXop5M_92fso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279c2568c4.mp4?token=dS3shC9ANhwkSH4c09is-8l7bG_7fKmHz8sMR2n5BXhaVut9ugLPx4yEpR6PNRKex1t4vmI9WKaTyEnfVwZCCzMvLlRpDZCi-gzeKFuM9EyWLv5kyh2XTDd8lcI5XkE6V0GbP287fbzWGr6HZByAR-mvD7EIqBQODeKeNoINP0GsrArdKPWAExBrcPlX2GQNO-Ny64exl_nMac6FwHWU9JntpRlbaaRPjDbBuMepfQ1p0h8rPorX0G-LbIlbecQ4iueikbSsLrDWGkyM2rtvLBJHWMPxK8JUK2CfAbmB4Qogh_LI5hvOnD-XEBH7c1q8zrWTm7NG1bKR6AWHOYOsH4Opv61RkD0_Y8JkMpwB_d-McjZseQmQeuPHeYoqZIFBc8wgTpbkfPIJdxs4G7v7XDSn-ojw5nOf_FPJa6jxWK_sR7qunJGhM2jNaehiCsDG1CezED3P90-vk7urtjuprF2b9Wqo0a_uYx7H3-WC5ndOOiH3akYN-U2RI7QGDZKBRTrAS-mDj3x7yE4fFiVGhD1XJsaJzzyBC5NCURENYeWb4EagGXKVIRLAwDizxD6JlMqU9zLnMHjBcGfZUPxSyTkEmnFprdBEym1ugQ21wvhV2nRXSd1YjfexyGeaIUzGXJTp6T4oFd2Lnvtmh0ZKiTpQorJ2ZSPHXop5M_92fso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع طوفان شدید در منطقه روستوف روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137639" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137638">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1dc51b5c.mp4?token=gi8klRoK95N-y1X11MTOsXXJwceIrwzZrOTeqtfo7fHxYLmPXGtUdi6BOUbZZmwZC3fCRkYpuz5pNiaxUR6ay6ozL1vCyBFL0dNaW83GaQSnn-wiRwt_HAbd935QQlco7WleS5meutTQRSVjr4fDhYKUZr9QWxzsAeaQv6OLtSgFhxPyHQcwTBFxMHfZa76-7J2353cOEUTQo1DobmphtWVVl1INPZn9kw83voSfgO3s_IKCz9v3-d7ZpsFnsPpV34lmR1Wef3H3HLBZOW1YlWMh_l2SzAfgsmUO4A81izJOt0xUvuPmDM2NSg2ya13-WoYf9Eliyv--cORSlA3rTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1dc51b5c.mp4?token=gi8klRoK95N-y1X11MTOsXXJwceIrwzZrOTeqtfo7fHxYLmPXGtUdi6BOUbZZmwZC3fCRkYpuz5pNiaxUR6ay6ozL1vCyBFL0dNaW83GaQSnn-wiRwt_HAbd935QQlco7WleS5meutTQRSVjr4fDhYKUZr9QWxzsAeaQv6OLtSgFhxPyHQcwTBFxMHfZa76-7J2353cOEUTQo1DobmphtWVVl1INPZn9kw83voSfgO3s_IKCz9v3-d7ZpsFnsPpV34lmR1Wef3H3HLBZOW1YlWMh_l2SzAfgsmUO4A81izJOt0xUvuPmDM2NSg2ya13-WoYf9Eliyv--cORSlA3rTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
مجری فاکس‌نیوز: اگر آمریکا نتواند چند ماه قیمت بنزین ۴ دلاری را تحمل کند، دیگر نمی‌توان آن را یک ابرقدرت دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/137638" target="_blank">📅 12:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137637">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo6ujMKDjVn5tVjcyLh1WTsnzIlDpTcE9qgEx0JO38v_KYyBICO_HlOz985p1Dmg2RXDq94G3M-EWVjPXxJrJ9NkHnoJMQ1tN11SX9DFYK1fSmJcdMNZT4gQAVGfxAE-rCynRwaW-13JqWCPnVniM6gpcb15oBXzU9oQMeeg8IBXJz03He7RxjiCCxWPiqEr0tG_FfCe-BPLrKWicOvcE6ieycfUqaJ0bmrt1DGwvG2-EJo_8GAElBySGMKSZbbYgmk7Jy-TP9VfXn_Xlbl7ThKiJSFHtGV0PC0akoqnfhq_28Oz_-5682YDUJJMpwx4VRV6yi_EgM3YBEH9z6kosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از زنده یاد اکبرعبدی و گوگوش
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/137637" target="_blank">📅 12:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137636">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سلیمی، عضو هیئت رئیسه مجلس:
برای برگزاری جلسه رأی اعتماد وزرای پیشنهادی دفاع و اطلاعات، آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137636" target="_blank">📅 12:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137635">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
روسیه با شدتت زیاد اودِسا چرنومورسکی اوکراین رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/137635" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137634">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
علی قلهکی از احتمال استفاده آمریکا از «بمب اتمی تاکتیکی» برای کوه کلنگ خبر داد
‏
🔴
بازگشت تیم عمانی به مذاکره و آمدن به ایران برای مُجاب‌سازیِ تهران برای همراهی با شروط و امتیازات جدید واشنگتن و همچنین مشخص شدن سهم مسقط از تنگه کلیدی هرمز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/137634" target="_blank">📅 11:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137633">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7154967b4b.mp4?token=uTImN2hcw-w4KHIOWOtLoG4_kCCgCpdDh4Fg9i8aSs1PrwyqJb6iTjrY3gnzNHxUNnS5zT9EsqyBZS4zmgErkOD_cnJdlc_wL47GmHvwVXb4H9a9lkOw76wNgMpU3pZ45m5rPDBXaM7D-1TKEry0QjWVGm1Ovj4kRV0nFE2zoAfPjlBVFGmfM_C_lpWfXCkjG8nC3SrzbBFGOisGpgB9NDWJs2bTtsYZdGQ5IJea2Q0rbyJkx-r-uGsvEjsiLkbgg4I97KDkN1yarZiHciavj1DSKHJuHD6PgmG07NbMzn2akxgTd8zIFx5GxHjIZpTIxo7qDtH8_Zabn5kbSapd2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7154967b4b.mp4?token=uTImN2hcw-w4KHIOWOtLoG4_kCCgCpdDh4Fg9i8aSs1PrwyqJb6iTjrY3gnzNHxUNnS5zT9EsqyBZS4zmgErkOD_cnJdlc_wL47GmHvwVXb4H9a9lkOw76wNgMpU3pZ45m5rPDBXaM7D-1TKEry0QjWVGm1Ovj4kRV0nFE2zoAfPjlBVFGmfM_C_lpWfXCkjG8nC3SrzbBFGOisGpgB9NDWJs2bTtsYZdGQ5IJea2Q0rbyJkx-r-uGsvEjsiLkbgg4I97KDkN1yarZiHciavj1DSKHJuHD6PgmG07NbMzn2akxgTd8zIFx5GxHjIZpTIxo7qDtH8_Zabn5kbSapd2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مستندی از دلایل سقوط شوروی که توسط صدا و سیما پخش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137633" target="_blank">📅 11:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137632">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، سامانه‌های پدافند هوایی این کشور ۱۳۳ فروند پهپاد اوکراینی را طی شب گذشته بر فراز مناطق مختلف روسیه از جمله بلگورود، بریانسک، کالوگا، کورسک و اوریول رهگیری و منهدم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/137632" target="_blank">📅 11:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137631">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrDE_Xly-khfL-EDEZF3WAc_cbdhkMl0m31lnl-cCM4rGONgHXGIq-Hb2YAM-oNuTdlV3uZ-9Cti4BnyN6RCP9o8ae-31UdPuGkGNECSa-XTQrthWrMajNHvQ1buqR6pqRPZzQW9kziKmagUp1NeGvrKItD7O2nwRMUOOT3a6SRxWDoeFe1Z9CR1p1A2wcOl8wMxfDdOLvGFIMCexJGEhokCatIB6UX0kgLTwpAJCzWZAhF72_MNhIFRX21n6d97j9gHZGJhFmYdCEx5a0wfh_OOvBtcqNmqLY95Q1N1jWmLA66KjkHNE4EMahbSgrUGPP5Pk71D5qA8NkGo0fZQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش‌های منتشر شده در "جروزالیم پست": عمان پیشنهاد ایجاد یک اتحادیه منطقه‌ای را داده است که مسئولیت نظارت بر امنیت دریایی، عملیات جستجو و نجات و سایر اشکال همکاری منطقه‌ای در تنگه هرمز را بر عهده داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137631" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137630">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بنزین بزودی لیتری 10,000تومان میشه
🔴
هر باک 600هزار تومان
🔴
سر سلامتی بچه‌های لبنان و غزه و هر درب و داغون دیگه‌ای تو دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137630" target="_blank">📅 11:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137629">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfbncKfB0TH07U3n0Y-gKH3zXFH449MIduz48Ku_ROJV1Z8WI99yGT8WS-2DdyG9HYz1l66ilA8V9CNcIEvdgHJuqvecb3rjI0R8bZt6xhhFne1-1pwKsUXaNEgN4OeZq54Rdg0_YF0A-8_1w59nqqcQk6PR9WtS60DIcweiadcqHOtNN-OQBtpmxRVS_6v2hszT3lA8C7kY2dreXlM4Y1ZpI9DbwEZLiYjxg9j74mNLxooIVnO1wfAKSs0L-XQLk92WqvJLzCNfF9m8JJ18q9bEiV1_4lELJyiFpcvvuDkAsDErMQTM0ldGOwilEMMzoMU0EZnfiyexI7Pb5dqeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنزین بزودی لیتری 10,000تومان میشه
🔴
هر باک 600هزار تومان
🔴
سر سلامتی بچه‌های لبنان و غزه و هر درب و داغون دیگه‌ای تو دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137629" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2973ce0df5.mp4?token=YWbtBw7vjq0yuAXRhzRVlUbxlrhrgo0XWX-yMVBvPAumL9EYITHWN2clhuDa9pvmfXu1V0mQv3TVGZfuDQlnCJq7epIbws6DMv_Nw_uK90Csy-4QfvU39FfMOjr5-tQY6fsJhwE_oz-IaYo8uwoLcEIUmKMFqGx3AkZA5t756dFsh05M6yAStgr1GZdbBw8LNOzv0-IyvEoqG6XdtT6airLUeL0vF-KM-hC4nB7nq4TMYuPCeKx-1ym3hiTV_WwwADWSYsYwh00BmW7vO-9RhQO_q4W4SZfg0jRhFvPMswnzSneRQ3i5GHbAv6EToYZGGdEvfnR_DgTc9LvD_7JOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2973ce0df5.mp4?token=YWbtBw7vjq0yuAXRhzRVlUbxlrhrgo0XWX-yMVBvPAumL9EYITHWN2clhuDa9pvmfXu1V0mQv3TVGZfuDQlnCJq7epIbws6DMv_Nw_uK90Csy-4QfvU39FfMOjr5-tQY6fsJhwE_oz-IaYo8uwoLcEIUmKMFqGx3AkZA5t756dFsh05M6yAStgr1GZdbBw8LNOzv0-IyvEoqG6XdtT6airLUeL0vF-KM-hC4nB7nq4TMYuPCeKx-1ym3hiTV_WwwADWSYsYwh00BmW7vO-9RhQO_q4W4SZfg0jRhFvPMswnzSneRQ3i5GHbAv6EToYZGGdEvfnR_DgTc9LvD_7JOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاید باورتون نشه ولی یه همچین نماینده کصخولی شده قبله امت معکوس
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/137628" target="_blank">📅 11:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a6283cad.mp4?token=LLnAVZjO0wMV-8b0phN92_w-GCRS9G_wukBYLmVWhsiETspEfLA8auze4SsO0V70T_rl-d3xlqK80ahWFqAT5HSIqjzv3u8yyBY6TQVsspd-Kz40MwyJIoD1y9f_Jjk1XGuVQVi_dcrNK3zY3PeyGgw-TiC-LqpgiGyC2_4zdN5zTmRYgYfwHnYfAYKqRJFFgisz6Se0h1F3ZeE2ZZ4ytPcGH4EvPtWlEjQNmEJcFiSjTiiVxHyRfi1Ws4T_XdUMS5OvlhUDUYJre8u_HC-JVKaK_jR6gPqHUUy9agOoUq07aZT988TwHj4V7yQZXew62iYLEDu7Tq54clOtOF0B7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a6283cad.mp4?token=LLnAVZjO0wMV-8b0phN92_w-GCRS9G_wukBYLmVWhsiETspEfLA8auze4SsO0V70T_rl-d3xlqK80ahWFqAT5HSIqjzv3u8yyBY6TQVsspd-Kz40MwyJIoD1y9f_Jjk1XGuVQVi_dcrNK3zY3PeyGgw-TiC-LqpgiGyC2_4zdN5zTmRYgYfwHnYfAYKqRJFFgisz6Se0h1F3ZeE2ZZ4ytPcGH4EvPtWlEjQNmEJcFiSjTiiVxHyRfi1Ws4T_XdUMS5OvlhUDUYJre8u_HC-JVKaK_jR6gPqHUUy9agOoUq07aZT988TwHj4V7yQZXew62iYLEDu7Tq54clOtOF0B7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علیرضا خمسه: اکبر عبدی یک جواهر و بازیگر خلاق، بی‌نظیر و تکرار نشدنی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/137627" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
روزنامه وال‌استریت ژورنال به نقل از یکی از مقامات کاخ سفید گزارش داد که دولت دونالد ترامپ، رئیس‌جمهور آمریکا، از اوکراین خواسته است حملات به کشتی‌هایی را که «متعلق به روسیه نیستند» محدود کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137626" target="_blank">📅 11:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
روزنامه وال استریت ژورنال روز شنبه به نقل از مقامات سابق و کارشناسان هسته ای گزارش داد، اگر دونالد ترامپ، رئیس جمهور آمریکا حملات آمریکا به ایران را گسترش دهد، واشنگتن می تواند چندین تاسیسات هسته ای باقی مانده را فراتر از کوه پیککس هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137625" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9154c6df.mp4?token=ldRr_1aIl_iUto6ZQIkVL1N3ckqoPrVme4jZSADW-7LLbtrlPYuKCOd6maVfgoEdkgiYOlPhJWiH-jTLmW8Fb6EGDLSeMxCjbBKNyypHeU2h9WwxQcVJof6NWa9SGCg--GPF7p-ssRiJawA5OSoFgHdBUDuhJ0YxaCQIk8EaoZOyAFcuyUKgjis98rvYKAbMvSGamIFEgLNO1gjR5ZRHU3rBi1-xLU4HRDhRsVrTG2vem4IjS9xXSkKHuNiwHrwJ7jybEdBYevCz9zx3wBD8lFKhRg9NsOYnk7gj2UHUbEh-kcm8I0nym3Es_T-ptsWbm2nZigd2xNHEWqHR9EGSoA_Eltg51La1vrww0gr3y91xy6o3bCBeRXdyQAG8K0h6UKQdTJkSIgqEyVjI88yWKKkCkbDFk8zQu7qubtFTIbMAb--mj4JCCBVlWGQ9djU1JoQSI-F2onOrWZvF1_XtaI1XvG80cQflUDbouQoDW4tSM2H_PciIhWwAu2HLas8W9cHTUO7DXq5qZj_4FERJ9DkXy09fGnKuroeIqi__xfEIe9Ome-A_bVckd7fDqQSqoKKh5VRTB156gNVWf2tGDi1r60b206jLeZoSpnRQgG0P9Yak8NHRwoGgd3KlzD1GzPwr_Jxz-9vAiR2lqCkmC-HpYSJqCxQVGZJO4d1gbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9154c6df.mp4?token=ldRr_1aIl_iUto6ZQIkVL1N3ckqoPrVme4jZSADW-7LLbtrlPYuKCOd6maVfgoEdkgiYOlPhJWiH-jTLmW8Fb6EGDLSeMxCjbBKNyypHeU2h9WwxQcVJof6NWa9SGCg--GPF7p-ssRiJawA5OSoFgHdBUDuhJ0YxaCQIk8EaoZOyAFcuyUKgjis98rvYKAbMvSGamIFEgLNO1gjR5ZRHU3rBi1-xLU4HRDhRsVrTG2vem4IjS9xXSkKHuNiwHrwJ7jybEdBYevCz9zx3wBD8lFKhRg9NsOYnk7gj2UHUbEh-kcm8I0nym3Es_T-ptsWbm2nZigd2xNHEWqHR9EGSoA_Eltg51La1vrww0gr3y91xy6o3bCBeRXdyQAG8K0h6UKQdTJkSIgqEyVjI88yWKKkCkbDFk8zQu7qubtFTIbMAb--mj4JCCBVlWGQ9djU1JoQSI-F2onOrWZvF1_XtaI1XvG80cQflUDbouQoDW4tSM2H_PciIhWwAu2HLas8W9cHTUO7DXq5qZj_4FERJ9DkXy09fGnKuroeIqi__xfEIe9Ome-A_bVckd7fDqQSqoKKh5VRTB156gNVWf2tGDi1r60b206jLeZoSpnRQgG0P9Yak8NHRwoGgd3KlzD1GzPwr_Jxz-9vAiR2lqCkmC-HpYSJqCxQVGZJO4d1gbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اندی برنهام ، نخست وزیر انگلستان: اگه چیزی به نفع بریتانیا باشه، جلوی ترامپ هم می‌ایستم، همیشه منافع کشورم برام اولویته
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137624" target="_blank">📅 11:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgqtvWRTWsPk6_wbHV8AayIfDdzGtu1fUIJF4cBh7FnV8Qbmtc6cZuTv9unyMqRQSkb3uTOnxmFEoQFI6rZBwfgyLuyM2S8uzmgb0Nsu-Gt7875831yCBmv3jhb9VjScRR9cKYtE0VH73803BbLEEm9Z-lNGaUbRHTXf5xS4wAjeo8-HyhgmYyDgQF4YWME5jQYdyHUgKoS36xbYHXmcR1y2O6aJkHOIh_sIgZpaOwLHCM667PTcrhbexNRuKD0tiN_U6__6KyquHtKi_9RPinUjx6ljDlZHAHSadaG27lMz_t99rDFmwTyDNUKHYdtBe-LkwuSyCczuLE5D-g6YpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137623" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
استانداری هرمزگان: احتمال شنیده شدن صدای انفجار‌های کنترل شده در جزیره قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137622" target="_blank">📅 11:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfGwrxIMzDtpF6g5cNdVnaHE6RzQ0IY_5qHGu4savkV2sX4nd3XmxnF1qS7Se8FZdUnezqBB8r3QZzS9ZuWfaRnWKgQW_KHiBAA-CzQ1T9Nijj7I4-Cd9grxuPWZjzQry1p3dM8f1C_38lAsf80izp_2Dzs5hHkb0UgM7ng0VQsYfAN7E3AA38CI6QX2JonEVTg5xo9jK_Xpbi7lzKdZTOT_KF1DPJv4QofsHE1EB_GFMviHlruywGBqJe5DR5e5ebwv22iUJwujv29CLnIxg_Bphzdad5ClIbFf3w9Eob7u0PWraTurBFiWzdoLgAmMI1GhwKfE1icZbtrRcxqtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏
تصویری از تابوت استاد مرحوم اکبر عبدی
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137621" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
پس از نزدیک به دو هفته حملات متوالی، ارتش ایالات متحده برای دومین شب پیاپی حمله‌ای علیه ایران انجام نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137620" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137619">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEXt39TK4SDZNBKU2cXOMyfkMGqRNJ5iaMRr6MciUW1wqWLExoW6GCkRl4h9gOMU9mo6hbZZI6ulW4lBYeJp3-I77DNLp04-CjG8wG_3fKfXTxo6bF57A8HHGRIiZdG2bXW2XmpzcW-F46hIW5Jol1rkaas4QOyTH2z-Cg8Nc4aeeP-EDBfoFZ7X_Fbmzam7Y6zTUD78sb3bRtFI5_yLv_6Ke3H7SoZxcHRq1IKt23h4LlQwrt89jxhFRpmD4ISrZw9SIYc5Jo1xlfbW_U5mziXjpzPtU57TXgsZU8EXaaoiFj-vJprBW5RRXTe1YbhKrAzQ3opUBxCHFVtyjrkOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
هرکی میگه با آمریکا جنگ‌ نکنیم بی شرف هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137619" target="_blank">📅 10:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137616">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvMi_UKdN6KqqeyFZ9wDvSwlJNa89Dtk-W9a6TSK4Il-3ao4WpDoR8hLzhtMiSpkpRHkQssi2Ac5gubnUw68dyzgYNECcrkMXmVv1C2K55oc9kRuSsb5blg4nKMqoD-0Te4ucfWerUxYPpZYjYmQwkO3D5UCxpecJt-sY32P20lIcpSzg6o8UFhNAK0ALYM4NpAX4sn77pHvsvaC_8rJoFU2yuOgixr4vkygxELpymyJHvenbH77pio8FR8PLNLATU_83GKtQazk6kzDcy-3EzZGZGfNEI2v3Q0oLVZAtXkwL3pj1GPcTVbLzCDWXptZ2kzi2XeZzKhZSe7850EnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9E8-dCfd8yV3YZyeZIRvfNQyiKGjDJlzMEjs74u_yBGkgqIXp4FobVdyT7mJWIcpUyYL-Vje6DfZEjHdBJGXJuGr9Pgk-Qem1PvuaFgTxBZ_CZuhc9x0guAX5vMVeTY1CfpzdINWfkfFBnXSwLJChbNuL6lKY2lrDI0SJGIvhNBhyBbIwxuO2DOw4RpVQGVbZTGmlo2596a4dkwej3JsxN5Azgc_aZFgb5oQidD8opKlSBGRKC4BXT2qj_2hFDYjEDW-kFyvUnH74RRRl0fv5j2Mg8IJIoXH-HpqmeCsMZa6ufET-ct1Fa9ElwD_jnK02HZU2URUSrVv94bdYMCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVqsdPNFdK2k-0aQ4pu7oLxDWk2lRkB5kyDbsxe34A8M-ddj50MJbtn9qXE8ZZu7j1wpFdaljRYyhfvRKE8u3fjzSGyvJW7SOYVC5uXxWhB8AXH6lddCGnj-k58j1Bod0WvKfY_5s5PX-xM_WkHIERMIe31oYWzsbet724Wv_PdjOKRbz365biiSDufSL5Ktb_30oqfK8PzrRt86a0xmg3uFhQDqkxI8jQClLFuurhr7q9C3Nq4s2rKp8JwNbtjG3I8zZGcPoYYbfsuS6eyKg0Dv6bnovGuFkBi9kx5YiBRgr63BsHylQr-fu7GvZ2yqdSq9Zj2wjtPUP5ydQyIDSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بنادر کویت و عربستان خالی شدند
🔴
تصاویر ماهواره‌ای نشان می‌دهد بنادر کویت و عربستان کاملاً خالی شده‌اند. یمن تأسیسات نفتی عربستان را بمباران کرد و نفتکش‌ها گریختند. مقرهای آمریکا در کویت نیز هدف حملات ایران بوده است. از زمان لغو تفاهم‌نامه، کشتی‌ها به‌تدریج کاهش یافته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/137616" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137615">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf6cd690f3.mp4?token=pgpKG7xAGt2G4kfyWOoQ7j_a_klknHpcRaBkaQp_vzMQ6W5Nel6j2kQ0a60zg2g9wZSzNK0AkdgHZ8QqVz0y50oEjnyy1eExxKI8X3qElZLs6QsuqrChIj81RG9KrbhfP2UB-aP4mx-EnpiEJZBpXy1pv9n_Ey6XxsfNpd2SXw1M0p4fR2T7oYOUU57gAsqQ3ywrzAr-69s_e_BHFk21f2VE0_vXaQjn1SRHgEGj4H7YdM7sggI-4f9aD7iRZ-bk-HIBtnfe4Vy3AJTkC0tNc3mT9TMltQN5poyK0xhoRLoMI2CLFRgy2EVLCdMx30Lq1dqNlw4cF0aflIgq_tYyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf6cd690f3.mp4?token=pgpKG7xAGt2G4kfyWOoQ7j_a_klknHpcRaBkaQp_vzMQ6W5Nel6j2kQ0a60zg2g9wZSzNK0AkdgHZ8QqVz0y50oEjnyy1eExxKI8X3qElZLs6QsuqrChIj81RG9KrbhfP2UB-aP4mx-EnpiEJZBpXy1pv9n_Ey6XxsfNpd2SXw1M0p4fR2T7oYOUU57gAsqQ3ywrzAr-69s_e_BHFk21f2VE0_vXaQjn1SRHgEGj4H7YdM7sggI-4f9aD7iRZ-bk-HIBtnfe4Vy3AJTkC0tNc3mT9TMltQN5poyK0xhoRLoMI2CLFRgy2EVLCdMx30Lq1dqNlw4cF0aflIgq_tYyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چمران: در صورت ادامه وضعیت هزینه‌های ناشی از جنگ، ناچار خواهیم بود پروژه‌هایی نظیر جدول‌سازی، رنگ‌آمیزی و حتی آسفالت‌ریزی‌های غیرضروری را از بودجه حذف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137615" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137614">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: در ۲۴ ساعت گذشته نیز ۶ کشتی پس از دریافت اخطار قاطع سپاه، مجبور به لنگر انداختن و پذیرش دستورالعمل‌های ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137614" target="_blank">📅 10:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137613">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4114548394.mp4?token=vQ3UXVnd2UFpf-DK9kHb20MGRONInIFZTVif9_DqLZ2kDluhlb2jhrfPr4O_CCGMue__B9hcXwlslPHuFYwxur3Ef_xBIAkCbyY3yRoI3SUHNcIWXj64loLul1U715z3DyhhKKqj8d4GxELjoxeRyPpXfWjfT-liKPggszYSKp8W42lRz8APiycliLPxPTTOd7w00FYxsfal15CjrllrKO_wgcNG_BLrtjbyEi8xPsK-t3Mm5E1n-dIczW2hcx_cXcx7OY5nZ4q2shAt-za6tIjt_6o-9ADAzckKhiJ2s9J4YEXy7sDBa-5pQi-TQSIoC7LeWuqGiUzwXSBo80yOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4114548394.mp4?token=vQ3UXVnd2UFpf-DK9kHb20MGRONInIFZTVif9_DqLZ2kDluhlb2jhrfPr4O_CCGMue__B9hcXwlslPHuFYwxur3Ef_xBIAkCbyY3yRoI3SUHNcIWXj64loLul1U715z3DyhhKKqj8d4GxELjoxeRyPpXfWjfT-liKPggszYSKp8W42lRz8APiycliLPxPTTOd7w00FYxsfal15CjrllrKO_wgcNG_BLrtjbyEi8xPsK-t3Mm5E1n-dIczW2hcx_cXcx7OY5nZ4q2shAt-za6tIjt_6o-9ADAzckKhiJ2s9J4YEXy7sDBa-5pQi-TQSIoC7LeWuqGiUzwXSBo80yOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارولین لیویت، سخنگوی کاخ سفید:
"من به مردم آمریکا یادآوری می‌کنم که چه کسی باعث بحران توان مالی در این کشور شد.
🔴
این بایدن و دموکرات‌ها بودند. رئیس جمهور ترامپ از همان روز اول برای رفع این مشکل اقدام فوری انجام داد. همه این مسائل تنها در صورتی بهتر خواهد شد که دو سال دیگر با کنگره‌ای جمهوری‌خواه فرصت داشته باشیم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137613" target="_blank">📅 10:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137612">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
هم اکنون حداقل ۱۳ فروند هواپیمای ترابری نظامی آمریکا از نوع C-17 و C-5M در حال ورود و خروج به خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137612" target="_blank">📅 10:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
امروز؛ احتمال شنیده شدن صدای انفجار‌های کنترل شده در شهر بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137611" target="_blank">📅 10:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137610">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwOuwDvOaKDMDGQGV72RVnkXsK0ykhLmZSuWRWZ-YffCBy_ezZZfNMGKUl3gt9KtxSOI4JL8rG22KkaRi4yE_bfttYVCFy4k3EHG8A1JWBWRxczrmf3fW6Yin9jfRC-e_Z7MLkzSpXD42QYLbXZEHgDmEdVVrnPbZ4oTvmHlig03jLKi-jsTIQ0bwNttkHm7gXZK-5gktzXfsIm8ajzafrgx2ZW6JW6e6rLmplQdxtX8VSZHFeo6TydTOLmLeWGbXuoxxFvkiT__zF-13R7FSuvqCvjYv58Dnl9IO2ou-VkA-BhRBOg344FwoyzxBImVb1Lq6LVNkmaHsmXZKNrogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در حال حاضر، ۷ تانکر سوخت‌رسان آمریکایی در آسمان خلیج فارس در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137610" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137609">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
انهدام مهمات عمل‌نکرده در پاکدشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137609" target="_blank">📅 09:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137608">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سازمان پخش اسرائیل از منابع خود خبر داد: در پی تنش با ایران، محل برگزاری نشست کابینه به مکانی امن در زیر زمین منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137608" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137607">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه اسرائیلی کان :  نتانیاهو فردا به واشنگتن سفر خواهد کرد و روز سه‌شنبه با ترامپ درباره موضوع ایران گفتگو خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137607" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137606">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhnjhEGadDfSmFRUlGWf9gkpsYmxjQDx-l4KrVcKHMZAGnt8PWy_6awR9W654zU18kPmDwOiDRS8idjxW0L3gyhxdQ8wlgKaHNxNykbFDnmUblOpaYgkLNIxOhpEqlb2Qmox2mLqZ2zL7lxxfWIm5VugS08estdAIXb4DW-UUNZYR0nXvG-u6caoh_rkAjBj74J8ICI1omcbYpCO9iDgWoWhyFfBIDj9Kgo2y5ZyfL6QJQqh_e2X4ZLbMSJ2cVtRRBwbTcmWyAiHrK4FLWwocKOjUyoK8UkbSv9sQ6Y6AfCmPOzt72vCVwe0KxIqxBiAujG77s5naYFvI5yqr_VmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌بی‌اس : مذاکرات عمان و ایران برای بازگشایی تنگه هرمز پیشرفت داشته، اما به زمان بیشتری نیاز دارد.
🔴
دو منبع منطقه‌ای به سی‌بی‌اس گفتند توقف عملیات نظامی آمریکا با هدف جلوگیری از اختلال در تلاش‌های دیپلماتیک جاری صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/137606" target="_blank">📅 09:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137605">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6gG1Igt13WWlgztPqUOWdMbg2dR7ybH9S-sVF2W_-k-We1mBK2l9XOSZZq34qhyDN1gusiZ9kjgjdkAfZao1bVUbj9rk0cRpRvf4udfEONJOz5wWxHwlRaL6-ovab-ic-dWsWd9eGgqee85dE-atSgJbto09tYTvMVDHZleYyw1bL7F2qmTYSD8duYMd0_zZ1ceqLLOpWicwcj5L-ziFktoCxnm5bZqQuV4Cw6yzv8DOjAliHk3r4vRvI3xoOIqsLgMa16AecfjLzQoAH-JOf6UMF6X2znKuF5AK5eXi3duSVEjgGc-I_5RVFUNlSOPQHe73NFFN90laNE1UKviUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی: تغییری در وضعیت تردد تنگه هرمز ایجاد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137605" target="_blank">📅 09:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137604">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فرمانداری امیدیه: احتمال شنیده شدن صدای انفجار بر اثر انهدام مهمات عمل نکرده، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137604" target="_blank">📅 09:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی شرکت آب و فاضلاب کشور : در حال حاضر ۶۳ درصد مخازن سدهای کشور پر است.
🔴
خط قرمز وزارت نیرو جیره‌بندی آب است و به هیچ عنوان نوبت‌بندی برنامه‌ریزی‌شده آب در دستور کار قرار ندارد.
🔴
مشترکانی که مصرف آن‌ها از الگوی تعیین‌شده فراتر باشد، هزینه آب بیشتری پرداخت خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137603" target="_blank">📅 08:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGE-_9p9Ez_XwBj_NmEz0poik9Mh51bz4-DYQfYSwqzdHOVQ8jFxkDWBoHYKMit56fkQUhZsN6hXyENKjluuMBv6WLu5SjqGa4VZIBQJl5ceNDzvsqJ2evWiN2DiWcMKM3tGLpnbMS2LrX9bJvw6TYuyjSeVZdLGXN9oS3ht76l-PpObY8vZ9TjYSowKZEke402TQGgXNLpUzs1mxT8VyUsdKIQUk1BO1yWxbMM3dEUGqgJDY_PyHJaa9cHCXvZAocVVCm7F1AAjupjN12fanZYf-8_8E-emzZDjinbUHrBlRJAKcsiWivYEiZIuPMf8gMCdJGaYUl21TPRYulfL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: ترامپ قصد ندارد تنش‌ با ایران را گسترش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137602" target="_blank">📅 08:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو فردا ظهر قبل از سفر به واشنگتن، جلسه کابینه امنیتی برگزار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137601" target="_blank">📅 08:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137600">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حالی علنا از حمله علیه ایران حرف میزند که مخفیانه از مذاکره کنندگان می خواهد به مذاکرات ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137600" target="_blank">📅 08:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137599">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-z1ntoeP45mrvlz_7NzQy-iQEtfklBnR4tNEgqgOe3zXc3KWWMdFA__7i5GqKZ2Bx6y7On-x4uA7mQxJmHyyd74IDerPbeno2WpeXDJNSc7WKheTFPrTGuq_iHZGBvXquVxM1y-ZVW1N568NRurFvFs_3TxWi7LI8z14oWUdVnDiyOaMFapPoDFRFDMQMB94mOq25AvkADvIUGFVwVlBwfl-qX29hMu5gbCqfeE4dVRg-BaLljs5y_S3viDhG1s55NB0lQuC4jA6T3ildiIxJaOsKJwY6wj0qYRGFHkBTks-_3CWbuiBSbROobmQKydu-AY0LxtcvjnKUFgXSThnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سی‌ان‌ان: «جی. دی. ونس» معاون ترامپ و رئیس ستاد مشترک ارتش، در نشست روز جمعه کاخ سفید، درباره ذخایر مهمات آمریکا ابراز نگرانی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137599" target="_blank">📅 08:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137598">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb72TwlarWlVf4DknPP4zWYU8Utwm3KRMBKoD03a2U9CK9LqMYyRi4GuLoR_7DcFebSwtUK4c0gjpRTX1LZC6lc-KcCuVKSF64XaNWGbOnpS0ZwYZ9jbs1J1-F2y9YpteyypManWMHZDslqdOdmpAIjqAAL8sFejI_BYG-mlR8N0hFqlKWQy9Z4hHvPFz12JuucYvkJU9oXwLHlT1eGxdRzISsfjVFYvUj88wpvg1118RdPoWMhjToucf3QelEGoL7JScvPgDK6svoMzHOQkz-gf_nWa6Ib0Ec305xmkEMJFmmXA5-qfcsJMvV3thR53PjGcbTNpBKnFKxpGfFvuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: توقف موقت حملات به معنای عقب‌نشینی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/137598" target="_blank">📅 08:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137597">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmcoRviqEcuSZco-ud-q1alVuQSh82Shv2bdBkqmFEgn2TDo49VevjTF1BWQnI1fQoXiHRpYtTi0k-g5WW43no3RemMOomZnCazyucfCTh4k02wudsDQzTWbq-rwlv-OpNXFlVsGL1iEbNOcKSa61v3U0lNQeDwPwoyccmA_9eNqGaqmMXrwze5Db-bX6z6wEwEC21_sRjHK0RLiko4RjDSEv7ExDJFBBnIFsMZC40ADhRswxatwbQ6McFQXyRMrmJNoeM9yQydEjapEreZ-aZjD9QyyhTRdBD2xTs3JxtfiaSWrYZFCPe_y86eyPg77kqthze-5_Is9dNcF-EHkjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا، ژنرال دن کین، در جلسات خصوصی به دولت ترامپ هشدار داده است که:
از سر گرفتن عملیات نظامی گسترده علیه ایران از نظر نظامی امکان‌پذیر است، اما این کار باعث می‌شود بخش بزرگی از موشک‌های رهگیر دفاع هوایی نیروهای آمریکایی در منطقه مصرف شود و توان دفاعی فرماندهی مرکزی آمریکا به‌شدت کاهش پیدا کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/137597" target="_blank">📅 02:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137596">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقام‌های دولت ترامپ:
ترامپ، دست‌کم در حال حاضر، از برنامه‌های خود برای تشدید گسترده حملات نظامی آمریکا علیه ایران عقب‌نشینی کرده است. یکی از نگرانی‌های اصلی این است که گسترش جنگ می‌تواند ذخایر رو به کاهش پنتاگون از موشک‌های رهگیر پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را بیش از پیش مصرف کند.
تهدید علیه ذخایر موشک‌های رهگیر، یکی از عوامل مهمی است که بازگشت به عملیات نظامی گسترده را به اقدامی پرخطر تبدیل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/alonews/137596" target="_blank">📅 02:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137595">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df9a7d6b.mp4?token=Cb3eyjfJn12hlhqGCnmhQOqsGRQ1c0n7OsBctGhmuQF3erOBfvFV-8RDQlDb_FsW2b5Zdbf2penKlG87GB_CM-V91yNii0mQ79Dl2YTvgPK6isV7HdSS1f3ywrAUWDN7dmKAg50lDGG1wbPT_D-iqUcjhD6QlMab2vHPAgC_om1VEVq_ESWtT4ndUzkQRDKdAH5eSIm-O_IXMfq1QV9To52WZWLS000uP8e3keCXp4hQW7ozWZvSizoscCdKBVAvwqg0AmSiw9iUpJ43_DwnkTSMS_OiM8AQPSppD2UTFeJyf2yLeoS-eFh1CIyipToh6ShQ_Y6YxGIPg4oi88pHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش آمریکا فیلمی از شلیک یک موشک هوا به زمین هلفایر به موتورخانه نفتکش لاوین در خلیج عمان منتشر کرد و مدعی شد که این نفتکش تحریم‌های ایران را نقض کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/alonews/137595" target="_blank">📅 01:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137594">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozenIUcvFftmkPFPw7y6KvVsR5bB4W7N5RymTd-Tmg_vRHpX8O3gZukrSGBV3NCMahss_gKnqB1D5776cP9TKLS0lJg62oApd90CzfuwgvLsw4SWTsdaxdBrQairOuV3vuIT04IxMwFA7XZ_TAkSCVBT8Km2r5myEwB67ETF25rBndzvkm6Se3Wm1rOLpGyPYBfXq0C_feeJVOj-pEtGVUNtvJDVIuGIqR2aqflpHTIxbCDNroamCHVNHVOJN3_KiQLgjPFTFWYQzkT9OCbeDBXrUkJCrz6StLjSop1OO3rXxqAJj8pRcrHidSi8vq-Rdf3m_asy_kR50HN-LdbIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/alonews/137594" target="_blank">📅 01:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137593">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سنتکام:
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/137593" target="_blank">📅 01:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137592">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0bd1b6b2.mp4?token=B1l8ynEF4QHnjMmi9HU3EjGeGwR18f5U4b5w9CHnK1BAoY4_MOSPmGU6Dbz8G6BIekpUrQEs7Ut_VAq4ULtXcHwzHhcoBVsXk3hIiexWpGAvgubxn7uUFZ81CnqbZhcx2N3ykyhpCF6TlEeggjub4GIwZ55SEm9EbAUI0hr-9xcBtMrr8mGg3M7saTXvJHIUm1FB9MnA6FozQVivoef5rq8JkYS_3GaFeJJmu0Qvl_lvDbWsVLYs9aW4drfo0Et26bO32lBE7-OjlaFNZ-4XP_8S2-v3mIfxM0tUTu_hdEpqF7KEnHR2QK1lZ_Sj2eBIBGvprNMBIV6CnMmy9YMktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحلیلگران در تجمعات شبانه در حال قانع کردن امت معکوس برای توافق هستن
🔴
یک تحلیلگر پایداری: با این محاصره اگه توافق نکنیم اوضاع بحرانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/alonews/137592" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137591">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/137591" target="_blank">📅 00:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137590">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-y91r-HMTpW8gJcKe8PnsjofNhv3trMCp3TzqR5uFWsXQMrH3yab84ug-RXGoHOfPcRXWjMGpKWMneUIjwKCoNaNtdF5Ehk3tpXyOjVedmcm1t6O-yt368YI_Aphn5grxPuGxjEUB6hs_y6uChji6omOJ7ttlzW9zkR708CcWGjlBn1BxsvXbgpoxJFVME-MOR2TG2IdpaKoSrM1aP8uuWSZXhL1mlP8DioPCfY1XKSBsVbibEBIQdIW7uyfUPzi6ZU9rBrEX6147OZsA_QetPUgUWO2HbYotfXhihxyVQ_E42bPUBeQEX0bbD_18nirniuifDMAPSpZxdVPmFp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی در تجمع امت معکوس که تایید کردند تنگه ننشونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/137590" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137589">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره اپستین!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/137589" target="_blank">📅 00:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137588">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2m_vo8KGJkOPyHwSOWL4j7uzYwoxX9mmfxxtnlHHisBq8SmgpEEiDoC_CUpFfYvYACqTMqWt2ATK5LG1piWtNvTgop8NqE1a5WREs7fN54CNFwHHDEMj0HvFrGv-IeElguvegmVhiMJUfIPswpOapbbObxzJFTAb7DF1pfqLJOmLGn_nNrsx-MJwpQBANKyLT7CmAy2R01AJ72MJgsEc-dcspHsGC-ZVyEmTe390hwOxkjuZfAQ3xYyoKpxuJ1EVxm2s4b2jYwTXFWYx7GboxwSo9N2Yq6WrcvwIky_EXsl1kSYUMrjkgK_i96-zrvDSGfQNlGjTdC2J0OVP4s61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7 فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/137588" target="_blank">📅 00:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxXZnAbsUBoeOuY2-G6N0fEYL_SrY9Zbvt5UM8B4nEOKM4zvhPfuRr4uNNKEGJq7NVBYizt7W3UTih2sbV_kq2_5GOobWxIPVIBpcvQrswfjB37FapXGhfnEbyP5JT3iH5mtJGpL7ROdShcqoDa1yLux_gTCKbdo5QqS98YKJnwXgbsQDQsy8Rf3UFgKWn107c8l0XCFNesPhw2LjQ6zAht7SQ8ZyTgp6pEFbe_L7YxqhCuiMaQ0Se_aDUZSVHOSB1LapMcAJPlLZ6_bQBpXJ99mYldrBXorH6SEUfXJbGwI5Lde9LgEYLb4L2xeepKeS9Yh0rMcTO_6qkoMQ6Oqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.  [@AloTweet]</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/137587" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0ac09831.mp4?token=fpHIThcXPyJ3fUirJQXlV8F86d6o9u6uwg6yeAmkoECtg_Bh6UTOdUqclbMeTEk84FOl5nELG_7EtV2wGQZoKgBdBUxQoSXkSTthvXq4qaQx_d1Yvk9r37Hw51RiwFebRQE4zrH77xdxHdo7JMS14vB08G4UejT1VzYgSjHDpSpqu0dOUZdfjkUhu5NFvfE8DYClzthSR9S8A-xbKnUoCL9OANN4AgqNm8fREVufxBDHWtxOEryn6CkZhHfFmqEv87wtHl5LA8IgYeHKabNnOIUPUvlsO5R5i7nBNfO3slKY_XaQ4UJISkiNtRnyicECy4Pkt5KiYUM4D6V4ZndVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جوون قائمشهری بعد از مصرف عرق با رفیقاش جوگیر شد، این حرکتو زد و جونشو از دست داد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/137586" target="_blank">📅 00:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137585">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAZMljDUMg5DRwCf-gW55bi2VSwZ8rc0sBP7NXw-9gAcSZ36l2OliTSt7HJ7K-mstg7uvw-FihwQ4Jp79nT6h-1yLrSRjpVtChc-iVcpO23WyN_c5BxasmW9cK8uQD27Vog591ja0mylsqKPY_6CGoQJD42k0p-UR4cya-wUMbLSJsPokFH2dAbUD-xjAkXQpjjy1u8Wjgxbkq_tRtCaski0pQA83KJ_W7Cz5cEEvTlU_f9o10q0Y9uUdimzCTPR1UsXqO_lK24HdGxdX1vjon3GRWvz4cUFmACJL8wlUWCzH3BFem_MIOPvQ-D4qwCLB3_f6tsVT6ka05OMakM0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری ایمان صفا :
من همونقدری که برای بچه های 18 و 19 دی عزادارم برای بچه های میناب ناو دنا سرباز های کشور و جنوب هم عزادارم
اینا همه بچه های ایرانن
یه سری تلاش دارن اینها رو جدا کنن و به نفع تفکرات ایدئولوژیک خودشون مصادره کنن
یه سری توله رجوی و چپول هم نطفشون بازشده هرروز یه چیزی میگن
من رو صورتم رو هم اصلاح نمیکنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/137585" target="_blank">📅 00:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
عراقچی خطاب به مسئول سیاست خارجی اتحادیهٔ اروپا: شورای امنیت و اتحادیهٔ اروپا باید رژیم اوکراین را بابت حملهٔ جنایتکارانه به کشتی تجاری ایرانی پاسخگو کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/137584" target="_blank">📅 00:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=py2F7bAueEhe2J9iGTps2bJdXx9mljvqJCHg3lLca3ii0kxKxyYK1XgvIc5Q3vRH5V5TtVgL9cq2tjqMu3bmZo5gpOjT5-9T39VbzfiPYTHFCn4I3n92S4SHNuygJ57UTqmps5pK9mMBD7_p2iPWTXbSPIjeMTz4NvFSd8TAx8mHnarDoQDNCKi0QWo-G8gf-P5UqVgDjYrFl0m4Ul7UQifJiukPnNTMsHkjiVDjqIs7tCZ7cEPEAobBV-IWlGxsbCMfCeGrNeDvOCmYBS0EfhPFIPuXXzCfjU2UMIK18DHgV7qjzzfDO7SoBZokLea1Wgvwyh0uwL_-cg9T_YO5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/430d4c737a.mp4?token=py2F7bAueEhe2J9iGTps2bJdXx9mljvqJCHg3lLca3ii0kxKxyYK1XgvIc5Q3vRH5V5TtVgL9cq2tjqMu3bmZo5gpOjT5-9T39VbzfiPYTHFCn4I3n92S4SHNuygJ57UTqmps5pK9mMBD7_p2iPWTXbSPIjeMTz4NvFSd8TAx8mHnarDoQDNCKi0QWo-G8gf-P5UqVgDjYrFl0m4Ul7UQifJiukPnNTMsHkjiVDjqIs7tCZ7cEPEAobBV-IWlGxsbCMfCeGrNeDvOCmYBS0EfhPFIPuXXzCfjU2UMIK18DHgV7qjzzfDO7SoBZokLea1Wgvwyh0uwL_-cg9T_YO5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شریفی نیا: اکبر عبدی پرفسور سمیعی سینمای ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/alonews/137583" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
العربیه: دولت ترامپ در صورت به بن بست رسیدن مسیر دیپلماتیک در خصوص پرونده هسته ای ایران، گزینه اجرای یک عملیات ویژه و گسترده نظامی برای ورود به تاسیسات به شدت محافظت شده هسته ای و خارج کردن ذخایر اورانیوم غنی شده این کشور را روی میز بررسی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/137582" target="_blank">📅 23:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoPAxyp-Dj5NBczODqa2YDvnH8UckRIy--5OBToFT6Gu_snBynSHEFmW-g6E_KDvTL1EpdlIKqJ-dfpE2Z5D2C8E6VHce0llmlq4uKLTqT1scJxlxVDlci73vYNju4-c7q-R7rl-Af8zw_l0_wwqMJRE1wiS7zjFVK__C37sK7Oolr2IU8PK-uoN5vii8LESk7lycB0FdTEr-4giyL4zIfL3ZD_9QjlDI2c0xLs2e_LY3il5OqvsRktD6mpFXH3snaT6Cctoy0ge_kIw3uOmOXyuCIS4XL7j4gUDpaAzohzX_lhJ9daKCDp_uP8n2cOJEzzjY6Ryya5Yi37S6la1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس تو قرقیزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/137581" target="_blank">📅 23:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YoYkXUJibGV13XkLr6DYu7VuMJVYGYWcPOYGk4Gq-6xNxViDavREq-3kQWcdiqprZcvMdyOHzxjlpILPiU26hEVAYiQ0BE8wEKqybUGyZkn6ijWXOKiDbgT00CE5EpXRPyZ6F4fTgc7jqEwAnmQhV0EWVF_ochHqOxAmt30RRmHy-HIX09MIK8nAHB5lBFDmCbkTsiCXZyMKJ_dodJxfBByTH_WgBotdMVM9gqHWR5zXhDs8Y8g2FEHkyqc4xx8bh3MGxGbFZXp8uSPxYRKqEEO7SmyCuDZKqADqdJCgT5ZlcP3NBnd5ioIBYkS_wK-oFDjcFrUPg8JOPv-ENcH0cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d2a9eeb2.mp4?token=YoYkXUJibGV13XkLr6DYu7VuMJVYGYWcPOYGk4Gq-6xNxViDavREq-3kQWcdiqprZcvMdyOHzxjlpILPiU26hEVAYiQ0BE8wEKqybUGyZkn6ijWXOKiDbgT00CE5EpXRPyZ6F4fTgc7jqEwAnmQhV0EWVF_ochHqOxAmt30RRmHy-HIX09MIK8nAHB5lBFDmCbkTsiCXZyMKJ_dodJxfBByTH_WgBotdMVM9gqHWR5zXhDs8Y8g2FEHkyqc4xx8bh3MGxGbFZXp8uSPxYRKqEEO7SmyCuDZKqADqdJCgT5ZlcP3NBnd5ioIBYkS_wK-oFDjcFrUPg8JOPv-ENcH0cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش : پدافند کشور بازسازی شده و بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/137580" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo4KA-XV-wkzLuHH-w3Ei1SCvsCQvsbQxNvPKd6HhhPtXk_ucHRJ5srEEfc265Ftmn926FDawKR_boqhAaF8KunJbY14KHUOcsK1D1RLUBoTUC3icbm6hL0MrptDf1o4vueWp7UdgO365grThYgB4t45m72YosgqtUQkoe7DooKgQ6UcB46FAWfwynII2MohjKu4t0FFO2vZJnqzT5a6LehIq2KFnqzaLDy3kn4gvZ65BA-iXk-qZuuqGdNXVxG01MK3S-ZAsgN6dhQWE79Pr-C-jDRlPLjXLq7Fi8BsbsS0zfSXusB-4czCoJRJZNw36uy6mm9eoIBaR33XjfqMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اخبار جنگ ایران و آمریکا
در سریعترین زمان باخبر شو
🆕
کلیلک کن
⬇️
⬇️
@Breakingpersian
@Breakingpersian</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/137579" target="_blank">📅 23:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137578">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/137578" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هیئت عمانی تهران را ترک کرده اما امیدها برای یک راه‌حل مسالمت‌آمیز و دیپلماتیک را افزایش داده و گزینه نظامی کمرنگ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/137577" target="_blank">📅 23:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRSn8I_tDH5maLaK8NQb2xI3Ca3gPIARPPlVfM9lBzMYvGlv5Ka5LM8vyZu8LqZhzz0EktjIQSkvNFcT7wGoc0VnjPnwCrPPPgoMq_Xb9xhuFpigYZmhwF33TCXeKBsvn-nssR78_Hb--9bshFNfzdOxaj4MFDDPoFAgs65Oxgeuuc4zmbpmW4hBGS6RCQUXJHt54TVAAQKhUl6us8xCZ_c6qjaNeRoYbnoeD0RxZQeMQ7PQQ4fn3FNQ6c2piLoVzIWZ3Kkzc3aHYPkUxfZjVQFhsL24q4NwUzQQErCvryX-06blprz92CpxNtBKCwRNBjLxZlHcGfVeukUc3UJvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:  حملات ایران به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/137576" target="_blank">📅 23:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اینجوری که قیمت تتر هم داره نشون میده، تا یه حدی دوباره به یه تفاهم نصفه و نیمه رسیدن!  ولی صداشون در نمیاد…
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/137575" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسانه های عبری: کابینه امنیت ملی اسرائیل، فردا تشکیل جلسه میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/137574" target="_blank">📅 23:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری / شبکه ۱۲ اسرائیل: نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/137573" target="_blank">📅 23:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcOICBTdYp0LC7coRr9Q8N0FZzn5GUoUNXkYhYRlyewjBgWU5Uu0LZ9437mOdnQ_lDBBfLEMkBMbFXsUV5H0_AV7NmSAExVBrarGABi-ZLA-Pa2Bj6gjdmT-3IXDixCHc0m3FBodlWjuRHi1kmwQ10cabJFWtApLxBoq8idErP3DYHsvt9UtoKnkLvpeGQVmNNyss5LrTvZfCbOsagIrO7VFJk7LXJL4RJsh1CwiEgA3smnuS16WZ-8q8PJ_rriI0Z3kqDjDix8D2vlo3Ya6dVNnqlPz1FjKgn6LRAvdi90K7fGluHzBzK9rKDFZToIqr0L2hHLT2Au2VlPMGRVOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
🔴
رئیس جمهور اوکراین: از ابتدای ماه جولای، ما نظارت ماهواره‌ای فعال روسیه بر کشورهای حوزهٔ خلیج فارس و تأسیسات نظامی آمریکا مستقر در آنجا را ثبت کرده‌ایم. این تصاویر متعاقباً در ایران ظاهر می‌شوند. همزمان، همبستگی آشکاری بین تصاویر ماهواره‌ای روسیه از این مکان‌ها و حملات ایران وجود دارد – هم پیش از حملات، در مرحلهٔ آماده‌سازی، و هم پس از آن، برای ارزیابی خسارت واردشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/137572" target="_blank">📅 23:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iALSUxRnHtVFjIsUx6bi8zM0JU5nJjvHqtX9VLpJ_SQ4V7uLCCsy5UKXU5Ca3Um9eerj0T8bBPNyKTUI7hqS3B_YFgGkKwSXjohMikavsHAnbGbvIPQg-90FanKaqVDx7rR6P_R4Ylb4rsunCNc0cCBYRzK6KUUmzxEBWhA29kP0pgFLmaRorKAw-g45uoy1Cw3lPaqkuXqQXtL0La_tzUp9j4HaHut2c9BbMsuPgqkEe9T1xBE-xcNW2g9yCfzf1CLoJZT1NcToPF3t_THTkZ8ChdLPV1_JxEo_-Q5xC6mZw6lZYImriMfJf6pbiJFJWOx2wZvcPtU9Q1I6Y3E1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
یک پهپاد در نزدیکی خانه بن گویر در هبرون سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/137571" target="_blank">📅 23:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی ارتش: بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/137570" target="_blank">📅 23:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ادامه آزار و اذیت ماهیگیران ایرانی توسط نیروهای دریایی کویت به مدت چند روز متوالی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/137569" target="_blank">📅 23:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پیت هگست، وزیر دفاع ایالات متحده، به MTV گفت: ایالات متحده در روزهای آینده حمایت خود را از ارتش لبنان افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/137568" target="_blank">📅 23:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3_G8kvvZjSWcuD4--wnULZJdxcoAY9D-gcricB2IFbPaiYsuV3-DtCX6guenRsSk9z1aCKYqelMGbZ9k7UrOKMBXKQ5xX1ckIUf_Qu9pAPTHqdFMRta-DAtQK3XiqCQFWc4jTUW1zlJ6IG0SVwz5VcvmN2OLAX0Ix8_zxvRsNB8zldtSRxfRZhFKdP87dlg1Nm8MFYDtQHokE3VuRFHnA6kQdTDMjTXPatfll_xaA1dDTjeildVGnei8cgmLgJCuBS2IMMJ3S-u0APWOMPrsC2OK5fhX6OdybkPsImMod2VKz0UYwD2vcmjWRZi-wjKQqOpnhchHqTM2nPcNgfSUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/alonews/137567" target="_blank">📅 23:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9qeRcV7BgyahtCzTCqfS08yGqWB6ieuFW_bLPgNJBFu92I4hCiRe7y8G8FBeQM0zr3DEmRk-DI7KcOp99xvb2xLQXjb3cKqOZkhTAujasHujMkemyRnTwRB5-D8WrDcCanZ3drRLrE5O0MO9FuCNw22KTILp1PUSBBA64vbxrYQ5cZ_TF3Gdz-lEZ3wtWGPTVuqlhyMXs4gwVIKsO4emjs49cwWz_co_lFRq9ejAYfY8K9plLY-kwy1z6J4FrezSmcY51_kK_TzozTfo19bwR__U2NAnHjO5oIJYVXL-H_xe46cQRvML_xeuiTeJPr6qCPNnR9dn57YZGasPNMaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری، گوینده جمله تنگه ارث مامان ثابتی:
اونایی که شب‌ها تو خیابون ول هستن، شعارهای
کصشعر
و متوهمانه میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/alonews/137566" target="_blank">📅 22:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137565">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل:
نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/137565" target="_blank">📅 22:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137564">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/137564" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/137563" target="_blank">📅 22:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V09hngwoz8d7UUi9t8rnNiBff6rWyoqPRH0MYC1zoxfGPk0jy-MfdFjn5FDechXsoYG4XCg3xu0DgLp_zQ6k9BEU8EuGzLqhXP3XBfSNWZaXJAC63jOmAc1nmfKkGMglvhPv0sRO4E9K3WK4_eo3hwpzv3e_slwClcTDLx1muMPCgNJlRLwMQGCXe5ABQ-55N2-qMJhg1cGPgz0DTaVskZkEgfNBwuqEVoaLB4gyZZDHqjDM7xx19foAFtD2mo5l2womhwOSPmbv91whGA3tQpN6K29h82e9iFEOyRLXOJSJxCReHa2BQTEgAQe8m4FG0iynXrWs2PwoFQXCJMFb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
وزارت خارجه:
حمله اوکراین به یک کشتی تجاری ایران در دریای خزر که منجر به شهادت یک ملوان و زخمی شدن یک ملوان دیگر شد را به شدت محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/137562" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjnapEDeVKh2JWzzeB1alQDVDTtWzEX3E7-OqP8zmcLPCma6oZO9_OGlEFQnsKPVXXiKjbQtm55LSPlAsUrSLU-bYvfQJ-8PpMCJ29WD2pyzSMZuVDWX2VpHjldsVcsNSDFHdejVg7Rs4T7BA5vRXgQm3NqSLfum7E-2KyTNIHvybS6hFaER-EB9vZNGjlEXOzJPNeudrpDOs_dFipjleDc3pXiucBkp6y7aCVFjXsXp9SsVwAXJ3vlTePtIIYWuXJw6FUv6Vwd49LzrE1_Y01TOzORZIgOzSmtqui9FpEyoqfuq6CuWIySGJBZfXSh1UP8piiQZMQ-l1tVswRL9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقت کردید از وقتی سوریه دست جولانی افتاده دیگه کسی نگران حرم نیست و امنیت دمشق رفته بالا و زائر هم اونجا بیشتر شده؟
🔴
پ.ن:قبلا میگفتن دار و دسته جولانی میخواد اونجا رو منفجر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/137561" target="_blank">📅 22:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی ارتش: تمام پایگاه‌های آمریکا در اربیل عراق نابود شده است
🔴
‏دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/137560" target="_blank">📅 22:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVVyb-g2YePYZou31bX3ZHDejh_PDr8yah1shLH_BZndqYluvcZOdelF6BKpvQrvdzVTQuw9yhqlkeLl2M7TvBraNzN-ic4OWnev7sPwC-yxVL4PxjG7tl21f6qZakguhRdagd2Rtxhc3BZCBjmHxLQNNZEktX9jYxFLqWdTWFFWdjajE8ySHWgocONmM_2KC7RHFEf858rqAvjG55cJcd6OSUafiM3wt8poUOLDuys6wLqkq2Ovcm24mq4IHw99dDljg1wN_jFzPss_a3BlzKdtyzRywBc6JyhMURNljw63ZoWZ-QUGldkrLJnrHoSqPMja64qSSgHx4oD4jQ6i0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش محسوس در ارسال ترابری‌ها به منطقه؛ به نظر می‌رسد هر چیزی که باید به منطقه منتقل می‌شد، شد
🔴
بیش از ۲۴ ساعت از آخرین شلیک آمریکا می‌گذرد و گام بعدی مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/137559" target="_blank">📅 22:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=W2dwFPhBmVvYZT2PbsF3sSygKuEFSubGZIOc3XNeoc30vgJmZ9oYnzq_8u4tyMsZdywcwuLt-JY0K3g62dv4mg01EMmEKZnGCei1pvo_fUlEm4lzt_iotg_1zzFF-j5YyAhQ62HfJljquGN9hSQ78hUT4sVgd_fA_IKGwabZdk6ZjMi0HpGTmGeqFDILLm1dMcFshF9C0g1VA0QbsW74fIZw3Mf8iXgl10Qxl9kaSyNQlVHXXHE-rxOm70kAXiQDiqafe44cpfPsXPjyRR-CgNUkHPi0RS0FNgZAhriB-QMAfDeheRMKxuqO7DxZgKRx4-oPZGXsMpEZ_P-I53bLgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=W2dwFPhBmVvYZT2PbsF3sSygKuEFSubGZIOc3XNeoc30vgJmZ9oYnzq_8u4tyMsZdywcwuLt-JY0K3g62dv4mg01EMmEKZnGCei1pvo_fUlEm4lzt_iotg_1zzFF-j5YyAhQ62HfJljquGN9hSQ78hUT4sVgd_fA_IKGwabZdk6ZjMi0HpGTmGeqFDILLm1dMcFshF9C0g1VA0QbsW74fIZw3Mf8iXgl10Qxl9kaSyNQlVHXXHE-rxOm70kAXiQDiqafe44cpfPsXPjyRR-CgNUkHPi0RS0FNgZAhriB-QMAfDeheRMKxuqO7DxZgKRx4-oPZGXsMpEZ_P-I53bLgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏مجری صداوسیما میگه موساد بچه هامون رو در دی‌ماه کشته بعد احمد قدیری کارشناس میگه در دی‌ماه در یک اقدام انقلابی گفتیم کف خیابان بکشید چون دستگیری و دادگاهی و اعدام دنگ و فنگ داره و مجامع بین‌المللی هم گیر میدن! همونجا کف خیابون برای حفظ« پرستیژ» بزنید بکشید و خلاص...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/137558" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/137557" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNR1dQYGWdIs4G3FnqUtQJP75nU-uddOxWLdYdajnAVxl5NQypj2M_xDGhNet2EOdEzZ-dgbE7M8JAaWOlNijH5eveq9-kemJV0unrp-nLFqpg_Fn3GTK73HML4ZmPbnscAP5rzBi0lH9puOnxpsFNulE78LDvicF_r9blhkwFDy6vbn4zKinQFfHJunmvwLdFxF15GPz-G_95542VlnWg0A6-lON7xJt43A5b1R7EuWnrPdPFRlVjOuE5seUYpsoN_mEQahvtmcR8jWP4z_plPusZLMK7FeUmPS_FpEzZjE0VvX5KJVM4g7K4_eCjrqDjeX46YxpthmsHfNKfQNtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژیلا صادقی: شیر تو آمریکا لیتری ۶۰۰ هزارتومنه ولی تو ایران خیلی ارزون تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/137556" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/137555" target="_blank">📅 22:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=FcO3IwVLBKUWOYt74DxNEZNB0jM-wLJ89DVg-LEMKKEGomPlu-lfrWEngB4m5nRylWy7RcQgnriUQH1uDptoKylBXIsoZeCMWjjFBMbRBNtvCn62VW4xSejnOa1fSmFD6GkL0gMWukxiqfA-N4kP-f3y3clTF7feJGbhmWxb4dhH3fNlLdzA9htXhClkJWCDAJLYi2hIYnB7TLMsHdySZz_vYqD7u1eekMA91GFIAxjIAg3_21xaRRJ_FAMC4mtsODWUdWyGQlEyAZdYUaB27p_cNOKNcdSmIEtZUj5Yp3eSUHEQBtf71uKjVRGnKRfK-chxzbGlnC1LTmeHLDjxGmQY1KDYVFfZBkuGZJEkeZ3RknI128UZbY1VOZ8yd7qh45mIvVP1-_e_BvIfxobnoq-x9K08uT-DPgc--YdAwjDWAS-FW1FMu4fTBoV2r9piKJ0han4oL-EkL5dbB8cJLNwL5Ln39SHimeZ7Yr62m8Cp21ubaockKe7HNXGDMYXJ6hRX3Fs6-13gh4Ody_Tgb7-BDAjZn_-SP--JKxfSg5gvT-3sKoCCaQdvjKf5Z7UAMhXEPr7FFcWshj4fTLKXDVQKNRliY56REcfi5MVqifEgiueMln6heXwqFrZjKSSDZh4k6IPZD0aceV6KzkDc48-HJsUEgKWIvVS0jah8PyY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=FcO3IwVLBKUWOYt74DxNEZNB0jM-wLJ89DVg-LEMKKEGomPlu-lfrWEngB4m5nRylWy7RcQgnriUQH1uDptoKylBXIsoZeCMWjjFBMbRBNtvCn62VW4xSejnOa1fSmFD6GkL0gMWukxiqfA-N4kP-f3y3clTF7feJGbhmWxb4dhH3fNlLdzA9htXhClkJWCDAJLYi2hIYnB7TLMsHdySZz_vYqD7u1eekMA91GFIAxjIAg3_21xaRRJ_FAMC4mtsODWUdWyGQlEyAZdYUaB27p_cNOKNcdSmIEtZUj5Yp3eSUHEQBtf71uKjVRGnKRfK-chxzbGlnC1LTmeHLDjxGmQY1KDYVFfZBkuGZJEkeZ3RknI128UZbY1VOZ8yd7qh45mIvVP1-_e_BvIfxobnoq-x9K08uT-DPgc--YdAwjDWAS-FW1FMu4fTBoV2r9piKJ0han4oL-EkL5dbB8cJLNwL5Ln39SHimeZ7Yr62m8Cp21ubaockKe7HNXGDMYXJ6hRX3Fs6-13gh4Ody_Tgb7-BDAjZn_-SP--JKxfSg5gvT-3sKoCCaQdvjKf5Z7UAMhXEPr7FFcWshj4fTLKXDVQKNRliY56REcfi5MVqifEgiueMln6heXwqFrZjKSSDZh4k6IPZD0aceV6KzkDc48-HJsUEgKWIvVS0jah8PyY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: در سیاست زیاده‌روی کردم!
🔴
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/137554" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/137553" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI) اظهار داشت که اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/137552" target="_blank">📅 21:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PMThTw6amBbDIyxqvihDbUs6OLiFzdaGuQExb-4Id0SRpK3FJoHbknDAOUQgwDEQ1ZdyrJoLxd5Y3oI-QR_tsrVb-D1qgMzrGCFSNTI2SROPRDuVI2cq95QJ935xgZ4YPfKKgW0GDu_gUcF3w3MOmnluXVzC6xRy8zFHvlevZquZ3SH7XlskVFy2ZUU4Ek1e8juH5EEft1IOB0g1_3O1zQj_YVOgC36ajCIf0N95pSlvK0kK-cnC7HQHABb7LDzTNOiwMPYeyacv5L9NsaXnFu8-0giKVxaScUuhIedWMJOycjuXpNepS4Kyw2rEfXfxq5-zLECONJzNGYZpNFo78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای آواکس E-3G Sentry متعلق به نیروی هوایی ایالات متحده در آسمان منطقه به پرواز درآمد.
🔴
این هواپیما شب گذشته حضور نداشت، اما امشب دوباره در آسمان درحال پرواز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/137551" target="_blank">📅 21:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzcnQkAey97nmKy1rxXJZFigy-iWUWJQXgTWssvlrhFnrGJvlnmIybsDIWCVKmB9CIC7aXH68gZmmHoOcGcNleiW57Qo3WG1JdInJ1lhI6npk4IUpcD1yMBDm7AaXove_1SxJRSoeEPOvm-VzUdd0uQTToI8puUw05FtYCfVuOe3T_NNAt2d3Oo7n4s4iuTDC4UuDgBC8V5cBHfEVAJw29Md8kf4GYzxe_OH5CLV5m7TkmAMOc_axV1vCgNWC6Ep6q3c786twOpjlLpi34Wu_csVCFTJdvqvODEFpOBo3U3B4Lpv-rnFeexM66PzdaiTla02PWGNqf8kVffsRDNMdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر میرسه عملیات پل هوایی آمریکا به پایان رسیده؛ درحال حاضر فقط 4 فروند C-17A در حال پرواز هستن. هر چیزی که باید به منطقه منتقل میشد، منتقل شده حالا بعد از حدود 18 ساعت بدون حتی یک شلیک، مشخص نیست گام بعدی چه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/137550" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
