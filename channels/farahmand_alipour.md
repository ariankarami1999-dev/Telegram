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
<img src="https://cdn4.telesco.pe/file/fKRgIP8H5co8nNtTNDsRYeIYLIDGrydXzC59Zj2YKpugKek-J1vRIK18TL2zXCc_LGxY8AlVD6ox8bkliYgk03GNXitEpTZLoGWz2aOMPUlJyffBeAECHgB8tGJcU3GLHJYeOsmsmH-Cka5OIqnQ0cmkWOqL3i5p_T41E2RcRgpH83Zi5Ia2ei-qlG_QyDZGHPsxu84-TKpkCQ57EhRDBIgqYtjynQBEHtDnvtJNWVP-YM1BZ8GtGvUAKXdUeiko7c6HSvA78jMpHAMlMhzuZ3kKwrHg66NBT_Dt2F6-LPDnmEsfN-AMPQP9aKelMuZz0Xzh6FPjAJkuV1gJknaPRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 14:22:24</div>
<hr>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFgTgBAaDE2Br7NXyrmnp5A7QvsRMXp2Ck7ehAh6P5elVRLqj4DKosPXIv5ny_gZodWWg5Vlp2w-2LdLpg6w8Ey9BOso-f_FOtcjTUS5LCCGQk12txvQ614Jvec3C1oK6_FJjC-JMMpFpqaOwzXq-j7MF8bvs4tqiztpIeR_i2ZGw78Gzgs-DSVzwgbNjCKM1kQOk_Q8twxYata4i2OS1XTBLxgfYLrGIn8PJWUA_vq_2FnvYdkIOqe942jVvaZJqta3eTKmdpUzVYwBDt_LCBn2nr-VsMuDAF4yQwpPthLwrxsBlB76FANGE3ai0AZPiF6hgVrNudc-oWl3gGYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Ojk1YGL9AKnaOd_HtUetvHBF04nt-0Kwm4bTBq1lhBZLzSdkFBK3-BT9dx0PZQT2iyZx-yTqJ4LayUq585gwZXX6_Q9Svi0ftgZVh_NrU_MQN5RqZWjIhjzSc6kl-o_xeyzoD42SByNx7ngY5DnA-wW-3wyIy84grrd09gVVOzkfXIm2tbFtYWCsX-VwwzBr7bjdxx7gskzAPf8D4e_HPMfZVdm489A8t21zy4G6y34OdZshMRGEIZ1mvZjItE5-rUVA5QP0kG-Kqr4syw3IlDH9MePCGosFZm4bDsb3ppWgsd3f7cJrCHpNOK4PczBwIIUwIwoHL3mUlkwC0KewcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Ojk1YGL9AKnaOd_HtUetvHBF04nt-0Kwm4bTBq1lhBZLzSdkFBK3-BT9dx0PZQT2iyZx-yTqJ4LayUq585gwZXX6_Q9Svi0ftgZVh_NrU_MQN5RqZWjIhjzSc6kl-o_xeyzoD42SByNx7ngY5DnA-wW-3wyIy84grrd09gVVOzkfXIm2tbFtYWCsX-VwwzBr7bjdxx7gskzAPf8D4e_HPMfZVdm489A8t21zy4G6y34OdZshMRGEIZ1mvZjItE5-rUVA5QP0kG-Kqr4syw3IlDH9MePCGosFZm4bDsb3ppWgsd3f7cJrCHpNOK4PczBwIIUwIwoHL3mUlkwC0KewcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=YlRGKbWXW5LweJBTNg06_1JRxhVDklC5xOZU01AiADOEqUxOAhk5OvrzZuRuXQ8ND1f8D9HyhGDYt7j6PZgOXQocmQeqp_p4p02Jyx7ULXL1yJfHK6SXEZ0HbMx9qYC7_5cAHxkOuz-ylRYMCzrQeaqMhTzMwf91rcNxlzt53T49ncq-bDW6Ki1HjCfZIthSadgCQ8e7nTEqq2u9LBKzByXP1K43pDErwwyYsJhaKyNozsH-9Y-QVEq7mQuzZxApl3CxQ5hMYTRaQpW8R7KaN_lBGT06siez5treaz2v-S9sGliNnZ9UCwZ2NPVLH_JIPJXj-T_iwc9_NLK0NsCXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=YlRGKbWXW5LweJBTNg06_1JRxhVDklC5xOZU01AiADOEqUxOAhk5OvrzZuRuXQ8ND1f8D9HyhGDYt7j6PZgOXQocmQeqp_p4p02Jyx7ULXL1yJfHK6SXEZ0HbMx9qYC7_5cAHxkOuz-ylRYMCzrQeaqMhTzMwf91rcNxlzt53T49ncq-bDW6Ki1HjCfZIthSadgCQ8e7nTEqq2u9LBKzByXP1K43pDErwwyYsJhaKyNozsH-9Y-QVEq7mQuzZxApl3CxQ5hMYTRaQpW8R7KaN_lBGT06siez5treaz2v-S9sGliNnZ9UCwZ2NPVLH_JIPJXj-T_iwc9_NLK0NsCXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehRwrwTTfHTZEAAkuJ_fPFbkAduzwzO3PLrfBTEFOmt5BGOdngG8rBZIawftJ-uHzaXl7GFeHuKoijh_6O4IM8PYDEeGdR-li8aVgioYJtVRty9JWWYONpLs6vCiY4bCSkcKdX2mvQqp1jTUSHku-RIS24H46sJmIDySazYMPRFn0zgSasgib5KOJTAZ6xb6K3rtRzbGD3BHTGPZzdQuRHKctmL-vcZsWlW-ti7zrhI0eExQ1CwoQLT2nN6NMOUmSpo5Tt9Zzhj2w8Svl5AH5HMIfFPp5jQ43r5Qjs62h9eU3zAZAHlydCvYITWRaEJf9S-ekXkbgBRudTefZIkMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RrAwsDMLyEYVlAP9O3cIHoqt1m6TKIwr2Vpb02KkW9oh8LmzojNCkuQwGHvp9eovnYJdvwq8BZPwwVkunlasHl2f49SMCXFYHFvPbADLSuE-5yEJZaGExpQGtrboXyfyKqB6xLwprqiXMFoB-Uf92VDhnaydsY2-HBlmEZWDlQMlG116xJnX6-KYtA4kJHQ3o_l3dKcR22aKyD32sXWJiSdTX-zkpzhDjKdFa-ZIIoP7sC0VfkW82JrvUkBcrO5BiKKLHdgRhvNarXGbyK1v7b-yBHqySLF3t3rDmWE0Yp2BnXcPQnPfiCJf6Tf9VmTyl5Z70tRZFQBivAK7ZwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmST5RLWGJmfjAQWAb1iXfv3Tjz2HUDKP9K_GvT4cuqb0eDShKRpG-dxB3GTSdld1koPqljudy4vBLbpWolcDJaivBdxF5DPKY6-KmvU7nAoQS_kveJaWRoOmUIipJoQGALbD_I7bxOeJvMiIQ49YnW7OD9SoIKBTgtnKjjpa8mWMGCXgFXd_SyEwTCzj0jWcCV0z4weyzl-2-wJdzzjtJefxqdF_Ej8I9lmGfug04FQ1IUIMrH7idWoNrWJxIyeygYO1KExQvN4lRoQk9CjaTwj7kp-9nRXif7uRjP8dZhLO4V8Rj8rvIcBaXRBhNZc4fP88moUg8XnyzUY6FzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=gME6EU6JC0UaXNoWEdrPrNjMZE8y_N45Y4_xd6jtZCbQabyjv2F7cgKpbijJTf1qRvCPLfnPCien3zl9zlmTgSVrALFVdxv74zvM3fzhbqxytp5vC6YZ0tvNPfisgcnNzQOHC6N455cRgHrzh3xzzFlqyC5AOT8404fKvtRPfLmrEy1LVp5FwPptsvy_56jj7uLPYvdptg4LRCLNu262cOCyt6PvBCKftW-OnjIuL09LIMqY1lHbkq0wTrzON1cPy3DZEmvgn6oollVDw1j3huINMiOE47FMIvAC8mDEt8yxX-5xoq8ctd5pW4e1c92tXhJU3CBljmA-nx28qqGKLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=gME6EU6JC0UaXNoWEdrPrNjMZE8y_N45Y4_xd6jtZCbQabyjv2F7cgKpbijJTf1qRvCPLfnPCien3zl9zlmTgSVrALFVdxv74zvM3fzhbqxytp5vC6YZ0tvNPfisgcnNzQOHC6N455cRgHrzh3xzzFlqyC5AOT8404fKvtRPfLmrEy1LVp5FwPptsvy_56jj7uLPYvdptg4LRCLNu262cOCyt6PvBCKftW-OnjIuL09LIMqY1lHbkq0wTrzON1cPy3DZEmvgn6oollVDw1j3huINMiOE47FMIvAC8mDEt8yxX-5xoq8ctd5pW4e1c92tXhJU3CBljmA-nx28qqGKLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn7E-ZJobfeTNH6AGrbUcLVU4xpDAQflfyxRmqaq4zthGf8XXJ_eJxunGEWa-w4MWiev1l5jMc_wVpqFXINVXW-xl2lOHB4yNmiAYehDikmNPiyLT_KgwEVnS1g-9oLE1ThqxWVmgJmnUXbwZietSRNa0FVtNAz08624GjD4ycxK4boMioW6HcZ6fXc-UwgkGVnhuOEp4cAVfUTZV7accw3kaY6EUVovM3YAu0aVnBct4u3Y02OJ1pxzgVQ0mYiLwFNsAOg-SRcL24K5ByK8nRelCVkBYKGJqBwvoFeRw3w_UvMBxhJZDTPJwxCpOASVujvckgr4nJLvQ0H3iACQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESrxsxZhqCdJgKjFQ42B4dVG2aeXpQlVwIRj5HoHDsNJXTVqPYanTXzQOVIrV_ywKRMNh5YU-5nPYIpN-SMXejObcSk8bp4YdcLM4qq3zgJuxkvtS8Z3TWpisMrmmheaZ0NkR9KsK4-4lkeF2J6X0l-tPL0bpanO1o3Ply4VnM1CN2Lq_nKO_PrnqQHxImyOMRvNzm9kDoPBbV7vEDvP34kF_ahTkFYJ_pzwSp5IKg6kR2JLBBbIoP9oxdLm4kHffQFR9dj2ZPTDoGYgslq3KyXxwjkZACSNkHWfPbSw8zQbqkrMEPKHmOSlHXH--ArLSIOqIlp1IQy46zEpuGgu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgM4TV_MSqAszk4xLats3HQJTEwKYGra7YrFGVlmf0S2ZSdhPja-sotIb74QwSMQIXW0y4uOobeTeiroSgwA3tOxhZLAElX5FL7hH8woi311HjjszQWk9qjF0ivYk1Z3XNRqSe1-0183-Ych6Qn00LIVaCdf24ozGbWMvvHdM1kOjYXC6xefOT4pZwaW0EsLUzbn1IGSi1LaivGIYLKXgLPKgSYtQIYeW5oz11SQX6rFtoUjeAzHT5IIOJeREg0xiwCksv1eDW6Hl8ol99BeMBYg-XRymeuwrF_qgSBV2eDu2U4KuByurBMIEixS7YqllqjPfk928yJF4pVzcwp26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhcyjiqDZfLOMVtxhQAAW8n6mBWza5ozP1ZnlYpmSYILCTJJMCF-EDLQk1zcfEUiH4kmivYc0Jrn62A5xeKzkkHEtUujwsESJc8yKQDG9ZaZ6lq26Us5DPCk23J63pjnV7zVaLS25zD4i6F0xRTuGmdjZBU7A4WvGJXk6d-xddZBizENbgRrY0zTTKhe3htugHdONnp0W02SGYI1TdrRO_5pmNjPlgZojCLFpjgjeN4rEsUuX4tOh-GkCXfu2Y8rDrsb571S5WOSwJklPkBgNV7aS7jIwvp-sH6Y_c0EtYBlelK1ll2Zbh59tEDzJKJSQIeaHuTlud937JkcpqWGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSqpGwHmBb3GeuJCp-BI33rGJSyqkRp5NVU5Qgk1Cd_pYxOS6z6MZb2_VuqoxywU1jJ-h-jk9r1L7OmPjcjuPE7wTvJHOEqhNQn2SLOMrGUthtNz47wekX9i2BfnflaVF2V6XYdomII4vkI3Tve-7pbQqA3GALj8oAVXEB2aaaMLPn12PxnZV1EcfyeQmfJ63bi9A4_6OO1s_7q-BdTf_sGoI2_WI-YdzcuXfesUFKxnnKPvk8e9fAcycw0MqdFRij2-t9GamSZv6j-VTJKvnNndAoOnsq8JXM4MsEJ0cSjYpgtwOXgZZE02bYVL9CDn2Th8yUqVVhatuMoNpFDvBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9MCqNt4MonU4vd9jcpu5q_whEQYi3wo4Z9OA2bY9xqps33DYm-NUK4Ou32IwoRvYURvt1PfXr8Wd7ZSNwAYxYZETdZvHFRVVCRRMSG4pNZYMLB8tvYN1XlnOgtvESwR250lXrblM6QSj8_QHxbbFI-l-1IsRb1zPRhC1-MUhGceCWkMOIpafq9GBzOI4RkiCH2Pgwbbl9eWohMlbaQ1DdURp8h0cmCgZ8hnxO1EkVF-c71B_E1LFWR_EXpi8Okls67ZZUioDP-2cRnewXXHt_23OWJR_lkeNH_vHrgR3o3gB9f_Gjy0TFXHmQ71d2kxAyfcekvSzGIStUNhY2NcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5dOmsEDSI38_fvdSNj0UcfjF_NkJANNYpBWGpt8kjgCy1fDTOv6j0GnG11KBueJGjfMbXTzgDxZaJJlTxJRwBMJjKyEe9AXg9DLQ-3D91aZ6MtUAv8iEcrnUkLSzpDxDcf8e2TgnbjAHxb-vCleoiO7aXxEPdkDM7uxvMtaQmzUQ3AHyFWFeN8Yb7T7OV9Na3P5nnzFzZRWnzjIF9cSa6KXdZEVPi1ix6l51a74QhM5D9p6iUFmElKOBD9tAJLSOU5r9GXrffd1GeoAZzlCJnO71z8Gv8mn70yHUd9Vv71WRLoxdpOh2_sHLrgskJqASLvF40hNwAkWsstfNkBNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMjISNzEZrxT5JjOC49sqKrkjNGokCeXJJcJMftXtqby_4XuUc87bm3w6Etf55uvxGTlNVUE14PfG3u0SqO9UhWmofceoG_nj1Cw69NROudyCBbHVWAi9fX4adzEpuAw4oVFxPO914Zx4A4euMsWKt6qiY4DK32aP6bcw8hRmfT4o2hzq_qYGXEUTgLUMSFKFzrz1jU7V0Ar33q5NqB0Qw2fJYyMXVEt91ZzC6wBVTRYfnUh-0dGvI2vWbZy72gIlkgM4cgkXK4URihGzyFPksVzwHK5l9-LI60t7NAuh4HrlER2tW7yqSveyoIK-xufJrMMecK1naUSz3TTAxmkGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4-Rnnl-8uWIbt2KovYAiyF3_XASpYl3qFV7frP0nWTfLiEzIGoWo81cvyolVsWHAe5BeNnNOLmDrLfX892ueduBuiDWD0iAJ8Dxk7t_8Vj24fBm5Vq6OMEyOBOupegBSSMPkcSxO6RjjlvpqZzDWuAUL8kUasyGB9VN5P5iUVU9N2paR2PVzTvd9SJGAckSxfYlNQhWnmlJORGcG6bNyDVQkLNlCDTihDLS89u2pq8zbMf9HT0_GxYaxmdSB7NecHD-szOXd6A7bF6QdtvpWDJHVcDCXjb0Zmy2-GvWWUvlQN7Aql41nIcRFrkqtgl02bo5-dmLDayHPaafiT-QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=br_5ci2lL70CXX1ZOiPUdfOGqS1RLFDKu3iXcw6f0_7zpVadK29TOGpIawvtwNl5kRBKLmDB_4fhVEc4JgmhSN7wjC6jAaIjuD575rxrpN2pq3X4esXqy5_JxkpPNOqyf1J3m8yolDVLIo_Xa5Y8_ihFIWLihmZkH3cZSiiLtG2eG_CvfEmaoNfxM6w4iReAoute0enh8Eo5F1cwHOm__t4-binaZw4TxcQEhe7sTxq1kWdrVlqP6SK8yjStXHPq_y-GZaw36RaxsMcOlAbBIq-E7XgapNIz0WZN3xfFXl6Dqx5ekF2On1pbHLLVPtfL0jS5NxCezrRnNB8cGPHg8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=br_5ci2lL70CXX1ZOiPUdfOGqS1RLFDKu3iXcw6f0_7zpVadK29TOGpIawvtwNl5kRBKLmDB_4fhVEc4JgmhSN7wjC6jAaIjuD575rxrpN2pq3X4esXqy5_JxkpPNOqyf1J3m8yolDVLIo_Xa5Y8_ihFIWLihmZkH3cZSiiLtG2eG_CvfEmaoNfxM6w4iReAoute0enh8Eo5F1cwHOm__t4-binaZw4TxcQEhe7sTxq1kWdrVlqP6SK8yjStXHPq_y-GZaw36RaxsMcOlAbBIq-E7XgapNIz0WZN3xfFXl6Dqx5ekF2On1pbHLLVPtfL0jS5NxCezrRnNB8cGPHg8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6OH-R_4sKsfA2cQx8r0ePwyKXIKgQLRbBxylJIaF-kx9gCZbhaKM5ZtSqNhoDTxZULciufBBZraVPQU3lwtd28C3AcMnoo5SgwxmArp_Y38gmMLFYaediAj1twtv9hbaT-sKbqRHyHoIwSeSkutqlg-vnMCw4yyup9GpiyVx5vh5kW_Vippqcy50g2KVJXZ5hr4mI2ySn63plt756bk_WrUDSmf90V9rXhKtRse9oITAUlOjQ30UL_CV350tOGwDe3LxJ5QFSZ2joKVM7ief0nb-l_ZDLEXk8XKcYRApccPB2FYLepC4su7DQ5vV3yejNgNOVZxMukzfvIwpgPdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSdLRUvRHPoglN7uW_jsxwS7aLK8NWDYkVnzPVcseKzXuEKXSxSsj_uYCA4eC-Ecw4o0J8ZoLTW6x3-43B7ARTKW0OIJ_N8SWsH4iqcc1oFsLbFrGGvxrthFzDKFJ0wJ2moYjVgFRg0AYq_AiIetDhng9Mhehst0EikBebAn2mS2kVPsN_SpJWeIp7c201vfH6Rqn1zSgf4MfQcI3cTAP5sZB1gmDNXON43iwhvMco6gulDDmjn3GZzgHiC9PBdFTnow1KyiUVWw7NsqDODJ-cru8CUXvjbjTMPO9mpPgsNUUf2cOdp9P6hkhQf_-ciOzqnb5J63pbXZxRbqvhbLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds7CtdR6WMekAHzGHLsxwcMYhE0E-z42H681wIpEl7UuxuxtSBCC9pJgvOY_Kp0cjTy2aIRIj8JGGXtDZso4GCBWuc2lYCMkDKNYIGphZsFkyc3eCqhgAZLVA_CIfCdD6uD-Z2FTYZqcfZfbotxt-VUgmdRzutXs0BPtUd_V-IckOcPxnuvIFwR-X6FXZdFdpWxTAjFlokR_iLpI1boqxYhgEwrRl-uPw4yJiPPbHts1RwP27RjR_nl_wrTptGplT5ikARVSHFBXI9Kcd1XITCSZ20HjJJIR48lgwdLtgGEFYFpcNiN9BuBnRWNdYEpVFVJse06_E6IofRuOmOsMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAyuHGmqXTUcLje948FVMz1yL1F4K5FeN0SN9GB6CooST8M9rTffxtmesmofUSrHDXK03PT5WCbqgZJU_v-HMSfnzfXrqYPIwzeJ4cS0Xd_wI8xjGUXiSWiCmvdl5O7XBIKDLNzww7Nv7QJ-mfazGQQEcMBbOmGue70mqfEcdT5ECYJXm9jSSoCbLlgAH8TZanpesyTEJ0T5NsJUQBJ2ke4X8j0wLN0NFwIBNd3FdQ7WReNF1vWF9R4Tja0oy0sIrCzaNRlLmJw9oJo4y2x3MS-AUeEBd5pO6HydbKc196JCp40AQKU2PWnWkV8o--iQgfY9TYbSxMy_4FAkjeEtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd7josD9paMfT-0ce_Zjj1h564ZhkmJvN9pj1FO160ERd3f8W4cAdNTDyLGRp2Jv-mIpmCHepo2DUtlgNkPXLFuynuA3MJdFaOpNe0SHql5C4UTwNOoU93oJqQ_TNEdk4LVU0j1FK_dgQhGg6jSTwluCru7CltBwzxiBHqt2bdBgitaFx7gIJ28Vp2xQxse1oFgq-o0Ywu4Jm_dSRo17gVzdNYxCDYMSNShDYoqnjT7rJYFiuCiFWLNxOgT7vIbZzzVfeTlYrXqlJz4LMnRynVQhsQo4UTIbc1GTpjEEGoN52lxVOVtu4fOJYKRWcOcqnhvSiM9uom8x2E7CKlvNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o04S44ALXzyGGEFPv_ENIkzhAFVKfO_LgoZuafQGu9v02vKTRcvazexnqQ7jK9f2f8Jfl_ifZQv6wJEBAYUvMLHGSXHpDaVU23un3xJTksS5DebtGUop2Su-Oc11qFHzgcEEI6cZftFrpzk-Oxq299gNgJi_pJRADl0y5Axh--1-JGRmuk7Xj7c8JpXEOa9cKscOHCXiZMEvVJ9rWMStiHllVWSiZu5t7S7-JgVJnKRkr9ZP3GhcGT5_4W2eA9XXl2UF0FT8RpgR0AYbtLUzhtGFKa8tftUVua-7RrSQTLPAhvcccTc8d0kgP1sMujKQzyBxBbP9YGZh_8Z8t6BdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsIDjU2DxGyn0EEq0bL2pNbMuiJH7TNZzzr2a75Vwsb06glqvpyvh2HSKbti5VrVt70rNKBFHgdIsuvsetedkxsEcCqYnmavhzblqmZIZDPABr-SZLOUTZVTwRYaOzJlfL8NQUalI_k6udvuzwfw0vSJ6WIHxo1F0-axd8gMOLQSKF-Ivp0F5vUmEtw-NIfdzuF2iD080aUSFqZXequ6eqEW5ohzgOSvE86Ds8IvrrEQKUxVOxbk3AFj-iyU7rddnGUkTe8En_dpGBubYHaWqZR2JEPEeNcgghRbKSV5oWsaGJBMiLmbNURtOzWFXhvmUBGSkLeAtQgdhCogk34b-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=DxxMPg8Y3FT_eYcA0NUZKEHyB78kfUpbjGBWHEneBYAC38pKgRtw5CB0TLBtGtAYAC_8fMDon5xRHXllo6ZO3sJcPHUnuP_yxG2onh38UudL-91zqm09n0aENvtIdbL5N4b_YDW29yyskrr3ecpyXhuOvS157tGFiNUDVGPTq5BeoGAmCOlxOnCMvXNlJPRjU2jbSuDbqXfQnY3Ae0GAcP8lU2WR8iUFrDCp8XMcH89lHywp4cJDGjGy2A9m4UVdOERPiaOtBAB3rZmUEoGotsdcW91mjT9mfuCHWzikq8CgmKuaU3VwdvHlH5d8KoIReuAV727vqfSrJ8PgtUPTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=DxxMPg8Y3FT_eYcA0NUZKEHyB78kfUpbjGBWHEneBYAC38pKgRtw5CB0TLBtGtAYAC_8fMDon5xRHXllo6ZO3sJcPHUnuP_yxG2onh38UudL-91zqm09n0aENvtIdbL5N4b_YDW29yyskrr3ecpyXhuOvS157tGFiNUDVGPTq5BeoGAmCOlxOnCMvXNlJPRjU2jbSuDbqXfQnY3Ae0GAcP8lU2WR8iUFrDCp8XMcH89lHywp4cJDGjGy2A9m4UVdOERPiaOtBAB3rZmUEoGotsdcW91mjT9mfuCHWzikq8CgmKuaU3VwdvHlH5d8KoIReuAV727vqfSrJ8PgtUPTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=rRSNWBE1n_J-yTWU4il6Ry0izEhcJ7PbbFhM05o343Es5BU2qPOqUPySWDSgjmkpJ5zLQIEx1xhTAvl0Os-_vmZz0ttpht5L9O9udgwOgmV7PQDy87cC0_a58elWWtOLJuiY-BoZoygVgF-6KH96NMfdDgkd4Fi5TdnE5ZLL6HRRcxAcUW7Exibl6uu7oh2K6qFiW2l-aBvNBdWjB89q5Su0HeOrw7DYdqVOvxcxWaxRPVlSbbsLu2z28ElQlOavL9pElEOEcIweO4lRV4rbCpmsXal0pTo6nAAaTlu_Fn9yucXjo17gNz4MdP1KtnUC2slenfMoAgWj49LyzQ62Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=rRSNWBE1n_J-yTWU4il6Ry0izEhcJ7PbbFhM05o343Es5BU2qPOqUPySWDSgjmkpJ5zLQIEx1xhTAvl0Os-_vmZz0ttpht5L9O9udgwOgmV7PQDy87cC0_a58elWWtOLJuiY-BoZoygVgF-6KH96NMfdDgkd4Fi5TdnE5ZLL6HRRcxAcUW7Exibl6uu7oh2K6qFiW2l-aBvNBdWjB89q5Su0HeOrw7DYdqVOvxcxWaxRPVlSbbsLu2z28ElQlOavL9pElEOEcIweO4lRV4rbCpmsXal0pTo6nAAaTlu_Fn9yucXjo17gNz4MdP1KtnUC2slenfMoAgWj49LyzQ62Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4X2qoS6yZZltTRixMPE-p8D8SDZ3J5XosBP3bCC4UUWKShYGfy9lvTxGioTbLqdHgtwvgypRGmCKZ2AIGS8VPKOLvqBSyxxxPo1W0Sc3rJ-chnzLMhB9pWqkgJUsWh_bg535Btl3EmRKpNbiRR2sO3vKTpkHz-HHEYSDTKMLeF61X6_nzwIFxuAWBmJN7DmW_vEKrBQpLV_k-YFX7l6kFQD_7mtGQrBVWt2cTK3W4Os6_SNqR9GzkSZlAuGPwS5fmTPhCmYVStWDixuASfYD_kPXhTO30WNduuHdu8P6Pt7TputNcdPeH-AYnt3xg3KD1b-4RtQM4LoGbPgAoGiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOc79of6H7PeF4A7nV_9ae6ZHtyc2eZOOm8EhPu5aX2EiGDZLfMTXc4AWue_cscWbV1TyrwfiPKDR_-_gHGB_LRv_khc4cjyDUEZpRoCFuALLz9OEXz4AethfOqDV3M47QMr8V0Mo_V4cS5js8dpvGCfozWPRHnCuyGHew944Aki_jEOnuCIGgwL4CiLWKFF9o_SM6W8toUcJsYYYGp3Dc3z9wYc4eCeouxWg6wVrygtbL8ajR6Bx609sIh13mz6mU6Syrixlu2DHg3npm1QPg6jT15bwLjFIYde4wrQUZGfHHda6_wTzmC20TY3Ouck9x3PiEBqJMJy6XzX3N2KCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=PlNX3HOrgE2XXMoqQREw1Kmz0wtmNCHeZp4hK0ykHt8N2V-LqmkwjwGrOrDWcAVg_04KB9Nvo4NYhPtOLFG15Tgad8B1TPRQzOFAYmtwI0S0MVI3o1lyIu91BnDx_eXYvqGoiYRb8YFpJQkaJcumdLKzxX7BNyc3olgyg3hNeA7lxWPc_Ca8FAnNJ1xtUw58BHs18__O2bFKjat9FsaSy7bgOsPRrNmmC1aAcoVOu4tdneF956ToqVZY2eNfUGylsYi_NaXum3tncrLEDmmhj9ervGBdS03jvfrYJUZ6BKSw_9e5pkWID06v-jifn1rmnaKBhPSDmU1JR01sGWjkwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=PlNX3HOrgE2XXMoqQREw1Kmz0wtmNCHeZp4hK0ykHt8N2V-LqmkwjwGrOrDWcAVg_04KB9Nvo4NYhPtOLFG15Tgad8B1TPRQzOFAYmtwI0S0MVI3o1lyIu91BnDx_eXYvqGoiYRb8YFpJQkaJcumdLKzxX7BNyc3olgyg3hNeA7lxWPc_Ca8FAnNJ1xtUw58BHs18__O2bFKjat9FsaSy7bgOsPRrNmmC1aAcoVOu4tdneF956ToqVZY2eNfUGylsYi_NaXum3tncrLEDmmhj9ervGBdS03jvfrYJUZ6BKSw_9e5pkWID06v-jifn1rmnaKBhPSDmU1JR01sGWjkwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eggipH38_QODR5L9agGrJqFGOG1K4V0i8BVMl8bHlWaCDs2NgWPvSby7nMAWYF83Y4RZQkbVR8pfYrNhIBYipktwR0mDFUL0Lstu7hB8pY5D4Q2r2Cb1qozU6UBToS9G2byVLgdDzzfncUHzc5QY9LNdalIjB-rK81y85hu1Ksxz-eh9wPVPLpFfVxijBnfIcCEWbM3gkvTyW_Rrf1yBQRPUbKKdb0CTBfWaAAlyBEa8B-5Xf85P6Bnp-0pdQ6N83VRySYl7uwoi6gTzLSL7Ie-MULPt-mwc-VioVjzNGbf9nY_Z7gP7AY0nE7PUmC9_BdsVoYi6lZyeZpS9HXsKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbx1dk7hzjCOX701b4Z1ArkCQhgFalglW8IGIpGFyyrNSG2058zqNG8mH8jeIVaMTJky7ea1SJ-b2dOqMDb61YM4sRmERhbT-xv1ZaiC9umsxzPtOEhO0xgamLEWkN0N2gGLdU1WU5cXykK7wnvOIiZtYf6elugW4RcdqQyiNVhA2Q2kf518wXMMhlL6S-dE48aO7mtTF4Edtt9MxCV_q3CTOLbrWThNAmSxbRtTi2x33ZU05vqIhgGIl0fA66GYRSfzlGwss1tf5br-pWhtj1Mb2X9qqmLQhfyBK1VFY21WQP_OpgPe6lZJqISNiOXIlIdgYGTT8L7C9b6aZ79Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=Rwf0irc7ImALU2NTy4NqdLjlDj7HUoRC9K252XobdkQtCwTmc-G2rdhpP42yA9ACAumeq4fubEHHJYe58khohL47OwQKzxJOAptYCLD0EqjM3Tpg_lu9VrM2zujJnmXbY-gpe6r3BLY8dEFkSUP-TB4jPCSQbyqqEjP1nrQcAI1zi8nwVsEGKIPszEQdFDm5k8YDPqvjMMYTqtMWJe136mupmYGfLsfKGBkx1YJGifOc57xLhAX2_XRCM-VNrfJdPllGTksTc1CBli5_9r_DoivElIYYjEOCKllNUFBhTm1Okvu2ysSACMePk9hWhDst0o3LIWvkII2WV8g8zz79DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=Rwf0irc7ImALU2NTy4NqdLjlDj7HUoRC9K252XobdkQtCwTmc-G2rdhpP42yA9ACAumeq4fubEHHJYe58khohL47OwQKzxJOAptYCLD0EqjM3Tpg_lu9VrM2zujJnmXbY-gpe6r3BLY8dEFkSUP-TB4jPCSQbyqqEjP1nrQcAI1zi8nwVsEGKIPszEQdFDm5k8YDPqvjMMYTqtMWJe136mupmYGfLsfKGBkx1YJGifOc57xLhAX2_XRCM-VNrfJdPllGTksTc1CBli5_9r_DoivElIYYjEOCKllNUFBhTm1Okvu2ysSACMePk9hWhDst0o3LIWvkII2WV8g8zz79DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=jJJa9fiQ7it0-LUcFuTPVjq_pK7tS85HoM49oPXy9KRZ37xSVHCw4ZkwQK0RD9PvkjJ0eQEmm-ADsLPiXyau9USoNYYf-HhtfotULWdgwz-Blt4ZLxyXFaxFcllMIXtelLu-ztN_CxE3tcW_wqHwftFUW8C2NPr2-ufvek_E7OcXID9gWBPvX_VC5x1WxAj2g8GbtSHEpgqju7_GIwox2sI1bel8oxVsdusiGUOyXGU1JiKbop6UrpcCQjHxXSsVF2NmEvmINNpRbOD_kI4rB4sEMUU-bHM41Ldk2_KxCs5O9YMDWEjuvCQQInnv7--gGWDNtTMJBuAhNkUSOXu8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=jJJa9fiQ7it0-LUcFuTPVjq_pK7tS85HoM49oPXy9KRZ37xSVHCw4ZkwQK0RD9PvkjJ0eQEmm-ADsLPiXyau9USoNYYf-HhtfotULWdgwz-Blt4ZLxyXFaxFcllMIXtelLu-ztN_CxE3tcW_wqHwftFUW8C2NPr2-ufvek_E7OcXID9gWBPvX_VC5x1WxAj2g8GbtSHEpgqju7_GIwox2sI1bel8oxVsdusiGUOyXGU1JiKbop6UrpcCQjHxXSsVF2NmEvmINNpRbOD_kI4rB4sEMUU-bHM41Ldk2_KxCs5O9YMDWEjuvCQQInnv7--gGWDNtTMJBuAhNkUSOXu8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=NfsuUdn6rzn5hr83Np8TI8e4koBhllc3x40RYeDoYHWre0tmEOW1PblDd6IH5OUlwtY3nPpd8HKBXs9I8NFvHUF3GfuxeA7EGvZay8E6lhpyNd8QO1R9JTpvKy4Dgthrf3VPyhguHYmqvUuciw0MgAEwCQ1BxOcLsIAv3y3lrX-cwRQVEuxPFqNHjLHIfZdO6DIHL5pmrZBymDNaK34e6qGKahGCslhHbSKPeQ5N9FSnjs_ESfofEvEH9-uK9diAH3OBO4rqvfPjBBIUGFx3qoUdOh4Ek2ZLp22n4FRA9F29tsh00lfFS3CApP_b6yXG6PR8A7j7lyc1y3GhQpej9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=NfsuUdn6rzn5hr83Np8TI8e4koBhllc3x40RYeDoYHWre0tmEOW1PblDd6IH5OUlwtY3nPpd8HKBXs9I8NFvHUF3GfuxeA7EGvZay8E6lhpyNd8QO1R9JTpvKy4Dgthrf3VPyhguHYmqvUuciw0MgAEwCQ1BxOcLsIAv3y3lrX-cwRQVEuxPFqNHjLHIfZdO6DIHL5pmrZBymDNaK34e6qGKahGCslhHbSKPeQ5N9FSnjs_ESfofEvEH9-uK9diAH3OBO4rqvfPjBBIUGFx3qoUdOh4Ek2ZLp22n4FRA9F29tsh00lfFS3CApP_b6yXG6PR8A7j7lyc1y3GhQpej9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_P561hiAxKGD83MA_zFINfiE0JqIJHT8fn6eGEbAM68wYE3ePH8K90xqSPoyUAwunm-Ao3W6pBqpCzuFrpW4sQk6haTs9HsRVsYzAGWqjJJ4XbQJ1N2J6m7NjySO5n6o_Wsiy0BJFkrzQgDAnsRYcNEzxmcJGAgvRZDMAiKnsPrS-hfW6Zlt-D-9fdWhKmxgQJRTllxVRPxMhD6plgBsE472kWDXIRdND6OCPENH-JTxmtPzgHqRWFEljEhFBJC2gzLOIDT9rJ5q06dWPL8k_04wUMGnHxETHk8X9ZGwjduQZNpkaehbKvQCKVXpRy9NmoU9Ts33tgIXOYalvmU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtcoBoay6yWGV6jxRIZId6EkAZvheQa_1WdFzhKOt6gA4DkL0AR4w4S70p_wN9Ljz7wrdgj4kLnmKL-cvrmXLlHWUDBsm9AExieBxzp9MU5DClikojsO9cVNFO5usshoNV9bR0JdeyMFc6gjp3dboHUN9IZmDmZcpqD5-Qe1PRwirE0ZnGoaZbfgAD9gWs6kOS9qxlk3fx6DHX78Z2Ww7I4Kfhhd3t-maW4_V_WkiW3mrY2bxImav1QfgarlRi6al26vXbU6F2xCl-C2NQOMJsE4oShKfAtEp3Z3iJWkseLJfQDZrbqCO7JKBsh9C6bofozZq4AGEtlG2es-Q1-mMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk0AYDZYefVXeN-UkXc51PEgqux9NyfuBinZOzrvGNqD7pymcfxtFh--va9_pEGf6QqIlkXckIh4Ej5Cz6GLn-WdZi_5V-A1W8u0E3jtSRBxn6GMR0H5_Wn_BjUebN8HABha22jAyswl0FBUWcoKtwLmsyddF_k2SJqxcsq-7rP_EU-sWaDRBrguB4Vk6HMswrWPr-dYlUjHHE78GGLZiERpUV9M19gBAWQJ3NkukhVyOW68Yx3HYf7w_xIOyrPXudpodu902PFllZoLnjPWrzyx1K9z7QV2tHAsGHiTwcfrFOEuYTAYvovrVMgCoFUJT3HOwuk8B83pIVcQrD9RhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=SomtcnaqHh9gyrsXcxlhl9iOSWz0gzUD1LlJUB_IX39ctcVVQSb6xoQzDFL0KgoxSSsi0c9Bj9SoZNjsq7oe3zOAy7twKkGPzL3lrspkmLm_K2yVTub5Mdr9WZqbCyF5RHfjHwWSDopABiMCRfPyF6T5XrYNZsOAYogfxZksCmtqagj9yxgAIej4Bjoo5sM6DDM8doxEv-DRODgiu6i5FpZEBIEDBmdChUTTCs6M5h48-Pda2aF9zuhYmb9GPxVtyWyu0s35vCcQ5S68BvSYUEqB1ANsGpU_cQUmiuwOX0E27LvGI_bCX8Llf68_cxsP7eIHb_VvEF7V1nrp1XLARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=SomtcnaqHh9gyrsXcxlhl9iOSWz0gzUD1LlJUB_IX39ctcVVQSb6xoQzDFL0KgoxSSsi0c9Bj9SoZNjsq7oe3zOAy7twKkGPzL3lrspkmLm_K2yVTub5Mdr9WZqbCyF5RHfjHwWSDopABiMCRfPyF6T5XrYNZsOAYogfxZksCmtqagj9yxgAIej4Bjoo5sM6DDM8doxEv-DRODgiu6i5FpZEBIEDBmdChUTTCs6M5h48-Pda2aF9zuhYmb9GPxVtyWyu0s35vCcQ5S68BvSYUEqB1ANsGpU_cQUmiuwOX0E27LvGI_bCX8Llf68_cxsP7eIHb_VvEF7V1nrp1XLARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=vLLXv5A-iLHYMJxKN8Rma9AcdqBSq3BNbUXDcTcEbpSE2gP-voPNevZHnOAw7o02qx8MdrKXf7h1nnoTdr7i5GKez0UHzMkmfQFi2GIi8FMGJY5dlipVtwtnhzTkgSA91Yj8v4lJS_RtzXk0KdeIHITHqZ1GZYGhydUIK0U1ZETxnxa0iQ5OXcaMRUR_xuFXmKBkwOlYL8zanMVsxMtytoYLni5zSjPeFywZR2-89uYa_8o_lkdX560rSXTZRBHuA9qpagky2ZSFUd3Pmo5Kwn6dPhrz_8mA4n7A_824u4ZQ0NBJ5vqAGYHAeFIwxRctSKQMl-xZbuq0fcVmJ2KGlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=vLLXv5A-iLHYMJxKN8Rma9AcdqBSq3BNbUXDcTcEbpSE2gP-voPNevZHnOAw7o02qx8MdrKXf7h1nnoTdr7i5GKez0UHzMkmfQFi2GIi8FMGJY5dlipVtwtnhzTkgSA91Yj8v4lJS_RtzXk0KdeIHITHqZ1GZYGhydUIK0U1ZETxnxa0iQ5OXcaMRUR_xuFXmKBkwOlYL8zanMVsxMtytoYLni5zSjPeFywZR2-89uYa_8o_lkdX560rSXTZRBHuA9qpagky2ZSFUd3Pmo5Kwn6dPhrz_8mA4n7A_824u4ZQ0NBJ5vqAGYHAeFIwxRctSKQMl-xZbuq0fcVmJ2KGlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=myFOE0n1vALRpSCXQBxbX8pCRvKOXXvpVncqOuMeMcCGgJRhye6kuvCGgF-nhDoRjQ59ps-MZqykXNop6vbGQvgHipmgMhl2DBgiU47YPIHFm_iL8uU_aC1XE820MK1Wz7xR69dJC_v-pPKVxohKm6OLtK-0y0NjS1z0mfpc0PqwGLkjyEfV5Dgd7-eXFjpnTBf78W_BRA7VyzH5PifutWb2nBFIDuEOLzLtQrH4b7MCS0pshOzQ3rxWubmYHaYcs0YOgMiOgakz1AjnWvsNqhq6xO6svhJYgP1saOj0xWaDxlMbQ7aW1PN0vpd-tOx9oH-QMy4J9lw1lxiTBVXztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=myFOE0n1vALRpSCXQBxbX8pCRvKOXXvpVncqOuMeMcCGgJRhye6kuvCGgF-nhDoRjQ59ps-MZqykXNop6vbGQvgHipmgMhl2DBgiU47YPIHFm_iL8uU_aC1XE820MK1Wz7xR69dJC_v-pPKVxohKm6OLtK-0y0NjS1z0mfpc0PqwGLkjyEfV5Dgd7-eXFjpnTBf78W_BRA7VyzH5PifutWb2nBFIDuEOLzLtQrH4b7MCS0pshOzQ3rxWubmYHaYcs0YOgMiOgakz1AjnWvsNqhq6xO6svhJYgP1saOj0xWaDxlMbQ7aW1PN0vpd-tOx9oH-QMy4J9lw1lxiTBVXztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=N_LzMnoo9b4ESBLgPhKenzhF-EqsoqnVloJsUOdiyHi3YeEb2f68Q4PCjKChPwjmRrgJ5ffn6yRMum32ocSOc63WvlwzUmkVbK2mCpTA2olRvgL4w46svhPJkLV_dGxmu0f_MZPNWO9ubZyGP3DmlsS_YNyECrYPOMe5V8pLI1bDGZt60V9cQMET-PW6ikVJf7zVd4lI6cDGh6rUtT_QQ_-tKoVHSLkW94CCYV6qRhKmtCLaKO06LSPBH1b5Ai1sIMH0K6lXcnl6Hd2x0tVGONPxh-H4B6q4AXOWecaLfYJLbtiustRHqmblWnWdJffGNu2mZmXQGmim2i7GN9Chjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=N_LzMnoo9b4ESBLgPhKenzhF-EqsoqnVloJsUOdiyHi3YeEb2f68Q4PCjKChPwjmRrgJ5ffn6yRMum32ocSOc63WvlwzUmkVbK2mCpTA2olRvgL4w46svhPJkLV_dGxmu0f_MZPNWO9ubZyGP3DmlsS_YNyECrYPOMe5V8pLI1bDGZt60V9cQMET-PW6ikVJf7zVd4lI6cDGh6rUtT_QQ_-tKoVHSLkW94CCYV6qRhKmtCLaKO06LSPBH1b5Ai1sIMH0K6lXcnl6Hd2x0tVGONPxh-H4B6q4AXOWecaLfYJLbtiustRHqmblWnWdJffGNu2mZmXQGmim2i7GN9Chjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWEQJJW8UZiddmO1T56YtWW-s7_f6qw7O7Q9mbqGFAYVVpsYXkY9OH0ATQ2_KaZ_zF7mIBxzLbQiqNEggUO1fX68BrfQKvcULCB96jYp98JhSq2u2sAB54ccGUCgwNm90Lm8x_s8-G-FIqo2ujcEtPcMK5KTQpivAOdT9FHTiZKGcd0DMLUVfX6MHsDqe8a-pfSVQGYznkfrGA2dgurHxT7nNKO3dq46VX_sRLSoAJlMoVvnqcInuutGizNOGNpng2MifT1h-i9gmW_lE5GLwZJy-bStotRWXBEp9EnD2zddBdbN80Hz4a-cK-e_yoVpNPx2EQHz7zUFld1XvcWn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV0CEj4zHy4akxVcDydvA4njB0-Wl0Mb5Io9c2eIVdQ73e8CJKb8AqOZrp0bBdsIDkm572BWDWmmc51hzu_DC0L5WJKhe73VhbtrIYj34w6vLuU1PYGMwDi5D2Hu_K6buSoFkjRs1rWERMBsAcWlzhFdlKtVv6cJgYkmFpnBzAmOGwMOAnxvWu1jBS-TpqtJmhiWJXzquqA2YC5A1xAznmW3pPUG7WAiCUqAnbWg-Jc5RIGxz8lYHSncx9dWWdzB7suVJ-L0brPDKcBZ0fuw9R1n8LUwDJ2IX2-mfqdUo4-Oe05dxI5-1J5aKbzSHC0FvUAfk7bHxxe3CKlG1ZFmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSEy9JQ-mBi8cF-3hyR32mTkjrBianKwLW_GS4soUwxRenbluGuu_5lTmaOyhzRJvd6Zb5kyn9ibbNyEAd5aaJzMLAm7XioO7i1qM2h8i3SJcJ7Pbv2PhtLiaSStumAbfda6mk0jqeSxEY0TkZP4NzSKePsTr5_TUU1PimXrMPugQOHPL_1S3ZhACU8xTsrtNtqXzAT0AdV8nU33B7wVLd8qFPsiZceYY9GA7w4kxfeHbz6hrK8ypdiNHUb2Jk26vjgJyldIWE_4LaGhAuaNVYBkCq1htF_NL2_WUmjYvAd-_z7xX6vY2d7dSeJTIrY4VciWQhGga4jQVO8oN8jwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fNiqqlYQRKoLXTYDlyAObvqS_E2vXo5d_ivFaAWuO_U5n8dR0LJLW4kt79dt9FjXqLBCVg6ND3OpUSF4zpn6oqB4VdUM3bqG9oecsujYnVEwJqI1wtTvQop-45qCjXRQfqFe05IsDiYIR1MKfXFZzsa0pkYfgW-33SwJMsT5X7TExAojZ1Bj6N6a0KaOIKEsZPyx0zyTEmZ-TmbN5NJzOKYmXqTmPslrQl9pNdjOFW8w-Yznb13l3-INGH91oZXB4gFvMYt_cOOyLo_yvtu5H_N-7_S_0Lqn0oW6_PIPeTJ_dauBLasnI5a0ocjYln29FzmgdCaoC6eooCQDWmQyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt0elNhBJ0JWPGLDPPOCr4tSKf_E-9W1HJj2crtao329CLgFfGq3_wsuTCsG9dT0yrNTu3_Sl36ybuuMf0_Y3oy5ua8A2hJ6T-aucnnA1zlqg8Aw3mo1on6rR8BLgF11OBF4O5VdSWTM7Pa84BD5KN0amS6r5d4sIdLL37ClXGQ0V8z-2ATgCiD3a5-CBJAP8YeTs41djRSYHxCFRKQzmVXPzkrhH7b3hYWFw_lzaleRz35uqM2THCqRipyWj2ZXei2hppmxPWrNA1Vi0b4AGjy2nAk2ww-L-Q8x-CBVYYOrJZQ_8zpDscz0go7nac65C2IVSkHa3Yu5M6NbD4MK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF1JLFrt048AOCK7Dnqmilk7p0lQewJ_6QiOG7eC1QIw5MMwn0Mr-zv6hxi12UBLJS-9qQ2o-06vS72zQJIbjfmxVPcpWpBEbk3qCsFkUHQRYrBuR_ukgYtDMXNGdyu_IF4V19zyDluu2ASc8JbHvlGvhYZ7mHdAbgg0I7vH7ppQQwkfhxGjTnNCA76RWOqPUd0Prkm0Q84yHRQiaeffVfQbKrCkoVBaNr55r4QKWTViAypxPTTFD06-G97JhhSmC6wYTV4xMDHwuqXVkxJN9wVgniZdsnHr0Ma9jE1ioDZC56kE0cuGcJcLYOycBBUIgJZ2XZFvMjCVMBpZI5Ra3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSwQ2YVKzggUWvdIEik1CC41C_SFowmJn1JUmOZ2yQMw6DqO32u4F7adqL3Lo5LhUnA4xTn2VATyY6YrqaQUI5dV7v558YdYoA-0AvznFcc40PvXmHhXVu1k-5Z7zgjMAs0CcprJNQ0ia37J7qXVs_-wybZfDEqK5GsA0EuoqlG5eRFnKEyjrNIMzGErxC1OIHdrbBfuK_tnpmysEzbNR4-GXKs5XOXhDoJCZP43wuYtvgj137z-ym6USLOcnmZn6_NC_vREUQSC3dwXKNF0v3LQhaIr1C2SKBozbNcqIY5kS3D7z3qKesV0-MyqeMOvwGygg3Pzs9jGOfFxd-M4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iABy9a0YZZXho-0UTZP4RHBjSpy3xqD5cO4gsYiVGjTzVunq9HAwI5QAvgISD1TzxNSu3GFd5Qlp60YUD4C7-sXcCzL0NGtqW5-0dnOHohSMNNPwsuozaDMlq4A-G1b45Y9dGzWcpbNb6tymvdeXfq_w72H87vEvZninm2ZP8JJfh9WVYiMI8hxEHFdzFl-1ciZPZkCJpo_iYlBn7B6NVVnRHo-YwHrSF_yQ-oyD5nSeKvFR8KziCajhWvvHIsbZVsPjErW_Aj6TYuq7hfcT2wy0wtzMZidev3Gup_i6bgVEV4QN6OTHsll5V3ExA9ARdH2VJaoKzwu_9GREFG_JQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWzZ635TkljtpMq1vT3qljsb9Uf_KIAa5Zi_FSzV5VCgzzLBa5OCB234oA90HAkm4BcfG67OITV6SW1iJgQ1E5OgkQW0BhuopAKxXantHeiLuIKKzfcK9bTeNWNXKOmnaBCUuEz7dvLUBdtal8je6Smvd0DJqReOCASglU7_yORBnH688efBUNPKEh8FPsiD2qbPwIspZRSS2TIMxFRbBFhYekkKiICDHhsP31ywZySOnD-V8S1jDRSGpjmZe9thWep2bWfzRDuMSmEdhxL5M3i8RDsdQu5CiQylr6pCkPI2odYxjsYbhn2A6mupgC2WQW4v_rMSWzKL1FvWnZp0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v58681fc6SilwIut1cr1aZTuW6l-7Keo7rChtOfqt-qDRJUjG-KkomROUrYTYRH_J_X28ixPog_BEpADgQMGK5XVpCNsE5xayAu3QgGCoccox-oEC9MZicvXiVW4_8tLHca2SSASc6ZGIi1wjDhAuhBcbtPvukLgyY36VJnvc8a-vI2-ARQhe6ll6OpfDbF7XU7tncWqmeEvqLILcFewwbZUWtnAUqPTsV7KABIZS-wa49FqK_cDmSLw4_JXyob28JR2OJGljnwP-DwCidjM12V9FLrne4-5YOoJnyXOMgQXeD_KI55nC4BxtfaGKgbraDXLMWXidln_DSJPl-iPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG3z6TIdXGt0CFmpFSvYx9PHjBVUta4AU54kcLegHCS7iOZMAfJFLQDi7QUfVtMGSbBJEMFATl0oOsrTU99ZKVUxZ_sc2DDy78xrArWPY_WdpG4aNyj2XvHoHgCxfi4cHuJOJkXPU8Nfn3yHFX3KgIq2KFzRsdDEKZ7iR5OUcpJzDD9BD2kV9dMXdr18-6THEKAyuHl29dVCyzPKictPGTrvBdR9XxNSHPj6p9qf----VCpmzktLeqEh7Z1-6AN4PEBsb7wvKOA1f_XKpymgBapUZ7iFwv6uL-dEJYE1TTvH6B2NQQ1NlbJ37C0b1ulOtdoIKQ0PFikUeG1Ib__siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5tqKT7OVEYfwGRh0tVrmH0B25oG6aTlgtSVHPsvZLlwCN7YLlro2YJuL_0KBF5r3TM94CMh9js4pPKN7huNghxmJOFGCl074Lt7vDz-hcS9OLTseYgdQrIoK9PElSq5OkNkAid6T0eUR5-RpXvkCOWHK1p6GU4NAlPO69V2t84jWBbOp_y-Ff3DpVhMI7YCHKZFpkcFstGv8P1lOWo6yAd4pIgFlAZexxT1uh4JcfIlEFOPzCaTdfNmH9AX_AYgwQocziCNiUxEajBzHlffdF1rRc_gdpj6qriwlR64DAGn37Cs_lYsv9Y0n527nxn45i8g23kcUe50U1slt-YlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiejA-X1pmUUTdpNHp65kRbJWMsWXFkjOnUtUSxI66DLR-hkGnZ5Zxd75DhckcOLb1UAambnf5Thqiebp_MIOYjPcEwddn6oTDdhDPPi4G5opPanyrgYin6WS8e-8qRymKCmYKNk2q7Zb-rpOMZ2Hw46smxckqThwfI8ESnotCI5Z4gfdDDO9j41LxvM8JORD7R1SY5pLoErdLH_aYIjS0bYXL5AbxFXZm8j8d6KcqrduxGAbv3fFxme7vy5LMaVwnHCDo6pQGdO0ctKbA3HytR2WGODFqBdiHpjHHAZ7Iqrwzv5R7CqEZNF2o-zBkHO0wx39jXX2VHoenucwZp6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF7WZRqY8oMm_PUbXBHpwECKPrVimH4O-5rbTTDJWDOQc4QmPIldluigBLlfUaXVJuHc0dn2Euin6ZXUw6yrQivRtM1VHzZSMRHNAZ2E1lOTfninDHfw9hKXignIwCqhGSt9wZVLD4iBks796ASjDwGeROLWLCg5-Pz0l1wgTRh3fDVTUlY49LP2zK8Q11GhwXqv6txprOaaQP_Y6D04XFKHK86ottYQ4D7Y6OTXmUcsR0Y_7hodJt1difp5NXDMMWLlh-7T91EKtSw8uOI5cLwh_GvcnAesMRf2FxhCtfTs2a4E4fCxqLjyzGSf1Uv50ZZ8Y6EmAzhN9nI96IZolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=gp5LT5ncRGstHTAaFsAy-O3IiOOidGD1HY124F0yFcgfhw-a9aGCv221gtoZFLHG-9StzCypHjUpqLJOaHOmsfO3ncAM_LCEXKZrrLUbzzgdCMDrZ10XaweeHXGN5BCK0lf9MbbW4fSWOtFzN67UF_4j910TDC4crGf5YT3DaL1t9F_rYITbZ-oBHrTecyNyMft2pccT8FN_p4OdJHYDCEa66ZuLa06qGsK-pSFCmob5AkLH7kktj9vLThe2-9IXVnkL9UI37v-2l9vRO0WHghmvhYN29kYz447WI4EKOaS4MRceJvhNCcXsg3QQd5Mjsbqa1cyB_fa2LPoe1WcdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=gp5LT5ncRGstHTAaFsAy-O3IiOOidGD1HY124F0yFcgfhw-a9aGCv221gtoZFLHG-9StzCypHjUpqLJOaHOmsfO3ncAM_LCEXKZrrLUbzzgdCMDrZ10XaweeHXGN5BCK0lf9MbbW4fSWOtFzN67UF_4j910TDC4crGf5YT3DaL1t9F_rYITbZ-oBHrTecyNyMft2pccT8FN_p4OdJHYDCEa66ZuLa06qGsK-pSFCmob5AkLH7kktj9vLThe2-9IXVnkL9UI37v-2l9vRO0WHghmvhYN29kYz447WI4EKOaS4MRceJvhNCcXsg3QQd5Mjsbqa1cyB_fa2LPoe1WcdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWnK-g03zT_S8qHnH14_ow6VZzCkRzMYa-PycQJz7RyZ1wNsBymfpc4G1WYagUo4bo4CZlr26zGprNMG8uFjmuufwDpnfuM9oyqUR9FEwLBysWxinIJO-C7KUMOvE2N_2eVejYkt_T-3qq52mnmAdsvQN6Fglks2D2vLEDnfnyip4aOQI_4uM2BeIgONTYSJdZ3fU21QbrDrWyhYQ_l1LCuoXVpujJv90hrp5Ul5RRQ4-bwp-T19ozbOYumKipc9G7F33eKZ07TIZ4kRj-W_i2uMDy1pu3wUvJmamELog0JquCjeLNDI5fFkZg6ryjeMfM96nUvgn5TTaNwSmwbXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyiIhDBuDMni4s9aPk7yQLo1cQdiTKmOSFqswXICwBs41a7Yg2yY96ycGCP-DTmfej1UqgL-ENCObf-XRvgYM8EdlhqKfoW5LcNj1dpvMNnU_WXsjzypQAj_20pz0alpFZVX90kBnA1QaQ_YJtQiNPF4GeB1ruuYo5Z4rarFIizBFr2Ah-vN-n4ltltg9AHQGFXy15t4PqLOGdU0i6qQhxneWJ6Xm1M4aIYXwLQOydlehtvleviax6FbiRz2Ggi8sWHVcfJ48itNDdUYOM1l_vkzIBG6woHzzqecDsm6CMKuwMAFrQ3cV91Fb_UlmHZCr0odPfbGJmuHnK5g2lS9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMOsT-bh7Jba3WK0NaRrl1z8STDJ8bZvgVJvxuR6mHbswmFxLDfxRFbh8_t6jSidMKdpLxlU6cZZWQyWDi9PqgPQ7NxXu5KRp0_pi9eR9z252Aly4SRbIw9DW2_LFbN0faqkgSZzC2r-lhL9oB1ROz_Cyc2DNhfObTqYYcMNrH0OUFj3gW2lRKsdXy2PXn5vVfl2StL5HKkSdBQl1PDvrPrn1zaZ7wkuo7F9jUpydCc3jQRf5PMGKQLQywxCxMNJsfJcJApVy8aeS6gDrW7isji_WcxhJmWYQQlCHyrgbLB37kPH5FEcT2LINiCDaM-LLIrWwcyys6Sz5rVvieOiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYy15odgSo4JJG8KtBfyYVpNpE9ACW9O0ZF9QJwDUl1NUdyCyaI7HS0rZkYkvHO5jRZXM0LT5EdbZFuTBtmVkoM1gnA3gN-aLzeS69g4lOGjj6KHWFYxw9_0LX33vLgbhYjDbUrpvyGqzmSmbJTlCIH2iVdiFn3FnxBiF5eyDLdR6RVw99m8emAPhMSdzrk65c4GmQ-qIzAb9xLr871t2MLqlq43epb47DPBqtD82Pst_Vfpt36kFdJZB-6PUKWvmC7SOaRPZjn1mhxGCfc2Yu8ZfpGPkqcz3FmTg6GsZ5LEzAg83NcIbahsXGnQNHEMegPIAMmzsq4qzJIqbI4Xig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7d8kDYcUwO-KrUFAi3ckTEw6yLid0Av667Wudyrh0lmg9yXySN_SnKsTM1v9AVJSmwV116ONjGdNbEAlaTgM3LtXFxuo0vwMsbLcPbK1S42E-v5W8tmUpWAXgM2R3skk-lgsR_pMo8zwXCTJVAZQMqFM0BaENtyFCbn-1vPctX_Oeso4x_w3bF3gDovTCrQNiLlUJsoHEMySW_v4MhX5sp5bdw_f3eXG9qpz8-rLsvMSEXjPHRyAtMSyvlaNh02vWVQdRserEdZfmGmgtVmXveKypgrw00kTcufLHmG1gR-kYV-iKcn_zbfPbB1FhjGSjWP9piZbuy4iluDWUEquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvlOpXyDSdx-x6VxnVlVUANP1m958E_IR1_GmNe-E00zUX34KD5YF3JLYOgngxsKRMxPHfMd2uiP_CIuJf-IB7MfwZAMn_YfrSPMqVQunaLM4-EzgGnSmKxIxCED2TUwFPAE8A8PV9tn1jbw2N1O01MzY83OQKab_W_PlGF4hmJTcrjF-PylTBPMuZpDvdbtj4RqiY6Xz9Ji01X0bvFYnkvDezsiOx5NzvOZsPM_zR42NWbWx4X6f9Q2eSblGjm4Qbg5_SqWdQV5enq9OPQPRzY2L5ygNC9wr6RUj0hCWzYEoI9s5VTXAwGFRWFlWptEg8okUWKqGPW7Xze3zcRQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRpGm70kmOmQeJ65auOiDGPaG5jS3KLXul8VLj7MnmKK22s7sWs5E-HlnYSqRshD6f0EvPK4e3_Gx6wZZtM80mfFXrIAhlLeeqFJalN68NijY1CLo1DlHpSo5ybNeMp6_DoKVIouKa52EMPdXVTPAVtF6MSUCnAfeopoB4npGK-mvASYccpEBtn5GjiNL-lxXUpEpUj50qUWvHADZKinKLQogxUN84XRvuIsABm2wC6dada2lBhehuR-I335RmrfmiiiSQAcsR6XfQT_EejlOfHuVH-sVtTbjyAWA8zb14sdkLv5T8jJYvkPNiqUhtAfSZLLxw0MjYEL74YB88LC0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvfN7X9h7uh5GYirqk6PezXHHguPDmFMwMQf3OS-TscKW7TiJniYOX1jJ3oiWjzwLHYqfMkl-8xP6_TNazoQIR_zIVV83hen2NX1sePdOrWNppQZh17DVGnxv5YmacdE5NkP8WuP8C85KV-_lRggOsQQ8Qq86tsCBeB1Sm4Kqe1pGn72vj7GizHpYXIW6fEjX5hgayc6kpEUJMeeNWx0cXm_9MDWlJEbRAd_PQOOKseR1FdGd_rsYqMZwhK5FnyeYGZLtuL1hee9anCuaSsfCs1Xx-TUk5HjjS849fGTx-UNclKwhD-V1qBWUceg87J5k4QHmTM9gCrlL1_Tn5hiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=Y5xUbMtByB3VdIlf8Ovzsi1xBubb6MQ7NnOjjwxeTIX1CAHacZVlyuYazJobBHi30OfzPCEv16EDWbD44cJrUR-6KWoFIvs0HRk65yZhaJ4GfpmM6m_Wc_gWVMa16ueadQIINdOIGExI1HbVaIvZdwnbzNa7yVjGlu_XSR4AavlYugZkBnF2MEejPKfDUxsNj2VwgaUmaTx7gsK--mZl-MSqfRReH8j0LFrZY0W6TV8gsKIJBcuocsQlIRwmGQ51SmQshrJRNLLU10Xwrhoiv3EKEc2RakGoTmDk-9X8vbmmCxEokBEJpNjAtTe5U2EEGQcQ29gCOgqmq15EVjvh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=Y5xUbMtByB3VdIlf8Ovzsi1xBubb6MQ7NnOjjwxeTIX1CAHacZVlyuYazJobBHi30OfzPCEv16EDWbD44cJrUR-6KWoFIvs0HRk65yZhaJ4GfpmM6m_Wc_gWVMa16ueadQIINdOIGExI1HbVaIvZdwnbzNa7yVjGlu_XSR4AavlYugZkBnF2MEejPKfDUxsNj2VwgaUmaTx7gsK--mZl-MSqfRReH8j0LFrZY0W6TV8gsKIJBcuocsQlIRwmGQ51SmQshrJRNLLU10Xwrhoiv3EKEc2RakGoTmDk-9X8vbmmCxEokBEJpNjAtTe5U2EEGQcQ29gCOgqmq15EVjvh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFfwTVOQkY-SIjDheUWaiGsT80n8x2PJW8ccThVk0ucMLTMJS7Q-6-W-6wtX98vYlJI8BqEmtHMTJrVK-Ep9c6ngx3JCHwVu1Ou8S9djbGTnKU_LOTzaxuFBZXMD_PpXKQMwCvqgWZ08O4mHl2uMnydN1e6tBOONq3QuZPGvPrJfPEk_PhVDFEodOFMxp_4zZyb8gstuIwhD1MxJ0mgwJXj9IScw_CvdtkPCNCeFeWLn3QBKqEVFP1cGhs8lGVQL_edeBLikVwn57tY-JkpqdSzIJWNHs3O3MNNzM7QPuvPfOGmLShEtibmjdBfoIT-USdeaglEMXrmXz998kD_KbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu9nzYd2ZtOHSlJJvjTy_0JSIZZdG5ze8vCWf-Izniphe62T3KcC94uie6RAhpPxFRbnBXv0MlgjiFHX68vsQGnr3-5EWfRd6WawrWakUwEec_AhQwaRQOLUHtxpYv_6H2MpVTtLWzG_1TYx67hrryVqHFO0ckvIZgFozoKANOeFrbNG2vrW-FgRuyCVFuUr3Um5tJXMrUgDg60X_qz0EOD8U4QW6fTMqT-vxSi2qJflXbQ3jrDoLyHbhUbqOWJpji_hKf-FfYZCXuAzvWuCAm31JGQ9lDCVtuVNg7LyuskhPXglJDUKO_wvefJ4tKCvhAQ3kgQnQeuwAfojbS9p3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFHZU8ebiGFOJ0TPf9ZJ04tMi_a0aAe3LbIQNni8jTsWPg1JmsCeaeclQDJ0ay3P_0Q432SengswdmKTOpyQKnqVgktHz8meN9PibFnwBB0ZfK9tN_G5d85JfWz3L-zsG2w1wR6gCCTyI7_QD4b6JSVe1kUHjZmO5elUlsFFZUUf4BvLras2ZVBFhD4R2EmJqdbq6FJykkVYB2R8GU7gCJfE6rM4NUaC7pZgODF8PEjGBiQq7nxd84XBx4_i-iO4YwynYsMYrlAgKZ9CHWPwZ5azhaFmAtdYw47Blj-5kmsuDRCGhMucJUX5jdkCPqdMd2hryVdQqYNGPC8mDaGW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miIxj9gH8EqiG30YSyPalbJBfd8Z58bxmK8IQR2e0mzgPks_01UfrV7NvbykYRKjz0TbPsOHkiMaISIpKl9OQBvTQ7tXnZAX-SJlNKo5DLEvDsxgYLSyO9BYuWe56Lld7OOm9hpLfiwEfBguCcZ5q7bxR8d7kU4YtiKJS-CoW2NmTjWtTqWe5UYb2cEjrXchFk7V5k1ARmYIqIIApqj2MPSpGA8T2VKM8J0deWY-v9z3_xS6c9D6uEWvx570eEig_QsbyDLeqRB3F2S5zGwVhMjMSaVUNsd1rEn_dNSgcBpgT6ukmEn4YAa1qxrDhMxT7r5ClRiRqXrufIEQRsyC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy1whp6bXz4JYbC0TuFcKnqayV6ZU6jr0ZwAeadPVmzjxogcPc4_9UYQQiApmO4T_si2_ArerlMUj--gRByNplR3eHvFv_arIdaiyBxqTxqunbfoJLlLcMu4fw1PWsyXQBOWtN8nZgDbQOFOjczO15IufGoiiADKBHZA0TKy9Rc5qTmRJqUrEEpv_ncZwuulYvp5aueja3uS4Qq7iQR0NQOLnN5PhzryxI5Wh8ALUFEEaR8DlfHZquozUV61d3aqkRCU-N8vOk8aqfjcPnJJauef7QaQOdoPOUvxl0oQPnefbDLiJ7F6QkD-vRONFyOJKt3F936wVn1IN90TeVBjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZqcAnUAC0ukPukSZgWB154LNMfD_idvOyyDo8K-FYDmwamj766FCH49RLjBIdpDk0WK9xQJdKYZbkb9U9Zw9zOz29PGBoTD2iFuECvgi_5vpahXbW8avPRMbycPiW1X5lL0eQiDGt3In7oDgYvJYB1oLczF094D0xltEVw6XzqoluvXU-lYHv14tVA0i1miWnuv1T75mL1oe8xgVJ0pzxHTbDVMw_0pzL1ILJPZl-xwmVt2ziPa7Y_Z6L2Xw55KajTLAm-9INC5zLgSatj_UPH7xl2XeIkoxOwsTvZ7Ogo7etfuZPDDDr3clMNF4WmyNPrJO1oKZtV0aZAvMOzgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8QOxUCKLqaPST61EfztqGuCBwed_AKz48V_4mCYArCKbvQxe2R0uWsNq1qPNRM79T-LrODdTYDIZZtxgr1xNT7lQ2w6Lq8wzAtktRSURbNzHFLooMXxcUF2edBn1LA6MxoiGwjgVTwJkk7RrqHs85-2JDX9YUMPtNYEqAFiquzAomAzEwru1aUUuK7AmgbbIS5ZN0Lksi41ulZe0k5-oFi42p2RcFK5yUV7ElVreYm6l_jyJEbU8edrI6ut-KX2JlbRn9Rb31eBompFyzHEkJty1_2XsYdpxDehF86bdFx1e1Nhdl10Jl6sLMnc4dwi2x1xdYffY3rfmERcIVBEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=GC38do7tvEgpSuJYnU2uIasdYbjHq3SYXlzljEnZsXgerVcGZW9_J6u5jODLxBUj9dsGEgz5iiBgk-KrmgthI7LfkLNW2EqPST1r2bvxOpDzsq7oJ0iO7qbWa9lxJtKbI38YYN6_F4nh-yBjwDqLewWEIeNy2mBus6rfOGWMnGSzw2OfGjZViXlOIb8GrY8toEQyURjsdDz35oLQy1ADizrUmpuolEo1OP32MTNvMH4w4KLkoNSCcGLDR-GN3WEKGVQsDgulGdrK3xhkjWBAuhBkWN_I_CCQcLk3KYudmks7uiKrIEa-oZ9MsVNKCDSyM6RDfkJH1lOiMSp2IIxrRb6_h2Xgiu7rsjKNM9L0VVA-3BsH5J4HFp4BIpGDHfQwMFw0IozDvyRBiiJv7dydOLMqYkDSVPVelfiVev8sUgnaMFmGMmRpErz75ubNJaC2poN4y4jrLu1ogNYGMz_zL9fYGhBp112M_vqK5_58hBV2g8B8Hnz7rWISX0TrV_V2SXLXI8Gs9z6CjRDSWQP8dK88taoLUMvvuY1HC3M0BhvWnVq6m_viF3dcuTCJcUL_pU4GtGcFCPUeuXxb4rMeWtdzoBN9-Fi9VFIjD0ibfYqkSdSHa3BlFyAXlP7aw7LbRy7vWT3NERKiAywYqB1TefPM9nyIc2J7njPbmvHVMls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=GC38do7tvEgpSuJYnU2uIasdYbjHq3SYXlzljEnZsXgerVcGZW9_J6u5jODLxBUj9dsGEgz5iiBgk-KrmgthI7LfkLNW2EqPST1r2bvxOpDzsq7oJ0iO7qbWa9lxJtKbI38YYN6_F4nh-yBjwDqLewWEIeNy2mBus6rfOGWMnGSzw2OfGjZViXlOIb8GrY8toEQyURjsdDz35oLQy1ADizrUmpuolEo1OP32MTNvMH4w4KLkoNSCcGLDR-GN3WEKGVQsDgulGdrK3xhkjWBAuhBkWN_I_CCQcLk3KYudmks7uiKrIEa-oZ9MsVNKCDSyM6RDfkJH1lOiMSp2IIxrRb6_h2Xgiu7rsjKNM9L0VVA-3BsH5J4HFp4BIpGDHfQwMFw0IozDvyRBiiJv7dydOLMqYkDSVPVelfiVev8sUgnaMFmGMmRpErz75ubNJaC2poN4y4jrLu1ogNYGMz_zL9fYGhBp112M_vqK5_58hBV2g8B8Hnz7rWISX0TrV_V2SXLXI8Gs9z6CjRDSWQP8dK88taoLUMvvuY1HC3M0BhvWnVq6m_viF3dcuTCJcUL_pU4GtGcFCPUeuXxb4rMeWtdzoBN9-Fi9VFIjD0ibfYqkSdSHa3BlFyAXlP7aw7LbRy7vWT3NERKiAywYqB1TefPM9nyIc2J7njPbmvHVMls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=TYKis6BZg0b6SQOjtblHUPaBnJlTei9kgJeQKfiFsaYJzHuw12xLVw9G_8Hjv5l54TbnzoePz7lLNqhNV6RejF1Z7Aos_DOVmAjTg8vTqGDt7laHlKSId8Ep6H_WLw6YsTh0aJpT2GO3TSP7JNu_uz4kt4eMit-tXJclKicNWzu7AuXDtjqq9hDPsmG1SoxSTo_CHStOKyQsImanTEQD5EeSn5hSrYAQ3nksjJ4ym4-AQmrGY0RLsiHj4a6wC4gXpQoSwHYaJJpR1czzLpFnEl5nrNYF-AEXDPKIsYhnocGkdiyQxZD7B6vAzi_t9C9WTIQba-uq4XrozmBeazkdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=TYKis6BZg0b6SQOjtblHUPaBnJlTei9kgJeQKfiFsaYJzHuw12xLVw9G_8Hjv5l54TbnzoePz7lLNqhNV6RejF1Z7Aos_DOVmAjTg8vTqGDt7laHlKSId8Ep6H_WLw6YsTh0aJpT2GO3TSP7JNu_uz4kt4eMit-tXJclKicNWzu7AuXDtjqq9hDPsmG1SoxSTo_CHStOKyQsImanTEQD5EeSn5hSrYAQ3nksjJ4ym4-AQmrGY0RLsiHj4a6wC4gXpQoSwHYaJJpR1czzLpFnEl5nrNYF-AEXDPKIsYhnocGkdiyQxZD7B6vAzi_t9C9WTIQba-uq4XrozmBeazkdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq4OPadxqS7mzBbyJtvcRTZP6mwKiQeL6NNuKfsVcycFwa3N_UNDtp9NRAD3qtLEb2b4eMDx4kQlh4ncynNzJx9acVa4b6UdxP_3Lfebr8rVXA-h8LLcG0mFxc0eHJmTVmHDbBDeEBIqZKcOl_GK1akMA8qNTzbj9rUi7wimgcFc7XGXfbbLX8TnFDXMUr216xXj66m_vg52wksqXlVCNd2ipXPHYObR5Qn0rd3ekBcbXlKOrLWJq2Dvfr9epUqiIPvwk3b_fkrXS9OdGA7zgzsbas9NNqgxkKL1NfqifUIGcSxdyi64X0ObBnAHVZnYFywoQNOUwmXLYr1-7B8IRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUGkyvPxSqFkpaNThjC6aIdOXwYg5UqyV6OSTCF-zg73wj4oWF7L6QNgu7DU2xiWhRRN_ngusDVvEqnAX8hzMa3IwnRCcFVZ1sFaCG5uC9Oics-T0KI2UeSCG9R4DF1FQrK7CyVXn0OdUQ6AUx9YRfwhWkxNxljM8fOJCMWSpQHt-MhsUw3h_nvhavY3FaN5RBPEf8JJNUt18uWFN1cLjTpb0PNv6ARjOMxSqLVKH3ScE2DS7whW_BiFXBcQsAk_yI1X-6RvDgTi9Ac0bA_OENVFzfWCAP_WNex62uXgIUgR-QtZAOyJmGu8bhNwSevdo_QXd28_idbIiMRK1IQd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=Hdw6TLYiUiNcKz20WeBBhbmhJtGzcohQDUb9lx7pE8Aquw19zOWX2zFiu1pSiAfdwPZ_lmWw0H6ZEcuObHfVrs6joOSdLOEUsG5cwgPo2hq_1rQNTh-3NkJL5XqGNW1G3juIa_7v05Bq7VYSYqqqeD2TDLZ5H4OZmkJ-KUN9r3nehJ5MNMHX85ztINIqrx9Eds3Hfh4DHky5ilIEGRJCH9ne0_e-dPUdbIPLNvIeE-C9XgqvKWdxoLkSdOpPtbqPXfsYRQ599Ni2UilB4Od3EYs-KryiGzQUfUc4d1-1Zf0oTquEl3hTIhgRqZsSj6uewgIHrQmt9FP5aEpX6ocRljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=Hdw6TLYiUiNcKz20WeBBhbmhJtGzcohQDUb9lx7pE8Aquw19zOWX2zFiu1pSiAfdwPZ_lmWw0H6ZEcuObHfVrs6joOSdLOEUsG5cwgPo2hq_1rQNTh-3NkJL5XqGNW1G3juIa_7v05Bq7VYSYqqqeD2TDLZ5H4OZmkJ-KUN9r3nehJ5MNMHX85ztINIqrx9Eds3Hfh4DHky5ilIEGRJCH9ne0_e-dPUdbIPLNvIeE-C9XgqvKWdxoLkSdOpPtbqPXfsYRQ599Ni2UilB4Od3EYs-KryiGzQUfUc4d1-1Zf0oTquEl3hTIhgRqZsSj6uewgIHrQmt9FP5aEpX6ocRljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg6pkry5H3oK1PqAT-_FYJHHtL3cX4_hqcVOy2nj3VyWoVpzTKRNkHOGBXPz2OBKdNJ0Nuw1jOiLhtKm0xau0gQi-uvXOvf72eqnuJje-NdgmZhGykY8OoNQeHx_RkHYE69ZsDppVb_V-5W4KHjnegmgYJhjVn_BXNBpEkd-G0a8T66H1Tf-nxdYqMLOlOW13Ph-rbOaWvy994IOKuQydHPHZMLeE5hLrjP2xn9iUujzlWq-wPm652XtrAJ-UINAhUr53axZJTOiSFS-Ka4wQkgPZVh3-bGL-mPg_oRekYcShrbvxtfCYEDhnNULkq7dMDNwoSLDLgzBpcO9AayoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmIjuPCngbF8ijWg2YQoGMiMhyGcfLZt8XMhRK9m8bkAPW2dkRFqseNDJ2kAoUD567DkGIrtephfAmyaMaBUsN81_619NTOm785iCcyXadRMDmMnbGWoQad1qXkMnkqDM2HxVNzOYgf9DOTkWwqRiY7_W2-pdiYoh08YEakakCDwTRCeYsqlCI9jEmEflp060gZFlcLyN3qmtwm86HwrkdYAoKIqxBszfTws9pQjHRRhvwNer4G5d94h0L4u0u49divTwmoyw9m8Rz0DpZLX83pSjzELOncJll3a21vmILM0m6GTFCvZA28twkd6XSKTlbuXEOm1rqSjAFUBHdvZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCoa6Gvlexs8Tft8IxTOlWZ7asYuRxYRh4C7zCymEnltMDlWHpWjyakKH92Jmjm-lPQ0taKZV2e04Q9EIFmEBHIiI9vl0dUAEKF-LpPXVO08OwOItJ9lofS3vbpLvlz2IWJiR57fyYmhqK6fkd-mBhbFj0SBqFZb02hDtapSe2tWlqLNLXNLDDPH8j0ekceGjRkgu3QhLKG6XSmPbvA5-8jshLw9HmzWGCqkVcVZqQRfipa9RJ3Hq0sryy1JIrAP0H6VrU8DcF0ryfY3MW8k80xrX77Deo4QGktKZLLDFrvmYAnwnnQQc9Je9uHFhqvz5ZM8RWmvkARbOGOH_WWOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R17eHyTJz4a6bQf-Y7Dwwr9ZfZ1QyfFJn--gy5R7SOkg-6Cwh93inaHdjTYqzDcYhsdpYSw5Xtog8laAXTEVXPT-F25TZ0QA9gEoj7DiGYoBRpKLyVrCBi_1lTU9p4hqSH6VIE6Evvqc00Yzm2Ms6inpUSIyBP0vk1P4JxRSq4HzQ2gW17jIq0R96IMlLwdrhDKjiwirueon2fOO76G-mJPba_SN-quM0vuw4F6lK6NPOBLxZBqzoC2cxTInbf1Y_eWrHJ6QNin8i7g4ZUFAV78PS2vY1UWqJW826Wkys-peHlku-WrjjujhaWiflL0ZwKfD9vKbCOyq6j8lurlSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_NqyspQxhbodw5AVVIm4Ax4d1isj2K-qiWQjXKfvRsXuVEmgvOEfOqK-ILM0o5QaPjepDsbssjJLetPOJcwDMzxHVrzIMpHqzczvWfaQSY_PYwJ2R32BIslKENuBP6JBtxEDcuKBq0vf9uLWrLdh1qpiTRLcRGeVdftyNL-rcrEvsA2-qd_TjrXWyUlKDoObKdYJrbJDat8u28o5bCp6ZfhQMnNsozkx50DSlJlw-pXrEp7q6hRtkOvhw9u-s66fxYddkmmvCTL6onYVEpyz6mk9Ybn_5RxqZRxHDyLPD25XXRZ0tAt6wmGpQFJ5zZl1C_dErOlvc8NJXCW9RUWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJYEXL6gos9HncLEr5FmicAx3YfJg2JgT3AlZ_FDoSP_V1j6IwRV4XEW8CO_7jvAG1AE0sjP6WFqgP_fA67agaxcaUbaaPoN9jGozkOvYuSkPhlLjpoSyxkHLHqydqtMNIKIYrnS0F03fipDDynLWXYQPrjd9Bs0gIu4Vuf6vf6dkAkP2JkPsf2tds9bpeltaxhUJNhr84mNdnociEyzuF0E7dQAsNkGKqEA5crd9kVmH6GievDGAe76NvFJ1qR35JpJrIBmWc0_aXP3Mbp1LWfb4fEVuwWfef18OhuO_2r9PMG8bYuhYYiIkRicVtqHCVRsdNYhpUqEOcC5hfm6hFN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJYEXL6gos9HncLEr5FmicAx3YfJg2JgT3AlZ_FDoSP_V1j6IwRV4XEW8CO_7jvAG1AE0sjP6WFqgP_fA67agaxcaUbaaPoN9jGozkOvYuSkPhlLjpoSyxkHLHqydqtMNIKIYrnS0F03fipDDynLWXYQPrjd9Bs0gIu4Vuf6vf6dkAkP2JkPsf2tds9bpeltaxhUJNhr84mNdnociEyzuF0E7dQAsNkGKqEA5crd9kVmH6GievDGAe76NvFJ1qR35JpJrIBmWc0_aXP3Mbp1LWfb4fEVuwWfef18OhuO_2r9PMG8bYuhYYiIkRicVtqHCVRsdNYhpUqEOcC5hfm6hFN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnAMZ1hJzmaRu8QeGDEVmqOPkJHw6w1V7YQPM4urOhQkaUoW7E7iXWxiJtZiuarUGnMqKlTpFqI5uY7UZKxVMlQDgDdJo5EDxITvu0OVH7AaYawbKyJTJSJSLPmPY5hZFQhzFKvorXZZTRIYhtAuR6AbCtPXUObSICj4vf2auRT__30pi7J5htXfSAHiVpsQo08VCgaXHhGCKGDtT8z1MVj_nvjUXEeGzY98lgmKLhIP6BfGj7lwVnS4An6FpWYjxIUPJKjFI0TWngcQ0rUyOftMOUrui3x3qRcf5uIRnr7sfJIXDz0Jsk4Ku0rRraHUcZwXEpC2ST3fENtlzuyJu93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnAMZ1hJzmaRu8QeGDEVmqOPkJHw6w1V7YQPM4urOhQkaUoW7E7iXWxiJtZiuarUGnMqKlTpFqI5uY7UZKxVMlQDgDdJo5EDxITvu0OVH7AaYawbKyJTJSJSLPmPY5hZFQhzFKvorXZZTRIYhtAuR6AbCtPXUObSICj4vf2auRT__30pi7J5htXfSAHiVpsQo08VCgaXHhGCKGDtT8z1MVj_nvjUXEeGzY98lgmKLhIP6BfGj7lwVnS4An6FpWYjxIUPJKjFI0TWngcQ0rUyOftMOUrui3x3qRcf5uIRnr7sfJIXDz0Jsk4Ku0rRraHUcZwXEpC2ST3fENtlzuyJu93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=ijs22ztVb1r1so3fFHN-MDz4BmEESvkxV3yqotUIcyldVARPVXyrZ1fm1xqHjOPQsWhtG0yFWKDgP6SwZN0TaYLIKxn-nvXaAX13_k63mE-jqsJFwynPYUxuAfLUDBRSkocMdwhaDHUZBC1661Jt7KblPGB2wNWpsOgbhdVzIFJOVM-QY_vIewfTX1I0DU1Z-d6TG-PKEVdK181POqnqaeijLCr6EgdhG8XldmbG7ut67XCU9K2bK-kSGVsAiim3aoZvyvLdkpsEX5RTzbtxCJpdHPo9epJ2uYsI_7psutLNTtrHLJ9NBeD1e-CSHD4BHNOumjcbKHMu0dDU-M7m_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=ijs22ztVb1r1so3fFHN-MDz4BmEESvkxV3yqotUIcyldVARPVXyrZ1fm1xqHjOPQsWhtG0yFWKDgP6SwZN0TaYLIKxn-nvXaAX13_k63mE-jqsJFwynPYUxuAfLUDBRSkocMdwhaDHUZBC1661Jt7KblPGB2wNWpsOgbhdVzIFJOVM-QY_vIewfTX1I0DU1Z-d6TG-PKEVdK181POqnqaeijLCr6EgdhG8XldmbG7ut67XCU9K2bK-kSGVsAiim3aoZvyvLdkpsEX5RTzbtxCJpdHPo9epJ2uYsI_7psutLNTtrHLJ9NBeD1e-CSHD4BHNOumjcbKHMu0dDU-M7m_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
