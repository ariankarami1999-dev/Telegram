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
<img src="https://cdn4.telesco.pe/file/M_53fvqR4SmW02ZuVZ_Wtgy27VeNp9vJ-iKO1VXRqzKXvqQA8VaRljANNKvkGpB_OmdldKGVZuDmua94UcF3ij9h0HuqQAu0wnDHE9DEBaGBJ0tYVoRYJ7BWb_AF4vqhwNtKX97zy1UpraSyV9zGxIqFwoA-p0qBsWTzWiGjWjDyBQZgCCHeSBVjM1t1O-q2S5a1jS_wdNqh3r65i0kVT8bucG7jAjblEY3rQaFc160PLiJAo5iUrxzV2jFjRwKCosoO8lIVynbXiQhnmfU6aPsfg40z4HTX7-lT3e665FP92o5SBM5Hg08ReQ7yFDQ7XMuyXtAL2Cr9yaJvpX1g2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 11:39:10</div>
<hr>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFgTgBAaDE2Br7NXyrmnp5A7QvsRMXp2Ck7ehAh6P5elVRLqj4DKosPXIv5ny_gZodWWg5Vlp2w-2LdLpg6w8Ey9BOso-f_FOtcjTUS5LCCGQk12txvQ614Jvec3C1oK6_FJjC-JMMpFpqaOwzXq-j7MF8bvs4tqiztpIeR_i2ZGw78Gzgs-DSVzwgbNjCKM1kQOk_Q8twxYata4i2OS1XTBLxgfYLrGIn8PJWUA_vq_2FnvYdkIOqe942jVvaZJqta3eTKmdpUzVYwBDt_LCBn2nr-VsMuDAF4yQwpPthLwrxsBlB76FANGE3ai0AZPiF6hgVrNudc-oWl3gGYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehRwrwTTfHTZEAAkuJ_fPFbkAduzwzO3PLrfBTEFOmt5BGOdngG8rBZIawftJ-uHzaXl7GFeHuKoijh_6O4IM8PYDEeGdR-li8aVgioYJtVRty9JWWYONpLs6vCiY4bCSkcKdX2mvQqp1jTUSHku-RIS24H46sJmIDySazYMPRFn0zgSasgib5KOJTAZ6xb6K3rtRzbGD3BHTGPZzdQuRHKctmL-vcZsWlW-ti7zrhI0eExQ1CwoQLT2nN6NMOUmSpo5Tt9Zzhj2w8Svl5AH5HMIfFPp5jQ43r5Qjs62h9eU3zAZAHlydCvYITWRaEJf9S-ekXkbgBRudTefZIkMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmST5RLWGJmfjAQWAb1iXfv3Tjz2HUDKP9K_GvT4cuqb0eDShKRpG-dxB3GTSdld1koPqljudy4vBLbpWolcDJaivBdxF5DPKY6-KmvU7nAoQS_kveJaWRoOmUIipJoQGALbD_I7bxOeJvMiIQ49YnW7OD9SoIKBTgtnKjjpa8mWMGCXgFXd_SyEwTCzj0jWcCV0z4weyzl-2-wJdzzjtJefxqdF_Ej8I9lmGfug04FQ1IUIMrH7idWoNrWJxIyeygYO1KExQvN4lRoQk9CjaTwj7kp-9nRXif7uRjP8dZhLO4V8Rj8rvIcBaXRBhNZc4fP88moUg8XnyzUY6FzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXLsFA0RZGt9PWdj5DmvVMw-8tZ2nRofxejMiyt273S4ChohX0t2ugsvhBHifwRurBkgA7OColWcxmCMyIUkwdZkvHUWYQ0U57RFE_vynVBTJHTWeCvpx5HTnrrT6X2H5hmKGSxjpckdU5SvKPWSzJtOqOxVG1w9IXV7m4PQG9qiF7AcDFTo2m5U22bGuwZB-9x2VagWKTN_oEkfTc9wUFnMK6OtIpcb1eLd_Y6npSscB1v9W98NJFXLZhEVm1kVRZdBCHipwdIxCVclcMuGkryjF67g3RUxLL5swIZ2lAachyAweJY6dqlM9Vbq6YOXpuu55cqGxvIaI3TitA2wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5EP2OnyGlMij2rSYBkxRh08_WtJyA1bxfO72yfiEhVzWxDhyIvaXMCspIhd-Oae8OGmNDA1_vfRXvJElw3xpUhJ7BrGT161qgwByUl73c6nN_T9a_23XZMAz7-fdCzzp26fQurqE4hjqHEXJhNtkarX0aE9aPcIFLGO7C_GyeCVrUN1A5Aemx1Rz03dF4lCLyTgHGNW8dw-MRvciL15jfALavIR42O9q6ARy7EXD_lRX4MAi9XJ1LETCFBhk_xhkNecClQbmoSOCicKaEI08X_mwiNoDlAoESgTe6z7vfwZNz4bB_cVm8yfyI80Q94MTtvazHgtWYp0wWMg3PJnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpdXBRt1CSn6QUNwzz29hQPSXDZCxjS-8u8hPh-oU7il4qWleb8FfHBqZLpAKRP62ceb9aQMDYYo34vb7Syzj5Ue1cXUj3xEf95Pyn0l1ym4-3pUkEDY6AfJI3DLkKLfjKplbn_lQd3nwlwsIbxgYTJBCoJCh1V6bvSFcjaXerraRoXN699XK6YOqsJNBUHJCmLtvs4VOJb50F5_KMdVl18lFc9L_88dtYVE2tOYwyaj6tBDNrkqSt0B4ClpxmmAM_jb6JHKINt9pKJsMXRnv8-8r2QAxJVbeezzTxB9pUN-y-jqsfInXqb5dcBBCJfOr_c7XaajHfehGf-PQCWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsXETY9c2Os5uLbaTEYUMmg3VBs1qfWDuKWlQ4GzgqstuWHMGxTOGdOxzN8GN8hmmKCAVn_9NQ3PkSytg19P7l0A1A8zi5aao6mehRqPz7GzMfvaGwNhAA9L7Y_d2efvCQ1H5bZ6CYkvS5OsqiNOLJ7alq-2x95CG1jpiaIhJ1w4DH0BK4S1CclLtXJ-7uXf5OaocbybQhLigH9s_ICshRfUilNOPpWByxFCAcocyBLOmeKPBu2n5UDr-USnA_ABy3FT0XGD8dhJXycInTKJmL8meUXsA30ZYXSJx5f96AKA9AYeeg6fUvgVa91euHacDi6AJ3-YCd8mCKKKf6y7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FET_pPQe-gWQJ2qtcQPTnatZu6KA3FrrD7rc_y1QFMn-kk08pjegTUxBDQz39yy0xCXtEsg4nUE_bv6twrJzHbyqvRlh9E7MZ7ybXi0igoO5BRspVmiM-X1g-f81n71Nj85T93dCVTvWqSRotDFQiCkkd-7gtqpcZfIoNYlSpt7V5s1TcQDenNrRuoi9pWOAOVnzLMfMNZyrvTH0hS3f73uLDfCizXcmvmXHh6D_w_FrCODdwIX3kGQajqWn4_z_GXautOkn7mVhow5ZpGV-1OYdHHetDmC2nM9XrM-aBZrTvTHplpUoxYgFC_28yGNQRK3Llm5KHIQVZu14bqejGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UfRfi3FOZ1GcyzYya9K5NgKAw65OXgnebnFsJ5cxk25ZSAwLIMw2WzAF7V2hole-QSrSMbHKWMMJX-4rP5I4aYDYEQ3btSskTZzHzXcwG8fbqyXSw5fTyF0WUc8HJKgsIAbxxhEUSgfAdJoQOkXD1G__XAdcYO2OHcYk6a1P3OAMEKhR5XhtwEutWgtJOfh9LuofCvo1XWSm9xgbDYB3_MmUQiLolsTxN3J1SSHFrs1J51fc2VsAmPFMDLlkeYzxZFUIpX-63fJllht3G2oEWzpFcZSLc0H6etDh3bLc3ZLSxJtcvHwtTfj9aZUxvk_1Ok_R0knT0vUsg2PgUAMBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMlRHsS1HBgRd_I3QocV5-QzFzZQhIDEtz1KEv5jkN0W0mz7rywAb8HzGVETcBv8pvnUC9w690Dw7wajcIkMn1CpqT7W6p3goSzb6j_y1F86wMbpy1VU98ZwDRnYVTxj2cB5uQaYoTCsOLk6Hd5-x9gQX2_sswz-DIe7WnfzRK9AzmXXQdTdQMIh_aI_fgshJMrUVDpPt-p8PkmURswkrhA8XX5PNa912uxVw2zAupGhPMbiil5F8VRxk3HnkU9bgbcS8M7HcCGElFr8xShkWVNrimVcp6TBuyJ_H3WOCzd2_uuQodp6Jc0JazQw56cEAcN4OF8_pfnaU8H7JkWJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpG2BhioQqsKL6P2o8CTwHnuqeYgjsWt4TCMP0DF7mmSGkJBp61mh9bcKoehbb8zpbPjf0HKymrJZd8IknKN7-5kRYqO99T6WxFdh2ZzAy9KABZSi-EZlcTtSR0ge-o5UhQiUH4vTFpWyENHkpS-7EeMq2zwYsfY-qo9kWJC4qCw0umRrn3_vXUJpf0-497XZOCUM8Z2np9kbli9XSDO05nLMJYSA_pXbRUTUdEZcluP0oUJz428oJkRzS6I-UjJh22SmQmxCDDIyhbv9ZRvL4YkUx2kKqoJ1u_JMLIo62TX19T2TNPvEAmvhgi3DJc2UjCBRerbKI8lUmXrkJFH-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3QRCtEULJp9yScrnMsbkGZpOOn1dewPaXIGunmWtBctp2QTp9oXwqgiomOGCYcS5Yb6AIc5cF1TFrdPVfplbfYAhyqc2pM51EBOuT0iZBg7Q23OMqUv1p4ce6qyNktqe6xe-qYN6sSNfBfk2Zma0GmsBspWnZdMQdW454E_gODQVi_rI145Rk4OiFqmOWNLXLKuFlvEGvfnD14Yu82mnZhY5f-IJQ6baNm6r34xW3ZSFgEnWX-F58MHHq5cKPqmfa_K9oKlUGpAfnll8ebQKVAGMsKvwNQFaNQ_EGdUYsWJm9JQ3RV93k5JAqAccMLpvZvMRW2SPkwFkoIqWpvR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=kRizKlOSeBDWqeEz88Zg_cREX5UjX5pLiq3S5G43WyImrZK5_sfs3Hy15sn-Jd-hiLpzDNl9ggio1yHozw-_gvGn7fIc0aUo9RhIlILWWf1obzr_CZ0svrdZHYQ8SxSXpiUYfE8HYl7P3yOSghqW9roPG_eI_pNH1sytDyFpVIKys38fc8PjzlSGsiIKuVAxbgFWoNUcL-LBtOeO-vGcH1DaI-uaoj8H5_Jq6oOlDSxyrwS9jZZ_qWaAK8CpAXSV2hupkVgXPss-hIy7ZUfdXwkcRNo3cx_8aM5eip0ZTEEWFcwQmnDEo7LxIfOa2czbQdS8Yl1N9smmJ4WpnPhUQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=kRizKlOSeBDWqeEz88Zg_cREX5UjX5pLiq3S5G43WyImrZK5_sfs3Hy15sn-Jd-hiLpzDNl9ggio1yHozw-_gvGn7fIc0aUo9RhIlILWWf1obzr_CZ0svrdZHYQ8SxSXpiUYfE8HYl7P3yOSghqW9roPG_eI_pNH1sytDyFpVIKys38fc8PjzlSGsiIKuVAxbgFWoNUcL-LBtOeO-vGcH1DaI-uaoj8H5_Jq6oOlDSxyrwS9jZZ_qWaAK8CpAXSV2hupkVgXPss-hIy7ZUfdXwkcRNo3cx_8aM5eip0ZTEEWFcwQmnDEo7LxIfOa2czbQdS8Yl1N9smmJ4WpnPhUQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJAALwrc6nDCuYRb7v_4OkXUCB4REI6jQyhmNcjggbaANgUvsVzmF9KPfh-1Z4i6Q7hYgRyMM8OVslewLTdsUep7cdLN68Bj2V5Pd89qFbdmE9lsrKhqFLWAcWB4uJBsi2bpJD77a9X52OVLWchzJrrhSDDqpHZKuj27wUxPJL1B_r_AgerCfbc8MmbWKPKT9I9CFF-mnZt4zrR-uCzdOYFj4oRZG42nZaHjpQDlIxXy0uJErtDaehg3BioCaNaHonNgPmHoWCyU-A92nWupAcWbto7NAn8akWnzdIOcTDr_cT6ABrI4_xPkpwstpyixcT7gxTIgTZ3oei6WK3bvLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0iGkJB8A_z1Prgv5shDIYPLISjWbUUg8EsnLpqvvsky576ne-UQHNnoiCCTHwKUakbD2OFa1-Pvdthmeyx8YxgQS9I-j9ERleuKx1JAcgxzlCoUsYpcuh-C-scR7G0laVsg4FWc5UA5kbv5Ookzd2jZAAP1TXzAZ3fxVOsvbR-G6J9g5u3zkRqHjFtbS_1xtOQ13bd9EVvhssjM7L2mjxAcMS4ZwBwSE9cKE2hDRK3Xx_6mCFWMUsesN0PYYQWLDwmR2a9QgS5w6ylCM4VXMINkBB32BjgVeKcKoBLNBwlvgKM5Ejp_y7EFehyvqZVq5pgT8zukxDK2ctIwJ1TJGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7WZmXsoxJzNNd0Ml4nVO7I16gSZgwNM_NZwTiucry421XTTsy2Bt2id5AAn9jox1rwzGuR2PG47KNVUdjluZgQKTDHYVtcqzTY6ZZZcnDvxk0QeMzyj7RMZdy4CzA3iqWiSTKwiNxjYp7ObsWR6Ti0KZPgfEFxRAfwJCrWLowBP6FzlXWcljMGG5YLvxOC0d15PigMeeAXKVHt-6sdVye3wj7fEusuZ27DVQK4pfmCDrgs0omaNEwJH3SahoOc9uZ62SdcIxLcJ_IUhvZ1ktv_C9HZQUjd_xusxnsltGHpQ_2Cml8tn36NCxLejcRZszXBkqhXJaO9paYFu8zgk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DobW0Ob4sM9EhcdH9wscJrvQU7s0ysmoS2YbNKjirIss8NZmRjfcFtTRlxgHJZOOCwPueR6ImPqHC_ydVFldcXED6PGKZ0eN0m-LABEbPjyAeMj_hIhcp7vWS0sg8jnJZ_HZwUnQp_H7ydIiyFwkNBhylcEi4mXmXl3GK35puSibqYreifFrO1ACrYvpVTd9tmPghvQdtjRpd_zazM8XoXlj2bZSRH_et3ZUCMYHhTYzIgGQkR0T2_Qdktqkj3IKbwFAI7GZqyKdiurAPQvLTFfA3SK0SPGhavpwS0kEMYatHOpX0UIbKgBvjnEj__IOHBzOuYd398Aa4g_TXr9ITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck_1mqQgNc0L3XAAsZmmuDWH6V8MFp9NBJILdoAEo8pHNJKggClxWJFHgehWpj8ebInV41rldRoGchJkbBn9co5b-8eiqLeLU95yyQaDOL55wmW2teHTXOThB0VocdGeCgQjC8QJonknGbEexH33iSuC9IRzdTqEmwtkbGhuvinNJqcqRn_ENV9jLfNRxhbXCQEuahYcydW7T_KrortFV6Uwavkh0ZbpaVTi1QldW_E5BFHlNDrbWqUiVtrYyFGBqfzLbj_tkHDSpRXS4sNZQ832Vq3s_RPAzfXbBthZ5I8RopGF4QP1uyhUNbjdr3hfO_QieJilZ3hx3XjV8LK8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9fVZnUwQJ1k-ir3UH5sNBLWYClGlMyPCgvbKQyM7Y02-d5mAKm85yxVVmNiis6kFcNKXvzkCXrV2uue3MxiR7HbmLiq-Qg5DFjUQgWT5_IYORcdhU-IYBN2uoyIAYwJf5Hlmzs8vA7rrrUH2HgtVvW5td6mySdyIYREOR2P3SRtz-8VudeIYtLWoL1ncDVhviT5enZHF67SVxX4ehmh55-2QtVRZuCXjTk0jLdA-dMLL2xxkvtpib1pYnQ_wTp78aEbNEOeraIbwVEg84xDN_9ZAVmlkJZyqqQY0lgJhOn7BTop5MDtQ0gd2_OlvqkW3AOB0lbVneRRQDJEMY-UdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTOHTb2pkw9qiKIgfY67JQe-NjQRr8ktIZl832B9ewsH0PgR6Kde5legtNbqxweDIx-FJn9_IRk-XaohYVzeDbL32fUgJq_BCoc-_S6Q7ViDIYlkyv80XgqP9bAQGZrVgsANizxn9o8W8Olfb6BAGDHM-ZS2-EkoU2a6nL2SlxsmlzXtrDz3OBs97uzU31sZX6-KOIGN8unGNs3HPg9yRyntR8TQKD2CUFquHJi52r2kwAEezrxgSubNZbLHpcyvZ1dDxg20JajKz2QcVTa7jqaWHCUtsUzqQ6zK-KrPRdYeqo7n2MZRzUl9y0YN_2OKFPONw7UivcWHUXnARgrygg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=Z64txz2aWpgG6euoY1I2nYokMIHnvpoEIDTyH2bK6DCpo7p7_88Vj0A7_kLzrM4luqpp0QHlSh2xCQU1MyhLRY4Khi5c8EK6t_5LaNu9I2zwO4hupsg9LfJG7iv35NnIX3mIACBs32zre5fvm4QJ_XyBLUd9OHWO7gbe3GaqHqZczSzLtnQsv7VGCUPHTmdxVTUvMJV8dAXvoO6UXCWPPfcSvZzgIu5jh3jeqjNN54iE90asYV0lY1ydDB4cGmPaxClTnuvxzVU0xEFO3Taz5quydFQHDgeyXxewg4zYz0YJYFYoi__KeJJuobppNfsXMzYKapKxjwA_Gi-p26vV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=Z64txz2aWpgG6euoY1I2nYokMIHnvpoEIDTyH2bK6DCpo7p7_88Vj0A7_kLzrM4luqpp0QHlSh2xCQU1MyhLRY4Khi5c8EK6t_5LaNu9I2zwO4hupsg9LfJG7iv35NnIX3mIACBs32zre5fvm4QJ_XyBLUd9OHWO7gbe3GaqHqZczSzLtnQsv7VGCUPHTmdxVTUvMJV8dAXvoO6UXCWPPfcSvZzgIu5jh3jeqjNN54iE90asYV0lY1ydDB4cGmPaxClTnuvxzVU0xEFO3Taz5quydFQHDgeyXxewg4zYz0YJYFYoi__KeJJuobppNfsXMzYKapKxjwA_Gi-p26vV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VllZYx-eytjAPalRhX3ElhRBgBPY_Ujo0yLKAdnsLw2wh2_DNBQfMFwnktRZqY1DDTZcvzVgTGqhCaFSK4w01YBTlt_HYRDpCix_wMa-FwQ6yTKNjjb_BB-_9LF9WQveftiUSxZ339Hec9wSkQpduTjSMNUXhw5IXhIofVhhoWk9Hmy4G8YKEi-cWUjUdO1cOkUTKfkDkXXFtM9vQjn16Fd7EgDrtDVn03foLXFpVEoD7PjJ2P6n6ggzF0DL8VuddfOfsHWSnjg1X93mOCtIu61v7SpkpwH3x7vbQOZeXP32shb5ma2WLsNPeKjUYCBToyGcb57NS13XG8Lcct9e0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_KmG97cvxBO2yM_XFRS-HikhD8B7_OFPh9Yj2ebMoCL0nyo8KjUb9fonL8vvJc8lJb_Fqvj0xns3xS0_wjzViwp2XHCu9VD6xOmvP5ASwHyNnoF80jkMMNarREbrjtWQ6SHO_fRytOE8mCGYKCBJr5UHfeEGBLsaFvSoF8fvPdjVN9iaVsbNld95kKbXmA6Hx_jXI9bRDyWkcLzPW_vIaqzWVZIkBXTDPA7wJAh2GAwYN2gbqPtUzpIx8cGVQ7ZM7EMZPpV5kGCxlaBXzM08JaF0PrlXByAAII-z9VHkr5SBhy6kGEAiKZ-O0_jD84OTY7ECsiuQ0WxZWuDj4uIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=RmXE_LctUwHxFHpC_-e8hd6KENPTlejB6z3qRNnPLyL_Psa6qZM5FQAiaAj0cCJ8TcRku-wKQdgy2Qkpwk935R0-0goKIZTo3b1__5F8Ji04QQr5HeWaWv8oRfbvfvJEQoc_eSRnNoA6pFadJ0xmxX6Lnd8WIO9IjKYQhDvV3gU7z2p6kZwEhfm_kBUw2gVozd0QaJV-zNX4NW-pY8aYxiJWSCMUXZrA6XJ1uA078dVnB-2dOZthxw6M15VDNgOhLoU0-KXvrEY9DjmC5Oo2FYAPuvDlt3RI7huD5wqI5Iqh6bbGAisZuPMtUR5jTlIOKpRaQqTwtHa6zrDyqwBcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=RmXE_LctUwHxFHpC_-e8hd6KENPTlejB6z3qRNnPLyL_Psa6qZM5FQAiaAj0cCJ8TcRku-wKQdgy2Qkpwk935R0-0goKIZTo3b1__5F8Ji04QQr5HeWaWv8oRfbvfvJEQoc_eSRnNoA6pFadJ0xmxX6Lnd8WIO9IjKYQhDvV3gU7z2p6kZwEhfm_kBUw2gVozd0QaJV-zNX4NW-pY8aYxiJWSCMUXZrA6XJ1uA078dVnB-2dOZthxw6M15VDNgOhLoU0-KXvrEY9DjmC5Oo2FYAPuvDlt3RI7huD5wqI5Iqh6bbGAisZuPMtUR5jTlIOKpRaQqTwtHa6zrDyqwBcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZILMMpftiHnwVenvM4dtGIxzLn98q5-nzza2qpTIpUldvSRz4dWBA6E3T0W_DwjI8YqQzF4H_rB1sVFlCjBIhYrPxHe1jfx44tbWFhUozYjSIOrjNX9fxbBFMvUkIbxaZtezUluNtWNc_7wFxlVcyEJ28R5LHwZDPBFuZfhRUOzsN3EOAOfawlhKlrTYHjfMDfo6iC1NhrAgNLVKz-dfZ5ebrU5jx0brH_-l3EV-KMi-Eo04sOANdHYxru_Q2oeWLTDRX8wxBy5EwQMLNw-dG7Mp8JPcNOSeLjuS4jdz8GnXOo23IF7R7tshLijBcuklFp_PBfadELUXY5B36kfqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS1TdytXHnAsQ756s__hARnohcDp0UPIVB0GOimAhqtBV6rGcNNSjGUKanG4eb5hBn2-1cKMiMZ_BiUi36SE7TArW1j0kwFMZsdF8DjLJAD1deOEt_YKaMp4jxDiPv105HBFiTikIr64l3SNF0dFCItHxOpNUYoYGbLtCwOwXdWOFiNxddVcOzk523RWXTJBTPz2XH3Z4cszG2JUPk_Wotoq_zoeVLZwLvp21uIq83-dHsI8FnH_10ujxTY7RGF-wxeNyP-26hIUVWplwtoaO7paVg555msBgv0s6CGNhZp5-ztcdJ1X5iesoGmkYrFxNbm2jQZSAY7typGPjefkjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=SS3yDkb6EedB0AJZsMHdubKpSyhf7D_9WFFstl7D-y8kbH0PolXAeq_EH3Qpkuzrq3Yf3oGnDTPSe1bP8FQXAtj--yPHeCjxkyRXAWGw_5thIeZKY7BISxyA43rLG9mzOZmBy5htfod8Jc2N2lISeSm2bf91l-UWJzD0cI-fXZERvmOyQDcK1y0xMYF6QRg63doRRIOxInkZQ3dC-FhvUg2xENu6hzQg5ZAqv5tvc_o60msWwdFb9DAWOgRcr_MxjSH3dLb37KJYsDRk8Ajev6QThqHK_XugekWDGS6R1Pk5YsYCNzTP2UVs-4owQ070os7XM6ubHGwAPb-kHha4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=SS3yDkb6EedB0AJZsMHdubKpSyhf7D_9WFFstl7D-y8kbH0PolXAeq_EH3Qpkuzrq3Yf3oGnDTPSe1bP8FQXAtj--yPHeCjxkyRXAWGw_5thIeZKY7BISxyA43rLG9mzOZmBy5htfod8Jc2N2lISeSm2bf91l-UWJzD0cI-fXZERvmOyQDcK1y0xMYF6QRg63doRRIOxInkZQ3dC-FhvUg2xENu6hzQg5ZAqv5tvc_o60msWwdFb9DAWOgRcr_MxjSH3dLb37KJYsDRk8Ajev6QThqHK_XugekWDGS6R1Pk5YsYCNzTP2UVs-4owQ070os7XM6ubHGwAPb-kHha4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=r-N5uEDzE82eUfmqjttiN4Cu24PbOxK3p9dIYubYOLMueDn617Ayg9uk1K182Ris7MpxKHlLK2y6EK8tmPIxOptprWbA3dZIMH4VgMd4lfNMruhx9RBfV_fcUwrfMNXakwtKMhNB38yR8WZLzS8gXID9mKAK7nJVg2k40MS5Xi-VrbV47VXUrcMM9_W2hiTkPpXJ1BQI5T-EMj_nC6ACVufr6GU82nw5t6iHAl9jJbonFj7VlQZpuJjup-38FqP215g8nU9stRLXYJDWhOZQBMP5cBv5rtVXLJesRkKxztMMJiMfU0xT1YvZ9GDA0mDHeFP4AcC3NEAGIBf48IgpQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=r-N5uEDzE82eUfmqjttiN4Cu24PbOxK3p9dIYubYOLMueDn617Ayg9uk1K182Ris7MpxKHlLK2y6EK8tmPIxOptprWbA3dZIMH4VgMd4lfNMruhx9RBfV_fcUwrfMNXakwtKMhNB38yR8WZLzS8gXID9mKAK7nJVg2k40MS5Xi-VrbV47VXUrcMM9_W2hiTkPpXJ1BQI5T-EMj_nC6ACVufr6GU82nw5t6iHAl9jJbonFj7VlQZpuJjup-38FqP215g8nU9stRLXYJDWhOZQBMP5cBv5rtVXLJesRkKxztMMJiMfU0xT1YvZ9GDA0mDHeFP4AcC3NEAGIBf48IgpQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpWAmo1upyWmNagKoSKEEB7timqSjBIfXYdNPZ6jCBUhQvvwQY-L_RtNRWKabJDn67_jXvAjFgZwxEu5REsB8dblLqOLGQlD80r7TurP7oogmOXbs95IfhLZTt9bZjf4LNhKVwhruPPsWd_Qv6Vd5rfJvilIK1E6to45MViT3teTzq7DRlAx56SVJ7e5x0PsvYPBIqb_ITIrpZgxZI2zMs3NLN2bSOovSy7xg3RUISIDr2QA2991h0ID1ottU_cT6ftkSI9q-XPwUGvgGkzds5FnaveeYXsLOQ1PKxPGi2jKzHZdJaZjY008dJmexe0sjGjK0lQMiTQdyVvUOHNv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFCuCFQVTjBZ5KC8cSYmgQucy2P5E7lOfWkqfAtVgkBTbUpxu5zdFYddvP7i8S87OGp6Rcf9Vx-WlyVM7hl6mpZMSp8TDAf_OylmNb6HkbNPzyyI9KDKW9F2F0afJCQJJbOJYfoenD6-UFsW5REB5gArnSSMhyGOM1DiCjm9wGzVu3PVzQDEsSLp06eOgzmoDQ9l5GRyo2ApnW9yTGsjfFOFVZ_AsagouPly2nXrFm9qFHViL3a59kP1v41dM2vIPC1V61F3a1vKu67VmhZFH_OSM5yiy42rGhHFdDN94M52tTUEgUMl9Er4P0825h2FHZu18EzbvOLFbfnnkuiPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG7S5fFHtwGtX6buz8kWumkHWWZWllKSE6uygJ2AX1VP4gIwrOW8VdZAL65ZXzmkSkXwWZnT-_G_5oJt26mtI7xGK-YHNnvFiUz-6Jjh9Bz1FL1Dgb2oRZDEe2l2FigxlIIT40Gy5V6xGDrKsX23ybgsp9EVxCz8iKbY8Q-bOmLmkkGlb_ml-aLQW4zmVfWLj_z5UX4a2_sC8oxVHVGucJZqa6VQ1qhYbgYkyDWkhBW6-gMwMTkbyhTBHGiCfBFH8ATSTB5e-fk1rBQFRU0_RSr1DPSWA_M3n5G1qGf9y3WOEni9Oh_J289qmw3KvKT_P7cGuXp6tw8J9Y2vFXUfYQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=AttgnYxBVhlCHukpdb_XZC98yGFPaEgM4c3tVXOwFXjXNZzGRYcN6yoZcbz0l9a6knUoUJgnsl2tqikmiuOE_i0ZZS0WpmZo2iHRo5QPwht3TwB6vWOhD_81IVIFg7CO3jn7Yug4Cfh3yeoFArWh871RGYuyvmBA9Dz6th1nMWAXf4AjV4Xyigr1z7EKxYbSIwNb1BBJ0rGLxrAj-MgizdQpcMHSbyfusnp8FkTOzsiEDAfLC8DRb2ocQwSO7XFFbgGAMNkd3db-CffTYuBjPr85ojQXZ1h8PesJg2ZZnHR_v7jSCniv7-GEKtvM3atVv3vuQxXJmGCm7O5clK3SLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=AttgnYxBVhlCHukpdb_XZC98yGFPaEgM4c3tVXOwFXjXNZzGRYcN6yoZcbz0l9a6knUoUJgnsl2tqikmiuOE_i0ZZS0WpmZo2iHRo5QPwht3TwB6vWOhD_81IVIFg7CO3jn7Yug4Cfh3yeoFArWh871RGYuyvmBA9Dz6th1nMWAXf4AjV4Xyigr1z7EKxYbSIwNb1BBJ0rGLxrAj-MgizdQpcMHSbyfusnp8FkTOzsiEDAfLC8DRb2ocQwSO7XFFbgGAMNkd3db-CffTYuBjPr85ojQXZ1h8PesJg2ZZnHR_v7jSCniv7-GEKtvM3atVv3vuQxXJmGCm7O5clK3SLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=RP_jj1JXmc_CFyva9mcy6pjladm84taXX3SM3ukLa1BuIuElp-59JpT7xXnmgCgpPE09GR2-OjYcM1EFVfLtXUOiBHbDL_gLAsnlUBLTLIC83ouw2A3guOly-wx_arR8zBdhT0LhV2vSJcdVsbd1oYKWq_iY7IcYGbOPA0OwVDiYU8BegxPz6_ueOsSEa4gpCSbd_LKIIC-FjXXrHcjDgbuCbGTfy_K8uxui4WtDFe2f7_uJYcRa44P0OhMlsR-FKbWsMFxs6sg_QtKgc8kMIrDwfRILW6eCEOMMCjrdOz4lL_UH_C6AiY1JejkwryziSF3Wd51aeTLAYhfR2EGtPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=RP_jj1JXmc_CFyva9mcy6pjladm84taXX3SM3ukLa1BuIuElp-59JpT7xXnmgCgpPE09GR2-OjYcM1EFVfLtXUOiBHbDL_gLAsnlUBLTLIC83ouw2A3guOly-wx_arR8zBdhT0LhV2vSJcdVsbd1oYKWq_iY7IcYGbOPA0OwVDiYU8BegxPz6_ueOsSEa4gpCSbd_LKIIC-FjXXrHcjDgbuCbGTfy_K8uxui4WtDFe2f7_uJYcRa44P0OhMlsR-FKbWsMFxs6sg_QtKgc8kMIrDwfRILW6eCEOMMCjrdOz4lL_UH_C6AiY1JejkwryziSF3Wd51aeTLAYhfR2EGtPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=twxKV9cJtWtM4Cj20EtL99TLmECFLLcVolJG6ksbU57B5hN_xVkXAQ2sQkno7KjJm3RHi56Z52tFbJHDrk5E_FFSBllgF-4DlvgU_UZpDLWVK64sT6E9dUwOV1PqhoNEr3zjiRAxij_GU5D20xJskIw-LUavDShEL6fjjNsG3BCNj81UwDj0Uu-VtVy2WQWLfsQ73MPeO0zQ--4r2n74-2irUJrUb6d5zqAaPGkrxPFcQIswKLjNdNof7ypoMzVXXU5IXLSvREdtV6-1m4W_gEv2bnktH9EUkrLGvWAzCRPwXmLwQTNRVsL7uyFdVNex2JL7zeO0wbC4lUf2ERTkZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=twxKV9cJtWtM4Cj20EtL99TLmECFLLcVolJG6ksbU57B5hN_xVkXAQ2sQkno7KjJm3RHi56Z52tFbJHDrk5E_FFSBllgF-4DlvgU_UZpDLWVK64sT6E9dUwOV1PqhoNEr3zjiRAxij_GU5D20xJskIw-LUavDShEL6fjjNsG3BCNj81UwDj0Uu-VtVy2WQWLfsQ73MPeO0zQ--4r2n74-2irUJrUb6d5zqAaPGkrxPFcQIswKLjNdNof7ypoMzVXXU5IXLSvREdtV6-1m4W_gEv2bnktH9EUkrLGvWAzCRPwXmLwQTNRVsL7uyFdVNex2JL7zeO0wbC4lUf2ERTkZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=qtWMmVR3jeOj26duWUWsC8R8kfCO6xLWQweI5e8OhPZJkHGvpgPRNOeqk8gksvaxuKdUd2_El6STGFl1Y_u1sgZOQURmbJlSZu7Z5AqYDEzcvmG9XRh2FmY4JlopNcDPjG5p_e7Yfmpvtg-KZCYo1irelmdVkA3lwRzByWxFemNqz9bsnEZlpWav7jo15gOYnHsFkIS_K_nezwfcH4SdbzO37QoYVLaQX6KPweknQWIE9LUGaD5BNoOziAK8Vf2wS7NcvVHzC-6L3gGzbu5B4UmqZAmAf9dWZdjOGBBVhXMRRwGzm5W7d9rA7pCOGSN5QpkHhnSyXG0cOgGZA08r0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=qtWMmVR3jeOj26duWUWsC8R8kfCO6xLWQweI5e8OhPZJkHGvpgPRNOeqk8gksvaxuKdUd2_El6STGFl1Y_u1sgZOQURmbJlSZu7Z5AqYDEzcvmG9XRh2FmY4JlopNcDPjG5p_e7Yfmpvtg-KZCYo1irelmdVkA3lwRzByWxFemNqz9bsnEZlpWav7jo15gOYnHsFkIS_K_nezwfcH4SdbzO37QoYVLaQX6KPweknQWIE9LUGaD5BNoOziAK8Vf2wS7NcvVHzC-6L3gGzbu5B4UmqZAmAf9dWZdjOGBBVhXMRRwGzm5W7d9rA7pCOGSN5QpkHhnSyXG0cOgGZA08r0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU5hXFd3M5vqvy8ybKk2ttda62ZVLJuIa2QMTZqT6GFxgUtJddEOFf1KJejUP8igvEyMikNjLAte_L6RJkO7Fsy3j5d4VFhUxgPBZs7L_64HPPkKHELSxzXiAWyjDManPeXBdCBXKCSM-VXnPl5aZ10Ns0Rm0ZtjrSx7UlSksMLJkSl3kMVkj0vYfsRv4XNIOeGObLObMhZeeXqERHGUGMuQfBo3ohofb2TKoUB7xF16X7IwyaPUHLS6CdAjdXn0THusuTDH85xD2eHrRKJe-Y07HxrpIEIXXkMVPJBPXr9Xzd8U4tvuDToL-V1m26rJ_42_RYbxGwGHSIFcbCMADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5grHqwxh_ELNRgJ4F2zQNgmT9XVV8wgZQ-_yKE3Aq3b5Bl1um41lPhFpIwNHkajuvNi5WoDuMuPOgen0tqMzjXtwUuxSCr1d5yH90AUkF7nEqEKAT_t0QHPxBPCvHdGamqBjAcoZqOv2qUpkKjdx5qbjN5sDsUaZm6pENrXPuHqpeQOVDgRg7WluORVhZQ2tbmTp6zmGq-GCMjiU1iDRmiHs5izn-XK9FGUTGUvc2IOkV2gQQEBdr4y80YjO7mcbDV8AD76-DdTJqMeyJ7SIiUMBvy6Z8VUxg_zPrwc0B-hYnhkGA_ZjoUBAfzomAfxRZPnaSwuNJNPtG5U4yHPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0-MKWI5IMaPY1kgCvg8CAk0MHg3CVo-oyb331A6KIwkCv8f-lmKDRNOFEXzqDeW6dcpRJrpmWe6eBekCIAnVgv2HgTVN0abtFUq71P0wkqtKnq9rTub8k5Mhh_U_ccporJ4sWsmK7OepDcPO5s5oZqsnlcX0ry8me4nC8nfKSfl6uz3cNfFZ-sIG7lCTqqbyrISSXavco9kJzlg-e54xU6Ltt_k54nzT3OkpcGc0yhBF3GTCq9Z0pvhBlaoiorsON0OMG6fMZOalDMqP4mB8MkAUglly_2kltFqlVyMdh5RPRGmU1aDQyiDZEe5_0E-ww6-YyuAWpbnPZ4S4oY5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHHlWVsTbqhPADnrMcn-lJqYoHXG6tM45WMwYnw7ODg_JdnvR-DEBYd_l9ztfGtVMbkkXsYlazPrZwMs-caFocPWrrob_qYV-12x7Zv1GbcQXXmxZJ4HFuQi4y5Ct6PU-9hrKUrg5qwBmEiRK9QVW8c0Jz_E0E4C7h5XJmfn_Dbw5bChgCgKflPUMBF0TcR7hDL8OVroMLi1dXZLIpWIK4k1IUjBTfW5gdbmcA7hX_Q7qFI5jZ-E5gUSDuupTwourzY0qi6pgnQlrvc07aw1syA5HmStSFHmPqDkhsv-UKQ6KrlxSnXK_UwdWMUAOL3D3igYF1mDSzugigE8UL-7DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqXwwRQUDbyG9ayYuirOeVhEVNaG0OskwlH7zR2VwYreme6Q7kEkj3SXaYVniso2KmgXI1hpdo_QxZZRKIAlXBi4pm2atLSYsGR9wamVANKQ2RA8hY-AVJuXsTu-PH9mtMSLNqIFLtXO41hyPw5sNz0y0eMfM22d_FIaQZ-2wO5GVTXAwwpGXqivxqfIhOUzn9vWF1tKa2OAhvkXyi1_9S3XYWtiMdvN1y8J2k8P3byc8AEQe01vuKIWuLSTzddDYOK3eIM_QVULv2E7asg0lxt3nGay1UaMhE5hHYqVw2hi-r8Z9G-Gz-M1o_Js1zpRNbOaShadppoMqF4juYUo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqrXx0LkBtPchOGLPimbWr3XBlD8JEAmVBceL_yDTzJoCQYT-6uGZqX_3klaiRyhhltQ5JK2u7TI3k6a5jHxJT602Y_fj48tk_BQ_BsQXEYdJfyZt0dlpjag1nydBS39ojC97f4pdXJWfNGUaQ1VTQVnEBDvfKCfjGGWgHRuPQyInIULEAnRqVgKRf06RPCYdFa43UOHe9N9soGcZQc0vZ-l2d6mwXbBy-5zMVBEHjJtYT7_bBoInsHLoGLuLVXdA-bE1MTaC5cP4SS6waXA3K4kJukF389giOJOJ1IiHeMpEV9RxL_74_lJJaPtM2hQqX4By2iqpQ8Js_-PPmZUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVdqsKQiHh_Ep4yQnzV28zpI3IA-RgMgN2zTx2OZm677_bT-BUZv0maY2xt_0EM9n4iPITNy8WBQUmMLghUIUblBVXVx4T0xCeJ0hyq5AkHUf9txHVr7f4YBZmKN5BSWQNYknVmvXu1df6YeJcPHsTBTYLqWVuz0TrX9OkVrlUfQfLAfmNF51QA2GtpPWYJDL5z4eTe3Daa9z_RrkCPvsvNfUCuDEwgHp1WFX7tMnYiwiYMISNUaZ6R2aq2drXHt_5Pb7yfTS6ikguNl-VWaEZgcpS_bV16XUFpSRIuSUh99UHgxYuLFsb1tH6IHs_f0bC9OvuVGKu_W8PYdaHFLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaDgewC3jpj8EQ435cdQKi8xS-KGZjrWyv8HF4TW6QTxOPzw5zKRVaIa5_oxUQ-c9FoNWORlX2lw5Gmg-XlgrS2s2esfrYfBz_Qq0Fxo8B2oZFANrjsVGlWnGrjFeqtbQzRF7IheKV86D8nz5NExZxZgPd8PM3m4gcr6Uhf8cb-e670xgE8Ga1J2xo8lAqqbOrXZKYhap0r610iGQT4b8WCceqxm4SB1w6CG_wDTv-gvyfYAK-99KHqXYv1CB4mm3AehNFhK8KfCpIBFEeOQ3J4dCEB6Q9oMuBFfcGbm6vom_l-ajTTkVtydwv2dRds0t1-N7aULxtbXTsE0b617PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnwlVcyiyXqGEzsPZoVjcHSTFV-lQr8AeBntVTXSJQKCAuZLWhyeZdAOrqsajiT5nqU5qOdQYkW3HM0rPapB9K23ozMHiGessGjr1uUuQZRAqGnDrjwqITH1a7fEXAEXDWG6EDNQNA5njXk-AcKJuTLCjwYxOzwrWkCKmEJ_OaqbMtWxpvfX5Hbwmr_gQcVnBjLZfmFsAEery212iYKbKpw1u3sjiV07avEOUj8D-XW_u5DjkEJf-OzShIbOOuSua0sa96CviRRy1FRRsBFNP-7BXZhXuOM28u5wwaKp6eJRqxiwtdyBZXOrSeF0tWgEZjb-6ho06BWAqZFQ-tcy_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2kye0t_eRmQENeyR-74gj3PDRDLSb51gkQXowSBYcG62pztAzvoRmS2W5OE8sYftMtIvkKBkbFZ0R-vvY-KXHLmn0eB0oYvzvuankYFNeoVU9fW4cX3dpzZOVyraRJQZGdbKgD9UtUXAr0tlcrSavsgpo8D0nwKhh5VEyAcskyUqAR1EhiiJyzTPN23krcBhkZ4WSpS6FHoZfZD47GVcWeOq7weYYvyNACJG_KEIXcVx-T-0Ga8ILYOF9R-Jj8qk1AbocP5FjG81tdJrw3jpCCxxHHCq9UWF4mlZk_8FL0bX0_9ey-RwiGfAvXW_UoVHlLonUO7L9S18K0108_Gjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QczE7h2b_6pbUH8mYo1Y7SBK-1XDbC7kvDllkwAealgiyuzZYmPLC6YlpobuqugxgJXodYyPvi56xfzHYcxxHjXXoRBtrrbVlggAd4lJY9Ulg1zV6sGrRyp6RIqKV6LPGz8KWbGVLpo3YpkV9X0HXcHsLRzMrEZ1JeKvKP8O6epp501WdVwueGZ3OWSWNDUpfCx_Dc2PLYHLCRfCXoGYrBq8Czb07JAg2ehvboDXyNEoGWQ6WrIX8BI3iMf7EptX9Y_nX8hg4Aj7yBXXohk48GVTvUSFRBqs4LzWcBVvs29nXY-B1ilkj3D5mkuRMzfjYtzM9LJ-0xzIWUUh5H9zsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnjkIBKBpGGlI56MPRJao5V_4bzxyMwyUNk-K8GbqDxc8C1sUCCew1dESr_smsNJX5e3Xn5otogLlR_Lur1Ammaiqw9NIegDkZAZkcDnJPIWb1ArBjVO3yEzyRw9XqZv5s-sij9g328XSZ3cm21gXeRHZS7OU9UxMfPV5M0rGSPZbiCDpbWYUIfa2s924BJW7TLeDvNPvYBpmc62PLQyoiIBUVAHtYYX7fx7g4LcTBL2_b1FFycR04MAJt2IctxGsknYjU6sMzOKQp970dvYXpdrlPEsK3FLDA0jry4MLaBLJIkW3IkEk4qLh-fyVmGumxE29xuoLn1oOlAgY5kAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUx4wo0cJz04vY330XR09w2V_UIvdSsommxnNB4M5P_HxVWoCF8TVYURGtsJeefCtdHxuFfZ60Ag1LGl3pIYrxJQrhnwv6kQZqXLL82qSyBkHQ9iTDH5iTNGPZeDqPKcSR32wMlSgy2e-4zMHw1tQlwfzNy8ZC141XY2Y418pVuXEFJoPFCT0O0GLozXlIEa_3sIaPDf3-GnDqTq9_h6RlNx9J1DuKZPyYINJ0LjmfEUJw4usWI3oFYOPrrVPnFfo1m03bNr8WF8P4sYoxKxeQ1csD5zH_fE2uksr6FfAY2tDjDJCw8sxgwFxvz8XA_k2UdjpUwrbGeHa_hI5GUPYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUQ7MI_KJEyPAstBJ4vq-vIxHrpw96L1EhcygsvriVIqjLJSVS-0VbTlscc70aqM3OFLLNqcUHfHAhlUnC0Z-zDF6f68I7F1nZJfAHSUotlPzMwJ6q-rw_u7NmTUsQ5FhzS6vEpCEd0a3rumRIryWUcftbn40AVpjBYTrrQLdTSLMb8YLHScrTuRHaRE3Vitjc1p73ErIsmYmIU7r5lYCiVAtEBuvYwC1R3oDHtRyGrwUa9mpkepKJtz5HOvGuMlrAJrohrroiyrBzLhD8JQ46HulLuGKVxxK8ndwzvTfqXL-kXM6nHUTyRM6R20BXORUlXu8Zon06m1H6CEsk-ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=CZbD-ZPqKzxVhCH3yZ2Xi5hDHvj6r57EPh7GOIPs_mMGaYwb0YNlRvVYRyfzljpAbXxi_QA-X0JofoLXWlbf5wwQHJUL7AfJtyIqEDl1wBSe2fIZfCt2ZjvMvDBMRLqeg0oJk6-hjgfxMXQUlpCFRXIKAGu_6ANijSQD2KMuK1XR7YRIaX6bMUynfOBqGEYC0trry-9nInzEN5PZ48pv38r5tTCfoDrcD-5xRWUsjKaJp2ilqAlETcxTK5cZl2JI_QtLHOTp2Dc4wy93CYdjCJ8IFZgYCnKT-7oVpIoGB_LQOPeHNg50KqDaR9wB_5KcRzL433dNR4_zbzo4-K3cug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=CZbD-ZPqKzxVhCH3yZ2Xi5hDHvj6r57EPh7GOIPs_mMGaYwb0YNlRvVYRyfzljpAbXxi_QA-X0JofoLXWlbf5wwQHJUL7AfJtyIqEDl1wBSe2fIZfCt2ZjvMvDBMRLqeg0oJk6-hjgfxMXQUlpCFRXIKAGu_6ANijSQD2KMuK1XR7YRIaX6bMUynfOBqGEYC0trry-9nInzEN5PZ48pv38r5tTCfoDrcD-5xRWUsjKaJp2ilqAlETcxTK5cZl2JI_QtLHOTp2Dc4wy93CYdjCJ8IFZgYCnKT-7oVpIoGB_LQOPeHNg50KqDaR9wB_5KcRzL433dNR4_zbzo4-K3cug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdt4jbiv80N8MVySHV3LVoJ8E97AkSVCgEJCm518TzrlfHkM_lc0zKl-UV0BSrrovM-f_zH3QJJfvrzGFEnbiMUUHQEMB4ZkyDK-cTVIX0t6_86VVmF0r8TuNqNHDJXRLJfAmfcJgoaZFCeudk5ORlWS7lXpt48BifE1HNV5yE08qc7vgx6dxmtlWTg_0JBYb3O8Fyrr0Z_lDPwQrrpVA6XnigVpkKLehfv9NiLKUUtqXZhE2o35bIj-XCU6WXiJPo0R89OQjc9Hqyxv12BroOAkpauTfpcYi7lm6F4e7TVyAa8uEerSR7Daxjs9-iKmLfVcY8LI7STep9gsSWsNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiuEDeHbrJ5pw5O_EmBoL8kp8bFXNEdMKuAHyqZ6SXqYW79SQN9nV7HMDsjQ5CCmVnRyUp4PpGt_gqEgD3LjfJxKHNenn0rA6C3q3Lh64O5H9h1fryHWpg6MeH1hTP5no7l1SZ7PwaP9TLnX16nRDo-CObII1T8RkffY2HkR7hFxYXNjc9s0syHsWEKq4yLF39DfELoyE708N1GOThma-GNEwxavXWkORx6_I2d01f2q1dyCnLOrgWNvy2CL-AIdmecDzrOZsJB9-ZasBOZ2CWkf100DQKXS98Vjq7UZ5MmjVqkArtPrhx2WutQWfbqtnLhTLm-TVxgO2hsCw7htGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV95ezoxdqSr3PJG8EKn80EYi4a5JXd6rwJ6MFyQdPlvMzWbLdWe0Ew2djCcbwuoIrcCUufFju5d9DvhFKqtgJxIAfGrldUGy6fnlhNXainDaq_0-XRRDcqKcpD_2U4nuS_gOGxrrlEg5Hr-IFeaLYwA9Y15MNB7OamrXlGmvH1uXvOexNZmD7MzP9pYLTboKS9pD7tSN0tpCEDqrzAgN-qJqj342f_5dW6Ga32bhQypPqOVoveU_ATtjblf1z_WAvWz0qMCcDfw3FWxOptzrNMSY6hdDfopNVNPtChDQkrB8-V4TTrrKWLTWbcwRaurW7NPJPxiO4rJey3xKYkHrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4zAoXCb3osKj4ymVmGJrMu79KuZ0DnCrdZq_9ZGuqI2kIlDLYdw0Mu0sETHaLkpb_KLMGOKtbv0aSKLWHEJ1FjWgDlfwUSVdi6pUvUlWWJYjgJn2r85WfGWGIYm2u1zO6kwn_pskZ752cCX9SPdSHHXd_Zwp57LzTEWGHl4YNsYxDCTXcxusSaSjfV4s3DymtKFqdD-BqQ_cFTogZYqt2BiPrqibmg8WA-vQj52uuko-O2gqhh27lgmsmy4j2hBr5LKRBlGFI-GydCIPQvqyJRwdjsv7XMz8o4cFhXatW1MypmoFq6AmC-XUmzsJWKfOcO2uEe02lA4eHVUcLcvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz08Ryf_LSHJibFuP4gTx7TzPVHcwLRhVP5uTX3kfHnzgguRRTgwH7IFUPZji_fycCuNc70YAhdU3ZlGlpL2KEdNR7Ok9zjxwnvoegZybi21ohCTKm9J5CxMWEYdOAmSdmNbU01Lv1tY4qgCMn19LKTQvY7K9AlMeUEt9kcgkmhHaK02xr3s2WDM03b2KRoEMoR_AQrMs6XttwxE-M88sQpOOEl3T1OFfJByov25X5NaKJcARkQ-5HXSItOp27OutzLRSiB2NlUliR3g5M-Thu0UQhX7tj7Eap3LlRn6pW48AXk98eH5UzNSsyvCFKJAkIvcUrkAVu_Mi4sw-0iNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCwk5eumowKnVNF9a_uBq0BSeam2dBsYGbn0esewzYaQAkMi7ljHgiDHsZJ8MvyLpSXoC6lLtUGb2_I33-yV888QJrlVKhexDkNaDND-u3HmiiuONncr777kdPYVm48oF8700G0DRIusjK0st_ozqA9TfAZLdKFFq3mIUIeFyvirXiyLgiOrwuMJiPbYndHr3yzAIbqS8vpeO7k9OjzRT_HoyaGmGWXgVHyn5rzoV-jfJb2rS0dWnfPChjz8Rme46OALtXMjZhJegztM239RywyH1unV4KlJuuk6tpGF3w1ZnsuBXXmnsf0pY2N_Rgmu8tS4pPa9bzXhcJNpPerH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz1AeSuEkZ1_FxKdW5hsUidQIRC2ChsNp-zpvwXxJsiV5s79dB4-H-PVCK-bMvL1Xl7vpwAJRGERxr8sOmRQYJUtiPXayg1VnZCKqlEYaDmHHDwBffeq2YGI_ZA5grzIiA57cWYd4bVZs5FglAknWjJI73LGZLglo66gU9sNJZw5Q1OADlRRksC1Bic7qPeyDj472AvhC_298ayKU6egDjfEeb-85syQK56KLwwy-Jo3qvjPJ0EtHjP92WAvEJvtJPbk6OdtMbFzZZ9s1jSnh5ZXwPsMpvWbkt1SMn3mglNM5XDYH7jbh5WQnEuuCyvTuziCOY-kjBf6vVWiJ_4gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pqj1Ze1CeONYh5s1tAre4UjgR-ZmXecWGcSDWyqeM5i3q7-KByVK8ycF5KUeFTNXo5le_3L-f-pFHAkF7xSxKocfjq4oV0PaHtGyQkdMtOLxkQyWTdKRbrF7gOQ5sjp8aMmNgb8JPy9xeK0WG-3R42KXrx8mR6BI2YYHAXEysPoj9QWK8jAsXe6dVAtdkB-p2RBFprjlRgeDB3jcebShQyzItaanNjO6BriIt0xHq0PXW3xSroeIKKlQh0CERmHuv_sZhorKyBNYExZGOXjezvBkf-vVJEKprzAfS2eF5Cz77ggJq_dBlFSZISb-jJHrLMuX3EscNsUO9YHJlbgPzg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=qYTxKrFnJgzmhIr4pX7FyKt2U4ithl5nJ6k6xn4pL0f3meOzvfjQGYsjnF143elYJyTBMuDFnbSiHPfrZkNK_gPsBbmgmlTBZK4v6ARAIC3hNq8ZVP9mDcaIPPAzSCwS5jn-L82okOKKLoO29jPa0mxdruKXQzL2KDOlvHEUVTM54PkDU4KmaYNvXNzZqYlWKx1yapjoGHJWi5t6eE5QUdpQT55OUTYU5iuRBzSUrILFGaGvRYsKsAJXagvEg3DMGSk-rY1xV1VL1M8KRcs510XGC9yuLJVgUJwQLVYojCom0gCIFJScqtB9p9B3MmbiKNRss54qhNHBbsq8k9nniQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=qYTxKrFnJgzmhIr4pX7FyKt2U4ithl5nJ6k6xn4pL0f3meOzvfjQGYsjnF143elYJyTBMuDFnbSiHPfrZkNK_gPsBbmgmlTBZK4v6ARAIC3hNq8ZVP9mDcaIPPAzSCwS5jn-L82okOKKLoO29jPa0mxdruKXQzL2KDOlvHEUVTM54PkDU4KmaYNvXNzZqYlWKx1yapjoGHJWi5t6eE5QUdpQT55OUTYU5iuRBzSUrILFGaGvRYsKsAJXagvEg3DMGSk-rY1xV1VL1M8KRcs510XGC9yuLJVgUJwQLVYojCom0gCIFJScqtB9p9B3MmbiKNRss54qhNHBbsq8k9nniQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7XX5hz7UNXeR55Ee19AZgSiRNdRfbctufhozVFn8uuu8sQ0mSVkfcTaMdgzZE323Ct6GbG2VVA1_Xb_XwYhWlCUTKT4BFkXC-wOoozg8EMAAWEQpWtn6HWtHSq02nEayTmA_Q3kxMLZvwbhaKO-6VPUomck2SJUFjnI1DSlIx83Apvur9plZgCeewfas_z2q2hP8GTPxPsQL4mDnRzq_ODxLx-X8Tk9fZMTU4qkhCHT-AOjsDm2qOnLVmmVy2lkcvePWULS5aFoTVN7O0MANuPV5crmf-hVYVD1_dJkJRQj67tQUG5lcnICWWoifLtz15ke5r5i5YpMSbBNmFhjKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPJnbF7L6wXiU_YbIu4pndtI7STxfgqZ__B9d0bPCWq-tn5tvJ8tOOUinJydv4cXZiU__26SHR-Nw_F83YewRtiUIGcPTygCSmMHUsarDQbhJDVuzJQiYxHhqnH2tjIz_fOTyde41GxXu34lQsj0sL3-1xmlr1vcQeAKJ7R4AHRwTHavvQ5pzy9hsdKqdEWXzBRrGYcwGjHHwElaQODh5Q0U1ZJwxcfRuycV-Ig1JzTTy9whrHmMyDFElrKt7U7aiTJNxUaugiPW60PDp5xmMAQZ5mWRHrOxlYWMbz9eGYEtb04r9REhC72wRBLr_7akol-A1cvsLRUyhBtPGsZV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8Zn4TEJ3IIVZ04l8aosgXmEDJS9_oigfbDaIs5aaKqgURoQRdPxLA9LKvKjZKz9yVwRguxU0Qb54jI8ERGg66RqI67-JpI9a1_eTk5BqtYy1eerMSTzyMBv3b1e5Nh24lDvh8vBK1IEu7vHOsyjSZgw9lIvlJVWM7rvCtGH5c616855k6H_fWIxfLBUi-i5bJ62zRXS48_0qhgEOnz2KkDw4PVZm62m_Qlq9tNHKlBEB4En1oeDuDriNtrGWMCoWq7wGJOtRRzWq6Uqx2uP1xV1J5VZK9fXRCX0rye8lPoDV_KzOGmErASSkFfUUr-WRpaoKnPE2Ch7Xd5KvFn83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2PNd3hXkiMeqTLwTa2jnhqcP6qEF95XtPTxwdXD78EC_zqd_2UTv_aqFBWgF4aLdeK4HKVGGPJrVJO47jPWhJ8K4C84lJkrHX0utDJ6iN3aaCSLU4G825rEPopmILMjXZCGyEIfKSueFjTj3jHBy8cCa3sY2MGlCNmA44senIZT2_aspvs_nt2ab-sYp8H-86Rf7sfHIOJu_tVt7Q10WokM1RR21_eyZgUh7E5zMmcUsyHVBY63pC-TA39YFiRn2_AANOgkcIigMKtbyRUWmVjUDhAukDlxe17ATxtj4sd04orTdwP0Zr6u-sNDr-yxlVMDYHXf9bpiHApAZvetYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REyvawvAgz9ttBYZnhyQr15ZAIeqihA89vvRfKCF6frupHEnQ_Q-TTngRBWiAJFxyYp8E71ymuubkNllBj4jsr_lBBW5M57Zqkv6PVSOksVDR9yqrlOTeRNwmPi0REe1J9MdufmH4QhyDOOjCGlkSq-mE15W00hgXoRBOMV1p6RQp7oAUmjZROrkDGXkXH1xih7cU6R1qRTXwLKhN2rDylSD7hgzaTSed2_Q1u3tg1UPcqhb3JgO2_nvas488L_NLBjfK0OQZuH9x0JlJah4Zum25LTmsYyGDk-ikzsfo4HzUmB_YU5iwqFfAPZRqWh6EOz6C6sFeBPCg9PPEYSUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXeJIi5tp1QXl8ym3YsXFsFcHG8orCqCMyFYcqFTLt8XEer1XAr03JRWus8PWy616QLRA3p2Bkv0g6BKVcKRzqKp6ehj2uB-DEyoRhLzY2NluJio8BoJaybQ8CfCjMQipm_K90GcpLT8qADrIZIQdpIyPw4Cb_WnJRcmrxk_DVF79ohp7YS1hpRy6eM7jzIfnEQ4GoMUQ8JC4H-jzP7H1Hh2ZiX4RBymK-b_IMBwwxRSWDVGeDk7Nc4i1UTIMipel_zCt8rOqQs9ZmZqk8uaCi9mkfBy9u_WdDwkOKTEdYu5qJ9go48c1-4h7I0U3311Ybtui5_c-Ql-TeGMMXLfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5KWV3z5tCRSMneZtUhRpPO6s36v4ix9PxvGV1FOe6r8QjxkGhsOdRYAq9LFkeES1hhr0YXaaILU1geWaAq8mcxti_HiaKTPxyiIrg9wUN7LTBicLGYKsxuGGqMMDQVZRmfmQcZ8aYppEOOD6mjyW3BUc9iU2xjBNJgfcRYBDCCh5S9Z-ZVuocFG80Dh7nZyrxfpCHbmPR1mDXqh4CrJTPt2Eb9XREXY8xxsHN9mmwCOfGjHn0wG9d3G1L02diL5wyVe9Xg1IXzOCJ5RtiaCxgqn5o4DiAz0CWoskjmv_8qoS9UY9amtucD3xXyYDEwC9NiU7E6lIIz03A4o8rR-3g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=uSvXoWAF4QJtciorAB5qNCDN0Fm8OT3IiCEl-7Akpe__5OPNafCfMEN-RzpMohfRgTcXsFDPty3SULUIiINMR6k4foOdzAXvwHyHx5zylcIvfH19txmsMXBvwDWaiIc8KlWNwQyLerUzkJ_2O9sH8mesh-jb7kugtzOgMzwY53-eLxcQRRhmCRl-cvZyF5x_3RUGT49RaKvS2kmRW6ZE7sUuuQ-jXQHGXnlfymc9F9sSFkqs-7HY3ddGXmseEhuj6wmvchWpMrEqN-LGoFcESU8CQ99RDLgXQlZVHCqo0_zemdImln9NxY3jg-tCCvVP_jb0BTkYH8YFZIAEsQmCjVcCUi_VA87v-MdSaf2OslIjDycn4gP6xhTEDdGLUHfMeTdtz1kQ8BfJivFZJ8af0kHTvhBEfaXOpboU8-W4oSmUq6bGFBdjs1T_iMC4ZdK75tFHUbf4B-Kea_HuHr1OMQ4o39bHOqLN3idmCnZJFNSCtTu3t3Y5ky6IQut4kZvW_5ehC_jN8eKYZ36Lbdzxpnhoz9o4RnDLy313vcVAFKE5JknB6_XXqNJA257xQRXQ5EW6AJr43SCTfsLfo6vNRcGyuykXHCtc1crsuTXeKly_xLoWlv4HOncjlXlRdB-P6kvc89fx41yx9YFnH7lFbnh6XHeJ_q8bwgGY9uEDqLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=uSvXoWAF4QJtciorAB5qNCDN0Fm8OT3IiCEl-7Akpe__5OPNafCfMEN-RzpMohfRgTcXsFDPty3SULUIiINMR6k4foOdzAXvwHyHx5zylcIvfH19txmsMXBvwDWaiIc8KlWNwQyLerUzkJ_2O9sH8mesh-jb7kugtzOgMzwY53-eLxcQRRhmCRl-cvZyF5x_3RUGT49RaKvS2kmRW6ZE7sUuuQ-jXQHGXnlfymc9F9sSFkqs-7HY3ddGXmseEhuj6wmvchWpMrEqN-LGoFcESU8CQ99RDLgXQlZVHCqo0_zemdImln9NxY3jg-tCCvVP_jb0BTkYH8YFZIAEsQmCjVcCUi_VA87v-MdSaf2OslIjDycn4gP6xhTEDdGLUHfMeTdtz1kQ8BfJivFZJ8af0kHTvhBEfaXOpboU8-W4oSmUq6bGFBdjs1T_iMC4ZdK75tFHUbf4B-Kea_HuHr1OMQ4o39bHOqLN3idmCnZJFNSCtTu3t3Y5ky6IQut4kZvW_5ehC_jN8eKYZ36Lbdzxpnhoz9o4RnDLy313vcVAFKE5JknB6_XXqNJA257xQRXQ5EW6AJr43SCTfsLfo6vNRcGyuykXHCtc1crsuTXeKly_xLoWlv4HOncjlXlRdB-P6kvc89fx41yx9YFnH7lFbnh6XHeJ_q8bwgGY9uEDqLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=WBk9n3ZzuyhZE8G2q-coArZwu94-l-a3HD1SUtXDXx_hx-O0XWvt2EgI03t9hkr1XiORFrywMZqTCvR5mgn6sSwd1iw4G8sqeorE_T6U2C2sinvRolQstGXsCB7n7B38meDJGnA176IjqN4xNcQf3DeuIAbFmB_OL7z8ng_-1cVLDJNiOMaJABTw04NaLH82Pp_f_ykn24pBX3RNZtIXKXtzvi75dfDNnt2TAp1d6qVEc_9lHKwHpPg0a0Man6kTKY1xlZk2Qp93Ala3zbgUkZ5w2Gd8vHa51ahBD_-UPbxDkwWvrY7WYjvhXIy_tDAQ5Hwb-3rZfBgkHS1m1plWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=WBk9n3ZzuyhZE8G2q-coArZwu94-l-a3HD1SUtXDXx_hx-O0XWvt2EgI03t9hkr1XiORFrywMZqTCvR5mgn6sSwd1iw4G8sqeorE_T6U2C2sinvRolQstGXsCB7n7B38meDJGnA176IjqN4xNcQf3DeuIAbFmB_OL7z8ng_-1cVLDJNiOMaJABTw04NaLH82Pp_f_ykn24pBX3RNZtIXKXtzvi75dfDNnt2TAp1d6qVEc_9lHKwHpPg0a0Man6kTKY1xlZk2Qp93Ala3zbgUkZ5w2Gd8vHa51ahBD_-UPbxDkwWvrY7WYjvhXIy_tDAQ5Hwb-3rZfBgkHS1m1plWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS8_-drJ47U9Cf0TmWFVPGa3jatRf5a-lSzqUCsm97PGKpbiaLTo22kDfYPBcX1zm9pu6lzp2g7Dp2SiyrQYhBIOAGpPb6O5OYCrlePI4RQXNEE0DPnWJFrTDfF6cXnMtlTVR4x7JViI_93mYrKbwemgL9Lb3sJjLNhMfbIOiHTGNMocy0r70WHJgbdyP_DCen2uu1BsoeyM9AqbFYSQIQl-EwQoqpnIBLe6KF2zXdd-Wph6js6IsQrSjHDPXQG8a3JpzLk7Pt7UebbUM88jriMTvdz36JI35cgNqqnxlTiT9gZsRo-EKt-6wQMtj2YvNKtkBCEmvGWSUAvpWhn6pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd5ff4KwDp24sCh1bwxT5235sQ0Q7oTkGN_ur9kOqnMp_Ez_w6agtNb0zT9U_VJ8Gj--uEz4ttX4Cjw7KcyqAoYhpAzYOm3SxYwq2snm50fwTA_A3xFBMYHLOv-p83LvvviRtrNJYtSaARii7puWJhr6UqtuLawnGXRQqmFAVcqhappt-PYKNjW_UsHGpN81YxbubiWig7BRIcjG_j5Ry7Qu-4wJfrPzJ3s3j07xGBoTorW5cjExRgxfJydrTCU3nBg7tYnCkx06sTXB8Xbp30-r30O-CexO2kMJesV8l64Wck8smz7l6zHO9LdkhZ-_llwkCUuRikEZ85PQ2n67Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=nKdN21oYogUi9iKLH8-2CqXvw566EarEocWEyeOLOoKwgoZcZrTuUOFnby3D1oZLBhaLNDFHnLw9ILSg5Tp65fH3OmMgrN05wSN2ptLievS291FJuOFvZb3SOsohiWwlSFqbiIU8gRTE9b-2TyUHFDv1NOZ6tMl_05nV95_XErZYARISreuLrXH9Wd51yWdWbqqHCVjdEsL5ToKXTAO3E0tQFwFWpj6ezl_HLdZo4lCo9nlRkS5UOevnZVkNo78FynsOV-67mP_3SsFeadoHRLczVqJURuBefwOZ4PjJgXfAFKf61N1h8RxEOIi5CuYuIK0Lgmq6yTZ9cl_JQ08-qjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=nKdN21oYogUi9iKLH8-2CqXvw566EarEocWEyeOLOoKwgoZcZrTuUOFnby3D1oZLBhaLNDFHnLw9ILSg5Tp65fH3OmMgrN05wSN2ptLievS291FJuOFvZb3SOsohiWwlSFqbiIU8gRTE9b-2TyUHFDv1NOZ6tMl_05nV95_XErZYARISreuLrXH9Wd51yWdWbqqHCVjdEsL5ToKXTAO3E0tQFwFWpj6ezl_HLdZo4lCo9nlRkS5UOevnZVkNo78FynsOV-67mP_3SsFeadoHRLczVqJURuBefwOZ4PjJgXfAFKf61N1h8RxEOIi5CuYuIK0Lgmq6yTZ9cl_JQ08-qjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0NogSzbdaS7ICkUrA7FdZM58A8gIjQdt-LWdHkG9hu5ubmt4LGmXTxsqwMUErG_JuLcWuCviRz1kJsql4CUPGbFSZy_masvEITLc5iU4tKZzbB_7p54-Ioz7V6_UKFHHZESJepSy3PpWufywWwbzZnS-4kuJoX0V_YVCX-1g9YnZfMc59qv7ud5UsIZ6FBRMEvfncuWypi9_dCeulmbn_C7ff5HSPxSiS7LFUj758bdSCbijg3CUl-EcjnYegWshcQnMP_Jf-QUVQlkraAxes5UVwUfM02ApCEx3Md3oHMvMNYxmInGi115kWgxT3EVvs_BIkR1Q4P5I8A6K5fEqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmwfcaoXrrbFuCHq4tQt3qm21i5nQx1lF6RwwLEi4xI9m5VVgIdR-eOsqIX1F1lWSlK0mZGr0ecuKLmnLW3Hc7RxjnkVVA17HZtWjsabg9Cy-I39I3XjOJPDsxTBOCvRRU7JTxBVrJLjU9KCoJ9y3FUpdKbooE8iVAKQJnFVjVl3Nyc8kcG5HvVsY5f1QCnAufCmZEKEQxgkMf9mkJ6LQ0dCnEIbj2UNHV0k6f4v_SfFbrdFIPyn63SYDKE795RzJqtnaoqyrPbFFIBmxqynLAed0sXvatTK541pnrdMpGRM7LhfUZDMaxGEkntcfrsLWYPCCXNqY43BAw1MFEwJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ9sJkcQg_7iTp2KFyY0YP-U84LQ_cPAt6B5xkXeRpItKDvLqq7F7ajWnY3YcbxR2CI2hvsc99poNanaLnKgpepkTa4JzU7Q_zYJDN6wkIM8odz4Tv_bjBbcZoUmHsf-3vrHiBd_dVtTmq0HNFcHdktm9j1TIfBhzCz4fuXQtx68dzGn-O0_9B4aidIl2muyJTPLTOmHsZu8XT7TnTM4HkQ0IJh5GmqlVRwt6Sr1VFGnCFB84h65mX-nj8-BVzoHhSbnayD-yEvdnp_vwNFooullMHojRWmEFzZagTQJ0X5bwLuAY4sOIv0wmgSJ3ovlHyFjm5ZDFo4vnpmhO0gAzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6hROXIIAKRqTR8S_Imz5TNsyWoyMe9cOwuMbVgcEQqIHf3ANXgHxoDyCiFS-BhZ_nJqb6cEP6qEU7NMS7MsP8lf7hvycAf_5sLXlW9iuLG_T6haLr6s2oC8ql5MZaPRwpTwDoTPRN8om_2fdrwtSuSzlzBTBPaWXedU6zwmvTRNVS_BO9jT9Xj81FY4J59fQ7mt9hVZyEyYCSzGEdjSwPnfH7j_HGCbAPQMKkp6yw-Q0jBeZCfW3B2N75gNLZuwTUOYlfKPB2LLgB6M2vglm28kFWpk3LZnnOwGmgaGnvNwRfFRTHJl7jykf_o15FbIbWKDs05JMCWmv3IRUjbOGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPG32wDtJCg06kuEfDDrzyhT3mzZffn13fseFz7yd5YbzrNCX6P5yzB6Z0M9-9viVImhXRKyaLHFR9pr4XrVEsCfEaXGNNxoGaup-agpiVvAoCwm5o4GXueatGgb_bL1Fcpwu5MOzvi0OHAwL_FkwLgY3Tc_2TzFRfNaBBIcyjyUuLaKyZSVN3hA8erB6chcm4IixPomRHIZiS0jJvYbfrNqFOIHrlxpaWZ3nixjui0BGVi_eM4JGCo5p6lI_TB3xz0ZTWSbs-Mq_M2ctgrtlM58bUuxXcXykTyWttLeJ0Jz56x_PV8B9yhbRpCZA7jlBxm9pFXUt_E-znaZprzAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJZVrwYOz5JslunUJmX6W7A9aXIDKJUq7Kf7fQO1Lf--SODqVGjosBxQOF4Su8k1o-rd7Sym5XfNIBJcA-gsFwNQ3RN83zFPLf2MIEj0CuoqbCjP3gx52ru64D9wY2rpwUl5qGv7_Eur4JJA3GyP7KSimJ0S-1EslGx-E-U5icHm2Ii64ZiWcbS6TZ606tVbFnWpGwUqy-vGc26FC_WEInmdOqqGap42qWZSuMdCs2wqDa20LCgNFsaWiLl7Zk_glxhPpQh47gYnlqJ_PZdQRwEldJska8a26AJUbdrrwrhxTlgiMDlq6ZD3B7hgEbnS9m14lZCLQCoTLFaW1_MddRSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJZVrwYOz5JslunUJmX6W7A9aXIDKJUq7Kf7fQO1Lf--SODqVGjosBxQOF4Su8k1o-rd7Sym5XfNIBJcA-gsFwNQ3RN83zFPLf2MIEj0CuoqbCjP3gx52ru64D9wY2rpwUl5qGv7_Eur4JJA3GyP7KSimJ0S-1EslGx-E-U5icHm2Ii64ZiWcbS6TZ606tVbFnWpGwUqy-vGc26FC_WEInmdOqqGap42qWZSuMdCs2wqDa20LCgNFsaWiLl7Zk_glxhPpQh47gYnlqJ_PZdQRwEldJska8a26AJUbdrrwrhxTlgiMDlq6ZD3B7hgEbnS9m14lZCLQCoTLFaW1_MddRSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnDtSkyJso1CqxxKYIs1l30zxzzvfDLF97wy2XMzA5N_brT-tAkRx_8jtfDUkotuWHmM3fSvdZq8fK90XUK-CrlcUB9ehjKLMN6ArzUSDFheV3VnB1TUR4ii6gRSYxEcTBUanKL3ZWY28YX_lkt4hzyf49ICrPa6vGMXz247gnvZV-w-w4n38Y1--aUpULV1sVQN02oLkzzYrmUUsWu30HO6G8Gu7ZT9J-dt6HGHgT6ZvdELXjtdgYRxIevbzTS4JLTiGXGMcl0VB81JRAxyStGtxVUU-TYCVXAWRLRvjG_9osn1bA_F8KodjZ9yoFspcaTJ23dq9ujLrSS-QvUKmKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnDtSkyJso1CqxxKYIs1l30zxzzvfDLF97wy2XMzA5N_brT-tAkRx_8jtfDUkotuWHmM3fSvdZq8fK90XUK-CrlcUB9ehjKLMN6ArzUSDFheV3VnB1TUR4ii6gRSYxEcTBUanKL3ZWY28YX_lkt4hzyf49ICrPa6vGMXz247gnvZV-w-w4n38Y1--aUpULV1sVQN02oLkzzYrmUUsWu30HO6G8Gu7ZT9J-dt6HGHgT6ZvdELXjtdgYRxIevbzTS4JLTiGXGMcl0VB81JRAxyStGtxVUU-TYCVXAWRLRvjG_9osn1bA_F8KodjZ9yoFspcaTJ23dq9ujLrSS-QvUKmKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=N_XAZG_ZULDRZ-qQANg-AfNqif1PQWoA4P9-OMMeG6GBAU2PkgzHIDlmij65fOvHMX2-cU-ADOMrCzwj0tGvd6f9_tab11DG1B_kzGJZFEdahN4GfwLDRdhA-iRLcadJH7PlwizHaZUFE2PJiArgYmwixJKTKKHihuAud3e-tugcS5DBykkVGjvop9K7zE4Rc1qzvzClsJmERNFjZnfuo3C-jE4eoF3FhzgJgN0idG59szGIl7ynr45hP3UZn9tFUCNgJepWBxpcFcPo3ZH-bkozEkoaJj9JcBKvL436dsnvYQJkFwkQ-lI_VLsyvRzLZFkNgvmLpHbatB8Fr67f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=N_XAZG_ZULDRZ-qQANg-AfNqif1PQWoA4P9-OMMeG6GBAU2PkgzHIDlmij65fOvHMX2-cU-ADOMrCzwj0tGvd6f9_tab11DG1B_kzGJZFEdahN4GfwLDRdhA-iRLcadJH7PlwizHaZUFE2PJiArgYmwixJKTKKHihuAud3e-tugcS5DBykkVGjvop9K7zE4Rc1qzvzClsJmERNFjZnfuo3C-jE4eoF3FhzgJgN0idG59szGIl7ynr45hP3UZn9tFUCNgJepWBxpcFcPo3ZH-bkozEkoaJj9JcBKvL436dsnvYQJkFwkQ-lI_VLsyvRzLZFkNgvmLpHbatB8Fr67f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
