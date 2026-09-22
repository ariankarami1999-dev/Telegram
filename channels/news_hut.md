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
<img src="https://cdn4.telesco.pe/file/lrwVBpeIKeEicp3YX4wDP_i2gOYKbdoo_gXW89bHRZgskEmRVv7AfJ6DP6G2vN5HoQfO_Ybb39DOrNXXtUovlmlAILJcUchy8VeJ_iN_YysOEfLk1GZTQADXow2eMs-A2NZ9Pf77nggC2ENZpHwmKK1NXmvAaISnd5yaCzqDZbceC4AyG-JqSamQmq4P9_2i3WtZ74ZSIFd4ZboorUEr5g1JuAEuYlnkwiy-xSkCe9dQLG0GBXGCZvE8fjG_PiZWWFjf1MFg7NDQwpNP9KAuw0IoZmblBP6ECVTQsCQDRRH_Mmolzzhqk3zbMdmVI-uzEubEF1qxKQD3NOKzTRNANA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-72032">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPc8osDYHn3jbAucrtLJoLVv93zKe4FdZpCdgzcYCJcfe4OAOiqmDeef9fNLBK9klKXjMgzB1ANn89b0DxaR39ibEI-LlYPrdL2o53IrGTS6KE2oK8mNKN4qd66UfC4wjzq4Tl9SI8n_vS9MGhGpPDC-Q_pX97wfqPorsqFQ1lhuNoGh9pfH6xtcRI4EVbEgXLUZ9pAL9QG3rjDLt1frt7YXUCtAfuEWjWlk82IodAOt64d9ePCkaE1Tev-eK3F7LZ4OVXWJ9moib-Mz4qddnrYnepJ0orUXPzNoqT7OAG0KxXx-yx2u3nOKSylh5Aiog4j64hqgv_kwRfaUQUPz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/news_hut/72032" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72031">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=gjL07BLfILxaXUs-uYwV729f7_kzQPKvINB0muFHd064A4JxBFGugDslWmZPQS-KimFehh8yc9xG6vCm3mh1Kt23xpWqpRDR8iAk6-FXwUTq1FfGkk6csNXMZEanrbpWzoPxrOgJDPG6RykGUC4WE6x6mbEtH3Gq9Dkrhhi0nhWg6pX3-uqkcJ-Yf1S22hI4csJRSU-JuUtBmHKQlR2khBVCfNwx-8cr1t3y69WA1dhyoMJGyh3n6G_MEhpw5zytKYxDWOqCRGTl1IUyxEM7erMTm15692RbRvxxDfMqEiX2_u7NuH-K0OIZxz1-0YVng6V18_K0MeFJVRFMNxVeqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3534317cc.mp4?token=gjL07BLfILxaXUs-uYwV729f7_kzQPKvINB0muFHd064A4JxBFGugDslWmZPQS-KimFehh8yc9xG6vCm3mh1Kt23xpWqpRDR8iAk6-FXwUTq1FfGkk6csNXMZEanrbpWzoPxrOgJDPG6RykGUC4WE6x6mbEtH3Gq9Dkrhhi0nhWg6pX3-uqkcJ-Yf1S22hI4csJRSU-JuUtBmHKQlR2khBVCfNwx-8cr1t3y69WA1dhyoMJGyh3n6G_MEhpw5zytKYxDWOqCRGTl1IUyxEM7erMTm15692RbRvxxDfMqEiX2_u7NuH-K0OIZxz1-0YVng6V18_K0MeFJVRFMNxVeqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت عجیب سربازان روس که به بالای دکل ها رفتند تا با استفاده از سامانه های پدافندی دوش‌پرتاب(MANPADS)با پهباد های اوکراینی مقابله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/news_hut/72031" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72030">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/news_hut/72030" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72029">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/news_hut/72029" target="_blank">📅 12:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCAxwowg34yv5T1dZ9cQ7PM0UE6CefyC_ERtRGINGV8sVmskJTHYP5RVOuRy4miFYtlwkjSGlCiyATUXVsOtRXM6SJzSsmbZgVoEtqYNS9egyug2t71BsEImHqWMRCnZCULtCAmCvvBYWprJOkgPpFLkxRKrJB8xgL7WPRIwGwJbKezuuRNdUxeKo3-X-oUTFI0EtFzWrkKY2o5z1Z34XBkZXzQac9838A25_VM6ODbFhf0TBR4V2eCExfmLUtBg49gQw8k2VdotZ_XG9VBzbS9BGwI76rtKMp57qKtp540OTNblKq0RiofF2e8FiLKduogl22C5xM77ZWzdy_ELMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست وزیر، گفت که بریتانیا پس از حملات پهپادی و موشکی حوثی‌ها، پشتیبانی «سوخت‌رسانی هوایی دفاعی» را در اختیار عربستان سعودی قرار خواهد داد.
این پشتیبانی که انتظار می‌رود در روزهای آینده آغاز شود، شامل یک فروند هواپیمای نیروی هوایی سلطنتی وویجر مستقر در پایگاه نیروی هوایی سلطنتی آکروتیری در قبرس خواهد بود.
مقامات بریتانیا گفتند که این استقرار «محدود به زمان» خواهد بود و احتمالاً «برای چند هفته» ادامه خواهد داشت.
برنهام گفت که این اقدام به دنبال درخواست عربستان سعودی برای «حمایت نظامی» و با هدف حفاظت از ثبات منطقه‌ای و منافع بریتانیا انجام شده است.
«عربستان سعودی حملاتی را تجربه کرده است، به دنبال اختلالات احتمالی بیشتر است و ما باید این مسیرها را باز نگه داریم و از این رو با این درخواست موافقت می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/news_hut/72028" target="_blank">📅 12:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=EYFeG_tl8WOY4AhVHJViuiD2T3uywAYtEJ4aLJBrKOwzf7GCvHz_NPuN_GE5de6rhKoLTFE3Fw3dg1XkNLw-9CQhH1dOAGNnYY6nPIfB3IMVjSHmWpgYD2beSecdUUzJJUSJTPh8BAtEYZnXfSMRKUFE9p08pJx2-Z9A9LjMR8WQ9m4SsU_GrUABZsp_Z8L_54WdgHIkQ8SoweZ7HzzH61e6rAlMEIGZR-y8cxVhc1x4e7X4AfrR2lXOd_8PU05aFmMPEqoNsyModjJywJwZWb4e_AnV2b7fz-r6W6hrhLEHwCWdk5TwzNN3mM1B7diF1Ccz5YGL6sdE-a3j1IEqiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e88d60053.mp4?token=EYFeG_tl8WOY4AhVHJViuiD2T3uywAYtEJ4aLJBrKOwzf7GCvHz_NPuN_GE5de6rhKoLTFE3Fw3dg1XkNLw-9CQhH1dOAGNnYY6nPIfB3IMVjSHmWpgYD2beSecdUUzJJUSJTPh8BAtEYZnXfSMRKUFE9p08pJx2-Z9A9LjMR8WQ9m4SsU_GrUABZsp_Z8L_54WdgHIkQ8SoweZ7HzzH61e6rAlMEIGZR-y8cxVhc1x4e7X4AfrR2lXOd_8PU05aFmMPEqoNsyModjJywJwZWb4e_AnV2b7fz-r6W6hrhLEHwCWdk5TwzNN3mM1B7diF1Ccz5YGL6sdE-a3j1IEqiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو صحبت کردن این پسر با یه پشه که تو اینستا خیلی وایرال شده
@News_Hut</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/72027" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72026">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/72026" target="_blank">📅 11:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=A21dZAOjir5KoxXlD1BvljSYhOg-9zqs7giyuBqmMoEAnZdUsDKzxM7Fp5ceLEEpLAvu7gqZlaxvwOchzEhtJ-cq35Vk_7GlDNwRMbWs11KOT7lIvPsUMhq7qUlhI9H0VQVq4_dwn80ey81D5DuW8-nWSDt3uLYCDDDfJ7QvjXBaANAofF8vc_K7rkYI5U6gGIqmyWWZCWiWkImT5tupKl97ezBCIp72W08oYvyd6pPcbyel_CCnHN5bDehrgP6cKNaOvo-G_fQlr6J7z7aElzdKBL4xsTf51ShQkewIndzX-3HCLyGsQfpNRyPirsehLxyLGDI8lyDsMvedWR3xqHNbeF9POWpiy-uaU8FQt3uR9qMeu4ye9WOt7w6sILqLetOreepCut-ZibzLpvhVmoKoTh9YEJB6FYJcTA-5SpiElPmE-w66EnV8QPScf2o2wMVNhp6vHoP5kDTrEFztu5h3K_pKrl-KnfRpK1wvjSakqAfRfxvlQtUtXYRoDEFaOKuSemuPpNLFmuoKR2UiJXx3F_MiEb4UCD9k2K2yUXPwh0PEKSMhToJHNRmAuO2MrF1PxCRazP1nMwUsoPJg3UflzmpSkS2Ac0xOI-txkVt_m-LT79Qt-FWCkbZqCT8vLr2r9K-1Lvml9IqRzaDaHkUU0AxL_UrC5HxBbvAeIaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6404ec7a8.mp4?token=A21dZAOjir5KoxXlD1BvljSYhOg-9zqs7giyuBqmMoEAnZdUsDKzxM7Fp5ceLEEpLAvu7gqZlaxvwOchzEhtJ-cq35Vk_7GlDNwRMbWs11KOT7lIvPsUMhq7qUlhI9H0VQVq4_dwn80ey81D5DuW8-nWSDt3uLYCDDDfJ7QvjXBaANAofF8vc_K7rkYI5U6gGIqmyWWZCWiWkImT5tupKl97ezBCIp72W08oYvyd6pPcbyel_CCnHN5bDehrgP6cKNaOvo-G_fQlr6J7z7aElzdKBL4xsTf51ShQkewIndzX-3HCLyGsQfpNRyPirsehLxyLGDI8lyDsMvedWR3xqHNbeF9POWpiy-uaU8FQt3uR9qMeu4ye9WOt7w6sILqLetOreepCut-ZibzLpvhVmoKoTh9YEJB6FYJcTA-5SpiElPmE-w66EnV8QPScf2o2wMVNhp6vHoP5kDTrEFztu5h3K_pKrl-KnfRpK1wvjSakqAfRfxvlQtUtXYRoDEFaOKuSemuPpNLFmuoKR2UiJXx3F_MiEb4UCD9k2K2yUXPwh0PEKSMhToJHNRmAuO2MrF1PxCRazP1nMwUsoPJg3UflzmpSkS2Ac0xOI-txkVt_m-LT79Qt-FWCkbZqCT8vLr2r9K-1Lvml9IqRzaDaHkUU0AxL_UrC5HxBbvAeIaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اخوند توضیح میده چقدر رژیم جمهوری  اسلامی پول خرج اینا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/72025" target="_blank">📅 10:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=oM3JTz_kyIPjhe5NORI33M5wuqxU21ggEr52Hzk6HYS5GxX7hih9gpM_e8yf2RZ3FGM1Qu2D6fcYSJ2iMb-f5Vr9RKV8cJfbT8n6AquC3i1V9QDfVQGvU2a8dQLTWJw2khKR-zCwcCE-5t0_5-GHpuyz4u-PBZXtEI1jiPxU6leTRI2V_fYTq1OoxyjuYsJbDpg1IwFloAwpAS0VvDBUA7dnlBdA9L-lECmKiqh4y4obxh-wSK719UxNvFJttUa4GsDNOP0TkjKQoXUOsWf8OkIzksVggO3VvSU5f-MPQ-WVjBf7Me8GbibgbulXsb3mbs9E6b1jKKtneV1vBtCcWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d71cb9ab.mp4?token=oM3JTz_kyIPjhe5NORI33M5wuqxU21ggEr52Hzk6HYS5GxX7hih9gpM_e8yf2RZ3FGM1Qu2D6fcYSJ2iMb-f5Vr9RKV8cJfbT8n6AquC3i1V9QDfVQGvU2a8dQLTWJw2khKR-zCwcCE-5t0_5-GHpuyz4u-PBZXtEI1jiPxU6leTRI2V_fYTq1OoxyjuYsJbDpg1IwFloAwpAS0VvDBUA7dnlBdA9L-lECmKiqh4y4obxh-wSK719UxNvFJttUa4GsDNOP0TkjKQoXUOsWf8OkIzksVggO3VvSU5f-MPQ-WVjBf7Me8GbibgbulXsb3mbs9E6b1jKKtneV1vBtCcWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال گذشته مردی در حال قدم‌زدن با سگش در کامچاتکای روسیه بود که متوجه نزدیک شدن سونامی شد و با تلفن همراهش از آن فیلم گرفت.  لحظه‌ای هولناک و در عین حال شگفت‌انگیز از قدرت طبیعت.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72024" target="_blank">📅 10:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu6kGSs11XPV9GiVqyVG5eFIs9zGgzvlsKJsqIEx7u12THaHgfXOiE0xUR4EllgPo9Xk3gKoYIOs7rb58rlkCn7wSb0c1al7gBK3D5EM9JABAlyreZu-xunwqHPzl3uR-a-flCHJkfcLxQ4NTcSs0Wwvzbmmk3Erp1rG-ScXBn5uCgrUO-leN6uWTRq-8ch65CiC16EPHLJrc8JIM6m6VEIGBxIUZ2xua71BNuxzKOtbZZyKoIXC9QAMcj_orIddgpz8VQsrZaGCHO9gAoe1mbzzy7-jkHHzbXOMglMRf0c4QVoutokCsfD1-uKr4f8aQgnZJ9T0vnqeZ88utTuZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پی درخواست مجدد عربستان سعودی برای اقدام نظامی، در تعطیلات آخر هفته احتمال صدور فرمان حمله به حوثی‌ها (انصارالله) در یمن را بررسی کرد، اما در نهایت تصمیم گرفت از انجام آن خودداری کند.
دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، پیش‌تر تمامی گزینه‌های مربوط به حملات هوایی را آماده کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72023" target="_blank">📅 09:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8969619843.mp4?token=UQO1bpGpgPI-YUrutfGVLtZaQZ5ByKeo0aPGO0gHeVE2Na7kYSTDqQAzKPSsYfmAXSxzItCM-NAp_QPRbHRjr3_sX1B7aj1YFzaGcZPS-nLkjUuli4s_wOnp_TuUYmhXz1SbxVITJp42VZlHTh87rvzJFA5WRufWKz5b5DvL2eleYVp4xzMa-PsQYMNGJ_aH2zQqZrkN9ue96obh1Z9E_H4P_9gDd7I8haij-5UvQraOMUPIe_9jlNrEty8h30UsbDyLo_rvpARTrB3b4vuJv3U7A5OM_M4lKMtkDSQK89K0e9VsOJjz8SIhC5xn0E3D9e34PfwcxuRHOH1qtxQvKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8969619843.mp4?token=UQO1bpGpgPI-YUrutfGVLtZaQZ5ByKeo0aPGO0gHeVE2Na7kYSTDqQAzKPSsYfmAXSxzItCM-NAp_QPRbHRjr3_sX1B7aj1YFzaGcZPS-nLkjUuli4s_wOnp_TuUYmhXz1SbxVITJp42VZlHTh87rvzJFA5WRufWKz5b5DvL2eleYVp4xzMa-PsQYMNGJ_aH2zQqZrkN9ue96obh1Z9E_H4P_9gDd7I8haij-5UvQraOMUPIe_9jlNrEty8h30UsbDyLo_rvpARTrB3b4vuJv3U7A5OM_M4lKMtkDSQK89K0e9VsOJjz8SIhC5xn0E3D9e34PfwcxuRHOH1qtxQvKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/72022" target="_blank">📅 09:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72021">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=CPmHGB-VPHDDzKe0FFhATXdqLFCG_Z5SOeJbiML0Xrc6yPEzBXgfpkqzHGfBeNVdjgJ1GeHv6bDF56A72_0m-oa7RuGhGGTDSlAW5AHUTJoe2IwaKizU8_UPftgVBP_dyj2YEolZ6zabq00e8FCHSYf6jzSv24WHfT518SlimCccPZaJxPjmd-USAvEPbWMMukDwO9zJnzASQj4tgyb9xRASSvfCFTpa1SPIuKdL5c5bJdL_r6N-1CCjftJtv4C8l6kTIM3AZsdd-Bk2YzOi5Cg2pk2K39D28tirxmhYO6e55fPUnD-5uAWX9VIq10CzXSsHGYvqzT9ods22pKu9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f75dfbec.mp4?token=CPmHGB-VPHDDzKe0FFhATXdqLFCG_Z5SOeJbiML0Xrc6yPEzBXgfpkqzHGfBeNVdjgJ1GeHv6bDF56A72_0m-oa7RuGhGGTDSlAW5AHUTJoe2IwaKizU8_UPftgVBP_dyj2YEolZ6zabq00e8FCHSYf6jzSv24WHfT518SlimCccPZaJxPjmd-USAvEPbWMMukDwO9zJnzASQj4tgyb9xRASSvfCFTpa1SPIuKdL5c5bJdL_r6N-1CCjftJtv4C8l6kTIM3AZsdd-Bk2YzOi5Cg2pk2K39D28tirxmhYO6e55fPUnD-5uAWX9VIq10CzXSsHGYvqzT9ods22pKu9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو رو به خاطر «فیک‌نیوز» از کاخ سفید ممنوع کرد.
فاکس‌نیوز + ABC، CBS و NBC در اعتراض، پوشش تلویزیونی مشترک (TV Pool) رویدادهای ترامپ رو متوقف کردن.
نتیجه: مراسم‌ها بدون صدای زنده پخش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72021" target="_blank">📅 07:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72020">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72020" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMVROq-CC8O0zdQ1cVMoWw_HoVHez-oGGftX1DM3pREWgZTMC6Wt-n278ZduH94NxvqnML7yIXrT9pLLGYxiCRJJgv-Pvgjl9zyfPBtqzP7lnhTH7b3AzveDndU5SpmqazD-GI7qw8fZlbQBWjbefG2Ya2uOTZDW6lb0CZEQnk2yVc6eAZN65ql4_NUtHIWn9WuWiZUlFxeyp-K2mt0kITy391_S1uRvxSrDBM2L8vtI3BhH2wkvc-Tsjtrplk9qb4nHYohd7gzEqdpnU-1F2huNRmM580iBfiFCrirFSfVQrgXyeFG79G0lnkBg8ZjiszlDhmQxVUBSJjVYKjrIgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72019" target="_blank">📅 01:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72018">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=JOFKBSZeA4TXeyZZ0XupZF_ko8SE1JpcvF-6FRgMFddY5mvAJam46cGBumle3oCBnb0lX3SmqO8Jrfjho1j-Wmk4Ff279KCLQV6xSopEKAh1vInBjozIkuZ59PvchBM8q645zqt71ZCKKYrhzPReHml9lky-K0-yCCpqMQjoCD-EJf7KxfC4412_1OhnLz9MI_3zOClA8IxSi58AZeQ6jBYOWEfm3FOnTELIw18a0BxZNZQhckhVfBzp0BuKsx9hpmIBnb3sU46XN8jfuR5Rxr8krPFcdHOa1aNYrd7RjEWPeBIA_cfa7tA3gg5LlmOqsirm3HRkODq7GvJhINRRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99b0ae83d.mp4?token=JOFKBSZeA4TXeyZZ0XupZF_ko8SE1JpcvF-6FRgMFddY5mvAJam46cGBumle3oCBnb0lX3SmqO8Jrfjho1j-Wmk4Ff279KCLQV6xSopEKAh1vInBjozIkuZ59PvchBM8q645zqt71ZCKKYrhzPReHml9lky-K0-yCCpqMQjoCD-EJf7KxfC4412_1OhnLz9MI_3zOClA8IxSi58AZeQ6jBYOWEfm3FOnTELIw18a0BxZNZQhckhVfBzp0BuKsx9hpmIBnb3sU46XN8jfuR5Rxr8krPFcdHOa1aNYrd7RjEWPeBIA_cfa7tA3gg5LlmOqsirm3HRkODq7GvJhINRRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72018" target="_blank">📅 01:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdUqayfgsKNyfpDQnbwK9FLreQP6xSRwy9LbU1wGClXNMMNkrhxgc0IOssbU1_Pd8ZrlGmPIZWJPUWEIYttqq9srgfbPFjk47ZsQ0h2qUYVlAymJ597SwmOrLy3pnuZi52oM4FwCbEm445oRUqfdOJD-Sj2UKG-P8pM-ksxY7zAFNy2YHk-ES96vNCYH26DZ624HmQ4anuWB0Y1DZmfgmRPh5xyVSUK-w3xuxB6UuQJCEpYhQxiWE_D28lfiuSF2fSPR2rMYzqcogSRcynGAv8BPMlm94buTSU4ynod870lriZa60hmQckKVe1f8WQPXMRBMxLatqOKnM__naLKbyb5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2686a0e6.mp4?token=japXbHE4KBLcRGCm2j7-waFEEMlkR_k6R8zAT5wOQvzIsHkA4LrdXF3QZhtRY235SyXkNb3_vq2U25QK2igifXnmipB4HXq0TMy-Zn-uq7UR-rJbhvbeakNsfJghKbTiHUSX-R3p00EGiv3mr4HQxXqMA1Bn7dz3nH3fb9ojWHyI6NG0Wwmj_upV99xSnL0vzEDnmFB3tGtHJkDY3nKJ5n-jRVRk-wYslLaDmUbAf3-8oZTB-lShNiXCZ70jlONQ4AsdODi_IdVo8cH94RiCx-Uxm1uRLcyuU68Lvs-_s1d1adXzItXz0IQo7pl02iJIN2SEXcspPmVsX3hyfKajdUqayfgsKNyfpDQnbwK9FLreQP6xSRwy9LbU1wGClXNMMNkrhxgc0IOssbU1_Pd8ZrlGmPIZWJPUWEIYttqq9srgfbPFjk47ZsQ0h2qUYVlAymJ597SwmOrLy3pnuZi52oM4FwCbEm445oRUqfdOJD-Sj2UKG-P8pM-ksxY7zAFNy2YHk-ES96vNCYH26DZ624HmQ4anuWB0Y1DZmfgmRPh5xyVSUK-w3xuxB6UuQJCEpYhQxiWE_D28lfiuSF2fSPR2rMYzqcogSRcynGAv8BPMlm94buTSU4ynod870lriZa60hmQckKVe1f8WQPXMRBMxLatqOKnM__naLKbyb5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبری فاکس نیوز به نقل از ترامپ:
«در حال تصمیم‌گیری هستم.»
اریک شان، خبرنگار ارشد فاکس‌نیوز، گزارش می‌دهد که دونالد ترامپ، رئیس‌جمهور، در حال بررسی گام بعدی خود در قبال ایران است؛ آن هم در شرایطی که برای دیدار با رهبران کشورهای حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل در روز سه‌شنبه آماده می‌شود.
ترامپ در حالی که گزینه‌هایی همچون اقدام نظامی، تداوم فشار اقتصادی یا تلاشی دیگر برای دستیابی به توافق را سبک‌سنگین می‌کند، به فاکس‌نیوز می‌گوید: «سؤال من این است که آیا و چه زمانی کل کشور [ایران] را نابود کنم؟ بهتر است آن‌ها درست رفتار کنند.»
این هشدار هم‌زمان با تشدید تنش‌ها در منطقه مطرح می‌شود. ایران تهدید کرده است که در صورت انجام حملات جدید از سوی واشنگتن، علیه منافع آمریکا دست به تلافی خواهد زد؛ این در حالی است که حوثی‌های مورد حمایت ایران نیز به سمت عربستان سعودی موشک شلیک کرده‌اند.
ترامپ همچنین می‌گوید که برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در هفته جاری آمادگی دارد، اما در حال حاضر هیچ دیداری میان این دو رهبر در برنامه گنجانده نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72017" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612f18036a.mp4?token=t3Ocls12Ch-m2DAsSBZYhL3xcHeWbTsaOuzFEeEn68PlTS7F4m0ARS11nGAy1uBKOS2FPy7nE0U900yq7OhVH2_mqJL6omrhuKm6jBgkkW1RH32po6Dz2VkAulHHFpwkzCnaSYD0yHlzD4IH3MDe0d22xpip-68DszNzHF-HtXQTlXcIo2fPjaLhmeyDZgF-bUA4KPjXmA1kMyZAYlrvWTAkCGjj6utsDz80ZpUNkw6TU4prbaJG-qNF33Wx8rZ8iKgNTv_SEmjz5m2rn-L82F2YGmVwSABSOFgp4OuAIVOPTtzF5Y8Sozkrrlij6qZLhJDgcOOF25jAK6RYd7P0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612f18036a.mp4?token=t3Ocls12Ch-m2DAsSBZYhL3xcHeWbTsaOuzFEeEn68PlTS7F4m0ARS11nGAy1uBKOS2FPy7nE0U900yq7OhVH2_mqJL6omrhuKm6jBgkkW1RH32po6Dz2VkAulHHFpwkzCnaSYD0yHlzD4IH3MDe0d22xpip-68DszNzHF-HtXQTlXcIo2fPjaLhmeyDZgF-bUA4KPjXmA1kMyZAYlrvWTAkCGjj6utsDz80ZpUNkw6TU4prbaJG-qNF33Wx8rZ8iKgNTv_SEmjz5m2rn-L82F2YGmVwSABSOFgp4OuAIVOPTtzF5Y8Sozkrrlij6qZLhJDgcOOF25jAK6RYd7P0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
وضعیتشان خوب نیست. در واقع، امروز جلساتی در این باره دارم. عملکردشان بسیار ضعیف است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72016" target="_blank">📅 01:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqSixJ_p0xRjmInAUAztuzp89ZSqOqUCMsnftT6Xp6DzH0iX6M6UbiSRyDski2QEKU2stuvYRpOP2Gt5DMwlGL3EI3jUvOgYMPfSN1m9oby3shPuWLKfjktJx9xEjmnGj29xSv5bKK-hGHKSeD_Uc_RjVQBm7GSzF4GckXAV0jPudfCGMs0raUBh_v_cqVxaUY3yGwH3hvOH_fl7n4jzwhdFR7oUoyMdE80ki1cfAyK-KHd64Pl-fNA5-6pWZs1_miM1QHcDSPSgs7UQng8RT6pVoHHMTCN9EtUW3wSZWYQoeerzABDnsISf7ISQ1mQhowubQAYLr_ARRCQbDQ-bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امجد طاها، روزنامه‌نگار و تحلیلگر اماراتی، با انتشار پیامی کوتاه نوشت:
«اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه. آماده باشید.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72015" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترکیش ایرلاینز پروازهای ایران را تا مارس ۲۰۲۷ متوقف کرد؛
یک نماینده شرکت هواپیمایی ترکیش ایرلاینز اعلام کرد تمامی پروازهای این شرکت به ایران دست‌کم تا مارس ۲۰۲۷ در برنامه پروازی قرار ندارند.
این شرکت همچنین اعلام کرده بازگشت پروازها پس از این تاریخ نیز تضمین نشده است.
این تصمیم در پی تشدید محدودیت‌ها و فشارهای بین‌المللی بر صنعت هوانوردی ایران اتخاذ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72014" target="_blank">📅 00:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GblVJmG04v3yRx_PDH_muhEwr5j4lH1mIbDC0Uc-tj4LvdaL7wzk-QyFHgdgSG5h-1x6QplQ5RF7xWV-7UAgM_0P6BjTpA5xRrA4LEA0NJHyrwJ7Eiv9Ts8eF4xCXNv1AnNGebTh3Gme_EHboAiUHxW0hiGMqG3zRZmMxycgiTn9vcBh-eBaM6ZQoMQ7muMiYtoTgRLBeVy2c35MbpVn7HYQVrF3spZTFd_SaC0yqe8PLhkrlpPT211ukeCjQHmDxBypUMkL4hHkq8dL3wn25QmwfVQV1XGpyYnIIK8C3WzO5vurMkBGxAvTzuGWQMXi-qdiaii6gEcLRaD9KWGGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛مقامات استان لوبلین لهستان در پی حمله هوایی جاری روسیه به اوکراین، هشداری مبنی بر احتمال بروز خسارات جانبی صادر کردند.
هوانوردی لهستان در حریم هوایی کشور در حال فعالیت است و وضعیت تحت نظارت قرار دارد. به ساکنان توصیه می‌شود منتظر اطلاعیه‌های بعدی باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72013" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#فوری
؛حدود ۵۰ دقیقه پیش، هشدارهایی در پی احتمال وجود تهدیدی در حریم هوایی منطقه «کراسلاوا» (Krāslava) در لتونی — که در امتداد مرز با بلاروس و در نزدیکی مرز روسیه واقع شده است — فعال شد.
جنگنده‌های ناتو به منطقه اعزام شدند. هنوز جزئیات بیشتری منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72012" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxk5dO1calg_KtGoDQWttmejMjm1wtyzF5kdef7Fx7aGYsMLP7SmFv6Bg6BCs4g_5DFRNgoR7NYNrbV5iypVSkvaNoc5EgL9YbJz4zNcS1UqfwTCp-hiAuxPxlWKit6RVD51_soNlJl0b9REvipuGagNL5sFG7KFd_w7DsfnXLrfrDF0N3ka0UcMpiXpua7ksKbyrtwuMwWJZlo8UKHl1D0jJ1UV2ZbWGxHk8bRKDku2opgd4HaDTHcpC1ljEdrFuBE3Zr3cLpC7rQ_uCMqqxvcoaGUsgnnXd76dVcW5LWBMN_9F9u82x1-qbFmIXDXSY6p-2zDJ8bifLSjimYKVMhY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e699259b.mp4?token=hdmdTH2-cNstkLIJh8Zo7VxVAwaHF0ffEnAHKhXNC1YhMkxJ4vHFF5sM6rU-3zE5gbVZTmUFhb-6OfWYIFZID4-gKzJTkOTzZd4NgjaFNRS6Z5-uJ04BdHVrkwRT8IOIexJ7Vhu9Hjhojn-jYYDu95C77WRuwZvxZ2mbTG3GnE-FHVU4F99O703QyyHb0Rs3eIu0pUATuHHgrX2kDfGn6-QyZjedSrSxbrNh5Uhik2miqxJQxF0J-Sdn7Lh2jDljlGHvUzztiDF8x5meSzZSDVonMMdZFCOO-tOCHbutesvkPqoJNOUEH-hQwWESIOiWcdYbbBg6dHIVi7saHJhZxk5dO1calg_KtGoDQWttmejMjm1wtyzF5kdef7Fx7aGYsMLP7SmFv6Bg6BCs4g_5DFRNgoR7NYNrbV5iypVSkvaNoc5EgL9YbJz4zNcS1UqfwTCp-hiAuxPxlWKit6RVD51_soNlJl0b9REvipuGagNL5sFG7KFd_w7DsfnXLrfrDF0N3ka0UcMpiXpua7ksKbyrtwuMwWJZlo8UKHl1D0jJ1UV2ZbWGxHk8bRKDku2opgd4HaDTHcpC1ljEdrFuBE3Zr3cLpC7rQ_uCMqqxvcoaGUsgnnXd76dVcW5LWBMN_9F9u82x1-qbFmIXDXSY6p-2zDJ8bifLSjimYKVMhY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلندی ها به این شکل پرچم فلسطین رو از دیوار کشیدن پایین
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72011" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=mWNruglmY7bRSFUCwXuYKNgmouS5J3CP_tRDsRS3LnQeCwhYHdhDlLG6oFPYGP_wrBf2t_mSV5lCMxgeBM5sfLlWqxnweZm-Zoe7fwfnr_k8OfkjHIPQ0_w_Co9qjwVUhaJXA6WJySzqfaxVRVZsYtqtXiRyFGwTLnEHCoKeBY-fwTNJ2eRn7-Jd8sPPi2Fzmt7xVnZM_A9pqqkJE8p5i2r2GiGFR_arEi81V0l0-13phQCa-cf70PGyhy9pTW_sVBXi-q9Z5Wwc1etuxQTX9oG9wbyNlC_ecR8BHGv7_98Lj6BQo2_tyJZGvF8qnUlQAlkCFCTz53v5yXxAUB2pBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7c63375.mp4?token=mWNruglmY7bRSFUCwXuYKNgmouS5J3CP_tRDsRS3LnQeCwhYHdhDlLG6oFPYGP_wrBf2t_mSV5lCMxgeBM5sfLlWqxnweZm-Zoe7fwfnr_k8OfkjHIPQ0_w_Co9qjwVUhaJXA6WJySzqfaxVRVZsYtqtXiRyFGwTLnEHCoKeBY-fwTNJ2eRn7-Jd8sPPi2Fzmt7xVnZM_A9pqqkJE8p5i2r2GiGFR_arEi81V0l0-13phQCa-cf70PGyhy9pTW_sVBXi-q9Z5Wwc1etuxQTX9oG9wbyNlC_ecR8BHGv7_98Lj6BQo2_tyJZGvF8qnUlQAlkCFCTz53v5yXxAUB2pBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر این پسر رفته تو اتاقش سیگار پیدا کرده
و پسره هم این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72010" target="_blank">📅 22:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ مراسم افتتاحیه (بریدن روبان) پد جدید بالگرد کاخ سفید را برگزار کرد، اما به دلیل غلبه صدای بالگرد بر فضای مراسم، سخنان او اصلاً شنیده نمی‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72009" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72008">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=FyreOsYmwtapTf9Jlz4HsdzJZyti2lpuTlsLRb8k20wx8CLU_y_mGy1JMBZDmZkr-XdChIWwKyK6N3G-rZHV5XsqOVF-8Q35DWZsMYgg_kwrfJjZpSKB2tYdIiUPu5MtpDeMu2f3FgJWTWJEeJzJyLekq16Mmp4qp4y7LDSwr8rwA6kbvwJnm4Hqo_Hbz4dsScNMT2IicBsIvqRfDfX7Zb-k59_BC_jn2-PUikD9e8tQb_8jOt06xgGZYbT-hXgEwngI-bt46A3OUl4fSlLZZA0uBEcc4K6_HBD3_9VzIOvB7-1-lCovr7mFVKp0gAQC0vCW6z52i-wb355C8XU7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f4ea7396.mp4?token=FyreOsYmwtapTf9Jlz4HsdzJZyti2lpuTlsLRb8k20wx8CLU_y_mGy1JMBZDmZkr-XdChIWwKyK6N3G-rZHV5XsqOVF-8Q35DWZsMYgg_kwrfJjZpSKB2tYdIiUPu5MtpDeMu2f3FgJWTWJEeJzJyLekq16Mmp4qp4y7LDSwr8rwA6kbvwJnm4Hqo_Hbz4dsScNMT2IicBsIvqRfDfX7Zb-k59_BC_jn2-PUikD9e8tQb_8jOt06xgGZYbT-hXgEwngI-bt46A3OUl4fSlLZZA0uBEcc4K6_HBD3_9VzIOvB7-1-lCovr7mFVKp0gAQC0vCW6z52i-wb355C8XU7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس:
ماه نوامبر پیشِ رو، لحظه‌ای سرنوشت‌ساز است؛ یا در برابر این دیوانگی می‌ایستید و یا با آن همراه می‌شوید. و ما قصد داریم در برابر آن بایستیم و با آن مبارزه کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72008" target="_blank">📅 21:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=ANCF9JV5XU_nH2bXOIdWdiiBolBaXCf_0fc77otJCagXOIy58sCWcp_UsnCs9XN6KzsL3-zbcJ5j2fhTF_NbKdUye7CRdVLuQaJbK7WkHuW7QLh5q88XKsv2GD3qJ6VOsxymoNfH2mzOJvZhSDMVbUb9cWLNFfPCRfZPFvHFu21lyhPXUBsZOHrCbzgX-1NeGfy_kAQDpkz6Xw6sB_EPOS9STApyo0VC5UufwQKu2-j54o4QJjy-22R2GTEt6Rt46bJlolYYwr1vkm6YquWVjx4o_5oEcIhcWBeBX4oqKT-pgfBrEazgu9UuIjZyaB1OoY7stpV9VFlz-J9z2b7Mww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9de7ae59a.mp4?token=ANCF9JV5XU_nH2bXOIdWdiiBolBaXCf_0fc77otJCagXOIy58sCWcp_UsnCs9XN6KzsL3-zbcJ5j2fhTF_NbKdUye7CRdVLuQaJbK7WkHuW7QLh5q88XKsv2GD3qJ6VOsxymoNfH2mzOJvZhSDMVbUb9cWLNFfPCRfZPFvHFu21lyhPXUBsZOHrCbzgX-1NeGfy_kAQDpkz6Xw6sB_EPOS9STApyo0VC5UufwQKu2-j54o4QJjy-22R2GTEt6Rt46bJlolYYwr1vkm6YquWVjx4o_5oEcIhcWBeBX4oqKT-pgfBrEazgu9UuIjZyaB1OoY7stpV9VFlz-J9z2b7Mww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس:
این انتخابات میان‌دوره‌ای، رقابتی است میان کسانی که معتقدند این کشور باید آینده‌ای داشته باشد و کسانی که ترجیح می‌دهند شاهد نابودی آن و بازسازی‌اش از پایه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72007" target="_blank">📅 21:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=mwWrvQXsdQf4HUy_8PoiKBrwSk40e-Ga60UvkB4S0KuAWcFNcuqyxBQMSoieC9On8ZHqUeIvzqDCMzYdr2uqdc_2nZ0eoajHBFhFlsr1bTK302mai6vi6m7Q2R9kpCVll-8dzniHhvTk7njBNmZLhr-413imALXN7yVLFLKRwQDtk_oQ8MVhbddYJhO8CtfMVFY_LJm0I7IBvcgMwzkVAmCvy8KZNjA_7IDNPXKXGF1DPGBNZFR13qzBgGmnzLsUUUGrnqkwAtJDXB9eb1is0uFLur4U4Rk9h1PKnGr_hx77Ux7SKciWWQVW7JExMVs60T-lu-UUsbIVAvHQ5sAMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0543c701.mp4?token=mwWrvQXsdQf4HUy_8PoiKBrwSk40e-Ga60UvkB4S0KuAWcFNcuqyxBQMSoieC9On8ZHqUeIvzqDCMzYdr2uqdc_2nZ0eoajHBFhFlsr1bTK302mai6vi6m7Q2R9kpCVll-8dzniHhvTk7njBNmZLhr-413imALXN7yVLFLKRwQDtk_oQ8MVhbddYJhO8CtfMVFY_LJm0I7IBvcgMwzkVAmCvy8KZNjA_7IDNPXKXGF1DPGBNZFR13qzBgGmnzLsUUUGrnqkwAtJDXB9eb1is0uFLur4U4Rk9h1PKnGr_hx77Ux7SKciWWQVW7JExMVs60T-lu-UUsbIVAvHQ5sAMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از آواز خوندن یه مرد ژاپنی خیلی وایرال شده به اکسپلور ایرانیا نفوذ کرده.
و حالا کامتای شاهکار ایرانیا:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72006" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72005">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a929447dff.mp4?token=gp8lfzS19qxjKr9NjUFsGlV8eXS2zRo8uJkTediYVwQOL1MKOEVWn96uGdLy3aG0skmMb3yNvJF90LJEIcEsEMc0w3bQmr34Ya8BkcP2qceXPXMh8rmoTiScHb-FBD_w8qrBqZ_WvMraMPkt1XFziYjLjAvwm5leTLWMLGNmno_qkM43Su0fp5WsS8ODSMKKN4_jzZ-uR5geN35y7lOAb4qFNCIbODOFU_2m67Icnctm3cp_1wxSh28k9nAg3laEYsVQMVpQyNhzp7WZI8yi-Ceol2msffXBCen5fcozKI5A6RlgkgBvENSdxEr8fKaUkok15MAX7FpJIXGv6_biTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید حساب کاخ سفید در پلتفرم ایکس:
چیزی در راه است. منتظر باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72005" target="_blank">📅 20:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ad0122e6.mp4?token=IrU5ss7i0eZFSfctcPMZuaA5fU8T3HIT6V9WsBHFN5SnzCR6mOgue6NrxEGtjgc_jkwSdekXQjqJy19oVWe34GGRMI7i0gy7M_HntBHlx1QO4Mm_VRYmuu4YzfaA9Jkz5XIEJb8o-Ck409sWVvLGxu20p8FaVSTZCBXHcB2bcDk3NypOApTiAxEaLHjpD3OhFAoHsKT5cRrxT917hWU417erBcbpnouPZoWdMHnsKdDxOhKAldq9huyTATtVpP5ywz-htqQbysEr3ZTzq-_XWRyUf6RPw1Yh5uGvBgEvfZAryBkLYFoLA4DNcW6PQoHg9C4-NeY96YdQH98KbOOEcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای حداقل ۲۵ تانکر نیروی هوایی ایالات متحده را در پایگاه هوایی العدید در قطر نشان می‌دهد که بزرگترین حضور تانکرها در آنجا از زمان آغاز جنگ ایران در فوریه است.
این تانکرها در ابتدا به دلیل تهدید حملات موشکی ایران از آنجا خارج شدند و حدود ماه ژوئن شروع به بازگشت کردند.
برخلاف پارکینگ تانکرهای بسیار متراکم مشاهده شده در پایگاه هوایی شاهزاده سلطان در عربستان سعودی، به دلیل اقدامات احتیاطی مداوم علیه حملات ایران، هواپیماها همچنان به طور گسترده در سراسر محوطه پایگاه پراکنده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72003" target="_blank">📅 20:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72002">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f71861d0c.mp4?token=ng9P0AVe2ORmhhpexhq4WpS9tGHJSRFIr_vDMe-4lebN8DomdOFQ0dcIhVh3cShYCfbb4kNv1k51VTeTu07e7njD8XPqxwK9EJToEzrtmffp2MIR4Uodm38ZtZ1VfrJRsnpq3ZwqJTz5bYv01c-7LebuAbSnHUHjZ5uoKBTvJCLzPfpNHGE2eKIQFKsDDBnBJr0H913_QZ_ymUHzaF0J8uTeBwZKGe5LsKmekLZ-i9Hcm2cBkYy1nBMtMUbBl1R09OL1Th2488QPkboMdajyMi0Oxn8dWRxFHV5uIuUyC5PoIZx2COSJD9Sst-NXjZv7VHBQdskhoffo88G5_TZbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مربی بدن‌سازی:
خیلی از جوونا هستن باشگاه ثبت نام میکنن ولی تو تایم باشگاه، میرن پارک با دوستاشون مواد میکشن
وقتی هم که خانوادشون بهشون میگه چرا لاغر شدی و قیافت اینجوری شده بهشون میگن رژیم گرفتیم و طبیعیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72002" target="_blank">📅 19:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=XLiWn-Y3E4YPv9yIOJvW4Uk9R1LVetW7E6uMUOk4j-1T04UOpgPtGQh3vN5TIcI0YzD23cNwMHxLl_-cR9kxL2jz6vgivsNeMmmVkfX5NM5HSUsNcihwfRPLkosrNvi8cYYRzobGEb09JQdPbOgiwSiYp1v1By0NF8vROREjiUqHTcgc8rgslbJLSz8usC39A5vcL6xDBA5dnMjeaU4ZKpHDHEv9mBWTYWYDlEuwQdxYI4xhZW6-vC-oPSMCziMB7Xk_fLSJMhr2RWKJ0wg46ccocr9OJeQHwnwSCYWFOt8SpzJ2gdIEm9Uo3J91BvP0MWx3nNFtKxMRxzB5hbhpSxM39A8qW1-Juei3WnbK40y3KNYu6hd1n8d27acQZ9h6fadRlNyxTbi1QyU2Fw6I6WXhS5R32rQHGCAx0NZq2WGz6u6bLMgUHB_dkhIH4Owz0OCZgF2JCYELrR9s1XVZ-GDyotE8G6LoyMRdHQl0aTEFH7buk31b2UQZs1gwzvliQXUkrEKAfe4TcMLWHIqXVz1Lz_R_5n-cl2ueyAzXltmI-kd0Fwei63TsLezY9PaCskhKRJRliipVuSqHoz17cuhM4QOeXffNmPlWZQwLWcL3V03w7a0d-u-knmyo4b6hSHanxIAl_pewkTD7bqczUHskuLRJrTxIDtFwnjNr_Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
ما کاملاً واقفیم که قیمت انرژی به دلیل اقدامات تروریستی ایران علیه کشتیرانی بین‌المللی، افزایش یافته است.
ما تمام تلاش خود را به کار می‌گیریم تا ضمن مهار این قیمت‌ها، در این فاصله باری از دوش مردم آمریکا برداریم.
یکی از اقداماتی که ترامپ درباره آن صحبت کرده، تشویق برخی ایالت‌ها به کاهش یا حذف مالیات بنزین برای مردم آمریکا است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72001" target="_blank">📅 18:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8571b32102.mp4?token=lrgS3LxUEtGLKuJnvMzyF-amSuV9nWxo_GMGC5jNwm9dJMeMu3eliH8YTC3qKNZy9ADb6lJ1-T7JOny1HcQ8ngwX9EgMb59vXq-uaUX6YBMJxm4iQZWDw61O-Nmu3uMrzmudjOUlZkJZU36Hj76v0R6MsMtZCcOWd-MtP5T4PznyFNevlFX-k1l5zedNQ8WN8K9ZxCW5L247pTcXLSdzEH2FKSeK6-sjf8vMNCnYE95ACPycjebInVy7B-OKqY_ephqa0zGJtMFnpv9DeNcw8dx_1ZsgXJaO7YNMCwX1sNVx-Ctn7kG9q1_yvB2fV2I2ViC-0n4RjuVJUQ8XNb4dkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8571b32102.mp4?token=lrgS3LxUEtGLKuJnvMzyF-amSuV9nWxo_GMGC5jNwm9dJMeMu3eliH8YTC3qKNZy9ADb6lJ1-T7JOny1HcQ8ngwX9EgMb59vXq-uaUX6YBMJxm4iQZWDw61O-Nmu3uMrzmudjOUlZkJZU36Hj76v0R6MsMtZCcOWd-MtP5T4PznyFNevlFX-k1l5zedNQ8WN8K9ZxCW5L247pTcXLSdzEH2FKSeK6-sjf8vMNCnYE95ACPycjebInVy7B-OKqY_ephqa0zGJtMFnpv9DeNcw8dx_1ZsgXJaO7YNMCwX1sNVx-Ctn7kG9q1_yvB2fV2I2ViC-0n4RjuVJUQ8XNb4dkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس درباره ایران:
با وجود اینکه ایرانی‌ها هر روز برای کشتی‌ها ایجاد وحشت می‌کنند، ما همچنان شاهد جریان حجم قابل‌توجهی از نفت و گاز از طریق تنگه هرمز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72000" target="_blank">📅 18:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97u8l4PoawtrMoe0373WyQuIA7JUPuzcATZE5c1I3TJR3Fd_HigLXcCwcMzmVMwzRT23xaj3DuqA7o9hris2rjY7LUss-AAWCs4XB1CoTYHyuOrFTKKRhw3PKP8VSrk6NwxTlno9X4m6u9h3zm7RMHKloBDJPrxvKmtDT2J4eEptL9XaC2TsHdv7IRykKswMEzhiLdOQJBklu15_HcvW5fZM8PQ2aCEHUN_bWpG-VIwnDS-DIpZi-URnPhrwMHbKX0MerMaojk-FmWq8ukKjgReedWDoNwwAn4bTao9z0rVce8WxclGUZwCQ3kKY89u9SBGMJYj-SqnLAMvbvU5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71999" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=OyF8gricTlmbwVQ8N2V7ZpAxqA19y-6H705UGVov7vgwkvQEB-zpJQHVGWquJUfQaAOPMF4dE3s0MZvGDtyNnzfrvyu1GVm36lueKrJLg_IjTVdMnpflHAapo0D41jSX4ZCoOmpYjJDcrhKhTvG8ipMtb5quJnkh_a61AKR_PZI2mhW_Ysvi1I-hEANdT3QLOdzMciAxXa4j3fg_kP4Gk1_4WWVgJdJJN-V5nSrZdQPiHpLlZIEi5SoxF2rvyeFHoce69NLn2piqJ6y2uqCrTe58NfYFKTd-driX-sm5P_gnWU3cQNdqebQQLG1yvZqEJUmDv2m85HYZlJZjOW_65A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9e105be9.mp4?token=OyF8gricTlmbwVQ8N2V7ZpAxqA19y-6H705UGVov7vgwkvQEB-zpJQHVGWquJUfQaAOPMF4dE3s0MZvGDtyNnzfrvyu1GVm36lueKrJLg_IjTVdMnpflHAapo0D41jSX4ZCoOmpYjJDcrhKhTvG8ipMtb5quJnkh_a61AKR_PZI2mhW_Ysvi1I-hEANdT3QLOdzMciAxXa4j3fg_kP4Gk1_4WWVgJdJJN-V5nSrZdQPiHpLlZIEi5SoxF2rvyeFHoce69NLn2piqJ6y2uqCrTe58NfYFKTd-driX-sm5P_gnWU3cQNdqebQQLG1yvZqEJUmDv2m85HYZlJZjOW_65A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران ویدیویی منتشر کرد که مدعی است لحظه رهگیری و انهدام یک پهپاد MQ-1 ارتش آمریکا در صبح امروز را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71998" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71997">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71997" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71996">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxFINv-sJH4G46uAr_7JPIAvWFSrzOFVKdW-51T6WWV6KPjlyKlbD5vIBvVTP01cknDyfpR9p0tWOTwPQwKn4EaKaWVYARseETfyBePp99u_40zCh57AOE9u8Ip6_x8qArhATG9suzlPyPPSwzutubngKIWg1s7j0ffaYZEiu1jp0Dl18rG559Onj3BMrw5RNvw1evqBtnV7cPMvT1ELzqS_jkgj7HeLxo3q2AH0Ym1KEfEQ_4-2WKRhtSfNzM6SojZJCwVxwkQ64QyqxsUTtygkFHbry4QL8KY9tL9AKEAqhd8cdXvGY_icmXqjeM9WZNy-5Gm9lJownXNXLDtfOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71996" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71995">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=Atb1dHSbfy-Su2jZ9XGkSOX0_DRAix4pdYlILC2sED-i6b6VV91gZ5tXzTMqOnmlgXTIqkFLXdW4VZbrd5fNXJyMMFBpbRjKSnppBqtu8TTnDjJIr0Mmd0B7pHikH1rtGEfR_vVHn7G_A953WEGs_uJ9WcbMD3krAgksrILyJOwFAah6xwWUfjRS-AmGNfaqBoiENThcbNTOHgUouaWFfPyxJgBCftZnURT3fieuGAfcRwxYt4lmU3P_rXEqzao5byZ6ujZhMz41y3TAk7EYARv6Zy0KgPq91SQDtCNNqKyx253MURLPKVVn0sn4TMT_2XMFN1eXkPcucnRJmal5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5dd9ae6ba.mp4?token=Atb1dHSbfy-Su2jZ9XGkSOX0_DRAix4pdYlILC2sED-i6b6VV91gZ5tXzTMqOnmlgXTIqkFLXdW4VZbrd5fNXJyMMFBpbRjKSnppBqtu8TTnDjJIr0Mmd0B7pHikH1rtGEfR_vVHn7G_A953WEGs_uJ9WcbMD3krAgksrILyJOwFAah6xwWUfjRS-AmGNfaqBoiENThcbNTOHgUouaWFfPyxJgBCftZnURT3fieuGAfcRwxYt4lmU3P_rXEqzao5byZ6ujZhMz41y3TAk7EYARv6Zy0KgPq91SQDtCNNqKyx253MURLPKVVn0sn4TMT_2XMFN1eXkPcucnRJmal5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک: این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد
ایلان ماسک با انتشار ویدیویی آینده‌نگرانه از تعامل انسان و ربات، فناوری‌های پیشرفته و سفرهای فضایی، چشم‌انداز خود از آینده را به تصویر کشید و نوشت: «این آینده‌ای است که آن را به واقعیت تبدیل خواهیم کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71995" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71994">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صدای دو انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71994" target="_blank">📅 16:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71993">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=dkGRsyXoXysWe8JvstlNxIn1CmmGDAb3rMrZ979qnFEqMf4jkAmfVhmL7RjlnmYD6mjoCDVxBQXTM-i1q3UZt5hf66tlaFrlKy5LXAwTZ2VraQVMRa-Zhb6WUhnv7e_xkfkbbH7OMoew2uesOCS-hl-aY6pdEOSf4ayIVVVGBTppWU7ptWQQ9NGD_uQyvyYM-QJAqIpXpFz2QdmqXVKxk23Ls0Ob55wnfRzMWhLY4ntXGafwC4dsE7bBLADBGqHDn_WycHYi9Vu1i83BnFXTrLRJY-8VKXLslR781p7VxChDqg0L507XkgM072KrxOh4YWD4BqlPh-RIBnV-4JAQRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f918318e4.mp4?token=dkGRsyXoXysWe8JvstlNxIn1CmmGDAb3rMrZ979qnFEqMf4jkAmfVhmL7RjlnmYD6mjoCDVxBQXTM-i1q3UZt5hf66tlaFrlKy5LXAwTZ2VraQVMRa-Zhb6WUhnv7e_xkfkbbH7OMoew2uesOCS-hl-aY6pdEOSf4ayIVVVGBTppWU7ptWQQ9NGD_uQyvyYM-QJAqIpXpFz2QdmqXVKxk23Ls0Ob55wnfRzMWhLY4ntXGafwC4dsE7bBLADBGqHDn_WycHYi9Vu1i83BnFXTrLRJY-8VKXLslR781p7VxChDqg0L507XkgM072KrxOh4YWD4BqlPh-RIBnV-4JAQRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت درباره ایران:
در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.
چگونه این کار را انجام می‌دهیم؟
اگر آن‌ها فرود بیایند، شما نمی‌توانید به آن‌ها سوخت یا خدمات فرودگاهی ارائه دهید و نمی‌توانید به آن‌ها بلیت بفروشید؛
وگرنه از سیستم دلاری کنار گذاشته خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71993" target="_blank">📅 16:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71992">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">#مهم
؛اسکات بسنت وزیر خزانه‌داری آمریکا در گفتگو با CNBC: فعالیت ایرلاین‌های ایران از ۲۳ سپتامبر(اول مهر) با محدودیت های جدی مواجه خواهد شد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه ۲۱ سپتامبر اعلام کرد ایالات متحده از ۲۳ سپتامبر (اول مهر) با اعمال تحریم‌های ثانویه علیه ارائه‌دهندگان خدمات هوانوردی، در پی متوقف کردن فعالیت بین‌المللی ایرلاین‌های ایرانی است.
بسنت گفت شرکت‌هایی که به هواپیماهای ایرلاین‌های ایرانی سوخت‌رسانی کنند، خدمات فرودگاهی ارائه دهند یا برای آنها بلیت بفروشند، ممکن است با خطر قطع دسترسی به نظام مالی و دلاری آمریکا مواجه شوند.
این اظهارات پس از آن مطرح شد که وزارت خزانه‌داری آمریکا در ۸ سپتامبر، ۳۶ فرد و نهاد مرتبط با بخش هوانوردی ایران، از جمله ۲۷ ایرلاین ایرانی، را تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71992" target="_blank">📅 16:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71990">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=UBX_ZLKwYtosqZFMM8A43xjaXF3rDqVIm4SNvlgIq9fFDLuhzANAk3Z4Lk0FrmV3GPsjp7axyjMrnvsnrjTxz7l_GtGJ0X1uINYSe7_7u4Wd36IFNc_En22zi04qwM_soifP98POwC8zp9x1w1s5N_s9zd-gz7hH60vDEFYUTY87iWKOyf5bMfN0ufJBJ3_vDzMg_i-4_GEy9LfyRBijgmndMR8dKSOr7lh2LfotpY-55XwSeq9pWQl52ITYVwb-Ex2rxmOEUI3nuiYHHvB2o0wa3pKnfPm0zzkCWqvQKbd1NcffqM5iB41YK6kZUsunWjW-q7sW8sCsz0baW1sDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939066a7e6.mp4?token=UBX_ZLKwYtosqZFMM8A43xjaXF3rDqVIm4SNvlgIq9fFDLuhzANAk3Z4Lk0FrmV3GPsjp7axyjMrnvsnrjTxz7l_GtGJ0X1uINYSe7_7u4Wd36IFNc_En22zi04qwM_soifP98POwC8zp9x1w1s5N_s9zd-gz7hH60vDEFYUTY87iWKOyf5bMfN0ufJBJ3_vDzMg_i-4_GEy9LfyRBijgmndMR8dKSOr7lh2LfotpY-55XwSeq9pWQl52ITYVwb-Ex2rxmOEUI3nuiYHHvB2o0wa3pKnfPm0zzkCWqvQKbd1NcffqM5iB41YK6kZUsunWjW-q7sW8sCsz0baW1sDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده نسل جدید J-36 چین به پروازهای آزمایشی خود در طول روز ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71990" target="_blank">📅 16:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71989">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=m3o_9rCeEqFofg0I3Vy1v7D5ifdmAD0iBhzQWQoIFUfYe_NJHzD6f4D3zToM8qc-WvXbWAoq78VvlLHhY9Chm_HtXFKO9ToGHJ30fzAGT-LfqvAOmhD--Avq6Exbl9yABgNiSuDaGrQ2qWTyR-NjBZU2FHeTq6ZLYun6tDl9pyo_Ojb5NCpfVpUyNyFxYAigXY1Nf3QsXA4aKYRjkeagzFaTy3u8m2NeeWB1DShiS6wvN1AURhQtYbHKmW-0WygNcmtD7iImUdh6XRf2irdZ6UmeHFyxcpjfWTHli1EOL8tXHuXgNyBN9N_I-O2Bjuc3YVJOVzYdQcJKuZBo62nQLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34a5f81c8.mp4?token=m3o_9rCeEqFofg0I3Vy1v7D5ifdmAD0iBhzQWQoIFUfYe_NJHzD6f4D3zToM8qc-WvXbWAoq78VvlLHhY9Chm_HtXFKO9ToGHJ30fzAGT-LfqvAOmhD--Avq6Exbl9yABgNiSuDaGrQ2qWTyR-NjBZU2FHeTq6ZLYun6tDl9pyo_Ojb5NCpfVpUyNyFxYAigXY1Nf3QsXA4aKYRjkeagzFaTy3u8m2NeeWB1DShiS6wvN1AURhQtYbHKmW-0WygNcmtD7iImUdh6XRf2irdZ6UmeHFyxcpjfWTHli1EOL8tXHuXgNyBN9N_I-O2Bjuc3YVJOVzYdQcJKuZBo62nQLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرکی به نام صدا و سیمای جبلی!
با تراکتور اومده وسط برنامه؛ میگه میخوام باهاش اسرائیل رو شخم بزنم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71989" target="_blank">📅 16:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71988">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL6RjJp5Jz7lEOqz_kEwHYwKMEfYJJIVzukqLw6tXcNsU-qD2aDUvJBF1eAYtLLcmHwr8VXBqgq-xJ_kYhGH5-ZpaG2VYmJIb_VBrGcFkQybUHkqtfjUL9UyC1w6oq16ku6u4_4ndLLede818JBoGzpMPJTI43VpyW7TYp0JifpiAlPySy8-lqajP1dEx_OcbSa92vXBEGKMtB7-wkCMBVihq9LKzvri4KLLUNZjnbDMBN4wuewGwbulKlvD7cBm6SfEe73Qw84QH_wu7R670hLhAnlRhTUPQmbzmMTOtqkqFQnkELyakJToikEVaixySA7UHZUlvy96OKeAFievgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:انتقال سهمیۀ بنزین به کارت بانکی از مهر در ۵ استان اجرا می‌شود؛
سخنگوی کمیسیون انرژی مجلس:
این طرح تاکنون ۲ مرتبه در چند جایگاه به اجرا درآمده و قرار است از ابتدای مهرماه، در پنج استان کشور به‌صورت آزمایشی آغاز شود.
طرح انتقال سهمیۀ بنزین به کارت بانکی به‌تدریج تا پایان سال در سراسر کشور اجرایی خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71988" target="_blank">📅 15:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71987">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=kk4BDdEB5sXjbZSFt0_9OcBE5o0nXyojvK4qKwNvjYEgpDQPe3gZXI9kCp8j2AKVbQsERzolhlgAg02Tk_k_6RBuo9oLqs6FxKDCXU1Re5hzvo1HtyNHJZ9AXHowdBCVAY3w_EWmGWz4i7E0kuJO8ASP72-pDci1rDPB31me30ipsOrfh6NQdayr1z9Dp9MxuhF4dPCfPeUT524dioiTuTOI3K9YkLxVx1Bk3lkIrnXuG30-q-PJph1Xq3o-tQdP0vYic-PbgzP5T3WyZqJrlhNoILBV5AoQqQ9m6OCb0z8aRtQnFk-RO7uYqxylPyMZabn95fgae9K9L-mYmdspaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86993a4fad.mp4?token=kk4BDdEB5sXjbZSFt0_9OcBE5o0nXyojvK4qKwNvjYEgpDQPe3gZXI9kCp8j2AKVbQsERzolhlgAg02Tk_k_6RBuo9oLqs6FxKDCXU1Re5hzvo1HtyNHJZ9AXHowdBCVAY3w_EWmGWz4i7E0kuJO8ASP72-pDci1rDPB31me30ipsOrfh6NQdayr1z9Dp9MxuhF4dPCfPeUT524dioiTuTOI3K9YkLxVx1Bk3lkIrnXuG30-q-PJph1Xq3o-tQdP0vYic-PbgzP5T3WyZqJrlhNoILBV5AoQqQ9m6OCb0z8aRtQnFk-RO7uYqxylPyMZabn95fgae9K9L-mYmdspaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خلبان در جریان یک پرواز چهار ساعته بر فراز ایالت های اوکلاهما و آرکانزاس آمریکا، مسیر هواپیمای خود را به شکل چهره مونالیزا ترسیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71987" target="_blank">📅 15:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71986">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1qjpIeZHuRQHMfiU_iCrUf3S_bvW6u5QZ-LqORKRTT4dmxsKmfqoXIsQpRIWTlYvBd9BPI2POi_Vb2dgzgRWbhnwaNNlgi1cNtYJuTpzjZho8z5O-kpfjVBab5KGCHRP9Y4Htao4NttYp9vYAX93lG5LRVPcxvPKbmYyA_KO31qiKTx1QrDg-u1ARyj2Xd6-piIWxr4d_fsQHX6muVspiyp0JgmHbOl8NRJV33-Zb4wJPIoLEiCOvrAxHc-xCngtnl0wEEatcobJp-NvxM-RI72gaRW32WFHnTzEHbkez6ixniX9TkGiHTGBQKFNwP_DvRqNmwW1mvQEIX-RNfZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولیتیکو، سی‌ان‌ان، ام‌اس ناو و پولیتیکو پس از لغو دسترسی مطبوعاتی‌شان توسط کاخ سفید، از دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدام نقض متمم اول قانون اساسی است.
این رسانه‌ها می‌گویند که به دلیل گزارش‌هایشان هدف قرار گرفته‌اند، در حالی که رئیس جمهور ترامپ از این ممنوعیت دفاع کرد و گفت که ملزم به پذیرش رسانه‌هایی که «داستان‌های منفی» منتشر می‌کنند، در کاخ سفید نیست.
انتظار می‌رود درخواست اضطراری از یک قاضی فدرال در واشنگتن دی سی ارائه شود که احتمالاً منجر به جلسات استماع و استدلال‌هایی از سوی دولت در این هفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71986" target="_blank">📅 14:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71985">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aBgeV41fmTJtSwPq8c34kuk_H4g-3Uk8YzuOskPgOZJeF3VYp1E4z2AjzqUfRp3W2pQL0ifpTYHbFCzMeCj1QGL_yKLuFILDzpeAAp3AWJlEhFeWIrT8nD0_7nD5vgx9tgb52e617-FaZnQFCDctw8mksH3R4OgD7pApuq6ngYQKmq0rJCg0yzC4Do-VMYto4BzbCEtoWls33UuOh7I-vhFH-9-H87oCTMdSzJfm4rOsjmLKldWYqboP5lL2BIMV-swPDWXKWqLqu4wkn63wlkxCcWbPgpw33jJK6GteBcxuTI249qa4zpykD65h6zBWuRniQGvnysRFdGvL3sFGxSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aBgeV41fmTJtSwPq8c34kuk_H4g-3Uk8YzuOskPgOZJeF3VYp1E4z2AjzqUfRp3W2pQL0ifpTYHbFCzMeCj1QGL_yKLuFILDzpeAAp3AWJlEhFeWIrT8nD0_7nD5vgx9tgb52e617-FaZnQFCDctw8mksH3R4OgD7pApuq6ngYQKmq0rJCg0yzC4Do-VMYto4BzbCEtoWls33UuOh7I-vhFH-9-H87oCTMdSzJfm4rOsjmLKldWYqboP5lL2BIMV-swPDWXKWqLqu4wkn63wlkxCcWbPgpw33jJK6GteBcxuTI249qa4zpykD65h6zBWuRniQGvnysRFdGvL3sFGxSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر قطر:
از زمان جام جهانی، دیگر روی آرامش را ندیده‌ام.
پس از آن، ماجرای هفتم اکتبر پیش آمد و از آن زمان تاکنون، هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد.
از همه خواهش می‌کنم؛ ما برای سال ۲۰۲۷ به سالی سرشار از صلح و آرامش نیاز داریم.
لطفاً، ما به کمی استراحت نیاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71985" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71984">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjMtRVkbwCyJvUnqwKYXer355s6OW6ADsN6ceqaKMbqf57pNBp01URrtIWZzWPJAHgZEYdo7zpfocDsZKE-pNvBBqEmjgn5wNn6XJ0VU65g7u1Y2WB3GxTwwt_xMO-4-tcnM3KOZQ2dlyrB-Fv0MSPL-TuEvh12SJugxaiF1w1XcwS4v4vCeBcFKxOjLdAGO9GIC0SissxyvU8RO-2NuvIXcpXiYlmNIIwt45DDL4rBnz96Om6ipO1iCvF_uNiAi5w1zIfV28HiLb5LebKZbx0ySGYe2zMgxrsW47LkW9z1w0mtF-xYrbP8GnRGgAMFxnYMW2ak8fLsy51bXr4UEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
در هشدار شماره ۲۶-۱۴۰ که ساعت ۰۷:۳۰ به وقت هماهنگ جهانی (UTC) صادر شد، گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است. دو تن از خدمه دچار جراحات سطحی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71984" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71983">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=hgc-Q5vWxsmNDJrast-QwuQQqDAuXSPAZbnfoFxOz6PoGR7ycdBM51fEo8qBawq98FZ2N1O_k5aUSdoSfCfCiFAgjuYWI79a2IXB6Ym7ZC0J-cDIbZ9-5u9lvpvBGSZsezQ9yvU74mQ5ILn3uNIPBb003LHslP0-KuCcmqYyLFxzrnyY10pJT1LABFiAROAdFOvZXWNj0xB8p8dX8lnF4QvRRUnNytTLeqstkHmMHzybeFAxqv0K8iKKO_qw3vVz9ZddMar083Tf34xyU36ioKJL4u9c5Ub3zux5GFwlb72gpjlKw72r22iSi7ffiVpuCivN1PD1Z4YGm7VGD_B64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=hgc-Q5vWxsmNDJrast-QwuQQqDAuXSPAZbnfoFxOz6PoGR7ycdBM51fEo8qBawq98FZ2N1O_k5aUSdoSfCfCiFAgjuYWI79a2IXB6Ym7ZC0J-cDIbZ9-5u9lvpvBGSZsezQ9yvU74mQ5ILn3uNIPBb003LHslP0-KuCcmqYyLFxzrnyY10pJT1LABFiAROAdFOvZXWNj0xB8p8dX8lnF4QvRRUnNytTLeqstkHmMHzybeFAxqv0K8iKKO_qw3vVz9ZddMar083Tf34xyU36ioKJL4u9c5Ub3zux5GFwlb72gpjlKw72r22iSi7ffiVpuCivN1PD1Z4YGm7VGD_B64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران دردسرساز است؟
نخست‌وزیر قطر: کاملاً آشکار است که آن‌ها صلح‌جو نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71983" target="_blank">📅 12:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71982">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=nbPGBnnrIaTXxB9Gge3hOfdioST9E752ARsocLuwstxPQCAjhZUM8VUS3_K2bjWyYbmRCCXiA6iAMy5iYSsm00Q5nUIeuZL8zRURrVLYHTmk6aql2NQgqD8myO-7sZ4uHH-sLGf5d7gqPCqi_u1xuyBRDotkBG56PxlVagt4KvZbFwf2i8B3HSTO316pO727Z-N6Zy7Gza_5qGb0_FyAlnKjAwBkZyqhmPognblvTM_NGb4JkWQGQuudiZ271dknIyyhh0AjwtAvL-a1zQz_Ryx6z5y1S66kc0LCz1jERs_a2i-kwVkWkkILvxjfcVIH8Da0sAvfaVCxSFYiy9fODA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=nbPGBnnrIaTXxB9Gge3hOfdioST9E752ARsocLuwstxPQCAjhZUM8VUS3_K2bjWyYbmRCCXiA6iAMy5iYSsm00Q5nUIeuZL8zRURrVLYHTmk6aql2NQgqD8myO-7sZ4uHH-sLGf5d7gqPCqi_u1xuyBRDotkBG56PxlVagt4KvZbFwf2i8B3HSTO316pO727Z-N6Zy7Gza_5qGb0_FyAlnKjAwBkZyqhmPognblvTM_NGb4JkWQGQuudiZ271dknIyyhh0AjwtAvL-a1zQz_Ryx6z5y1S66kc0LCz1jERs_a2i-kwVkWkkILvxjfcVIH8Da0sAvfaVCxSFYiy9fODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان هم به این شکل زنگ آغاز سال تحصیلی جدید رو به صدا درآورد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71982" target="_blank">📅 12:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71981">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71981" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHjbr35HjLGtts13DwYyL4uopEJ1MDUBngPvoFEtWb2o7Bw5rdbdwgIeJ1kqvVYLArZm-W-dXOdnRBqDJBwxmlMmxVxbxki0XTbU-0q_PTBTUtUsE73BhApT_AjRqOK_E07oaAYuaS3XLjAgXeO05pzkh4RNUo6WFfalkFWbwDtaljNrcS6tj2mrlbgMW3o8I_L78unqHui_96n5m6JUQrRJPTg_t69i7sbkP1MhDcF94bcKBzbsHrPJXtx6ZZTOuprMO21fhQ-OgfHAchxFkEcjhxuOC9OQKPayxl4AYcxXxHbbz7H8sJ43HdT2PgccUbCgQ4hvBweExUBm7gUIBg.jpg" alt="photo" loading="lazy"/></div>
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71980" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71979">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=nCzq5StZ74Em5UVo38GYN6-D1YS11RIUDg4yaiVyuFJBf9BRlNdUWYU9pU9BSAA7KHNjbDQkhO5HCoziMsqKGRK4kY8FzywRt9aEkeJavQGjvoskOGymecHJBE7-g5bB4JjhdVgq9mqulp1uEJktGvyv_zIbr0tBcj9VLwXlLDTgDyvPwNL_jDDg31utdFdpgraKAMvI2vady2jtybj5ZpOREMX9X-d3Ws1XrsEeEbqnp0KUKtIWMohF2807Z3fZsLnB52ym_j6E1BD02J-_tWj0v2PN1Wz9m-LZdFK1xV8btmyPX2R6Kr--p81p5VgfTDo5q03cGjZllxPieKOS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=nCzq5StZ74Em5UVo38GYN6-D1YS11RIUDg4yaiVyuFJBf9BRlNdUWYU9pU9BSAA7KHNjbDQkhO5HCoziMsqKGRK4kY8FzywRt9aEkeJavQGjvoskOGymecHJBE7-g5bB4JjhdVgq9mqulp1uEJktGvyv_zIbr0tBcj9VLwXlLDTgDyvPwNL_jDDg31utdFdpgraKAMvI2vady2jtybj5ZpOREMX9X-d3Ws1XrsEeEbqnp0KUKtIWMohF2807Z3fZsLnB52ym_j6E1BD02J-_tWj0v2PN1Wz9m-LZdFK1xV8btmyPX2R6Kr--p81p5VgfTDo5q03cGjZllxPieKOS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی، یه دختر نصف شب، این شکلی دختر خالشو سورپرایز کرد:
یه دسته گل بزرگ+ آیفون ۱۸ پرومکس+ کلی شکلات!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71979" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71978">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=gAz_hJcnYbd01AP-dC3RZDZXxDIpQCy_Miq2obHou0x49cQb6APW62YbUQBMUcLJiMDx5Phr1w5lF6wq-7GSDY-he5TFvW1PdUQ4YxJTKo41WgXLHmF6ELSEP_WQoOe448BK3fdThn5fEHgrKysqF8abda_tdmkfezB5Hn0axQtNS1ANeI5OvmerpEKGyGIOSsZLrWgypEy_rftvXYlHbj_OXbVESyDUgSo4VsimIp_ejrPGlT3RMBH8jIglHMf_YLzPcEmZMyj1BeK6kmbAowEN2JIhwdZ5w552CAakgzkiYyYDO9V29gsJoYFMcEXlEGxlSuj24Hu506AaGhSTcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=gAz_hJcnYbd01AP-dC3RZDZXxDIpQCy_Miq2obHou0x49cQb6APW62YbUQBMUcLJiMDx5Phr1w5lF6wq-7GSDY-he5TFvW1PdUQ4YxJTKo41WgXLHmF6ELSEP_WQoOe448BK3fdThn5fEHgrKysqF8abda_tdmkfezB5Hn0axQtNS1ANeI5OvmerpEKGyGIOSsZLrWgypEy_rftvXYlHbj_OXbVESyDUgSo4VsimIp_ejrPGlT3RMBH8jIglHMf_YLzPcEmZMyj1BeK6kmbAowEN2JIhwdZ5w552CAakgzkiYyYDO9V29gsJoYFMcEXlEGxlSuj24Hu506AaGhSTcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از دو دختر جانفدا به اسم پرنسس های جنگجو؛
میگه همه با دوست پسراشون میان رزمایش من با دوست دخترم
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71978" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">محبی، سخنگوی سپاه پاسداران:
در صورت وقوع حمله‌ای دیگر از سوی آمریکا، ایران واکنش نظامی خود را — از جمله «جغرافیای جنگ» و تسلیحات مورد استفاده — به‌طور قابل‌توجهی تغییر خواهد داد.
«ما تسلیحات جدیدی با قابلیت‌های تازه به میدان نبرد خواهیم آورد و جهانیان شگفت‌زده خواهند شد.»
محبی افزود که ایران همچنین «اهداف جدیدی» در اختیار دارد که تاکنون مورد حمله قرار نگرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71977" target="_blank">📅 10:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=KS4womPA5lYYhbOGFcNAgLdEVP5ipEhxjCIGiDy46iJtLn_gwSdSXJ6474E3teniCj08VWoY1iZHl35Ors6GdMKCVC7mVZ-d0mpFXsanDOJKdQK7YHYWTanS1Oc24saJF-yVZNNmwSwPCl0B8gQ1lKGaLvb2CkjwkgzUuVOQYKdjp3-HAkW8XcZ3Kubd_ld7jJJ2DU6XT6CTq_gJ4UC1l01VjGM3PXq9-nG6l0rOvotrpR1L2eHFlCmeYgGCmfamIOu0TWlxUyK36Lj04v6ycWPP5zJp3vAYFcvqsRCtmnU3MI0VOwsIT2bFmrEzHnhHGsU2fgE4EPiDuXgACCq7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=KS4womPA5lYYhbOGFcNAgLdEVP5ipEhxjCIGiDy46iJtLn_gwSdSXJ6474E3teniCj08VWoY1iZHl35Ors6GdMKCVC7mVZ-d0mpFXsanDOJKdQK7YHYWTanS1Oc24saJF-yVZNNmwSwPCl0B8gQ1lKGaLvb2CkjwkgzUuVOQYKdjp3-HAkW8XcZ3Kubd_ld7jJJ2DU6XT6CTq_gJ4UC1l01VjGM3PXq9-nG6l0rOvotrpR1L2eHFlCmeYgGCmfamIOu0TWlxUyK36Lj04v6ycWPP5zJp3vAYFcvqsRCtmnU3MI0VOwsIT2bFmrEzHnhHGsU2fgE4EPiDuXgACCq7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات پهپادی روسیه به زاپوریژیا به یک مرکز خرید و قدیمی‌ترین ساختمان دانشگاه ملی زاپوریژیا آسیب رساند.
در حملاتی جداگانه در منطقه اودسا، انبارهای مواد غذایی که گفته می‌شود متعلق به فروشگاه‌های زنجیره‌ای «سیلپو» (Silpo) هستند، هدف قرار گرفتند.
در استان کی‌یف، این حملات به ۳۴ نقطه در پنج منطقه، از جمله خانه‌ها، انبارها و زیرساخت‌ها، خسارت وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71975" target="_blank">📅 10:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=a2Zv0Y_FMZ1u5H1oFFgPnxfbodbAROS-proKIKuYzmQxutK3YglA5pFeUSgHFQ71A0PpYULr-3e8sRx1zyRnzcx_kubiU-68S0qk2Ds9qL51RLdIS6Y3HOatdjmp6omjDqA9ye55-I_3NW0kxFD6hc3A4vmsvHOj0OOCvvqqtbdsfnrVjKbGzkIEO-f4znhXQmnLyE0QtFQL_5c-zDl31wdhm7w0650XjPOWzW19Ad5z9iKmW9esJv5nuwvURC7zuiqcrzET8VPGoxZpZH9A5jeFUOFreeHJDl3d6p8anS4KsRMqSaPyULFj-NilkZQzySXkHq8QKUh8p92Ue6JK7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=a2Zv0Y_FMZ1u5H1oFFgPnxfbodbAROS-proKIKuYzmQxutK3YglA5pFeUSgHFQ71A0PpYULr-3e8sRx1zyRnzcx_kubiU-68S0qk2Ds9qL51RLdIS6Y3HOatdjmp6omjDqA9ye55-I_3NW0kxFD6hc3A4vmsvHOj0OOCvvqqtbdsfnrVjKbGzkIEO-f4znhXQmnLyE0QtFQL_5c-zDl31wdhm7w0650XjPOWzW19Ad5z9iKmW9esJv5nuwvURC7zuiqcrzET8VPGoxZpZH9A5jeFUOFreeHJDl3d6p8anS4KsRMqSaPyULFj-NilkZQzySXkHq8QKUh8p92Ue6JK7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مونا محبی، تراپیست :
«یه بیمار داشتم که سه تا پسر داشت؛ فقط پسر اول بچه شوهرش بود. پسر دوم بچه عموی شوهرش و پسر سوم هم بچه شوهرعمه شوهرش بود!
حالا بچه دوم یه مشکل خونی پیدا کرده و برای تشخیص باید
آزمایش ژنتیک
بده؛ آزمایشی که ممکنه مشخص کنه بچه، بچه شوهرش نیست و این راز بعد از سال‌ها لو بره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71974" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=RgPYIZN6Khp3GNW5o9FFEW8Wj-anFl0MkraymLdZSGb7Y_OOrJcxXVsEtZsa6MiC81E2zsbJP8pjlT_as2te25Kf2wFVlVA0WmbS09DDJ-P4_YLz-sJw7UyfFEP-50sF8eoogZu_fg1IEgUo7Wm1VlJdhBk-omsMqhPbkcyw1BvAyGvW8VvBqc2dp-yizq_pbKqhaNqQQ6907yD622nYK9DhqD2lKIwyDO2snqLQw5tjuKIyQ1xnGwSI_qbvtv65XI6uqRqv_ghzhEjv0Bkg7lUyMLdHpc39rvdPkMjQhDO0YiyystDivld7gvo1OoHVxuGNI5EH3YHx_-NjWiNBMwJhGkp56_mdA2UnR7V7ia_OtW98c9CWtluWhbR1ldkqQN-wIs3m_JERsB3X0P72eOnaIGpl8tnD6bdXLrhj5ICl3i2VEi-A9Crm8qp04-4LjTKT-iR0LjQfgqD4pZN50PEyop-bvDuwea31fNRSm_Ii1HUjwooSMmgXuAP-d0tKvTaiM7vgSF27x9Qji9FMsrZ7JdtQbxV6FSjVSl2TNEmp8zREq0vqdirNd4kfiFoDvdARvkPnYriAeOGPw_DY4j1jVpLpvgKnZX1KWnglSSK6PHlv_PbWRClQ9TncnVX1I5kAGDpJN5740SAXtozbJxVh7bI01FD3umca3B65ayA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=RgPYIZN6Khp3GNW5o9FFEW8Wj-anFl0MkraymLdZSGb7Y_OOrJcxXVsEtZsa6MiC81E2zsbJP8pjlT_as2te25Kf2wFVlVA0WmbS09DDJ-P4_YLz-sJw7UyfFEP-50sF8eoogZu_fg1IEgUo7Wm1VlJdhBk-omsMqhPbkcyw1BvAyGvW8VvBqc2dp-yizq_pbKqhaNqQQ6907yD622nYK9DhqD2lKIwyDO2snqLQw5tjuKIyQ1xnGwSI_qbvtv65XI6uqRqv_ghzhEjv0Bkg7lUyMLdHpc39rvdPkMjQhDO0YiyystDivld7gvo1OoHVxuGNI5EH3YHx_-NjWiNBMwJhGkp56_mdA2UnR7V7ia_OtW98c9CWtluWhbR1ldkqQN-wIs3m_JERsB3X0P72eOnaIGpl8tnD6bdXLrhj5ICl3i2VEi-A9Crm8qp04-4LjTKT-iR0LjQfgqD4pZN50PEyop-bvDuwea31fNRSm_Ii1HUjwooSMmgXuAP-d0tKvTaiM7vgSF27x9Qji9FMsrZ7JdtQbxV6FSjVSl2TNEmp8zREq0vqdirNd4kfiFoDvdARvkPnYriAeOGPw_DY4j1jVpLpvgKnZX1KWnglSSK6PHlv_PbWRClQ9TncnVX1I5kAGDpJN5740SAXtozbJxVh7bI01FD3umca3B65ayA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پاراگلایدر سوار لحظاتی را که در حین فرود به سرعتی بیش از ۱۲۵ کیلومتر در ساعت می‌رسید، ثبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71973" target="_blank">📅 09:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=PemPbT8KOOkWtwyLqbZqumDuYb8u5PwJ78YF6xfBlO2zb2KqvR_orQg7OPO4t4GKGpPcGdAdyBrWYinhbLg7Jo-6m3iXaJcEHCdJ7o8vPsD9kPRwJOk6Clrx72m86NoK3VIYIowGznbghut3MzTGYwyFufchQVXLktorv80LUXF_esFnR8RDctzRkrXF_zAaSfmExFMR9rFEcijp1pGSoZ3cDFC6GffhmMoSOqy9gxWkr0HIhaGZ5j43Nq8zyaP-b5-o9gNwUO2d4Wpmqe4d31kK50gBIgq8Je21cf0cm-MSUYnhSJalErdQeCz8CWUUCaIe9V8S1yoFXB9F-DyXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=PemPbT8KOOkWtwyLqbZqumDuYb8u5PwJ78YF6xfBlO2zb2KqvR_orQg7OPO4t4GKGpPcGdAdyBrWYinhbLg7Jo-6m3iXaJcEHCdJ7o8vPsD9kPRwJOk6Clrx72m86NoK3VIYIowGznbghut3MzTGYwyFufchQVXLktorv80LUXF_esFnR8RDctzRkrXF_zAaSfmExFMR9rFEcijp1pGSoZ3cDFC6GffhmMoSOqy9gxWkr0HIhaGZ5j43Nq8zyaP-b5-o9gNwUO2d4Wpmqe4d31kK50gBIgq8Je21cf0cm-MSUYnhSJalErdQeCz8CWUUCaIe9V8S1yoFXB9F-DyXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شجاعی، از روحانیون حامی جمهوری اسلامی:
امام‌زمان برای ظهور به لشکر نیاز دارد
۵۰ روستا در لبنان را که سال گذشته بازسازی کرده بودیم، از بین رفتند
دیشب طرح آبرسانی به مردم غزه را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71972" target="_blank">📅 09:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71969">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9mquHPQtPP5RT3MtCuKNhXaG2AK5T9AoVapISXCOknwwPjF0XFagTbNndZzZiLPudBJ1BPMh5UGMp4TOqmsUgM9N7a_6a_gBHs_puFxTI2DjD2mybHNnd3-qbgpviCVGWhy7UNr5gWgx-KdZpsfmk4Qa94tJxe0V5f1mczbHGs9cHdheoJDNjMafEab6cZDl-SJaiGbXq6oZmWk_ypZxoFNj2wPSHtIoV5LBmrNYQSqbfFw0QgYjBAYVFuMM4YYEh2ohCd4Js339TYc3uwtH1xw4YxqQMQEAwoAy6rBmLAlwXMVzacwgcAwZUfoolnDW9lmmgXBhWxAxsF00oWKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=P7wl5veYmzCLF5SvldGBkHoUSFxqJDzjREZosCQGOy7iGgVMkp0uGEn0U15aFrUaBGhgWbWXKeNEiv3yNBFUzluac6oz9nWL6Cs3DZm5L586J6ZT26aofJiebjPdaf3253M3kk79-_a9xU7VD93L7oAWw90YFS5IQHVl2Q9xW1M9kIyZ0M2Fb_U14hMnLurjVVKNY1607PxAakS5Mrr56QYk_GawQuUvcxGpOp7VlPGJXXca-XhDenLqM3n3CEErJPrAK_vZK9n9NeQO2RMhY_NqHEsAGQfBbI8gzU-khALL-FZMwxdZI788Z3JzSB7rqo_Y6vekMrRePww--gWCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=P7wl5veYmzCLF5SvldGBkHoUSFxqJDzjREZosCQGOy7iGgVMkp0uGEn0U15aFrUaBGhgWbWXKeNEiv3yNBFUzluac6oz9nWL6Cs3DZm5L586J6ZT26aofJiebjPdaf3253M3kk79-_a9xU7VD93L7oAWw90YFS5IQHVl2Q9xW1M9kIyZ0M2Fb_U14hMnLurjVVKNY1607PxAakS5Mrr56QYk_GawQuUvcxGpOp7VlPGJXXca-XhDenLqM3n3CEErJPrAK_vZK9n9NeQO2RMhY_NqHEsAGQfBbI8gzU-khALL-FZMwxdZI788Z3JzSB7rqo_Y6vekMrRePww--gWCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ساعت قبل شخصی این ویدیو رو با این توضیحات منتشر کرده؛صحت ویدیو تایید یا تکذیب نمیشه:
تهران ، اتوبان آزادگان
29 شهریور
از اجرام ناشناخته آسمانی فیلم گرفتم
واقعا نمیدونم چی هست ولی نزدیک ابرها بود نور های خاصی داشت و بدون هیچ صدایی در فضا معلق بود !!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71969" target="_blank">📅 06:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71968">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71968" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71967">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71967" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71966">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=XnwBu8zW67KwPOQi5PCRLZ7WH6B8lbk1fBZEf7Ai0reNt9rW2QXZvaXPIOhjFrgwxUqT1GRQyuwtx8eWSbqVGNqdc4gSjWXlAVB3WM8YQKqBVt-hRkUa7zpLmWbx_07X9ZmxQtkj33tqP4K6bpqKD4p9gvcmNTcYRPBMoAZQgQa1qXQI63QahBQTjZx7Rzy-e2L5E9sZIWiXjl7B5ZVCK4K5DUbNAQm8zDiomCNn3pGGA8YLK6RWJW327nNLnKm8v3gMBluiAni-lmrZTVcbkejPS4loHt_rCFPrJ_1klRAVWFHy17KrPhbslfOdPR84kp0EtUlSW6kKsR7AN5TqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=XnwBu8zW67KwPOQi5PCRLZ7WH6B8lbk1fBZEf7Ai0reNt9rW2QXZvaXPIOhjFrgwxUqT1GRQyuwtx8eWSbqVGNqdc4gSjWXlAVB3WM8YQKqBVt-hRkUa7zpLmWbx_07X9ZmxQtkj33tqP4K6bpqKD4p9gvcmNTcYRPBMoAZQgQa1qXQI63QahBQTjZx7Rzy-e2L5E9sZIWiXjl7B5ZVCK4K5DUbNAQm8zDiomCNn3pGGA8YLK6RWJW327nNLnKm8v3gMBluiAni-lmrZTVcbkejPS4loHt_rCFPrJ_1klRAVWFHy17KrPhbslfOdPR84kp0EtUlSW6kKsR7AN5TqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها:
آری، امروز ما حرمین شریفین را هدف قرار خواهیم داد؛ آن‌ها را هدف می‌گیریم تا از وجود آل سعود پاک‌شان کنیم.
ما این حرمین شریفین را هدف قرار می‌دهیم تا به چراغ راهی برای مسلمانان آزاده بدل شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71966" target="_blank">📅 00:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71965">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=JCiPUEn9mSgxDwss7CW-j-Vmfr7zE37zJrV1lJPOvvVFEZhyW2eUWf4vFWO5a1G6FoqIsZ1tNZyYCMRZKhvp0rxaPQX8zC9SoWePw_GneaJXvjEl2inR4_PcmKgyH87KoPw6pEL0ZphAap6uqdXm0faxQuE5p1RagM6VpRFltf61cq-W9vElXTk_XBXr0vtMQiPJml7HwyaSoFFQxoW6JdTgY0q9Y6r34kC66DTRdtgl1-gR-CcWv99LCAJhn_i8NrtNXZtNIXlVd-wcgoyblEdcB75CtVGqfnHoWA87k7b40zXufvZdzID_7ToER-lcSAz-tw9OaEo8lok9-_WVVRctzogUNOjsoBA_WygkF24O9kPYa15JVmqH9sdIbKpDq-2JDsmrt8auJ1mhlBfsou8lPgxtGf3rHkYyJ_IPNhHAZQOF4Xl_kRBEYeK9ctaaExLpxa6Qgim4Sd2UXQm1dHMufWZwh7aUv2aQvGaAd5u8E7tYeBqrmLymGqRKdHEQo1OOHQaopTA6pU6wPM3ibVeWu-v1zhD8QTKvDMR6z_2FHJfU6ZofPZEndv51d573sBBb0BWswPZzGSDZUl1kJck93ia9kNZA1h5Q9UqNqHPGftS3X5X_moCC30tjftr_hyQlqfRkX0WXSOgilg5AKlVZpLejckiNixUO7JOrtHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=JCiPUEn9mSgxDwss7CW-j-Vmfr7zE37zJrV1lJPOvvVFEZhyW2eUWf4vFWO5a1G6FoqIsZ1tNZyYCMRZKhvp0rxaPQX8zC9SoWePw_GneaJXvjEl2inR4_PcmKgyH87KoPw6pEL0ZphAap6uqdXm0faxQuE5p1RagM6VpRFltf61cq-W9vElXTk_XBXr0vtMQiPJml7HwyaSoFFQxoW6JdTgY0q9Y6r34kC66DTRdtgl1-gR-CcWv99LCAJhn_i8NrtNXZtNIXlVd-wcgoyblEdcB75CtVGqfnHoWA87k7b40zXufvZdzID_7ToER-lcSAz-tw9OaEo8lok9-_WVVRctzogUNOjsoBA_WygkF24O9kPYa15JVmqH9sdIbKpDq-2JDsmrt8auJ1mhlBfsou8lPgxtGf3rHkYyJ_IPNhHAZQOF4Xl_kRBEYeK9ctaaExLpxa6Qgim4Sd2UXQm1dHMufWZwh7aUv2aQvGaAd5u8E7tYeBqrmLymGqRKdHEQo1OOHQaopTA6pU6wPM3ibVeWu-v1zhD8QTKvDMR6z_2FHJfU6ZofPZEndv51d573sBBb0BWswPZzGSDZUl1kJck93ia9kNZA1h5Q9UqNqHPGftS3X5X_moCC30tjftr_hyQlqfRkX0WXSOgilg5AKlVZpLejckiNixUO7JOrtHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
من به تمام کشورهای عربی و همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند در روابط تجاری و مالی ما اخلال ایجاد کنند، ما دو اقدام انجام خواهیم داد.
نخست اینکه قطعاً به شرکت‌های آمریکایی — از جمله شرکت‌های حفاری آمریکایی که فعالیت گسترده‌ای در پیرامون ما دارند، و همچنین شرکت‌های تجاری و بنگاه‌های اقتصادی آمریکا — حمله خواهیم کرد.
ما آن‌ها را هدف قرار خواهیم داد و اعلام می‌کنیم: این حمله‌ای به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران است؛ یعنی مقابله‌به‌مثل در برابر حمله.
از سوی دیگر، به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما نیز اقدام متقابل انجام خواهیم داد. اگر کشوری همسایه در اعمال محاصره اقتصادی علیه ایران — برای مثال در امور مالی و فعالیت‌های مرتبط با ما — با آمریکایی‌ها همکاری کند، ما کشتی‌های آن کشور را در تنگه هرمز تنبیه خواهیم کرد.
ما بر تردد و عبور و مرور آن‌ها و برخی فعالیت‌هایشان محدودیت‌هایی اعمال خواهیم کرد، یا در زمینه همکاری‌های اقتصادی، اقدام متقابل انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71965" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71964">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=g5sU1_mrY914FWJCRSJA7MI-WlOftddHF2hgMRrRQi8VYLnWT_rNTUCZJ-dAXA806NnWJE4wGTeJEATBhuYKAiRjiyukLHRsW7QbptE6RpIHN2g_FIs2KrBaLzwEWwglzNY_4cEtcW3q3vsbOR9EUGlhSwpGklLExlla-bHX_M7DSJq7uoqxJ7ePAlUDqKsgzAGKAxDdTadYIF_-XY60wZGKkXx2U1YxjNn47of1PG95UC_GRuIf9qnCOmD2YVrpojwvrTbRwjKlP2ca4-Mw7_jMQQmE-B_zxMbhUm1UTuSAIoLRHX8yGCn7trxuUZXTRTPrc2sBnYMP7vZrUZwQdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=g5sU1_mrY914FWJCRSJA7MI-WlOftddHF2hgMRrRQi8VYLnWT_rNTUCZJ-dAXA806NnWJE4wGTeJEATBhuYKAiRjiyukLHRsW7QbptE6RpIHN2g_FIs2KrBaLzwEWwglzNY_4cEtcW3q3vsbOR9EUGlhSwpGklLExlla-bHX_M7DSJq7uoqxJ7ePAlUDqKsgzAGKAxDdTadYIF_-XY60wZGKkXx2U1YxjNn47of1PG95UC_GRuIf9qnCOmD2YVrpojwvrTbRwjKlP2ca4-Mw7_jMQQmE-B_zxMbhUm1UTuSAIoLRHX8yGCn7trxuUZXTRTPrc2sBnYMP7vZrUZwQdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران دختره بعد از اینکه پروفایل اکسشو‌ چک میکنه و میبینه اکسش رفته با یکی دیگه درجا سکته میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71964" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71963">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Uya-qGmZzuMJOhTxxRa5Bf2Xwi-mzM100HBzyb4pWM7lDTpNqtPvZmXqmdN2bSWzskhVahZcZT38rQB7YGUTs6r9FcSoovfNPnGMuNFx46y3X8G7pMkTTROrsXiCezXvtmzhjV9wvXowjcMDqc_A0pA3VmsvXxrOwTDksaALNC9G6h-O3fFe0xb6y7HtFRGegJ9vIWDpPyT3twTsh8ktf-s5jitwSd4ADM6tCmt5duTyTUnQYBzO9Vdsb28sCXV54W0f0oghegTmpkYSrVIuojdaTuyUb0iPshiLbgZyyi1OKfuJYVR6VBXaP0L84kLHNbkLVfNhsIGDcOC1a_yusw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Uya-qGmZzuMJOhTxxRa5Bf2Xwi-mzM100HBzyb4pWM7lDTpNqtPvZmXqmdN2bSWzskhVahZcZT38rQB7YGUTs6r9FcSoovfNPnGMuNFx46y3X8G7pMkTTROrsXiCezXvtmzhjV9wvXowjcMDqc_A0pA3VmsvXxrOwTDksaALNC9G6h-O3fFe0xb6y7HtFRGegJ9vIWDpPyT3twTsh8ktf-s5jitwSd4ADM6tCmt5duTyTUnQYBzO9Vdsb28sCXV54W0f0oghegTmpkYSrVIuojdaTuyUb0iPshiLbgZyyi1OKfuJYVR6VBXaP0L84kLHNbkLVfNhsIGDcOC1a_yusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی چند ماه پیش:
کیرم تو جمهوری اسلامی! کیرم تو قبر خامنه‌ای، ایشالا تو جهنم میسوزه!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71963" target="_blank">📅 22:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71962">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=uf2aUs530UE4OMf7mCyNsW2Hkc1M38wYxXRWANS981wjYKU9uS0d_nBH7v9OoK6R9b9EA3uMHkgwqBqruGV7As0DrlEh1jJhYNclfYkW-TgSYmb9wvC8qzUWhTTWMxZFMh1nZa5MaRUFHyW2pjf-WpshAVNGZ-3353ZCrQtbrfAFL4DdJJAzyaNtyqt51RGAl51DZHFFtrvJrhwOwhihS5MRgAeevKkus0dDd09ndOa8uWCtrSp7aIGA6hQfxzIrcWd7YqcRpg5rg9r354O1G8BUqCp3S_kZrqFN_f22EQFqyoB4gZ9dx9iY7USAKOgcceW22n4zvqh1apfMpoMahA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=uf2aUs530UE4OMf7mCyNsW2Hkc1M38wYxXRWANS981wjYKU9uS0d_nBH7v9OoK6R9b9EA3uMHkgwqBqruGV7As0DrlEh1jJhYNclfYkW-TgSYmb9wvC8qzUWhTTWMxZFMh1nZa5MaRUFHyW2pjf-WpshAVNGZ-3353ZCrQtbrfAFL4DdJJAzyaNtyqt51RGAl51DZHFFtrvJrhwOwhihS5MRgAeevKkus0dDd09ndOa8uWCtrSp7aIGA6hQfxzIrcWd7YqcRpg5rg9r354O1G8BUqCp3S_kZrqFN_f22EQFqyoB4gZ9dx9iY7USAKOgcceW22n4zvqh1apfMpoMahA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانومی تو تهران میره به پسرا پیشنهاد میده که با حساب خودش برن کافه، اما هیچ پسری قبول نمیکنه و دست رد به سینه این بانو میزنه.
آخر سر هم کلش خراب میشه میگه پسرا پرنسس شدن و تنها میره کافه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71962" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4YjfjrAKIg_1SfbCEKBjIgLa6z6StbSfkLlWVhV3It0R47-MTvhb-E2n4RKclheZUt8pYrQTZ8wstBem4HFluuPAVxtV64TUy-9GwIoDFqzC2NsJUpv8YiD-dPv6pIAMpQaOwUPAeMZJhGbJzFI5owy6P6AuHg144e2oOU4awmSkztKhIXBPmjWu9yIX_bMW0LBHCKjU_g-BC8abMb9q7bQ9GYl-91BbklSHc3zln8kVO1cl0K8jSow4QWqEeE4cjrE7SqoVZT04Fai6X58Blvf7rfLsXr9TnLqkr72svnWpCuqB7Cc0Gms5Wj2YYIMxyfhpkPyHwuYJjaOubeFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=rSnab8zxYutSC-lSOXiaoLBcG9OkiJsWRw8tozQqWGXL8Wtq-b9VjPubLe0sPG5Kg5VNAjNl4qiB6XDKmscBrQcH0h8AA_-X42fqRyi1XCIjtXwlGYrmzMqRC-MdikEOCfDKOUQI4AwWO5Nauia4DljcxK6x4xqJ9-_Kt7tkl7CH1brBqEtL2kLMqQlfIGi8y2RdGbkchHtHa8YBzZb8WN4cxQlmmTNE02TpWCL1vvYRAOXYAMbApSRH9mz2B8BA7-RyoaGHlVzXhb51Hyr9WQYMxP3Cb3qTbIX6ZPtKWEdA0l2M8kjui3dT2F4Jxi3HqBTFdcrmrciCBZfTirwIUrolOfyWyV-uiBU62A2nVei3jwvw-5eFMJo_rThNhyQ14g4kjyLGPK-NsJWXH4TvC53kbh33Qp1FkbANg9RgBDc7OQyPyIP03W7-3uQJog538TXVUIGaEui7wA6lnWZJddCjvslVQSfJH_MEO5CtAJkGoz1RByQ8BTOT7FvpZb4dcZdtVNzfYcCCB9W9a1c7Qs_azfxtQSyfCQPTH-z2NGWSm9WshdCUb93IO1RhlP0GrDXhojbeYqpMfGGg2ytRsh4Xic-B06y5-WRB6JOAcNdbABBbsX2Cx8XnsGucD34Bdeu9jpxEZY2u4WNozz-eehknSmdaD0tdSZN560sz2A4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=rSnab8zxYutSC-lSOXiaoLBcG9OkiJsWRw8tozQqWGXL8Wtq-b9VjPubLe0sPG5Kg5VNAjNl4qiB6XDKmscBrQcH0h8AA_-X42fqRyi1XCIjtXwlGYrmzMqRC-MdikEOCfDKOUQI4AwWO5Nauia4DljcxK6x4xqJ9-_Kt7tkl7CH1brBqEtL2kLMqQlfIGi8y2RdGbkchHtHa8YBzZb8WN4cxQlmmTNE02TpWCL1vvYRAOXYAMbApSRH9mz2B8BA7-RyoaGHlVzXhb51Hyr9WQYMxP3Cb3qTbIX6ZPtKWEdA0l2M8kjui3dT2F4Jxi3HqBTFdcrmrciCBZfTirwIUrolOfyWyV-uiBU62A2nVei3jwvw-5eFMJo_rThNhyQ14g4kjyLGPK-NsJWXH4TvC53kbh33Qp1FkbANg9RgBDc7OQyPyIP03W7-3uQJog538TXVUIGaEui7wA6lnWZJddCjvslVQSfJH_MEO5CtAJkGoz1RByQ8BTOT7FvpZb4dcZdtVNzfYcCCB9W9a1c7Qs_azfxtQSyfCQPTH-z2NGWSm9WshdCUb93IO1RhlP0GrDXhojbeYqpMfGGg2ytRsh4Xic-B06y5-WRB6JOAcNdbABBbsX2Cx8XnsGucD34Bdeu9jpxEZY2u4WNozz-eehknSmdaD0tdSZN560sz2A4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=NwjVjE8krGPdXHcVQGK2fJTmeaTbmO2exBK402u1ad45oTiW49Nk_QcNEZua-Nlu6n-Qt1et25DWMsD-iJJB6UofTK2-BYIYxZYXGhs_tHdyP7s6a2EMFkOUwnyjAOOBUYDd_7gMDjI-p7xMNqDSqlD61rWkTyQP4eEUFxByz7ONrgc62j6cLLS4OPM-9HJDKYNPbg6qRH6p1dJ_V0TLgFZqdY_dkMMhEmtcrWSTbSzPXHMw-j-mg8Prcurqq-1vmlybFfXsMK2G-IvJH33s5gRHT8atNAkjEGqBevoqJunLGOhqO-CHaJC_Z8b6hbt77OZDs8aik7Tttj0bbgoDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=NwjVjE8krGPdXHcVQGK2fJTmeaTbmO2exBK402u1ad45oTiW49Nk_QcNEZua-Nlu6n-Qt1et25DWMsD-iJJB6UofTK2-BYIYxZYXGhs_tHdyP7s6a2EMFkOUwnyjAOOBUYDd_7gMDjI-p7xMNqDSqlD61rWkTyQP4eEUFxByz7ONrgc62j6cLLS4OPM-9HJDKYNPbg6qRH6p1dJ_V0TLgFZqdY_dkMMhEmtcrWSTbSzPXHMw-j-mg8Prcurqq-1vmlybFfXsMK2G-IvJH33s5gRHT8atNAkjEGqBevoqJunLGOhqO-CHaJC_Z8b6hbt77OZDs8aik7Tttj0bbgoDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4MmAJ_Zft676Xauo_cnooSEkkTg2G6xQmseBi33ZESCsjKgX0sNWliJqIBZbUs5uiDiymEWYQ-81R6vMI7rcdj7MyeEjTDE5d6c1p85khrz0tUr7O0z5T03IjpSdtpB9lqp0gCOUcdHHFL80LsFEgPAzW7pxja9PuO0cbmtAyoafrBgAgEuHWK_br9hQVSPF2CsNmWFrvhuK_IEbRQDPL4zxnNTpDMg0MX8S1PXkt7_H84P7Vvovok_ZOOOjtYHAvwLkwlqOpTI-J7BxGfhtiSlxS9XHl_-VVTpVlH6TIL6SIGILZ_PVLZJ5n8gO1uzjtKtBW_ODIFrWTuGmqXgBg9DI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4MmAJ_Zft676Xauo_cnooSEkkTg2G6xQmseBi33ZESCsjKgX0sNWliJqIBZbUs5uiDiymEWYQ-81R6vMI7rcdj7MyeEjTDE5d6c1p85khrz0tUr7O0z5T03IjpSdtpB9lqp0gCOUcdHHFL80LsFEgPAzW7pxja9PuO0cbmtAyoafrBgAgEuHWK_br9hQVSPF2CsNmWFrvhuK_IEbRQDPL4zxnNTpDMg0MX8S1PXkt7_H84P7Vvovok_ZOOOjtYHAvwLkwlqOpTI-J7BxGfhtiSlxS9XHl_-VVTpVlH6TIL6SIGILZ_PVLZJ5n8gO1uzjtKtBW_ODIFrWTuGmqXgBg9DI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=kf8l12C4lcA-g6C7RA3hJa2i47KChee3aTad3eRcmO8vlb-63lXOqkDbG0ylVDt0NiwlkVJHQrxWw4ayo0H2oK4YlzmNp1bODhhVftRHIXjPK9hdBRYfZqEfdkZoZBZVkhCo6oqCtE0nl7_wwunddfd-q4lF5qu5ASzT7ObSIbFAkiUVTCnZmt-v-PDDUjALf03EZImq8Tc4UiGK6znXTGH9AoJaborDx946z_fd2OeI6NxoLYurJZBZ1SNDSat0vmjrE4fX1oQMUbHB0FoS7pVAT7MGIoFcYa17VS0VzZ9ca_TNC85E6RTUWbqZ8maLacEW2-hBPaAXMcmYX4ej6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=kf8l12C4lcA-g6C7RA3hJa2i47KChee3aTad3eRcmO8vlb-63lXOqkDbG0ylVDt0NiwlkVJHQrxWw4ayo0H2oK4YlzmNp1bODhhVftRHIXjPK9hdBRYfZqEfdkZoZBZVkhCo6oqCtE0nl7_wwunddfd-q4lF5qu5ASzT7ObSIbFAkiUVTCnZmt-v-PDDUjALf03EZImq8Tc4UiGK6znXTGH9AoJaborDx946z_fd2OeI6NxoLYurJZBZ1SNDSat0vmjrE4fX1oQMUbHB0FoS7pVAT7MGIoFcYa17VS0VzZ9ca_TNC85E6RTUWbqZ8maLacEW2-hBPaAXMcmYX4ej6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71952" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyVBUf3bvJ64gvP4_IMcxr-zNfkhKzafjBLrm4Dt0tq1ddAOvqgtqX5CQxzBHVleWyRLcB7oJp2dFRte-kRD4LSNpmhz3wpnaCaI1zrO66WN5LVym6eV_Sh1YNjiH4SJIyqnmMNT8vnkL1rC5ryU5ARlVmKkDhzVuAGs2vsB5ioKOT8262BfLxA3V4-P9LGJ0Ka8jK9rq6QBrDCLKPBXHp1zpQimxfVR-eafa2O12D3gFhYu8cutTsWYNfven8LNHTP8NpeJ07HtVtludmlTFGIyjJuIR5t7GtCA2OcTbgbPmz9Vk7GYOxw90OeLpY8OiI4b-gPy3xNN8zS4CySixw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71951" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=eRRRXrz8T3cxSGMzN2B-5LZjXbNm4pLAqd3Rx7hsRtOySsYUyn0I3NkGyy_pz04I8TQl0vyynF53Adb7Xyn11F0Pr00eei6-86tZ4ToCbnMxpplzwBarMDabqRQ8FmyozSikPH1XVpRSkkrSxTHlWGPjf1EU869sfXoMrBM0WFjECoHgK85Q5mAtdHRpyGL26x-4a9d74tO2scdH-BsmrHz6Y8vhNNM8UFGoAnxFd3qW6CjFSpz7oijr5x2IO2-zPN5PcYC10Z625ONRkWfIXxmeebUuI-VzxDtdQPFa7VqlS9-l_iQutCpFPZ8qpv5lMG5l5DgWQ6zxtDGL2psvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=eRRRXrz8T3cxSGMzN2B-5LZjXbNm4pLAqd3Rx7hsRtOySsYUyn0I3NkGyy_pz04I8TQl0vyynF53Adb7Xyn11F0Pr00eei6-86tZ4ToCbnMxpplzwBarMDabqRQ8FmyozSikPH1XVpRSkkrSxTHlWGPjf1EU869sfXoMrBM0WFjECoHgK85Q5mAtdHRpyGL26x-4a9d74tO2scdH-BsmrHz6Y8vhNNM8UFGoAnxFd3qW6CjFSpz7oijr5x2IO2-zPN5PcYC10Z625ONRkWfIXxmeebUuI-VzxDtdQPFa7VqlS9-l_iQutCpFPZ8qpv5lMG5l5DgWQ6zxtDGL2psvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=rt0NTQkRu8gTndv0-zgspFebVaYZ7lVpR7pK17IogEdxUHcJk4j3yKvoxIJ49ohzBT0oijiw3DDEeK9eo_uDIwMoxdq-BuO0hByeVCmsuIUAN59GubDthCpP0WEsTbMd0IhfcDqSsFcGFbLlo_OWFO5bDJpzlGUd9mHJY5Jd8QYDHfhN5xt_IL7qCbajQi2NH0Uenp2F_PXxeJlcBe25vykcJRshXoGXGYx8qKoL7S99SClELalygmmaT_4eDl6-uTRLC01FAJHo_WfZQPg1xiVwae1WE9SCtGPGqSmFYCe9fEsQrsu-HeE64MZ7KEASdIrPu-Aff4mqDjGsbU1V2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=rt0NTQkRu8gTndv0-zgspFebVaYZ7lVpR7pK17IogEdxUHcJk4j3yKvoxIJ49ohzBT0oijiw3DDEeK9eo_uDIwMoxdq-BuO0hByeVCmsuIUAN59GubDthCpP0WEsTbMd0IhfcDqSsFcGFbLlo_OWFO5bDJpzlGUd9mHJY5Jd8QYDHfhN5xt_IL7qCbajQi2NH0Uenp2F_PXxeJlcBe25vykcJRshXoGXGYx8qKoL7S99SClELalygmmaT_4eDl6-uTRLC01FAJHo_WfZQPg1xiVwae1WE9SCtGPGqSmFYCe9fEsQrsu-HeE64MZ7KEASdIrPu-Aff4mqDjGsbU1V2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=eThcii3uRoxvHtz92i3MGKsY9ZwQIX5tXqlya7R7A4pcEpQwNEtTV-fjEx6yITPjNSeix3PD7o-nnZy3Sqp5SA9tjCxvpa1gwwpgyuEHwGSP55SBkaxvnjdCAIaD5xduHytzdUpTcjlP8V3KeAUVAPEo393A6t82jfNVpb5UX45YeC8t6ENg05zTexdR_S8YdZ7SxAeRTsragOQ9-d36v9ho9BCQSFoL0X7HRJHTZUbiGsACCjOei0b61ZXD3fU4v0cXI_Z3RjNCjsA4X8LmFiow0V2q7IueDMXT3bUIA3jO9ZuoURfb1Txv2voOaWhJpyBCp265rPm6km5Ddk6BaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=eThcii3uRoxvHtz92i3MGKsY9ZwQIX5tXqlya7R7A4pcEpQwNEtTV-fjEx6yITPjNSeix3PD7o-nnZy3Sqp5SA9tjCxvpa1gwwpgyuEHwGSP55SBkaxvnjdCAIaD5xduHytzdUpTcjlP8V3KeAUVAPEo393A6t82jfNVpb5UX45YeC8t6ENg05zTexdR_S8YdZ7SxAeRTsragOQ9-d36v9ho9BCQSFoL0X7HRJHTZUbiGsACCjOei0b61ZXD3fU4v0cXI_Z3RjNCjsA4X8LmFiow0V2q7IueDMXT3bUIA3jO9ZuoURfb1Txv2voOaWhJpyBCp265rPm6km5Ddk6BaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=llRfONkPbdajJYZhxMA0avrKrzGlVQGHek5ucKCB-IERkJPwqVVCHg3uIbOA0qIwdBJQTNqXCwwd7UMBUZGgi49BcZQTvb-88qNQkJnn30tHPAch1s_YhfwX7kTvvZwWqryEe3Y_UsJJLC8Ap8-UU2Jz1RDyoYDcz0Un61rOq2tjT3VKeNjr6oCve-L0msqgxH6UxOjzzX8EEOL1YS5gKS3Lz7RHngqkSyTq2w4DTpvRajX3CVPvWHq96cVNwEnaeigEm76huYJy2PYr3BAcRsRBCJTZDqUjBjBPjrq_wUmRSDL8fJExHoIo8Ms0a_syK2YWqXq-aiUtVb6N1uR9IYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=llRfONkPbdajJYZhxMA0avrKrzGlVQGHek5ucKCB-IERkJPwqVVCHg3uIbOA0qIwdBJQTNqXCwwd7UMBUZGgi49BcZQTvb-88qNQkJnn30tHPAch1s_YhfwX7kTvvZwWqryEe3Y_UsJJLC8Ap8-UU2Jz1RDyoYDcz0Un61rOq2tjT3VKeNjr6oCve-L0msqgxH6UxOjzzX8EEOL1YS5gKS3Lz7RHngqkSyTq2w4DTpvRajX3CVPvWHq96cVNwEnaeigEm76huYJy2PYr3BAcRsRBCJTZDqUjBjBPjrq_wUmRSDL8fJExHoIo8Ms0a_syK2YWqXq-aiUtVb6N1uR9IYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=O06QQQBMzTSmSUUqNtmxBJhySlWxVWI2D8VEmBwCKXc3FO85I70WFBXaROz58ND-fmK75wXjeM0Bx5ekX02MXhIE_NfEK12AFzDXcrau_ZRa9yVQEEp8iqyEqR66ezoQD6vXJzOdA8aMijBs5jkvI-9O8-W1_7PKrhCVYX6oM38_-hD2brvr7m0XzQQQbBgGoObbyb20tWGdj1arZbNftPtn_pmCwMq7Ra-PXj8ZT5WHo7WeYcw-0zXdUzPfKHp0l4UtBxMiM4sOaqzpeKg8RrCD3jOZ63PHON9PTO1shsJwgM2cLDgfBUrXu0pgyt-CBMcFH5gS4sUoP2VEWaDoR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=O06QQQBMzTSmSUUqNtmxBJhySlWxVWI2D8VEmBwCKXc3FO85I70WFBXaROz58ND-fmK75wXjeM0Bx5ekX02MXhIE_NfEK12AFzDXcrau_ZRa9yVQEEp8iqyEqR66ezoQD6vXJzOdA8aMijBs5jkvI-9O8-W1_7PKrhCVYX6oM38_-hD2brvr7m0XzQQQbBgGoObbyb20tWGdj1arZbNftPtn_pmCwMq7Ra-PXj8ZT5WHo7WeYcw-0zXdUzPfKHp0l4UtBxMiM4sOaqzpeKg8RrCD3jOZ63PHON9PTO1shsJwgM2cLDgfBUrXu0pgyt-CBMcFH5gS4sUoP2VEWaDoR4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=r71GMtvZ1m7qTF3NIXVFRHpoJLB10PLyiVq6OC4M_r0DheWNF6rlJe6IocoOZ-8S-o4VmwcDxcOBqOH1zeCI15TDyWwKkMCiNs4QZ2O7aygcH1R2qjwnDtgBCK1X2Pm81rHQJKVzRZj0tWazRQnW7f5nOQ5vkOMug4MKxwt0hgPauwazlVQ6svuYi_h4Bg8z3gllA4PC3KJxoZ80BrHZMZpVwWII2suT4I8Vu-TJsTiM6jsX9XrIZAIHgCCxoNA6bt5BuVsmPfGBdb1xdEzUkYJ598fnnfRhpQopH4v6RpDgNNJz9WsWBruu1tMUR2lrEYlmFlflBF7q53bNifRRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=r71GMtvZ1m7qTF3NIXVFRHpoJLB10PLyiVq6OC4M_r0DheWNF6rlJe6IocoOZ-8S-o4VmwcDxcOBqOH1zeCI15TDyWwKkMCiNs4QZ2O7aygcH1R2qjwnDtgBCK1X2Pm81rHQJKVzRZj0tWazRQnW7f5nOQ5vkOMug4MKxwt0hgPauwazlVQ6svuYi_h4Bg8z3gllA4PC3KJxoZ80BrHZMZpVwWII2suT4I8Vu-TJsTiM6jsX9XrIZAIHgCCxoNA6bt5BuVsmPfGBdb1xdEzUkYJ598fnnfRhpQopH4v6RpDgNNJz9WsWBruu1tMUR2lrEYlmFlflBF7q53bNifRRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=NxqCZa0N-FytwvTwc4VUX_SWAZ3rG7F5-U5VCSVeycU7ubHXrH62qDIbesVRxMxMdFZ_TtynarQ938WKwcTMtxzyFyTE8nf8Kk2xo157h2dcaZHq0DCgmbH5NQnGuraxOm4eQ4Sx9gKK1jkbSFuaZvfFAlBDhNkIj4XtBa6jDP0si0FZv1adylYUDsQuqZn2w0Jf-nnPeUqTJmeJ6SGrCEoYuNfHfp6UIBP-To-SJHPcO4t6v5ipXPknv04KgXO3SL-FJe6HLac-gIpaFCFxxLK0iLC55K4oofh9wwWetpiUay35bWDJLZJmz79aPgf8H2JXKmYIMt9WJlw_qt8ZbnKcax4NQfUhRhMLFfDB1k3WohheWHXLy07WIoVbrcaDehYQDcqOKW8xjgN3hlE_SB3tCWJ-qv3gKJEniZNgFvdXXsqfP1y1gNsehzmN3qaoqqGEFHRpeYFbtrcyYtVUdBfU3q6sPmq9gP5byxFA4t11XDLNXAU9S5U94lrjOTTxE84JBw6HkbMMAzJFoQ3PGRjVOLeh8-fdve3dcUq3nItcLZ-muoJPyb54P_9mr-7xZYO_LAIwNPvTurYIl4UnUZ8OIzDBd9YY81FFd4EyiBrlCX589gVSrzmfsuAIYPRmcMHz38iBMonI9cP-baq1SPbnxYyeZNTr1hg88p1WVDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=NxqCZa0N-FytwvTwc4VUX_SWAZ3rG7F5-U5VCSVeycU7ubHXrH62qDIbesVRxMxMdFZ_TtynarQ938WKwcTMtxzyFyTE8nf8Kk2xo157h2dcaZHq0DCgmbH5NQnGuraxOm4eQ4Sx9gKK1jkbSFuaZvfFAlBDhNkIj4XtBa6jDP0si0FZv1adylYUDsQuqZn2w0Jf-nnPeUqTJmeJ6SGrCEoYuNfHfp6UIBP-To-SJHPcO4t6v5ipXPknv04KgXO3SL-FJe6HLac-gIpaFCFxxLK0iLC55K4oofh9wwWetpiUay35bWDJLZJmz79aPgf8H2JXKmYIMt9WJlw_qt8ZbnKcax4NQfUhRhMLFfDB1k3WohheWHXLy07WIoVbrcaDehYQDcqOKW8xjgN3hlE_SB3tCWJ-qv3gKJEniZNgFvdXXsqfP1y1gNsehzmN3qaoqqGEFHRpeYFbtrcyYtVUdBfU3q6sPmq9gP5byxFA4t11XDLNXAU9S5U94lrjOTTxE84JBw6HkbMMAzJFoQ3PGRjVOLeh8-fdve3dcUq3nItcLZ-muoJPyb54P_9mr-7xZYO_LAIwNPvTurYIl4UnUZ8OIzDBd9YY81FFd4EyiBrlCX589gVSrzmfsuAIYPRmcMHz38iBMonI9cP-baq1SPbnxYyeZNTr1hg88p1WVDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=eKGOL3-Pua1EKynr6ZXtOoHQroaZz6ro0wbfzdrkZ-bDeISgLzJwDi2Lc0wKg9N-KjpKrkVROojoILN3ph3FE3ViPxk2RmPXsielxYK19QPoaoLjDstzCTBw4FjiB-j0xVCLd4N86UpBrp1eLfZmQ2nNoS7lUOgYyAvKlPRYl38tezAhyc-HeunVHZCvQ63OpwN1s1_QfcWmIEOOKuIqAnogvWb42cOZPoBh-ZcHJTlh2cwwIPonayTPyNEVHGxjI0SQ5-TDXB83k6qEzY8iHwtRuaGg-a4gUF4bNH3Ba9k72MrJZFDWIt6TtXq7IWN5_CTQUgf_8269GZgchHFkjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=eKGOL3-Pua1EKynr6ZXtOoHQroaZz6ro0wbfzdrkZ-bDeISgLzJwDi2Lc0wKg9N-KjpKrkVROojoILN3ph3FE3ViPxk2RmPXsielxYK19QPoaoLjDstzCTBw4FjiB-j0xVCLd4N86UpBrp1eLfZmQ2nNoS7lUOgYyAvKlPRYl38tezAhyc-HeunVHZCvQ63OpwN1s1_QfcWmIEOOKuIqAnogvWb42cOZPoBh-ZcHJTlh2cwwIPonayTPyNEVHGxjI0SQ5-TDXB83k6qEzY8iHwtRuaGg-a4gUF4bNH3Ba9k72MrJZFDWIt6TtXq7IWN5_CTQUgf_8269GZgchHFkjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=JlKtG4T0NQCh6zLIW0RvS97tTkF8QeJ-U1bHWEzHpEOiU4P2sl4VQa2RN4dO1kVfvVCHVQvT7g8YxFPJJAMB3ejaRkyWmSMsi83yGDlbk8qysKnIWJ9aBpiKmGWIEOzttQtHTfl9GbPLh_9a7TmSgi2W88ehqLKq-R1vdxX95e_NubiTPWLrRh-D3pO1oLz2Nwo8XbtxUilNp1w2-cTNWglYTS63yVCFEj67h-42Aa1bFqqP_AjWGxdIzyFyztJ2PiOxQOP3JXzm8raY9Cq9_41a2X64GahplKzZOGEd61eRt6381IYr43MlybmGb-qNfPBJU6LWu3tgPEhF0AZslw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=JlKtG4T0NQCh6zLIW0RvS97tTkF8QeJ-U1bHWEzHpEOiU4P2sl4VQa2RN4dO1kVfvVCHVQvT7g8YxFPJJAMB3ejaRkyWmSMsi83yGDlbk8qysKnIWJ9aBpiKmGWIEOzttQtHTfl9GbPLh_9a7TmSgi2W88ehqLKq-R1vdxX95e_NubiTPWLrRh-D3pO1oLz2Nwo8XbtxUilNp1w2-cTNWglYTS63yVCFEj67h-42Aa1bFqqP_AjWGxdIzyFyztJ2PiOxQOP3JXzm8raY9Cq9_41a2X64GahplKzZOGEd61eRt6381IYr43MlybmGb-qNfPBJU6LWu3tgPEhF0AZslw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=O4ODI00pt8hCmXNBLAks7XeoTn56X3tDLjPudQunT3nbW_RCCEnuQymGa7Jqh_xAZxgfXfULCATg13Gf3at1q6LJuiLBdq1UY728wkGSNYPr7c-KPk95JrFnLS5tFz8uj3bpnjpZ8_xsRl48DdGc-E3KVTrjh8hwj--1k1SUJO1uakUpRoUDerQwo4Hgp7H2xkp6w-9vYyTZwL0azA8u-WVhhVSyrXN4TZjCCIYJxhb38gduixwCxAMCWaub48yECWrAlnHCBHpdZyjRRxyOp5raxXlbfnGk7QCJZUNvFLX3nqphxTRB98KA16-FfPX7BG8Q-lIDWoNC9awUpakoIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=O4ODI00pt8hCmXNBLAks7XeoTn56X3tDLjPudQunT3nbW_RCCEnuQymGa7Jqh_xAZxgfXfULCATg13Gf3at1q6LJuiLBdq1UY728wkGSNYPr7c-KPk95JrFnLS5tFz8uj3bpnjpZ8_xsRl48DdGc-E3KVTrjh8hwj--1k1SUJO1uakUpRoUDerQwo4Hgp7H2xkp6w-9vYyTZwL0azA8u-WVhhVSyrXN4TZjCCIYJxhb38gduixwCxAMCWaub48yECWrAlnHCBHpdZyjRRxyOp5raxXlbfnGk7QCJZUNvFLX3nqphxTRB98KA16-FfPX7BG8Q-lIDWoNC9awUpakoIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=NEKEbPLPTCPHueRAW4QNW8LoRIHhg73xvNChHi_djKNjE9r3QzDyDnN_fqab2pNI2o0Rgv4oVbuwS_BK2UeQQcdKq8e6gw6xnft3DirsALGlWx3Nzfl-XWkblUlr_u2A4vyc4iC6DP2qoa-IANqGi24VHYca990HDGKbtI9YgdvMSls7ekKaA40LcMNy5n4KKOy7PKmfsNmjkMC3nycLdx6ISNDvpSDuYOcSw-oP0Nn0N1qxHAPbfusjWi6M2zanlpEKgiSYp2I18aQuY8LGQ98gUjCTzu2CAwt8x1au5-jDee0H5mEfHp8ofBlrkf_WeojFjBI6hzevtzvU3Z4-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=NEKEbPLPTCPHueRAW4QNW8LoRIHhg73xvNChHi_djKNjE9r3QzDyDnN_fqab2pNI2o0Rgv4oVbuwS_BK2UeQQcdKq8e6gw6xnft3DirsALGlWx3Nzfl-XWkblUlr_u2A4vyc4iC6DP2qoa-IANqGi24VHYca990HDGKbtI9YgdvMSls7ekKaA40LcMNy5n4KKOy7PKmfsNmjkMC3nycLdx6ISNDvpSDuYOcSw-oP0Nn0N1qxHAPbfusjWi6M2zanlpEKgiSYp2I18aQuY8LGQ98gUjCTzu2CAwt8x1au5-jDee0H5mEfHp8ofBlrkf_WeojFjBI6hzevtzvU3Z4-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=HzePbt0D0Q8v3USjwJB-g3MHk9niZ-cinSjckOpbPojCYozki6T2F9G9aderhSKyn9vSBkSaZyKIHKKovQlTujhvYPEYV044p_5WjSQMUAjlPNi5D-bZh3a3xnhbonHkp_9Vw5tO_fZEaVzo-cyvmOZOdKN8MtraFf9HJihjdbbFI_N4kwinmaq4UObQBL2HPYZXAPb5CZ35OPNlE-Igy6hs1WNgduUWeHmIey5g1k9pms-6MUs-s2qJjG7zXzjO2X1Hf8zTlfx9tICdVXBTqlqa_tOOpsWg5hGXulxwr0KybRYwG1kspB-kmpc7MleQaFw5ilK_IwMmuLv4VvhZzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=HzePbt0D0Q8v3USjwJB-g3MHk9niZ-cinSjckOpbPojCYozki6T2F9G9aderhSKyn9vSBkSaZyKIHKKovQlTujhvYPEYV044p_5WjSQMUAjlPNi5D-bZh3a3xnhbonHkp_9Vw5tO_fZEaVzo-cyvmOZOdKN8MtraFf9HJihjdbbFI_N4kwinmaq4UObQBL2HPYZXAPb5CZ35OPNlE-Igy6hs1WNgduUWeHmIey5g1k9pms-6MUs-s2qJjG7zXzjO2X1Hf8zTlfx9tICdVXBTqlqa_tOOpsWg5hGXulxwr0KybRYwG1kspB-kmpc7MleQaFw5ilK_IwMmuLv4VvhZzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpf2KRTisT2tA5F6ELx6eHbicc1Wqc-OlY8Q7VObg7KtD1YmM668q48bauzhO6jS-Db3gtK7_CJmcoD9KglnLPxTs13zJOcTsBoZQ-wMFbBHgrm8UoDqlAc4kMRCCquyUbJo1F8obSwKKCF-S7rXkSHQyfHZ8Cmp2z9vCnZDoGZYJ9nQA1aY7svnXDYJauOIUnDLbtuYiifxqLawuY6CLwnAVCRDf1lW3umyhFpXz-W-RgXmuaW1maG4HQdP0-cbFTy_WyhpeyBf-vPysB4wvp_DgqJrO-iuEZbkcIKujYlwe8a6Ce9wUuuwz8Vzr3u9hIgCYl18jJNAOrbd9YEqb0TnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpf2KRTisT2tA5F6ELx6eHbicc1Wqc-OlY8Q7VObg7KtD1YmM668q48bauzhO6jS-Db3gtK7_CJmcoD9KglnLPxTs13zJOcTsBoZQ-wMFbBHgrm8UoDqlAc4kMRCCquyUbJo1F8obSwKKCF-S7rXkSHQyfHZ8Cmp2z9vCnZDoGZYJ9nQA1aY7svnXDYJauOIUnDLbtuYiifxqLawuY6CLwnAVCRDf1lW3umyhFpXz-W-RgXmuaW1maG4HQdP0-cbFTy_WyhpeyBf-vPysB4wvp_DgqJrO-iuEZbkcIKujYlwe8a6Ce9wUuuwz8Vzr3u9hIgCYl18jJNAOrbd9YEqb0TnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=iuj9tTmhi6goJtmsx8FU_LM5mA4jANwoWfdQbH0yUq7AvsAfm1htYoyC4GL876dBv0uUvQBjDX8j_ZRzn-enrj_DIWo_QPjSUcjNjDS2MD296e8s8MrTK8cmMwm3WA4Bg3JGAkQ1-mvbGHTn_hXl-zAlQT8dxPameN0spJkCnXQnQDHNdOdVZsOM9iSZLgKUkzEE9OAg3OQqG8h2ij_ahytgkU8lVzioknVkfeiGkn4JcR9bNqj3AfkZiyoyOhKaBG1e9uuUBMVDvGWjC35bdltMYy3Ym3UKW1yY4NYcBhoudc0RFU9w_TUxnbJ_bvmizp9izvoCEv6NQ-zjFvnTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=iuj9tTmhi6goJtmsx8FU_LM5mA4jANwoWfdQbH0yUq7AvsAfm1htYoyC4GL876dBv0uUvQBjDX8j_ZRzn-enrj_DIWo_QPjSUcjNjDS2MD296e8s8MrTK8cmMwm3WA4Bg3JGAkQ1-mvbGHTn_hXl-zAlQT8dxPameN0spJkCnXQnQDHNdOdVZsOM9iSZLgKUkzEE9OAg3OQqG8h2ij_ahytgkU8lVzioknVkfeiGkn4JcR9bNqj3AfkZiyoyOhKaBG1e9uuUBMVDvGWjC35bdltMYy3Ym3UKW1yY4NYcBhoudc0RFU9w_TUxnbJ_bvmizp9izvoCEv6NQ-zjFvnTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwwDAAXzbLPnu3VG8NqlXRwlJkFiireFHUcIP7uYV03KrxZDkykiY75fvcnFKMenpvaSC-QTw4NCnt8SAPv3iLR1hzSn_RKK6LDHmeCW6uLDfWu9opNiBHgGB5pjr8EUMkU1lRwNrpsrRNVya2r5prF1ydhjxnpoEhz9D7lp-LvZMrq77558efODA4c0cvnh_zBB1Ly6NnXSqfoayHeXfzqHeHH02cbabEJroYztUjwzBdTR0oAEWrxNe1XFWMZ0i1VoLH4jLubYGiWenAcAk5TEMtjkYPoXSbDC4xBdp-EzCyzErr3oQbB5ebHrk6pUwjeweslBljaSnOwCMUEMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Ii7hKdgg_dbVIbAhrqOXZg1RnuJdPdWpH6EWzsvH-wYR8cU-hLC8ctBfiejPz-8gfe-yx0oOrES7hO5fGtLhIizAx8iryD3pwdILuP-J6YCaodCwvKD5xCH6YZD79N8Qn3rNPGOLqK_wV5BO-UjAxQ43JaM7I4yRaN7jOrN7a8PatZaMYMQmm7H02s7RxBKvP1xNsCryJiv73WD07B1xHArFw8-yzX0mP2wmkwzanIa9K4gjs57rJVG8HIggoLEkbxJS3Iuhb-CZ5At7tYyyKNmaoVqmh0VwGSMv3H6YWtK2nl7wLhfI_VdZMYPJK_SZixxWDGeJnor88i9vZ35mJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Ii7hKdgg_dbVIbAhrqOXZg1RnuJdPdWpH6EWzsvH-wYR8cU-hLC8ctBfiejPz-8gfe-yx0oOrES7hO5fGtLhIizAx8iryD3pwdILuP-J6YCaodCwvKD5xCH6YZD79N8Qn3rNPGOLqK_wV5BO-UjAxQ43JaM7I4yRaN7jOrN7a8PatZaMYMQmm7H02s7RxBKvP1xNsCryJiv73WD07B1xHArFw8-yzX0mP2wmkwzanIa9K4gjs57rJVG8HIggoLEkbxJS3Iuhb-CZ5At7tYyyKNmaoVqmh0VwGSMv3H6YWtK2nl7wLhfI_VdZMYPJK_SZixxWDGeJnor88i9vZ35mJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=Yloez-nPtJf5wFszne8xcFrtNcWxYCZ7gmFBjVQBGqI_bMibOCAnYAEINARhU1ZzMQsHnKENZ2IrkJ4MCNYGdts0VTEavDAWBsooPiFMBP2EAtwAWk5b1UaGnv2psDTNVv4FFpXyC4rxKIw1gITpzgCleZD03nW_weoqpQxy49o4qJjLAfNyvzmPlcu_rFADiIhHIEZApNQ9DHfhBoVeaftUEmp45ollZllTQNIUQGKFxD3gqmpG4yCgaHcidbgnqNJ_Rio7_sMhfSX6gEfeSTNnn8pMgT0S40pj1JuowvUdoxmk1zXlKnRxlYdBBleMGVGS2L3pfD88-gEzipwGMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=Yloez-nPtJf5wFszne8xcFrtNcWxYCZ7gmFBjVQBGqI_bMibOCAnYAEINARhU1ZzMQsHnKENZ2IrkJ4MCNYGdts0VTEavDAWBsooPiFMBP2EAtwAWk5b1UaGnv2psDTNVv4FFpXyC4rxKIw1gITpzgCleZD03nW_weoqpQxy49o4qJjLAfNyvzmPlcu_rFADiIhHIEZApNQ9DHfhBoVeaftUEmp45ollZllTQNIUQGKFxD3gqmpG4yCgaHcidbgnqNJ_Rio7_sMhfSX6gEfeSTNnn8pMgT0S40pj1JuowvUdoxmk1zXlKnRxlYdBBleMGVGS2L3pfD88-gEzipwGMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=N-QM13CJ6js2pYYVViGPS3aqf5mSF3P0bAnZvb_DJ7ep74NS-_wWo0HZ089hAWNUoZN-y6R0adiETIzaNp84PdF7ZRcw1Py1ha25XyRBveGQ_nHSBDlFZmmfC27Iu4n4Xz_6iy6fLWKJJqtmE4eEFNycR03FKMrTZ1fyftnBScgmoGlJaf7njHWlMCI2nRGXUrk-Ek0f8I_kX5I4gPpSbz1llXPiEy66pnJE-Ew8yaUEt1KjPiemjtw40v89btitYgXtEiuUkOPuR_e7OD_o2AiNxwPKDlavym08p88JDSeW3_GC68FryCmPa2p4OOYSUwX-_RXmboUEhs2tbm2Rlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=N-QM13CJ6js2pYYVViGPS3aqf5mSF3P0bAnZvb_DJ7ep74NS-_wWo0HZ089hAWNUoZN-y6R0adiETIzaNp84PdF7ZRcw1Py1ha25XyRBveGQ_nHSBDlFZmmfC27Iu4n4Xz_6iy6fLWKJJqtmE4eEFNycR03FKMrTZ1fyftnBScgmoGlJaf7njHWlMCI2nRGXUrk-Ek0f8I_kX5I4gPpSbz1llXPiEy66pnJE-Ew8yaUEt1KjPiemjtw40v89btitYgXtEiuUkOPuR_e7OD_o2AiNxwPKDlavym08p88JDSeW3_GC68FryCmPa2p4OOYSUwX-_RXmboUEhs2tbm2Rlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=bOF5Dhidh-hxgJVw33ha_Q5XRzVZ_TnJn__rQqSrXubY15-mi7f_K-7Q2N8UFTExCVfx5kDRyzBpZ6zhYemYgK5LiLY5jQsWQ9G5UeG-xNa5nPNwaObcZfyGPA92E5HYbf1YHFOvuTugOaA7-HKBG0lH7C9RmehGzZiq7cDJdy2U-ljaunYMCg58OqIfhmseb3H1JXmZIo0M7yoV85HltIJksbCvuerqsOswuhiqyeIy5pdfBIdpuxRMjBb5pt9R2DXn4D6FnYQMrlsLyw-Ez8N0j7plu3l0V7pxZxCeLNxhg7ZayfKHD52p-AhDZiBmWLuqpfudVRUk93T1njVwow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=bOF5Dhidh-hxgJVw33ha_Q5XRzVZ_TnJn__rQqSrXubY15-mi7f_K-7Q2N8UFTExCVfx5kDRyzBpZ6zhYemYgK5LiLY5jQsWQ9G5UeG-xNa5nPNwaObcZfyGPA92E5HYbf1YHFOvuTugOaA7-HKBG0lH7C9RmehGzZiq7cDJdy2U-ljaunYMCg58OqIfhmseb3H1JXmZIo0M7yoV85HltIJksbCvuerqsOswuhiqyeIy5pdfBIdpuxRMjBb5pt9R2DXn4D6FnYQMrlsLyw-Ez8N0j7plu3l0V7pxZxCeLNxhg7ZayfKHD52p-AhDZiBmWLuqpfudVRUk93T1njVwow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=fHqzp8eehzUGScJW7kU6l0Yp9P8010ELM7Mpc5PFbW0Sn9tNjG_isbWGayx05nZJz7zgzSa2skTJiDH5dJ2csoaDLIfZPf9fPMEmXreuYRFLjVYskHY5VnOVyusmBuukAGzKJ4KHC5ED12h8bcmvt5PPMsBOSh8HZ13C1ysEykQ3vh9kOlZbpj-d-HiBJdXDIXKidIGiTZr7PAXN_007dLCw6g8BRgTTIbuHO9FHObSVuPbVlvsa99QbV8tfxjRBOdUiaiOSq0cHMoNYacbBRKSBvGgq0FoqvLqcJQ5Uk5Jn_lnGcF53Ay636Q8PzvKo-i9Xu1yNCDs86pO9ciQ71g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=fHqzp8eehzUGScJW7kU6l0Yp9P8010ELM7Mpc5PFbW0Sn9tNjG_isbWGayx05nZJz7zgzSa2skTJiDH5dJ2csoaDLIfZPf9fPMEmXreuYRFLjVYskHY5VnOVyusmBuukAGzKJ4KHC5ED12h8bcmvt5PPMsBOSh8HZ13C1ysEykQ3vh9kOlZbpj-d-HiBJdXDIXKidIGiTZr7PAXN_007dLCw6g8BRgTTIbuHO9FHObSVuPbVlvsa99QbV8tfxjRBOdUiaiOSq0cHMoNYacbBRKSBvGgq0FoqvLqcJQ5Uk5Jn_lnGcF53Ay636Q8PzvKo-i9Xu1yNCDs86pO9ciQ71g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apVq2Eu80KqOOAXiQnS1NIb9CQpJXmaNw8l0ZyM58gKJZz6vGV9YzQHyUrZBPwYMd3LCOWtdxRoIOZghI5pYH3rBv-brI09NIYZdWFnnXP1WQQ-Mq_u4Ojabv6LDdfQPDqHywNJxGAe23a7Dukda10xLgflDtWWfY2RudzizSNekY86S29qttqQecamwAEUWpq5Xw5bMlmKPZY2KxpRBAiWVhqAQcYRqD8ndhFSo3fFH_8CRcERhla1JU612idiwifBzIUQ_KA9yr6IyEs8G_jGgd4eY4bWRvhxmlIujskoe4u98e_NARzflNYpLsM84w6O36JBODUpO6YaA740piQ.jpg" alt="photo" loading="lazy"/></div>
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
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
