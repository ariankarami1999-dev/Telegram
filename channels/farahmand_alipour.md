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
<img src="https://cdn4.telesco.pe/file/SepMfHyKSsnNNn-DqhS8P0aZbrxIyHWlV_CKhy3EflRsZIj76jcbAqwEPqnGLrAdBV_aYpOChwTMU_5k-z0z559iFKLpS1A3R8Plwu2l8L4wfFIQWJSkT_RTzrCj9v4EeNT_LdPINkZAmlD8z1-YgMXX34RqPJ4CRQ7IkpYDon4fmP-JqGeiJAoBSyjMsiUj2fIPwVQax68BMc5zT_EE_S8xt3M29N-taDtmxZyoytntb0IiEBX3IxGdJYKzGJunc8DQUgOGqCLvxxy19gvNRRSCI9J-wec8FGCaUzp-buFX98SKdXUGhq1-XLaDaJjuijisJddIGLpb7NOJevHy6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=WSXWH4OrIOevXv0ir4ZQ-CPWs6VIbU1yq_L02b3nRA-kVA4uJFCp9nCknhvgb3-94gAcqbqvnYUduKaLNVwIb2a5bGe7sIipZL1Vnp5NL8kDeQXPzhzFvLEWMYDJXtmhrHwLT6ItggGIALFrBNzJVpGkx02YrEZQYmGorSR4xB-G9K67GXMwp0BqTLsFhby0wOzPmlK-jtQsr9rHXB45zZ3v61c4I3xrb5aTLTYjURTv4u6ETa-fyooZwnNAugOM0YsFJH1mTTZpI8j7eZHlEKlODfwCDdw4H2Df4vj9hKVWVLaE7jgJzErDoMffYaBPQT58ybnyzUZXrptod8fHgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=WSXWH4OrIOevXv0ir4ZQ-CPWs6VIbU1yq_L02b3nRA-kVA4uJFCp9nCknhvgb3-94gAcqbqvnYUduKaLNVwIb2a5bGe7sIipZL1Vnp5NL8kDeQXPzhzFvLEWMYDJXtmhrHwLT6ItggGIALFrBNzJVpGkx02YrEZQYmGorSR4xB-G9K67GXMwp0BqTLsFhby0wOzPmlK-jtQsr9rHXB45zZ3v61c4I3xrb5aTLTYjURTv4u6ETa-fyooZwnNAugOM0YsFJH1mTTZpI8j7eZHlEKlODfwCDdw4H2Df4vj9hKVWVLaE7jgJzErDoMffYaBPQT58ybnyzUZXrptod8fHgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc-xv30h4RzEXN-kemBCnM_lTiz7OrVmECVyTAJZYrENACKbFlws6BpIZwkMcdqImWB2oLOUd5kvZ1k4kf_A8yx3AF0owcG1gyldXAwTb6Gb7g8inKintNZFzY7nRdo54qgBSR4aSPCvU12z4Ga7-fOMasgMA8Egtx0hEjPxF1Tjhb66DItayItxyv6i6mHszZP4RhGORZ42kAcrR023UROBZDXeyQz-fhPzTXCtFsCZEDxcc16Mkf2aGiY7Q9uK7ECIldXt2OQVQARRuJiV_zx-64Y2lqN9U0HBgz4RfopNBLfat46HwYj0KwxSiDE3et9IO9K3IsMqGjGUhT8tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DBSXdQvPCVJZO5mdmX84V8gV22pQqu-ija5g-z4X2nxRvyyT8z3XQQAf-yEf4Kd2kXHPCtecUcOLepXZRZPHNE2ro3IxQx1vgZykYwV2DLp1Td7isWFKreJ_OR7oEdXun6-BSEbGHwgDsTk1JIMLwK4s0mzOnypxI9Oqpt1ri8dwpJuEGWQuuCncdcmf1I2Hve2fFaDctzSg_qK3FZLWylNAZRwkyVZ2qxY2PvSCeaIU7NrYUn7R3sjuu3fgv5ysOrtD7FpeJpj-Hk5Xs1aAVnx5TeCpCd3jAWwBJ8qzWlRJnmgU6nHl3I61skVkzdq4_WuU7KLrFHBozPvV1Q7C4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DBSXdQvPCVJZO5mdmX84V8gV22pQqu-ija5g-z4X2nxRvyyT8z3XQQAf-yEf4Kd2kXHPCtecUcOLepXZRZPHNE2ro3IxQx1vgZykYwV2DLp1Td7isWFKreJ_OR7oEdXun6-BSEbGHwgDsTk1JIMLwK4s0mzOnypxI9Oqpt1ri8dwpJuEGWQuuCncdcmf1I2Hve2fFaDctzSg_qK3FZLWylNAZRwkyVZ2qxY2PvSCeaIU7NrYUn7R3sjuu3fgv5ysOrtD7FpeJpj-Hk5Xs1aAVnx5TeCpCd3jAWwBJ8qzWlRJnmgU6nHl3I61skVkzdq4_WuU7KLrFHBozPvV1Q7C4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=u2_TAJDOZe73SJ4oLzE51p-QMNaeVNWKcG0FyGYutoatsm2M2iWK5cDy1-9Sqf_hXuqR0HKmdudnue1Yp5Odr3Fj9QUkzjG_XDWrYrGNHypa2SRjYD6w6rdS5Ty_rqI4sSf8DVI5qOqgdOgZCUU_ol7MREqai2QDcx-r2oDBgxl5q9N7sTBa-Qm-tiJiQ-yQ7gH-DDfFidcmcFjj89AkBVV0z8zgbNhWnPfqAdBrWQsGuibX-zWbYo-ZYdUKmti3tHvIolh7mTGTHZAGUo1GZYVMpk-qZW8oeObvIdf2imm5ITYeRxqmC6pzBNl0h2iTVwZR17tOE83LdzXHFEz3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=u2_TAJDOZe73SJ4oLzE51p-QMNaeVNWKcG0FyGYutoatsm2M2iWK5cDy1-9Sqf_hXuqR0HKmdudnue1Yp5Odr3Fj9QUkzjG_XDWrYrGNHypa2SRjYD6w6rdS5Ty_rqI4sSf8DVI5qOqgdOgZCUU_ol7MREqai2QDcx-r2oDBgxl5q9N7sTBa-Qm-tiJiQ-yQ7gH-DDfFidcmcFjj89AkBVV0z8zgbNhWnPfqAdBrWQsGuibX-zWbYo-ZYdUKmti3tHvIolh7mTGTHZAGUo1GZYVMpk-qZW8oeObvIdf2imm5ITYeRxqmC6pzBNl0h2iTVwZR17tOE83LdzXHFEz3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrMq9Wzesq4_4qIkok0LNTAIB14CQSEIakyKX21gkiy6QjZabNqYmzz6EIYXEgVCzWSQ8i5gpnW6ttH98nPNBUNBgQChSJjPzrhx6TXqWxmPt1cEh9BlqIePYj5Hf1_vAlo-D7T0tuRgp5OxkHKi6Rc0IKl_gbnE4XOzHDyqskGJtOu3LNnwcP0MCBdNp4e2BoHVcWodBS5jOI_pOAwce-lvYG9NU5KivSYnZoizgHdfGgGf49ediMcszAmMT1snuVzRtn3w5W8F1plyjZcJgRs6q5SxOyXZKV8rwvE05KtdGrI9Be4cRL77BtfqRV34BhjixmtFO25_XCCth9WUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=l2jQvmbDJBQlNa1OwpLS5cU_bJUxNbHO4Iv535ylGb8pJyM1TTdMn1tArP8y70CVXPLGHhr8Qa5rsbforvn2h5UMEqUBswK033ez4ZCJUWp3jBmQqbEWvcQj5OnAr809fmqAuesvD8Ao9WwHjp1j9QRRV15INQTlEQjKWeMHmeZ_KcUJcaK4O5wTgujU8b9jx-Irn7-DacBzA4PXnYecV7_RSe5853BZR-x6esz_dnXWfI0q8UPApCuKXI0QmiPuZeqy5ChdopKCM5tyDif9F6n5jqrBo0A5t4J7rwPAmxPtkBBwFkIcpQzd2Npyqr3t5q1O3sMkYmSqfnu-EbjRyl8BbFOObA5rw1tCNCJbdWZxmz6lnnQ_YR0hlyEByg58BxMHvh8wu0iab10m8PH32lOoBS7R9Sp9xByfYu9DCZXMn60GacrdwHBCDm5lJz2d_Zf-CMubfM73jp-cbUpOcjeDSmmDqt9zAkLp9tRae0WP-q5OhtG0iU3wD7N8KXLuSQ4H9JkOfp5GsCkv1mdwita-9-PZLh07nC5DgAFrwOGrtUsP7oPRBu0LWJPUcmPDwPkaqSJDyb1E1L-8CIVvagM5OYHbCYJC5qoztNj-0GIx_ztvzPiAwh-RWcn30ScDdnC9W5iwqwkgrBxT1-_ioQfFVPUBSIUiU3c7TjhhSTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=l2jQvmbDJBQlNa1OwpLS5cU_bJUxNbHO4Iv535ylGb8pJyM1TTdMn1tArP8y70CVXPLGHhr8Qa5rsbforvn2h5UMEqUBswK033ez4ZCJUWp3jBmQqbEWvcQj5OnAr809fmqAuesvD8Ao9WwHjp1j9QRRV15INQTlEQjKWeMHmeZ_KcUJcaK4O5wTgujU8b9jx-Irn7-DacBzA4PXnYecV7_RSe5853BZR-x6esz_dnXWfI0q8UPApCuKXI0QmiPuZeqy5ChdopKCM5tyDif9F6n5jqrBo0A5t4J7rwPAmxPtkBBwFkIcpQzd2Npyqr3t5q1O3sMkYmSqfnu-EbjRyl8BbFOObA5rw1tCNCJbdWZxmz6lnnQ_YR0hlyEByg58BxMHvh8wu0iab10m8PH32lOoBS7R9Sp9xByfYu9DCZXMn60GacrdwHBCDm5lJz2d_Zf-CMubfM73jp-cbUpOcjeDSmmDqt9zAkLp9tRae0WP-q5OhtG0iU3wD7N8KXLuSQ4H9JkOfp5GsCkv1mdwita-9-PZLh07nC5DgAFrwOGrtUsP7oPRBu0LWJPUcmPDwPkaqSJDyb1E1L-8CIVvagM5OYHbCYJC5qoztNj-0GIx_ztvzPiAwh-RWcn30ScDdnC9W5iwqwkgrBxT1-_ioQfFVPUBSIUiU3c7TjhhSTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U03Tyxz-YyX7NipnIJK3_RyYk9UB1F2ju1L8vWjUHq5tzsL_2XI-QLTsHKu2e5paIMBqZCot0l6-ZevVWumrPY0aqoAoL3T9KvN_I__eUWwjbh6aa68Lp7WGXmdX_eZoq_Jla419Hh7zLBZOe6h2h2KbkAsdRyxQ5WhAHKP5100Fu9es6ufcyu3oeIP0YqM_ENfryLHlMwIlmhvP35pO7FmVHhTSLlxR-Nmr0cctn6SabcxGjLww8pAQW4s0I04D-zAgBiNH5LMPNvM2vlToAbRjG4BU7cGNhUmPqjqRZ7nf5GXVQzcfz9U40PLCO-vDFZeUKGzkHUUXUjaNodq_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=KlmCR4DBDyHqws_AdCli2bhNqi-cB7zcQIETnYdXyQOONbC78_kQhH0__WKK2VwW36Ar8Y88exWXWoxJcwNMuXAzcPQNBux1U6OJ0QRzU9mymjW5U40DlItvxIOnoomkQFiVVaC4ha6yT1ARL_Loj-kn1g_v6K0tDF3CuDrRI3JlCr0pnHNyK7ovHsyrw_z9D92i20HgR0MOuLj5VtB8qfhCkeEzadSzqWYWLnmXbSOREgz3u8G3vd7Pp8Vafj5xCVhjthRszYn_mi8GtPp5P9ZqFP8-M-uGv9VHM_WJGgCTJZOHeNpwBztb5mtubpw9f1adVRf9qlBQH-_YjbKUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=KlmCR4DBDyHqws_AdCli2bhNqi-cB7zcQIETnYdXyQOONbC78_kQhH0__WKK2VwW36Ar8Y88exWXWoxJcwNMuXAzcPQNBux1U6OJ0QRzU9mymjW5U40DlItvxIOnoomkQFiVVaC4ha6yT1ARL_Loj-kn1g_v6K0tDF3CuDrRI3JlCr0pnHNyK7ovHsyrw_z9D92i20HgR0MOuLj5VtB8qfhCkeEzadSzqWYWLnmXbSOREgz3u8G3vd7Pp8Vafj5xCVhjthRszYn_mi8GtPp5P9ZqFP8-M-uGv9VHM_WJGgCTJZOHeNpwBztb5mtubpw9f1adVRf9qlBQH-_YjbKUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ktOz-ivEjARKzIhjEikGyQgqsgEyCdW3InRpcux68fv85nCkUVy3yg7hhlrfAsbG_YSxx6FTsxwqsibwLdCnFyzFPM06NroqKyarkC4wffrRoP-TfaLqrGU2pwAnuZJPeu6xWifuREXungP6D8SSv2id0Sc55ipM7urrNT_y30EN_ycf3Qmuq24Ov3V9xKXXWnsuzM_xXcCVgHBXAFiUTIGafKOrXh26j_DIgRvsvzFMEz-drCaJoLxPxn3jzogaNNuZVLbcD-sljrbfa8Cf8h87TAqFr4raGX0r038PDVqwXr4SDdtP-nEmQPXQDdokO0fU1cAztFav4Q-SaZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJllLWqGcfN7Cq1cBHIoVVC8-HFT4o0dQEABs_V_LDKdEWjve0OjyWc603JbH4fyuoFSmh_Ieiy7Pe5ZlwfgD5d9INQpOxAryvAcAA2uAt3QWnw365JnejRgdj7ync2_eXT35Fh1sdwwH6jaPvvj47jouLA_hRNoAZVB85pKvhGKXaCb5TKJxhFYJHFvMSGb77jmD_-RuUDVh_hh-tNCzEypgrR2K-nb0KO8fzqQmR1XYCuH1V7Mhb2T7LpD_BOGW8TBvecVRHMn01hbYBoh8yR1ZcsqQdhwh-YYyIHTxXIExd6aMuAzx8EsH3WQgfzZTIe5X_VSTKbSeKSxejqWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRen3YIZczMjoZKUMZfD0VYilxG_2jkAL9hsevgRE5soBwEn14A-rdwS4g7EVMhlUxMWsH-PS4ppvaI3c0xDEBoyeR-NDX-YSUvs5zDs1SZSqQts7xXckNZyl5SBAyn55Tas_hrpnVBIVpLD9F5nBT7uwREa11cezX8Yc-4vo_BxM7WEObCgy0Qay7VSXU6TiuQK9-ylvFkbdEzvO61h6p19xrQWgODiRoRxupUmdBwBfqOrB2Enci7C4e81e7nE_h1_rzswg5KVnstN391vBvS40r5eLIcXR8Ag2k4owluAa5yHX2whvQaBId8Roa-nDwI2TxZbLtGNh2ko08dqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=pLxeaz7oI2uE-5lo8e2x3iGapfVcX3Tjy9dJ0_LNmaZ4Xn85cnzucs9Avvwv1pBYDvj6BPbzxzwozhQ6UYaUKnHimqI-0-rth7OWm5V213aON6v3yo_6hbQiG1yBx8xXMBDn08hOei8QNDefhzzJpPXMjfIGT-5YKF_QtcrLE8u146nLI2Xith1yjZ_hzeM-zG8OD6JAHLN9Dt6Ma1FmUHveUGg8b_3ddo7Hbp5aoB9ytzH55mGmmZvsXYrfC4onOh-AyfM70IeH7_WAc5tX6Tbqb9QGDkGHwojwDbkliF7xkUR6sg5YV6R2iUZVxFflYkwaXcINJBRUUjVo-035zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=pLxeaz7oI2uE-5lo8e2x3iGapfVcX3Tjy9dJ0_LNmaZ4Xn85cnzucs9Avvwv1pBYDvj6BPbzxzwozhQ6UYaUKnHimqI-0-rth7OWm5V213aON6v3yo_6hbQiG1yBx8xXMBDn08hOei8QNDefhzzJpPXMjfIGT-5YKF_QtcrLE8u146nLI2Xith1yjZ_hzeM-zG8OD6JAHLN9Dt6Ma1FmUHveUGg8b_3ddo7Hbp5aoB9ytzH55mGmmZvsXYrfC4onOh-AyfM70IeH7_WAc5tX6Tbqb9QGDkGHwojwDbkliF7xkUR6sg5YV6R2iUZVxFflYkwaXcINJBRUUjVo-035zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnF9zx8bpbTSGZxaQgyRVW3ApJgIi5nDs00GtPz6dQRjUEYRLctTArX4dTDWDEzeADgTCgLuGFWS__KKlFAwTGgP8U3tSPIr2PzTMd-qzxVotz7vggJrbFKieD1KQhPRcsS2_DhZG3XbHbF5nME10R6vYFf6fd9CLNiqtn_TI10glwGpxKBdKFVafSzTzHVCX8Yso7Fa2MV_Z0b6n3rfYeGfWL5w-pBSAbGikHPHJpX-rFa4q3TT7UAH_4kQBTB7G4NuvSYekie119A0S-T78TgX8h8f86bwQPJ-xodduC0IZBXDTvEU42kftnQHRM8M8n68PL-JlnOnynUGftQJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2Ig1O0t1ISVkkbLCKqsB6lTE7uiqptktOdY13j7jkSvuNcDslO5Ad03jDxaW3guFGaZ1QLI_a4XTA9w6tLKI1iOcKYWs6bHqvQCX1mWhhkYntDPq-xltYzul91uhu2VmIuy1UI22HKoy8QKK_3odTbNShmaGgrvldRtFISJyjIYLWH0J2fQuaxhSRtwneJHBg51DfPWhudGp3UJuUtD1OEFqCxAz2AgP4OSlR78Vrt_hf2rSvNo37Veb6CAb4vEHF347WsH4BWQTppgkcCLkLnN-z5NUh8VxOF-orREhvU0weZL_5YNLRshL2TRZhUDjcAVgMHQ7hHCK2maVIBpnHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2Ig1O0t1ISVkkbLCKqsB6lTE7uiqptktOdY13j7jkSvuNcDslO5Ad03jDxaW3guFGaZ1QLI_a4XTA9w6tLKI1iOcKYWs6bHqvQCX1mWhhkYntDPq-xltYzul91uhu2VmIuy1UI22HKoy8QKK_3odTbNShmaGgrvldRtFISJyjIYLWH0J2fQuaxhSRtwneJHBg51DfPWhudGp3UJuUtD1OEFqCxAz2AgP4OSlR78Vrt_hf2rSvNo37Veb6CAb4vEHF347WsH4BWQTppgkcCLkLnN-z5NUh8VxOF-orREhvU0weZL_5YNLRshL2TRZhUDjcAVgMHQ7hHCK2maVIBpnHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6o5hNVxv16PXfsJ97SxVnL9HOk0m17X3q8xEaOQ7kFwZig6eM7L_95t3xMWG_L3AdtTmrLA3IqTEdmxUlueMPpgLyh8NobOqb5zf-zZWAioDwcz8otYxvFO0PEef8PZBCVDqH8GnWy2kpGSeXWtfi6KHUr2NW6BjDWm0OVK-cKq1kyZ1bovMwMFFrHRcXWsBjBGpCiA3A5aOb14LKyocGToNTgK6ZU5vM4nlKfOjdvXIF3GjRc35ypu9keTo5fAoqdzPCn_-suPCJNdMxkvJE56A7v238-QdzqMaGPV2dYOsq8Z6xZjhDFtahzcvDxG9oq5sK1_6UccH6-YHS2k-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6o5hNVxv16PXfsJ97SxVnL9HOk0m17X3q8xEaOQ7kFwZig6eM7L_95t3xMWG_L3AdtTmrLA3IqTEdmxUlueMPpgLyh8NobOqb5zf-zZWAioDwcz8otYxvFO0PEef8PZBCVDqH8GnWy2kpGSeXWtfi6KHUr2NW6BjDWm0OVK-cKq1kyZ1bovMwMFFrHRcXWsBjBGpCiA3A5aOb14LKyocGToNTgK6ZU5vM4nlKfOjdvXIF3GjRc35ypu9keTo5fAoqdzPCn_-suPCJNdMxkvJE56A7v238-QdzqMaGPV2dYOsq8Z6xZjhDFtahzcvDxG9oq5sK1_6UccH6-YHS2k-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=HdzkjcsON1CdlOUf5kT_8VxIOPks2Ny0_luJ6TykhFzDOaJGgkEV-zuLFsn3BEeLj4wD9BRjmUX_AZp6TBZ4IJ7PBSCPB-BD3i5FKZZkOaBRI7t4CmW_YSyOTj0rAKfCqH7zAe19lHSMRm-cgYmQp9aPupkPmP6HdFEaMb336EwIsWNuFJ3CrpWLDmwXZlnTabrwsSf1cqUGBMxJec0gNekC791I8Qal7wRASIPA4Jd7SVz-ERWmZauqGKEXwJML6KmgPkBDquGHeLXGxeF1RgawrpXP1uCE0uTSUCQvTdqNduCasIUozwNHYAdSCkxfSAGwyON-kwDiy9pmQLr0oQK0DGz8x-UHWx7agGRAjGq4JegBrmZ_iop1Dlj9FFEErhPkbmcrLL8sltp04lkUrfGifKGbWJwgCPMvtb95T0ckGX2hx4BT4I4eyZvGESDCRjOIjUy3jmu_seMRPUMAIy3OsSs7Y5e8CqumWMMM0uLjUjNxgbQOhaiBY2CWQpIw0Z1JSzEa5KTYlqJ1VCZZySvgTPyDfWQSeoCnK3ZFR3xH5_6LXov13F_MhMvk5vs2F4flEDAcWx0PxQmsVA02ecdZ2UO3lj87h6T36iyM639q_fRGU-kRS6rErC0FRKa02wEr9dbGtiVMfVTUq15-ayrrggvPHJhXcr60X-XVUso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=HdzkjcsON1CdlOUf5kT_8VxIOPks2Ny0_luJ6TykhFzDOaJGgkEV-zuLFsn3BEeLj4wD9BRjmUX_AZp6TBZ4IJ7PBSCPB-BD3i5FKZZkOaBRI7t4CmW_YSyOTj0rAKfCqH7zAe19lHSMRm-cgYmQp9aPupkPmP6HdFEaMb336EwIsWNuFJ3CrpWLDmwXZlnTabrwsSf1cqUGBMxJec0gNekC791I8Qal7wRASIPA4Jd7SVz-ERWmZauqGKEXwJML6KmgPkBDquGHeLXGxeF1RgawrpXP1uCE0uTSUCQvTdqNduCasIUozwNHYAdSCkxfSAGwyON-kwDiy9pmQLr0oQK0DGz8x-UHWx7agGRAjGq4JegBrmZ_iop1Dlj9FFEErhPkbmcrLL8sltp04lkUrfGifKGbWJwgCPMvtb95T0ckGX2hx4BT4I4eyZvGESDCRjOIjUy3jmu_seMRPUMAIy3OsSs7Y5e8CqumWMMM0uLjUjNxgbQOhaiBY2CWQpIw0Z1JSzEa5KTYlqJ1VCZZySvgTPyDfWQSeoCnK3ZFR3xH5_6LXov13F_MhMvk5vs2F4flEDAcWx0PxQmsVA02ecdZ2UO3lj87h6T36iyM639q_fRGU-kRS6rErC0FRKa02wEr9dbGtiVMfVTUq15-ayrrggvPHJhXcr60X-XVUso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=sn4riaP0h1N4ZQMatEbc14Sql3f4_sxyBBx6ChYRc-wpioIOWFcEQ5_TDnxPYZDpFAQfvb99JVAOH_wMhB0mrGyWGSFIpGhBMmnsGh1xy25QKrtReFmGkrZiC4paSeewKPwBxzywNl59Ul_efMnsG8nqcUR5eGHhZbFBimRJsNelcgJNW8urkJ_7sL8ENPHeA7LxWV-DOHkN0fH0NduGmD2rbMlwK4CJiXumQenSKrRR8dRZTgt1FfpUymecrjqq7BMzHeG7MhbVPGGlHYpCb_5WKetwujOGHslFfp4SfRd2_0hq_8rJDcxfFMO6rZZHdYGYvETPoP32DZMtPXsWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=sn4riaP0h1N4ZQMatEbc14Sql3f4_sxyBBx6ChYRc-wpioIOWFcEQ5_TDnxPYZDpFAQfvb99JVAOH_wMhB0mrGyWGSFIpGhBMmnsGh1xy25QKrtReFmGkrZiC4paSeewKPwBxzywNl59Ul_efMnsG8nqcUR5eGHhZbFBimRJsNelcgJNW8urkJ_7sL8ENPHeA7LxWV-DOHkN0fH0NduGmD2rbMlwK4CJiXumQenSKrRR8dRZTgt1FfpUymecrjqq7BMzHeG7MhbVPGGlHYpCb_5WKetwujOGHslFfp4SfRd2_0hq_8rJDcxfFMO6rZZHdYGYvETPoP32DZMtPXsWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uy4nH-kKxODfNjdSGgbAfdein1C319E-D48YMNe4kW6BUuMg-4tMXjZo72hxcR3eGCzg2zE76mMyfPxJAUGG4g3tzM25TcdgoRXv68NY9PgAFBbZQSJ6chmCL8Z8CSvIt4RIWRIVjcV4-fW_m30vlkwH7jZpfi2pTbo5tmr1LqhrLJq8e9dlC7XSh2CBuCkUNHailwpk5FjKld5viOf6EInSkbSLvXz7jSanimdJGfnp-A7F9WFsTxYvrgHlM6BBAau-Sl7jJGBhdZiNELQlhmKxGW_8Cr3_C9qggjNBacfRhF6wIYyw-kY4RLu6AhMf4wqgMyVuWIUPa1MuZLsNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=RmO4Q3kSGjrq52RYNjwOAtzC4wije_yDmRIsH5vhiEsobk51OULaGmQoFPpJSNWhpHHa04EICoOjv5Q57ektV0W_peR3k3SUgayrJ5g2dO-xl8rfxBPYDd7J1ZbzlFAEDnzcRMisAI-l9OMbkgVg1Ap-xK61SmzBJPODGgJwWm2fhUl55-lCrgQX3ra6a-4OMd_wWc6OMysOesgdjTNNjBwZwTX7o_6YKBtYmsIDug5Xdc2Pa7jSrsGyLL6dbjzUW_7Wukh33JH1Fh-2UNEZIAKMEH5UN0Elf_za8OcLMD6HzHVv11ZjNl4bLAlPz_Y530AsexHqT_xAH_osGqJPtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=RmO4Q3kSGjrq52RYNjwOAtzC4wije_yDmRIsH5vhiEsobk51OULaGmQoFPpJSNWhpHHa04EICoOjv5Q57ektV0W_peR3k3SUgayrJ5g2dO-xl8rfxBPYDd7J1ZbzlFAEDnzcRMisAI-l9OMbkgVg1Ap-xK61SmzBJPODGgJwWm2fhUl55-lCrgQX3ra6a-4OMd_wWc6OMysOesgdjTNNjBwZwTX7o_6YKBtYmsIDug5Xdc2Pa7jSrsGyLL6dbjzUW_7Wukh33JH1Fh-2UNEZIAKMEH5UN0Elf_za8OcLMD6HzHVv11ZjNl4bLAlPz_Y530AsexHqT_xAH_osGqJPtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=jvLoSmE9kHOCEwUOhdga2vtJcDzWmgZXfHnlQvkaPTmC5Vo7DJ5kX0_IanaX6d-EHxkZlPMDW_xKEmQDchQ6RUuszJgn3KKL8zKMBqG1BnnXX8d7jUzk_xB7fPqdAdmz7IK0Svyo3CFmxfi9y6Hq9qW0-8SmOqRvGprFM1mVEUQDHbd0tjmYHAuxwjqMl7mqnEdYFFuB31AcwkT2Ya-yC8zOgX3n6QODSTA_JR_7Up04ZYjNPljH_1PlSHQyDQJ8HxcGxA0QIA14Kvh8WbQ3ywXpKvrVlaTE-bwqFm8NH_tCfstTAFt4ncBkOP0OIjW9-c3Y_QhUE0qLdn8EX6CCPz1Jd5uguyzmp8KK_GJmyUi5GcJMCd0sr7tXuzSFK206zsx4HREVZyAPG6BUQTa1DgJLwODiV-opYBqvcaM1ON4UywHwdtsgNzpB0p25Y2RPvnczmWKWspS5qfR4-5nijrWgsnXyCNfXbDL_hdip3-CzzgMAhPoX7MDGzz_IrkhwLafRQIyiJ4mnKYYoCZtgLybaZddu5fUCzUd7VOPD3nWZ8BfNccMSF54nBc0OeLU6_HSbX8uASStOMkKNjVxjSp0OjJHDhXDGrG6qp9Go2GcyJ9aF66CDUyA_nARcwh6l8dY68U7tYCFGR7VfXtk0McIq0b_OtR-lFhjl7_XUrQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=jvLoSmE9kHOCEwUOhdga2vtJcDzWmgZXfHnlQvkaPTmC5Vo7DJ5kX0_IanaX6d-EHxkZlPMDW_xKEmQDchQ6RUuszJgn3KKL8zKMBqG1BnnXX8d7jUzk_xB7fPqdAdmz7IK0Svyo3CFmxfi9y6Hq9qW0-8SmOqRvGprFM1mVEUQDHbd0tjmYHAuxwjqMl7mqnEdYFFuB31AcwkT2Ya-yC8zOgX3n6QODSTA_JR_7Up04ZYjNPljH_1PlSHQyDQJ8HxcGxA0QIA14Kvh8WbQ3ywXpKvrVlaTE-bwqFm8NH_tCfstTAFt4ncBkOP0OIjW9-c3Y_QhUE0qLdn8EX6CCPz1Jd5uguyzmp8KK_GJmyUi5GcJMCd0sr7tXuzSFK206zsx4HREVZyAPG6BUQTa1DgJLwODiV-opYBqvcaM1ON4UywHwdtsgNzpB0p25Y2RPvnczmWKWspS5qfR4-5nijrWgsnXyCNfXbDL_hdip3-CzzgMAhPoX7MDGzz_IrkhwLafRQIyiJ4mnKYYoCZtgLybaZddu5fUCzUd7VOPD3nWZ8BfNccMSF54nBc0OeLU6_HSbX8uASStOMkKNjVxjSp0OjJHDhXDGrG6qp9Go2GcyJ9aF66CDUyA_nARcwh6l8dY68U7tYCFGR7VfXtk0McIq0b_OtR-lFhjl7_XUrQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBOVNbhSdNUGlird8pqHhhC2OJ4S-YQnZnN0zcEqQm7d0oUa3fQilTmok-R94qgf-JVLp0hot_O3OoLN8nmrGoDSGw9nCD1hGp7r5TeoU9oleJqVRPqXXLTGuTqLHxvEwlhzWVS-bHr1F_jBZKEyUOd1e8NU09gkvLpQENpp4d19ahUNniOr9ImK5V_k7X47h4vLscd0NzZgpjtdR6Lfp2_7XRM7FR3YwmAm8BY4SZ46MPPqDj4EeGnvKriBQLLtNHBulmeON4N3SymU5F8CkWCaMr9Dklog3IWSdh4dt-hCqhi9dJ6tD1RdHzazy-vWN2JsSg31vbSF4IMTUmYoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=IsD3Ta67_jGoQn7sJXMv58xxqkZ6INp_6keXn2Nk5suyOom8to_96UcGiP821hXoFfRjxxffNqk4NjRBV7obyqQ7jNqKNECU5HnIkKxY49a0fxh5jjS7x4WJR5RJrOaFLf2JMulOE_co3jA01gLYKcP1SAPSk1b-MF6lUBdq-d3fqZ1yrBpAlV0K1Ov4GNUL_daFPfCINRseTFr8FEYzsSqcCskLijG5dUC5Cg985I1QWUDuU9hOzSEjctmQEFjbEH5WWjwB3m6_DhXjzMK1_lmZM3Hwk1uP86oXLKn8xYF8flKJX3Evfu4s5ov3TxOpuRRqYZDd79ZazwjsQ_9xMaKStBCCB_1CtnPoGBG8-3-N17XozEiWXPqrQvZ6jjk0ygRXBeyudluJlfNXJO0QypRtBj5wpR7cRvlyYM4pr24J5GvAuYnanuY6BwXIlEPrqGSEzCSQJu9IBV248t9HqF_G-WcWMKtT-O7nxnILNHY8K9tdGrFcrRG-J0v7J02CoyDJ0Nec9aVyH-Ya7ZBjTaUCf-idpaV9KXSA1djaXtCsfeW7f2q2m3NBL6xjIibtUYkyBITiZjamWMb26Rd5T0tRFAqKJ0KcBK-m37xXBKuPG6dsNIx3yNS-Npm-zqKZjnJxBCQ4rF7v3sNqqJtaqpP6dP7YBNpq3LE-rY4RfcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=IsD3Ta67_jGoQn7sJXMv58xxqkZ6INp_6keXn2Nk5suyOom8to_96UcGiP821hXoFfRjxxffNqk4NjRBV7obyqQ7jNqKNECU5HnIkKxY49a0fxh5jjS7x4WJR5RJrOaFLf2JMulOE_co3jA01gLYKcP1SAPSk1b-MF6lUBdq-d3fqZ1yrBpAlV0K1Ov4GNUL_daFPfCINRseTFr8FEYzsSqcCskLijG5dUC5Cg985I1QWUDuU9hOzSEjctmQEFjbEH5WWjwB3m6_DhXjzMK1_lmZM3Hwk1uP86oXLKn8xYF8flKJX3Evfu4s5ov3TxOpuRRqYZDd79ZazwjsQ_9xMaKStBCCB_1CtnPoGBG8-3-N17XozEiWXPqrQvZ6jjk0ygRXBeyudluJlfNXJO0QypRtBj5wpR7cRvlyYM4pr24J5GvAuYnanuY6BwXIlEPrqGSEzCSQJu9IBV248t9HqF_G-WcWMKtT-O7nxnILNHY8K9tdGrFcrRG-J0v7J02CoyDJ0Nec9aVyH-Ya7ZBjTaUCf-idpaV9KXSA1djaXtCsfeW7f2q2m3NBL6xjIibtUYkyBITiZjamWMb26Rd5T0tRFAqKJ0KcBK-m37xXBKuPG6dsNIx3yNS-Npm-zqKZjnJxBCQ4rF7v3sNqqJtaqpP6dP7YBNpq3LE-rY4RfcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=LPDDZwkmcIfcnIGx0IFPQKTa5U2UCdf_FEXAAsd13DJZzfRa5FNQwfdZoejHvbyZ7PddhGvn5ur71b6Rq6bGyM7wRnsljInqS50jLgLJQF0ZB7moviMr_aZ8f9NU8amhpNHPO3G7qvqj7UyjWjOMIKGsqcIZzyn7h1JUN45uQLfGT01EZUiyTNM8K0PrcDmSE7imkEmQN1E1MONwWOFvAOHNs2hteIaIozARne2s1wn2sdk5_eXMqcvXNeZSFLcjZ9m0Jeg_grm3_u2-SnGn6jAvEzWn1uGwWRNRSA_skauTcOgiZlPAdCdwumyL1hnLyR5EUPnHTYfsBUtKcK38HE7XPceMVebGgJZ8RcwQ_ctDdPsu1fnfjXNvNC5lxIqr326tCCvAv90soqnXCf_g7JVFoIktJs_c3qiMgo96Fuh7-Tghi9749Segv6s6zFs9MSbqYHGZ_LXsnjfmmXAsjTGmj3xRHbS8xE8b7hjDAGgIyaxbU36zUxayTYqv-Qn2ijVBpXl_9g72XnbOjZHmfK-pvvZdt6IPfByCJiQ9Ggmvnr49OfLL2cz2PbEn49wyOG8OSNohhNylKzrFO7v_pTnHkeAldZO6RF0Bfd_0pvNskRYmxDu5mI401nalMwSaQLwA9Hr4Sf09IjbppOmXD9eH8GCeC2pNBygORG33GpU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=LPDDZwkmcIfcnIGx0IFPQKTa5U2UCdf_FEXAAsd13DJZzfRa5FNQwfdZoejHvbyZ7PddhGvn5ur71b6Rq6bGyM7wRnsljInqS50jLgLJQF0ZB7moviMr_aZ8f9NU8amhpNHPO3G7qvqj7UyjWjOMIKGsqcIZzyn7h1JUN45uQLfGT01EZUiyTNM8K0PrcDmSE7imkEmQN1E1MONwWOFvAOHNs2hteIaIozARne2s1wn2sdk5_eXMqcvXNeZSFLcjZ9m0Jeg_grm3_u2-SnGn6jAvEzWn1uGwWRNRSA_skauTcOgiZlPAdCdwumyL1hnLyR5EUPnHTYfsBUtKcK38HE7XPceMVebGgJZ8RcwQ_ctDdPsu1fnfjXNvNC5lxIqr326tCCvAv90soqnXCf_g7JVFoIktJs_c3qiMgo96Fuh7-Tghi9749Segv6s6zFs9MSbqYHGZ_LXsnjfmmXAsjTGmj3xRHbS8xE8b7hjDAGgIyaxbU36zUxayTYqv-Qn2ijVBpXl_9g72XnbOjZHmfK-pvvZdt6IPfByCJiQ9Ggmvnr49OfLL2cz2PbEn49wyOG8OSNohhNylKzrFO7v_pTnHkeAldZO6RF0Bfd_0pvNskRYmxDu5mI401nalMwSaQLwA9Hr4Sf09IjbppOmXD9eH8GCeC2pNBygORG33GpU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=eWjX3-QvMKsDsYAWB27vfhfggbrsQ4vYGW7DrGVWsfNNA-9b6ZyUR117EJ_U6seiVetneYd6Ulq8uQGvweSwCkgoKXCs2QiYUuKL2A_IYG7_MWbMcO3diPgAJnvE0L2eD0BPIPCievYJAaxINRGBzv_VT2F2xt-GH2BPIVlINvelAOAY9vPuH-WtEgZ75kheiNhCUrsgATNQEVWPX3x3fbOfBla5Vq3SzJgUSs4lJOQoAv_ItwkHAh0dzf4Q3HmEmV4wjAEkyJcNzx1HVZP2U8TwLfltumUFKtQl6wMd2nn9CPP547EiKy3NONQrQJnHQGfcdcxOsy0ud4uIl_Y7Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=eWjX3-QvMKsDsYAWB27vfhfggbrsQ4vYGW7DrGVWsfNNA-9b6ZyUR117EJ_U6seiVetneYd6Ulq8uQGvweSwCkgoKXCs2QiYUuKL2A_IYG7_MWbMcO3diPgAJnvE0L2eD0BPIPCievYJAaxINRGBzv_VT2F2xt-GH2BPIVlINvelAOAY9vPuH-WtEgZ75kheiNhCUrsgATNQEVWPX3x3fbOfBla5Vq3SzJgUSs4lJOQoAv_ItwkHAh0dzf4Q3HmEmV4wjAEkyJcNzx1HVZP2U8TwLfltumUFKtQl6wMd2nn9CPP547EiKy3NONQrQJnHQGfcdcxOsy0ud4uIl_Y7Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ReNA-TNgH4JBvBRiYT-33eMZQCl8w9oAvOa4Svr_Rjf28lS_nNui0f7Gu43xpx6RkXIsV9ZAsrCiH2UnaWnYrBDXc8USYq9HoEKA4H0YYID5zbZuZdxQzFHeLi4wwTMbiOlc23i_fM8IkXWnIRZoRbkbhUZiM8pexQnXfLg26J66VFpvkAkwVfVw__OHEQR5hN9rUf8eUmyQpbvoEr8zJnaJq7KsuXQStdESuk9XP4Uer160wTTjwjXm4qOojgxu5YP2O_N-tEXprfJNrWzw-mShpkQXGN0yydjJXj9NUuYb0cPGYjt2khMzq7tHNx-mcMiuJ5Bya1hI_LL8EjtIIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ReNA-TNgH4JBvBRiYT-33eMZQCl8w9oAvOa4Svr_Rjf28lS_nNui0f7Gu43xpx6RkXIsV9ZAsrCiH2UnaWnYrBDXc8USYq9HoEKA4H0YYID5zbZuZdxQzFHeLi4wwTMbiOlc23i_fM8IkXWnIRZoRbkbhUZiM8pexQnXfLg26J66VFpvkAkwVfVw__OHEQR5hN9rUf8eUmyQpbvoEr8zJnaJq7KsuXQStdESuk9XP4Uer160wTTjwjXm4qOojgxu5YP2O_N-tEXprfJNrWzw-mShpkQXGN0yydjJXj9NUuYb0cPGYjt2khMzq7tHNx-mcMiuJ5Bya1hI_LL8EjtIIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=mPAppDVDVUepxCHh17etXCZaCWV4dphX6B2eQQAABul8lL8cenrvjflpRWyfSXBEBUjCuXtCitatPxthW1ApEbXwT2iX--QexUrW_9t4EMwQqXDFM6LCDnWkILuf-gWs3c9V3wKkexXiPx3tV2CL-4yr9mq0AbBGDiDRx6dMQsbOQtBPw31afceOH7cNveuUByxAnHsvBRBuYWdXNVxyNQ0NGAgx33lSQ3KAOorA0T_4SsArAztfA6472ZF56T3Z52UBOQaO5ka7Z-0M0d5JbYExZD-cLydruNJ7VBCL4t7hhRO5M3IUdeLdnz0dZSrMDwepBlNrNso3VRTp1uxnZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=mPAppDVDVUepxCHh17etXCZaCWV4dphX6B2eQQAABul8lL8cenrvjflpRWyfSXBEBUjCuXtCitatPxthW1ApEbXwT2iX--QexUrW_9t4EMwQqXDFM6LCDnWkILuf-gWs3c9V3wKkexXiPx3tV2CL-4yr9mq0AbBGDiDRx6dMQsbOQtBPw31afceOH7cNveuUByxAnHsvBRBuYWdXNVxyNQ0NGAgx33lSQ3KAOorA0T_4SsArAztfA6472ZF56T3Z52UBOQaO5ka7Z-0M0d5JbYExZD-cLydruNJ7VBCL4t7hhRO5M3IUdeLdnz0dZSrMDwepBlNrNso3VRTp1uxnZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=XbuIjovmT95KKObFyB7tKT-wOelwfig4-x61aYxj2F9fOaf6O2TDxxtGTm17RMd5JiOTDbIicPbkj6xHOTkupSMxe98EFw_dcqp1aWey-LTHaRgAoRMnXDGTGdc0yeyRXjkdB5a0m271X7E_-PnQTX1riS7jVrV_gSZbG4nze7oCDjwQayJWbrsptqOuw-KCrooo7_h_t46eIu5E4DFSqodNq3t2KZFb914AtkrC-NTalF3jdDQS03hl5hIZioyW2PuZAb3yzpbHZWxrLS10o_W4TLmLt0Mbo-JM_4lw37BtBLXkLt1qF14ADdPVnQmZRTj19dTuXo0chSWKW3pB2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=XbuIjovmT95KKObFyB7tKT-wOelwfig4-x61aYxj2F9fOaf6O2TDxxtGTm17RMd5JiOTDbIicPbkj6xHOTkupSMxe98EFw_dcqp1aWey-LTHaRgAoRMnXDGTGdc0yeyRXjkdB5a0m271X7E_-PnQTX1riS7jVrV_gSZbG4nze7oCDjwQayJWbrsptqOuw-KCrooo7_h_t46eIu5E4DFSqodNq3t2KZFb914AtkrC-NTalF3jdDQS03hl5hIZioyW2PuZAb3yzpbHZWxrLS10o_W4TLmLt0Mbo-JM_4lw37BtBLXkLt1qF14ADdPVnQmZRTj19dTuXo0chSWKW3pB2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=OeYB98lD7bnTMAiBDobxLS1F0Ug37QQehPrXdBFNM9Tx3sSBOwq3MM_5bw_qVRIWZVfZtxw_be7BFS27ciFgEkZFNOxQA_vzbvtzt7O2mqnkPRpePiJbBKQhADNP4A-aMJXmimDfDd5xvyC2nFGyFz11gII70g6zecPfGKGzM2F2Jd1wQoTT3-j3iEPkaafoBZkUzeHKnB14osJegdFdO5B9hUFhdyK0WtJgrdphqCYC9SY4utAEqurPIR_DlNslriSBu94UIGKwMzOV4b6G67M5FIGpRzyio03O2d-mZIvjbIDgrm3dtnMtbCozr8l4tX9ChXg2j2RPnAQJrqNn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=OeYB98lD7bnTMAiBDobxLS1F0Ug37QQehPrXdBFNM9Tx3sSBOwq3MM_5bw_qVRIWZVfZtxw_be7BFS27ciFgEkZFNOxQA_vzbvtzt7O2mqnkPRpePiJbBKQhADNP4A-aMJXmimDfDd5xvyC2nFGyFz11gII70g6zecPfGKGzM2F2Jd1wQoTT3-j3iEPkaafoBZkUzeHKnB14osJegdFdO5B9hUFhdyK0WtJgrdphqCYC9SY4utAEqurPIR_DlNslriSBu94UIGKwMzOV4b6G67M5FIGpRzyio03O2d-mZIvjbIDgrm3dtnMtbCozr8l4tX9ChXg2j2RPnAQJrqNn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=m_E7mpjVJGIg0oFy8AmzBRTDAd6K059-u5UO2JQ249rQZBaBksriOIgZqgVB_EDn50cEhgZKlwV2hkJ6MqZ1WMW5NH4-QuMj_tD6MfNfOitwjq4okOFgyoXWWPF0ZV1r-El2AIJgwbdZu8Y2eXcGcgKTN3mYn5TEo7sX5R1DmBlKaoVYzUR1wLV82ZNSZjBfsfcUdPI_3a52Q5tJCpEn9weuJtdkP67mFO144-X-ID_6Z7dp83I9FnSS5wYOSmSr3HDbPFiJg1KSu7dMXauq3xiwOVfEcUU79JUxJcIRY6v0xhHSwqI3lbFOpnP2elerkuky0eHUbi_DkXdpuQJX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=m_E7mpjVJGIg0oFy8AmzBRTDAd6K059-u5UO2JQ249rQZBaBksriOIgZqgVB_EDn50cEhgZKlwV2hkJ6MqZ1WMW5NH4-QuMj_tD6MfNfOitwjq4okOFgyoXWWPF0ZV1r-El2AIJgwbdZu8Y2eXcGcgKTN3mYn5TEo7sX5R1DmBlKaoVYzUR1wLV82ZNSZjBfsfcUdPI_3a52Q5tJCpEn9weuJtdkP67mFO144-X-ID_6Z7dp83I9FnSS5wYOSmSr3HDbPFiJg1KSu7dMXauq3xiwOVfEcUU79JUxJcIRY6v0xhHSwqI3lbFOpnP2elerkuky0eHUbi_DkXdpuQJX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=hdRJ9afBpUbACZO5nv3uoDN6ZAXRahq2gSajQzCQfj7iQVlg3a__tVXR3ye189K-uuowI9aIdPG-avi24tMevZcq_1oR_ujyVkJjbEfwP8Fc2tuZhJwn9RRa6sVkgRBDCmo3gxFw3yTb1pQLDVII1uaGGnKXmSgF3Yrfz5ReEJcpmUr0hVjiZfHH4k3-08ISLxGGuMuymSmdFlclcXsRyT30crbbP2sO8Xl4ihev-CsbE-q6okVTULn5bCSZ04PawkMUD5MA7QqzqgXFkH6pyRJ9Lg455_P6fsW5tpume83YuLATrgTt9VC4LwE_epEYZ-EMujrabQvzkO0RF5083g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=hdRJ9afBpUbACZO5nv3uoDN6ZAXRahq2gSajQzCQfj7iQVlg3a__tVXR3ye189K-uuowI9aIdPG-avi24tMevZcq_1oR_ujyVkJjbEfwP8Fc2tuZhJwn9RRa6sVkgRBDCmo3gxFw3yTb1pQLDVII1uaGGnKXmSgF3Yrfz5ReEJcpmUr0hVjiZfHH4k3-08ISLxGGuMuymSmdFlclcXsRyT30crbbP2sO8Xl4ihev-CsbE-q6okVTULn5bCSZ04PawkMUD5MA7QqzqgXFkH6pyRJ9Lg455_P6fsW5tpume83YuLATrgTt9VC4LwE_epEYZ-EMujrabQvzkO0RF5083g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_qbng3Yb1wGtDkzHr2Mk3g--xL7itb-SkMl3b-FwC62atPCgTU1OtXOmBubCTZ7GxyuwTlTmWSy888JMLGU9VWCpiG-RYXTiu7YRthMoDV7e5VUYxOfGgHanuVpI-MnstvTb5Kg6z99D6Zipoa99q1g9vXiGVNb8XYIzHaGD45Hk-ni5JocndSXODUyUMIFRnYszuWFdFiFcjk87mZ3W-d_xn_oyxg5HOnnlYpoAT7R5dMGoWtrJB-CSvN-K8Ucgd9a7APVofxZDFiuBXAhGofosqOPFIi8WxBHRfUvlGenJRH2OuovUHOf5__alQ2sTemGO1ipT0Z81w5lulv_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=rLGqMyAGYkWDbnl4TRMEORXE10vpuoHBl9Oo7SnomAX9cOjW60cftOmHFZzhKs2j3pplHGrcNvOzBRw8FNdJfWFqMYSxD21wbooKdJmyey658lxfNvTVMaxQRusyN1bd1qCgk_8cyi9DfB07KgX82ve7SuQuakCSYUZhhYpW1n5mfSCqpqUhFZ5CU16VPCngbS06g2Y1dkVtyWN-O8GFp1Lkl4W6Oln6UfPv1kJ6sifO-jky_yo7z82SStAme-CPX-Z4X4Yzr4_BKBSQqWDRKmv6vml93_t3DkJ52zqYIM8YQMjw571o2__C2k78RBqnTlce4W-7ixkM63VC5uOEEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=rLGqMyAGYkWDbnl4TRMEORXE10vpuoHBl9Oo7SnomAX9cOjW60cftOmHFZzhKs2j3pplHGrcNvOzBRw8FNdJfWFqMYSxD21wbooKdJmyey658lxfNvTVMaxQRusyN1bd1qCgk_8cyi9DfB07KgX82ve7SuQuakCSYUZhhYpW1n5mfSCqpqUhFZ5CU16VPCngbS06g2Y1dkVtyWN-O8GFp1Lkl4W6Oln6UfPv1kJ6sifO-jky_yo7z82SStAme-CPX-Z4X4Yzr4_BKBSQqWDRKmv6vml93_t3DkJ52zqYIM8YQMjw571o2__C2k78RBqnTlce4W-7ixkM63VC5uOEEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=RUnfGRKsyZyQAYXxAx6pvxhOxwIs9pVa8_etTd_ss83mCWn0wCLpsk3aIxCFBZxSv7PK5u6pKRm5N6O49ZdLAHM5sel8mgA83zoK1XoqyQYfMJkOrVSSxozV6UUBTN_K-_P5ywvxCx7y4ZiBmfONbb47ZRP26KzZjnsTAqGKsS0DzXm078jaA4v0BdW5BKqDFlmT9BHHYLDFAmatida9JYiYzV690VyXpWsxP01i1gdEznoa9IKdUMVfy37_SQBbTfaHJqXGYe5WpOzpbpp_B1nq9sbBOEfPgBM6QzAbdGgeyIb-7esOiyWggbzv5CTsvs8HKR5B1iAJ1DCGl_En9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=RUnfGRKsyZyQAYXxAx6pvxhOxwIs9pVa8_etTd_ss83mCWn0wCLpsk3aIxCFBZxSv7PK5u6pKRm5N6O49ZdLAHM5sel8mgA83zoK1XoqyQYfMJkOrVSSxozV6UUBTN_K-_P5ywvxCx7y4ZiBmfONbb47ZRP26KzZjnsTAqGKsS0DzXm078jaA4v0BdW5BKqDFlmT9BHHYLDFAmatida9JYiYzV690VyXpWsxP01i1gdEznoa9IKdUMVfy37_SQBbTfaHJqXGYe5WpOzpbpp_B1nq9sbBOEfPgBM6QzAbdGgeyIb-7esOiyWggbzv5CTsvs8HKR5B1iAJ1DCGl_En9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=SL9pj6igtDMTbMuZ4yeJDEguOhMXdy-srv5CFPmX4l7QhCN9QhJzcNvIwdKUHZBM-lDz50Xf9_hjojHlGXKr1gjFQhSfPFl2TpyExPkqdYeh3jiQM-DfqYXV2AzWA82bF8B--yxR9Gwqdl8iPFbHg_MGRnUMhNbvvzVFgndgZpdBZ0kWDEcFUsp7wIYQ2vUhjo_gBAHkbv9QOcT-pSfFyOuGbktBeQE0nUpDAYOXjF9gxpdG6jp7NL5araaF4R2tKfBSJvLkDzpeC9RdCmOKihMVaP8IdKgTpLXAXnvagInilN8fjOeCMKYRjd8Hs1Yd1NPTxATPGFehCM--wsGLCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=SL9pj6igtDMTbMuZ4yeJDEguOhMXdy-srv5CFPmX4l7QhCN9QhJzcNvIwdKUHZBM-lDz50Xf9_hjojHlGXKr1gjFQhSfPFl2TpyExPkqdYeh3jiQM-DfqYXV2AzWA82bF8B--yxR9Gwqdl8iPFbHg_MGRnUMhNbvvzVFgndgZpdBZ0kWDEcFUsp7wIYQ2vUhjo_gBAHkbv9QOcT-pSfFyOuGbktBeQE0nUpDAYOXjF9gxpdG6jp7NL5araaF4R2tKfBSJvLkDzpeC9RdCmOKihMVaP8IdKgTpLXAXnvagInilN8fjOeCMKYRjd8Hs1Yd1NPTxATPGFehCM--wsGLCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ugwrlXLoPjIkOeZdd_r7ZNnxMHvaiW1u72JwKMyHBlGCZKnTtCMSC1uPLfJhtyidUFFMFmFXYorNgwlB9NK-9wNRqvpzhTNqlmt2IYzE58xy1OczDVJCrULDkIvG5o2B2xQamJvlX5IgkbehD_LhcaUBKqm0HSeQNS_EYO7UEoDmt5XmdXfDS23iiKZrsOARzDH3mz6ba8EVpfKX23AUp65zF8n-zGIkfCMwYFehpUWQrrQou6dRCLnyZgKce24_NvkrkeyaSuh5LXM79DSHCA_iA4b--n8Q1VVJ1LYq5ISeg37kCy60XoGy2uWhcP7aYAmCXGjXCjTx-jHYq_sRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=ugwrlXLoPjIkOeZdd_r7ZNnxMHvaiW1u72JwKMyHBlGCZKnTtCMSC1uPLfJhtyidUFFMFmFXYorNgwlB9NK-9wNRqvpzhTNqlmt2IYzE58xy1OczDVJCrULDkIvG5o2B2xQamJvlX5IgkbehD_LhcaUBKqm0HSeQNS_EYO7UEoDmt5XmdXfDS23iiKZrsOARzDH3mz6ba8EVpfKX23AUp65zF8n-zGIkfCMwYFehpUWQrrQou6dRCLnyZgKce24_NvkrkeyaSuh5LXM79DSHCA_iA4b--n8Q1VVJ1LYq5ISeg37kCy60XoGy2uWhcP7aYAmCXGjXCjTx-jHYq_sRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCQiRF6NfCUeAQrJ2EuYipHblIg8aoJvv6kINsK4s4rwUObfDeZ0xMduzFZygiu4VGWSc7kZa1mSAGY1Vs7bqiMdTXsNJOipsSQ9KxalRpY8SBq-SKjfJ2-JEtSBqAHqo1m4t_w49BUUzAjPCPS_Tabm7PGRiYIJ9gqqj0ih5Ov3IiYRkJFZ3M41dwdR7OEnb044WdU-0WSTCxOjVJcGojfK4FtfH1ss77rlZGis8EhVLq4-HZ8nbWXwfaWwOOR8cx1TlX4PFt8SYxwT9iGfdLxUmkzcUwEqj6BuvY5bJudAJ_tv7wDu9sfotTg1xn1Pa8-9plxsuG3MECZ3-Flb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=OlQuyNDIIMf1GAKNeR8Q0N3YM5ufN9iKLP6xxEfGTbyeJW-Qd8sD4hpxBOMQoMbnc1UzGOrlL3luUX6S3P5XJc3aPAcHVct92vOrrqejGUMDOFw02vHVD7NKbHfr78BM0g3Y7-zWmZ6OkaQX4aM8HBLalZ3m7Nvf9Rdmjc9wJznfBc5ezgJQgZRzSCJ2pOduFmKYVVAUo5tcMcKRtQPdxy34rBOwWOr25MQCjS78v2n_YWamXfLfZSi8fX7AcGLPYoIR1ejvLLUcY65VHyeD4t_PaWZCkMAHY50dFwedmAvKKv7TXvdqTsaJd5aars4E15qwIuKC6P5tEivA-raDFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=OlQuyNDIIMf1GAKNeR8Q0N3YM5ufN9iKLP6xxEfGTbyeJW-Qd8sD4hpxBOMQoMbnc1UzGOrlL3luUX6S3P5XJc3aPAcHVct92vOrrqejGUMDOFw02vHVD7NKbHfr78BM0g3Y7-zWmZ6OkaQX4aM8HBLalZ3m7Nvf9Rdmjc9wJznfBc5ezgJQgZRzSCJ2pOduFmKYVVAUo5tcMcKRtQPdxy34rBOwWOr25MQCjS78v2n_YWamXfLfZSi8fX7AcGLPYoIR1ejvLLUcY65VHyeD4t_PaWZCkMAHY50dFwedmAvKKv7TXvdqTsaJd5aars4E15qwIuKC6P5tEivA-raDFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=dp5Hx8I_4ZjHS68Z0_WmsWgIXPmYvPS8fkuKwIvPBSfF-LwUgE_8iyH5DxTZONI9Wr798X28yycso1PP_BJy0LefqMoAOqTiDAv1yZLjuBbKFq8J5gy1s1yzd1V4Q3pbBypYaPlV7TWt19MjNqjgO8i0dOQMWVSPYGyBbJxnUjbHK4_nLt28UTgsf6-egYI8yCMyWEOReuavaFs3EJh17dGwKbhwOmqXhFbwseODhs9KHdqC_eja_2XpYCbuBUlxBsx89LRZmPsxDc5cy3VnfuH59dLpkoRxFwjWoESLNvXyQcv7QTAvA6F5L4bioLj-9Bi2xMB57F0a8ykdWvgAeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=dp5Hx8I_4ZjHS68Z0_WmsWgIXPmYvPS8fkuKwIvPBSfF-LwUgE_8iyH5DxTZONI9Wr798X28yycso1PP_BJy0LefqMoAOqTiDAv1yZLjuBbKFq8J5gy1s1yzd1V4Q3pbBypYaPlV7TWt19MjNqjgO8i0dOQMWVSPYGyBbJxnUjbHK4_nLt28UTgsf6-egYI8yCMyWEOReuavaFs3EJh17dGwKbhwOmqXhFbwseODhs9KHdqC_eja_2XpYCbuBUlxBsx89LRZmPsxDc5cy3VnfuH59dLpkoRxFwjWoESLNvXyQcv7QTAvA6F5L4bioLj-9Bi2xMB57F0a8ykdWvgAeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVIxXk2CvMp6imY8Xob0i0quiFcrwFdld5fLWhHuwMeavqYxkJy-NG3DZV0iezEOQVaUD_9RYadGreVmItiTZwlPaKl-gpt-nA8uAW-PWFqFElK4aoR0T83hS2fZBL4VkGVW9t6pgd2H6p40YOHC81QxBoQ8ncvkKMAkaAi-yFFwcM_T_4yZARtVeXZU2BYsBfWgM9V_tUtzbEoZFYH6HAEXQzEvasRnj6xxBf919HMVWuXcaA2Yg0iac1ossallSKUyArZ1CQdN46WRzc8P9i7lrTaYYIG8tCLrlJLMmHiFE7TEwlbYsO9DIfJLdUgVrBvCOs5pwomCOJdAz4sSyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOPrNgOvyu6H-s-zHCgxT55HPuHQlPcBmJkaohCDYImIRwvXYbBcSkJVsEUAPBqVLBXTEqvBkx8hK-8Z3juys6G-7JRCH4wHKlzOiCoHb4I2405jLY80b7S1Yk2JVfkBPjbYXb4163E9OTmMhHYmvBW87civlC2YgRA0Gh4tza94zyR7SgIu2mt3qBLLDxMy5vkxn-MJkxr8yq2nWEOA9qwcvz4a28y-jIlodEGd2-L91MaU9jIIDIlgzJrmJlFd2OHBgnDSiS6DEIGrJk1mfhdk-wBa9p12jySWOQ5TmatvP3WJJJwEbVtbHklpcl84my_yYmyCFqXes5GXkTxPIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=CYOUk13mkk3mBxo-9Qz7Rx_FDE13MbIWxyxlACjLH8RbK_8eCREUKB16ph4nkxXL1f7tvyq8rVFX_gf0lAx95iNRTsfkHp5NAmYhatLC-pKSzKYCUEM8WCyl9CwhlsGFMmAREWD3WHViPTGzMWnWVqwJcTHhTQIG374Lh24lD2W-24CmmcYNbK5ZCNs_3Z7WUKFLypdRuBCSaij0OfAHcj7qt5OjVvV1yqhU1hfeX8f9dn2TJIArUbyOYNH-OC7v299NeAwKlVbdaEYB6dohKX1L5M2tnhF466XZrCwvk3NUmxF0iP5bkcdT1twyTy4oz0bw61o6wJJvasO2FQ8Gmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=CYOUk13mkk3mBxo-9Qz7Rx_FDE13MbIWxyxlACjLH8RbK_8eCREUKB16ph4nkxXL1f7tvyq8rVFX_gf0lAx95iNRTsfkHp5NAmYhatLC-pKSzKYCUEM8WCyl9CwhlsGFMmAREWD3WHViPTGzMWnWVqwJcTHhTQIG374Lh24lD2W-24CmmcYNbK5ZCNs_3Z7WUKFLypdRuBCSaij0OfAHcj7qt5OjVvV1yqhU1hfeX8f9dn2TJIArUbyOYNH-OC7v299NeAwKlVbdaEYB6dohKX1L5M2tnhF466XZrCwvk3NUmxF0iP5bkcdT1twyTy4oz0bw61o6wJJvasO2FQ8Gmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvegGpQ9V27d6lkqOFFmE-VQd5DMe17cZkRPXwH_MwTnBY3ZGzdkKJLzHr6sxA-J4g1Md0tPugNw9mtrlpYwMNo928IFQKfn-T9RsiiaCfuUmSwCa6gpTeLw5Wy1Co_gcv8ojAsOfRHe0BU9Lx_l4Bw4W34spDPPKCcqLSbP2bg32TawzI-k04FO_0AaZndbAuIX6EKl3IKLBB4ns-tB5zMLDRhlvWoPY--EnVVzNYfl7MP6CzMxbGHgykpR1GxQx87i5sCShbH9LY0b--xJlYyz0gNYKCrWl5RQ6zifOI9XlluYJkrueGmKxeV34XTkYcfRyFAflI62qlUrg1JIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sezuaffqr63Ep7zcP1HAC4I3GXLg22D2SwNX49hyaCtlNOPaLYBHvKsc6U1VVIRWrsx7kEH4jqP5geF7hMdg-NmlUg2EweBS4_3ptw7ZdljHaPxY43EQfHB1tkBbqXAarps3gEU5C2wEqfSli46PkIFzBqRVQv2NwDi39gcVPGWJ6ffyb1tVJ0HX_1g8efoQakwCNty2b5eBfZCujWcoGUqhv8yw6FAOscXoky4TDaJSfFTw7-l7B84Z4mNvZL3fToR80ZF2ff-pbGoKM4joaOZaojNKjxAxsX1hnS6UyRjxXMpFmnToB2HJDUSDmqi_HEWUBfkFV_85vVmmIYS-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qg_H9mSJrfyJZNILy8SxvdfPUS_U2cUVG6_88REgRhhDTsqOed48sHNJ4WS1Bg16SKD4zLCvVpuejZX5RGKuxyT2uCMvAEe0icEAoGd2yzqOWe_VR6VLzAhyEvUvRYi2MAQjgNjqg5sJK75A6dYjkxKs3oy9Kk_pRnFVfaBCUP0C41ZBIFenICQhYMHdnEiX3BmKukFMFM_HAm85uFxua9HXBcrqs7yOTWDQaqZ9g1OVS1RDU03vefAumTkPvFHxH_N_C71p_MZbSNWatKmQykQjApC8NxZ6GXjQc7I9Ayuloy1AGHU5e00VyRMQWJK64jmM5LT83Naa9t3SOAx00g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=gBMikS_WfU-ql2CgSTeFNkXPRaq5CG5XhdHDXhqVKuzfO27Aq8xLcppyaOVaYIn0hNoeEuK-dwxcnJTG6cwx1JqbmwA7QPsJPBZ9wvC4vg5HfARzxmzwF9qM6TGIshdOmzcEhlbhBO6rnnqNFZG3AZ1KghoDeF2LHDxH3dvCFfxgMnNKudZKQojNgRni6YsYJAYiEdF0--D4Zo-svs4OYai6x6hyTuW-n8R9hgpT_Jy4iBPtluf02XnlgL_TZlsiOOMem08Cl5k8Cb9CKx9tXvXuh2KcEpisn3CBj9yEqZdDm_xFfCmloJX-uEnqNMFNtLv-DGwOd_Y8vkhiFvMJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=gBMikS_WfU-ql2CgSTeFNkXPRaq5CG5XhdHDXhqVKuzfO27Aq8xLcppyaOVaYIn0hNoeEuK-dwxcnJTG6cwx1JqbmwA7QPsJPBZ9wvC4vg5HfARzxmzwF9qM6TGIshdOmzcEhlbhBO6rnnqNFZG3AZ1KghoDeF2LHDxH3dvCFfxgMnNKudZKQojNgRni6YsYJAYiEdF0--D4Zo-svs4OYai6x6hyTuW-n8R9hgpT_Jy4iBPtluf02XnlgL_TZlsiOOMem08Cl5k8Cb9CKx9tXvXuh2KcEpisn3CBj9yEqZdDm_xFfCmloJX-uEnqNMFNtLv-DGwOd_Y8vkhiFvMJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=bC3kY3BEzLGBCmrkEZZhM9KYn6VeWtE0GEDbWTN7lLg__qk13fQiKgV8unm7W7y8kuBYGBNqLdZXhTgIZpMUf6IyTjODy0MtFQ5nmfL275MF488nOUBpaCtTU5BWmSp030bKYDx8QlrrtjiEdtJUscnkrry9XY7af_yfxcNLAxTgH90C_29nitg4mKPr6CkCSumVe2lYZNnhPyC7VhGNsF4Rxk84zz4Y6lEbDR4mDzDPVCbl--tzLyFu_kvuG8rup6BcvyRIrsOTeBr5YWDLP0BUltMD9YEAMW_zTjIOMqBEmj2EtS7Ls4LSATtY6vNVpa_JmxMTnOSsQ1dMjkcfNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=bC3kY3BEzLGBCmrkEZZhM9KYn6VeWtE0GEDbWTN7lLg__qk13fQiKgV8unm7W7y8kuBYGBNqLdZXhTgIZpMUf6IyTjODy0MtFQ5nmfL275MF488nOUBpaCtTU5BWmSp030bKYDx8QlrrtjiEdtJUscnkrry9XY7af_yfxcNLAxTgH90C_29nitg4mKPr6CkCSumVe2lYZNnhPyC7VhGNsF4Rxk84zz4Y6lEbDR4mDzDPVCbl--tzLyFu_kvuG8rup6BcvyRIrsOTeBr5YWDLP0BUltMD9YEAMW_zTjIOMqBEmj2EtS7Ls4LSATtY6vNVpa_JmxMTnOSsQ1dMjkcfNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=b6u5w7_xJd06BiaF4i424gYdm5__RYMzHososeEzuIae3Qp9aUJs_LB6swtgj95zGHKGZ-1XGZCZ42_QhbtqjkGquYzhOMhLRu3tcQJ4LXyNq8hM6LWOmluJ895Ca7vgXRLwD4YoERO4M1qBRotNmy4QHEZ8rfiuVSMxM2vHAu-cYdNWAmnkLVXNG3FZs45S4TEq31alW2h2XXBfErMS3OVR1DYLm0IA9Ktsa2-jzD5QjU0FfmrpYlLfxg42BquZpymZgzGlD3A-HX06OAyBekERjGTNL4meX5QccGhCMpr4tsG3eCAnXf6dJ3ks2_4S0Ak57dR1sQlS3UAy2CyxlKz8yBdjgMI6J8-SxdvMm3wxGKKVm22zDwQlYXwbltGuSpnw_GxlBjk3H6uCMlNpbLuEqrXVDr9u1TSMW7n37La3savsInXB8aoTW0gh0JcsfxobY9GvJeSMl-TpU4D5JNQZqkiO02Ct3oy2L6CaOiEYwmV9nbDcT4RnY9fPHbdE4eDaaJOxl6eIxdGceOhAALvcHWkXB7GNYd0ycevUvhdKMGyfLv3Jjz2DSYejA5T6RFGp2aLxRVxNGfHfciiWPYhdNO_OhDm4yQyWWetpfStjvuxPVCogqrRFdWodRb168MJpGkA20lOziRgUichZzdsPz7-gYC6NE1q9EL2nwI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=b6u5w7_xJd06BiaF4i424gYdm5__RYMzHososeEzuIae3Qp9aUJs_LB6swtgj95zGHKGZ-1XGZCZ42_QhbtqjkGquYzhOMhLRu3tcQJ4LXyNq8hM6LWOmluJ895Ca7vgXRLwD4YoERO4M1qBRotNmy4QHEZ8rfiuVSMxM2vHAu-cYdNWAmnkLVXNG3FZs45S4TEq31alW2h2XXBfErMS3OVR1DYLm0IA9Ktsa2-jzD5QjU0FfmrpYlLfxg42BquZpymZgzGlD3A-HX06OAyBekERjGTNL4meX5QccGhCMpr4tsG3eCAnXf6dJ3ks2_4S0Ak57dR1sQlS3UAy2CyxlKz8yBdjgMI6J8-SxdvMm3wxGKKVm22zDwQlYXwbltGuSpnw_GxlBjk3H6uCMlNpbLuEqrXVDr9u1TSMW7n37La3savsInXB8aoTW0gh0JcsfxobY9GvJeSMl-TpU4D5JNQZqkiO02Ct3oy2L6CaOiEYwmV9nbDcT4RnY9fPHbdE4eDaaJOxl6eIxdGceOhAALvcHWkXB7GNYd0ycevUvhdKMGyfLv3Jjz2DSYejA5T6RFGp2aLxRVxNGfHfciiWPYhdNO_OhDm4yQyWWetpfStjvuxPVCogqrRFdWodRb168MJpGkA20lOziRgUichZzdsPz7-gYC6NE1q9EL2nwI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=srEo4TVF0IjulXWYGK4LJiJBN4GuGUYhknHTMzCLz-7uL8O1397DjOfraCyHg41qFMMzpdbAfNwUrEn5vVh_p9AItugwXrYL631vpLffqSPS4NJgfFQiCpjrbS82BYgMo8PEh3riwYSuw6uOn1lAnB-TJ7oLEvJxZ6iQzjyeUzPegoY3T0QOqexnn62GxsRf238wQr5BbJNTjgzkc7AbrTFvz9WffPFwWBi1vEStmfHt26RnXunomkmd7_nY9NcZexRWtN2_jaAtcKJxcq77XXKeLP23ZGgbA1I-JttoPZb1lrrV4ilr6DCV3nLCIyxfP6OCgOxfVTik4sIURJz4xjbf2wFPvZfiyF5Ac2lnV_ExtyvvY_omHzQ9MWIj1_cg-scQJaNWTkLBJ0q-HFS5g3gn4wLGKg9ET24LWN9h8P4BJIz031eLrEWHtGsf32IvbxJ7XbRnzZrECTMuVHIi1kexloFZxJRKoJghgIM-pgwOpkcKKB65M3Us9MSehaxtuSNn_uJffnU2mVGH8HUj-v9O74UTxYpOGc9yiOX9uE-2JVZS4R8wNY6S5zhxXOAIm-Obpplh5_mjHr4Wz0G8rh8ACEMeyBHYj1M4MuKWmGVPjwNhjAgIBwrZGdsEja6aKw6rQiEUXozXf7SAcRkdwqGX51QNZmQ-PQF-RDaBW7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=srEo4TVF0IjulXWYGK4LJiJBN4GuGUYhknHTMzCLz-7uL8O1397DjOfraCyHg41qFMMzpdbAfNwUrEn5vVh_p9AItugwXrYL631vpLffqSPS4NJgfFQiCpjrbS82BYgMo8PEh3riwYSuw6uOn1lAnB-TJ7oLEvJxZ6iQzjyeUzPegoY3T0QOqexnn62GxsRf238wQr5BbJNTjgzkc7AbrTFvz9WffPFwWBi1vEStmfHt26RnXunomkmd7_nY9NcZexRWtN2_jaAtcKJxcq77XXKeLP23ZGgbA1I-JttoPZb1lrrV4ilr6DCV3nLCIyxfP6OCgOxfVTik4sIURJz4xjbf2wFPvZfiyF5Ac2lnV_ExtyvvY_omHzQ9MWIj1_cg-scQJaNWTkLBJ0q-HFS5g3gn4wLGKg9ET24LWN9h8P4BJIz031eLrEWHtGsf32IvbxJ7XbRnzZrECTMuVHIi1kexloFZxJRKoJghgIM-pgwOpkcKKB65M3Us9MSehaxtuSNn_uJffnU2mVGH8HUj-v9O74UTxYpOGc9yiOX9uE-2JVZS4R8wNY6S5zhxXOAIm-Obpplh5_mjHr4Wz0G8rh8ACEMeyBHYj1M4MuKWmGVPjwNhjAgIBwrZGdsEja6aKw6rQiEUXozXf7SAcRkdwqGX51QNZmQ-PQF-RDaBW7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tzQFHysU9RM4GFNXV0BtH8j-5uCqWXEdE6e9UItxk7_cNc6ZSS0Wi3PIjp1w1HEC5lgbXB7BfAq_VmLKejfPIH4qCTMBtuw2pArDfAIyDz44eyNOfTZleNNWdtBO0zaq6JOr6gc8OOf0FfwLpyMHi0eku7SV49slcgIgkWmca7BLxaWfj9jeoY4PeiJU6QOa8WhmWNbBsMycEr0BU47tY20ZN5jxbUQP0npGtYVHadhVmgih5oeeENCGvm6kvT0B8sKTe8tVDg9v_82UHtgkXagAU4FDiTIUTa0b9I4H_mvVsf9jJHpQNWhuzkCAxHI0SKgl5-42NgDe1DHzNi7dIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tzQFHysU9RM4GFNXV0BtH8j-5uCqWXEdE6e9UItxk7_cNc6ZSS0Wi3PIjp1w1HEC5lgbXB7BfAq_VmLKejfPIH4qCTMBtuw2pArDfAIyDz44eyNOfTZleNNWdtBO0zaq6JOr6gc8OOf0FfwLpyMHi0eku7SV49slcgIgkWmca7BLxaWfj9jeoY4PeiJU6QOa8WhmWNbBsMycEr0BU47tY20ZN5jxbUQP0npGtYVHadhVmgih5oeeENCGvm6kvT0B8sKTe8tVDg9v_82UHtgkXagAU4FDiTIUTa0b9I4H_mvVsf9jJHpQNWhuzkCAxHI0SKgl5-42NgDe1DHzNi7dIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPkEYpjrbZwIyhhTUa8blEaFknbyzpZLicRjrHYrUDSq8vLABDOdz65vVS2zA2nsQtiTAbqOhw7J9wrWjCfMT7VdRiP0mnvEiTcMfwKFOh5oGMbkqLNm14UxQvJKyP5KmgX-t6QSk4NBg9lD67Y3OqzvTN8yLZ0WnniWgZCgnO-4jTFmCRLgXpZv-Z5Rn6MNc4qeYnAFuHVoG_auZw5T1Ygc3IttpEDbd6eqmv_F2h34-prCXV08Sv4nxPEcDqmp9kvQeyp2wVIUL4LSR9qfEasPmV9Ksehtbmp42x4IrXIMlxq2k-A29jAMDnK1HaD_bx094IRH676za2EWVrpqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=qZIFIRidcBLwlNeT1Qq23V_ZzcoQyIrHlrBruFsk1FymeTMHb5Qk1J7B_LJFXYnErnKk5dVH_-k9gbob5nysk9OzN0hcMXHondWLIKJy7sR0Trvue2Hz7pWq3UjlqqFV16dznn3U0pNjHPJ-CngV-4hj-cflKKjH-QkiqJTx_yYyMjSAsv3NB0LlV9zycLYHmPHCoF-z-5fbyItaTalVxlHcV8CQUCtMOHWTLdg_PDb8Z6WzYCHZqLWXvN6K0tn0zNkksqWftd2KSaUEq8XuRW0O7jjQwCDiFi0eDhwIunuBn3ptFt_y5fXwqRLa_9TQ-KbzfdKjnmqgMo-rDrQHGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=qZIFIRidcBLwlNeT1Qq23V_ZzcoQyIrHlrBruFsk1FymeTMHb5Qk1J7B_LJFXYnErnKk5dVH_-k9gbob5nysk9OzN0hcMXHondWLIKJy7sR0Trvue2Hz7pWq3UjlqqFV16dznn3U0pNjHPJ-CngV-4hj-cflKKjH-QkiqJTx_yYyMjSAsv3NB0LlV9zycLYHmPHCoF-z-5fbyItaTalVxlHcV8CQUCtMOHWTLdg_PDb8Z6WzYCHZqLWXvN6K0tn0zNkksqWftd2KSaUEq8XuRW0O7jjQwCDiFi0eDhwIunuBn3ptFt_y5fXwqRLa_9TQ-KbzfdKjnmqgMo-rDrQHGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iPEAFliKOWZw4SuDUTGGNAnxkykCE1-WzVEU8W8HAAjv08_4YxYy9Ors9_rn6lTwLNY6I5JY2BbNmag3XhjX6ClQGGAuhMoqsQYLydR2s2SkHkJvueXNV7axdpit421_lT7oniE1LkHER1Gs6y5fRa_Ml7vFXNI9x9uIODl-Syr4chM4wa6K0nOOObAHWCCz9ly-k_jNz6krF6YRL9t6ztmCiqnFyCf7om4LdW1yc4qKFpfahZA-AUV1UywnCvPPnPU8dmD0bAoCEMuFbYKVw-0P0mLyCHMk2Z1yT3wigSQf8c-xt5KG_VUqQKLsICG8Mujs66DR-IohiasAaV5P4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iPEAFliKOWZw4SuDUTGGNAnxkykCE1-WzVEU8W8HAAjv08_4YxYy9Ors9_rn6lTwLNY6I5JY2BbNmag3XhjX6ClQGGAuhMoqsQYLydR2s2SkHkJvueXNV7axdpit421_lT7oniE1LkHER1Gs6y5fRa_Ml7vFXNI9x9uIODl-Syr4chM4wa6K0nOOObAHWCCz9ly-k_jNz6krF6YRL9t6ztmCiqnFyCf7om4LdW1yc4qKFpfahZA-AUV1UywnCvPPnPU8dmD0bAoCEMuFbYKVw-0P0mLyCHMk2Z1yT3wigSQf8c-xt5KG_VUqQKLsICG8Mujs66DR-IohiasAaV5P4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRl_JwS-eAGj8yHpw1gmBQVnlNZG6vfqLpd4HlpnxZOntM22nyFNKsklnok13iJHbwmXrMcQbho6j9ssrPs-j6Mw2hcDytA3UEJE2BxU3vDkcZINzMDHcT0fGq31DGHj9R0YbzYDGaUri258_njCvvWvNgjcMgjxuTPB_RjS6eMkEmey2OI1k5eUy3ATVRHkfErnYtEcFZ96BOb9Lrg_U4IFSOfXzDzjMkTxjranmzYV4wpnvKdl35IkLuZFrb67aeEvpz_njbzuX54a80oCQ4RgkITntCyR_ptAiBEzyiBuCCGGt_35ZLiHEVTOT547BvRVlmHiLJhwtmhJWruRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJxZ4-4Jufdv_x195zpJisMfUwU8A3Gr4FgKWWHMhKT9q0bzJSMkq3wlheTIm7MDavoGUdhpIBfNjvnxmEkR_-pYh5eWdY3jgr6t-PQWrXxBECTtaeA_IxCi8X2bMT93DxEIA1pk4yIK7UXOk712Vr5FOpeOX6iHxWTJMHAVNWHlolRlR1Q-l_oaXb6qtlxxHRSapCpkrRsI_DjZqrFwTmIUV7tVpbCZtWk1ng9A5M9dof864orUw_eGlKdyVRiW55-hEjVpgnQ3YtXFaZLG4HJ_0DxWDgNQyKPRxhxo-npCUYwy3e27yDKQAJK8uYGNZUiLqCz2gyMQ4UjRz8HEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY5_yMoXYVKI6XW87JhQtEz2GKiZ12Xsv3SA6nxW9537ze5uA_79XA0UvebZH67oVaQ_rTwByuAQv3VwumCPqNCCAK98EKGQedK6nQ1kZrVNDghoMpw3QY7cF1j6F0IGYItPuW52pMW192eVo_1q6Y_C4gjePiGvYF4NAloD3fdbWaFeviXBHiiXC9Q6TzxJcHHDvq4ydiikmRfiBIprI-Zc1MxGNwZjUnRoAuROp8OlwMGH6Kzeg6jZvHtHPieLjccFpSah8fr7xlgLf6_mnb1zuSCgYiSj1sG8Pvu3SjLZJBR4V_NT2mZO361jedbSv-r_wrPy1sxDcKzGJ5eq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltGUrzcIrGf5-citQUTRRhxVw92DtWduWDd9B0puxbI9dYBKsCoVnCrYftuUziJb0oo2DPpWerbPbgIbO3QXzYK4Z0Wi_IX1cCa3shxxhUKXBx2Y11vIc-oO_yW4gWf3qdOpirX9Z1aIcq9nYv313ni1BAFe0reaGIsdQqCev4g3oYmKjzTxNgCcygNVhgXPwHWwp0iPZByVgDRJiQio8Ae-ppOGa-QSm1WrW-ds3bAlp6-Gz_U8yf6qN7G5lV24EV_Tqc2A9nIGDf5XlnnLihjXR7RY72HadodbcsOAf4gAGQrfN9T-s4dBHVyADZibMr53BYYMUKkib9jUeD7moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiVILuxZNkKANNCxKqPLuyBbPXzqPPbvA3iD-4WwyV1DfN11NwFZ3-W4wND-QcHC06bKMD0VaRj7hsKzRSimKFMDcteF5xjmTZq1L4kSWT1xgRBEWCZVC7sjJ4-e9XaFY7yi86SubL1Zo_eFZXfvL2P_7qfoXz5t7Bg4-_QnXqmCahmorJtIuh0xevvfAY8YAHMU92PMjC3PIEe_QKtQYpQRU3-ALdUWEtFCOvNT3vohGPHqZ38xCfoYIHh_7LR0GkbvQzzysq0gCAO7wxF1YwF-jOZbES2ktofU22-cYkRKEBLl5Ffw6gy6nfXot3iM-QbS61-HzB7qKX9LeVTLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2DxZA1m7l3swEd9N4wH03LIxkALCNdg3I3duPl1bgBh3u-7oySK2uMgFkZRSv7PF2rSMTaPgzRYJSJ4x517SFe9ExHfqN_qWGIXQOTxr2sLaRILdxeEK9lb4Z0KmHWX28Qw7MCUaeYnOWYw-7YccSaVSuRpuD8Gt0hqg78bTQub-6Br7QcRtiUez2A82pQkj1EWUJqeNeG0fLnv-cWhZswunypuB_RPEsFDgY7J4I3WSbX-mxKXZ0TA6gyU8KZGG-qkLLWhJtl-v9ZBxRBRnhT2yEOcafVBGeNvpUK8svH08Ke9mAUhXsJyNPNCnbTHmPSWSFjHkiSWHZ-YnR4oIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrbBVTHd-lk0UicHB52sFaUNJrzqGYSal6Lnh48WExwgGmteDJmuSMXfm0rQKuikPlDYl_rK7W5yLGK2RaD8A0QaxdQ29auwfxzFz4TNkXXDBCQEDH1N2o8RrAFcZvCGbyiFcjvgRCmX8cAXmcX2xhDenj4rrbUbCt343aiZxlOJgREtjJ7cdjUZM4q-tu6-nY23kBAI_GlwPrxggHp5zPRf_U_gj0X6SYGJYP5MtTxoiE9Yjop5loKp-JzVz1DxfvPNnOJbNhmiY3PyQcJCcwibsgpo4XJHsaBZORdaRbo4A7WDptv4YrbCPeiqxFw6iDIvxwSgPtx5RxAOWaUXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmfMsXfHxrXdDZUZelCbf5ybihcy1iO7ICml2FqKHEqFvRnUF14X_bXK7fbvLK-L32n7hwn5MlGK8KW7-EaWcOv0mXP-4Wh1j4bTbvX_8IqF9PlCyHUEXlaYZrTezApQDswv2Fe_9AH3nIkpGfAUEu_f-Tf8DNH4WKKXb-SoT4386xlCLwua6h_YQEcosNCGgojZ4xcWxrm0msfZBpIyayZY4fQIQpIA1OCuEMIZ4d6gAE9oDf-1V2SPAA7kxCsfA0f4uzpZyDMDOlvkBohj4oRwmtmzcz-7fB1gHRuRJMO0lxYrDMxHSwy_WNewvClNNm5I-IhRG0TOhKuiafi5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdyMEZU27rDzFKFcCjV0Xw1cg_LpDTcT22AvJgRozd8aXrauY3GzACIKw3I8f9q26L9xoma2WDh3RMdqky5sdLXzVGGKYI9skU4j8AYvVOtTCtYpnav6HXCludbtLCUJ3L8LI3Ufao13PXHSBxFHIyI82MWQEOye7YJNY1v0z4cWqbfHhdzvsBMtoQE2dfwlMUjnqfQJSVxHAZiu31765FJiW8U5E9e8R2Olg4y8YVTqEpFwF0qPgCv1YvdlgjDX_IafP8TJ5yB-Qe-wRbHcNYhA6noIOnMc50sa7pMThooVequ1pNDi8i1oGkQM13VhYciM-JCaB8fflYlWcMhFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBkVdvonEV95sW0K_y71KVyNkTOivggJFHpiyjw1K1vTPQnf9wpUe2DnLESvoka7yJSTeRMzF9Ar2YBib7EepBSED56lhNWR93sJ1yzMYi_5Wt1qTDcS0BlO5s-BVsLtp0Ag_Jj8zTPaG1euzUAYQrNs0AUhr8q8bXxNJKW5Ol_N1-p_Ap_2T3rfyAf5HZ_x-9ntjia-99dsQWPp7C9lEg8_lE9Lo09wMpSon93vRwheBtm-8jMZa7SmH4iNkXOTXHm0t1Fu_cB4khij0qZCt8NTfgbDtNNZ-MozFdKBFocIJI4VWOqQ0wq8KZ92c3JRtOxorYWXghCtPWjnuGQTcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=WbSD7yeVE7rz2cmuNHnYOQUCFk5nvRuUsVLqnpekyuzKBuHHlsVzHyUNA7BSCAJpQPAveszDwPKcDxxt_xKkKtQiqVtZuNaeX6ORevzI4A49xxVYxbmeVmgKjTDCHju4KSRAf1u6vTOAaBROHjrdRnIHx20Xw_zrh560PrV0_mkrSWDWc3kghhQKu8PGGyCoho8P1tl6NV-0iuEMO0rHKk_wcg5DlInTJ9sOKLoA5TR6F6dzstC-362fgvKNPIfK6yIifUhaTBfWvtX1gpBhlbphMJ3Ydo2-D6_gIMitPVJTMMmcIDP9vyyAB6_1q3Ax3CD_-D_je4w4Z_8CS5SZ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=WbSD7yeVE7rz2cmuNHnYOQUCFk5nvRuUsVLqnpekyuzKBuHHlsVzHyUNA7BSCAJpQPAveszDwPKcDxxt_xKkKtQiqVtZuNaeX6ORevzI4A49xxVYxbmeVmgKjTDCHju4KSRAf1u6vTOAaBROHjrdRnIHx20Xw_zrh560PrV0_mkrSWDWc3kghhQKu8PGGyCoho8P1tl6NV-0iuEMO0rHKk_wcg5DlInTJ9sOKLoA5TR6F6dzstC-362fgvKNPIfK6yIifUhaTBfWvtX1gpBhlbphMJ3Ydo2-D6_gIMitPVJTMMmcIDP9vyyAB6_1q3Ax3CD_-D_je4w4Z_8CS5SZ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFhWvPQT9Uxf_tlufmRLknK19qA2RWq1W2PewexQ3awyjMKRqK_G2iHdGrFXh-GSkLQGzUhJgJxlxzFMVtTY-2AT-jIk6pIGd2pKOkmu1tjeJXscISbu1fFtWlEItcyMndNWUIEe3a-FJGaBF-n9O0gX9X99eccByD9lDgLEM9QKrWy5yfdSE6ujicr_tTbnydFF-_hkPzCrC8w22hTKuwd6RunmDDyMWqa5-I3P5CyCx1eDYRDQkYQOMP6UlGbf0W5aVOKON2GCEC0JO96-l9TlOJRZN8lTxhhcouAt6eVNRU-awOiOVnOeyLd7unu0VgZskdU_faGNDEqgypE0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAnroedNkU0Kl4DhWKEhchNqQHZJMhAo6asq-HsXx6lhDPbYn0U1Xwi-MIECk7mJmwU1O42p0yArVGKK_vucODpRCzTN76ZNT8e4IitsuGyqoSITHQzai4usezX0VbBdVIAELmd3fGGifI0DpQ_8InFVW31HcHJqD-w44c7QmXxwOkqdJ6HIqkiXob1aP-rk1DShcaR-dyz4iCrK7TYX4xn0fh-S30CnryM88hCOpqduEs2ju5gi5VnyNblNc8LJoJ2D5LUukGy-DCq2YlhzjscARRjfDEX-S168P7aCdSkRuGtKuyAGfTmbNb57PEQSyJSTZANLX74FXvHZW9M7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=FXCeBE5gdjk_9NPyz5UE5idGAve2jzKpddrcez3rpxxD4jZzzSDaPaJEqJ-F9qOUAmvuGTAM3-Vvzg20G1uxRG7Y7qoof9c7eGjokpRsLmgwrzqTVfbgCdqvtjyju5W2cj2Fbm1dGHNbz6bZqa2L-Bt-QRjXL7mP0P8pYIoUWrvLA-_-TfzNNSqdm2sEeWkAk1Fq6px1Z6Mxy4hDIzqb8Wp3QGlGTw5dmAlgB_g8Ob9DDRcKJlpRhUf878QPaGaX4Oqa8R-qi47w_MNvKTG-dQIxGXxtdT_2w9WYOOIpKmLCNLhqXla943Z-UexsulGjm-0o3_FuVk7rLI2_rPvOkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=FXCeBE5gdjk_9NPyz5UE5idGAve2jzKpddrcez3rpxxD4jZzzSDaPaJEqJ-F9qOUAmvuGTAM3-Vvzg20G1uxRG7Y7qoof9c7eGjokpRsLmgwrzqTVfbgCdqvtjyju5W2cj2Fbm1dGHNbz6bZqa2L-Bt-QRjXL7mP0P8pYIoUWrvLA-_-TfzNNSqdm2sEeWkAk1Fq6px1Z6Mxy4hDIzqb8Wp3QGlGTw5dmAlgB_g8Ob9DDRcKJlpRhUf878QPaGaX4Oqa8R-qi47w_MNvKTG-dQIxGXxtdT_2w9WYOOIpKmLCNLhqXla943Z-UexsulGjm-0o3_FuVk7rLI2_rPvOkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Dml7PciP_uOeXK0oFEKTeZsxQGS1ZjphOg28s4sN8DpOpXwI63mVVTWXYPbVkGx8y2rP5rrZIPEnb0ArW87rugZz89DBI5hnSQZoaBmzHKhDbzQUamRt65Fag2In5ZiKxx5NiA-ulR8yPun1KMs1TQwt4Gcq38SjoivjYALKal9cA_GX3OtZT-DcfMLASHY6fsD5x7Pnv5RiQsNeWICqjMGrM2rH1LtfUQEIm4AYIC-XDtF1-1WGfZg0wxY8WQgDxBlnCc6LmWk6XrvaUX24aJ0XCsAjJU9lcnDMT4qMsMmif3FGqiiH1zm_HrpWLNWVHnt8BMGb7fKlzgD4ar1ZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Dml7PciP_uOeXK0oFEKTeZsxQGS1ZjphOg28s4sN8DpOpXwI63mVVTWXYPbVkGx8y2rP5rrZIPEnb0ArW87rugZz89DBI5hnSQZoaBmzHKhDbzQUamRt65Fag2In5ZiKxx5NiA-ulR8yPun1KMs1TQwt4Gcq38SjoivjYALKal9cA_GX3OtZT-DcfMLASHY6fsD5x7Pnv5RiQsNeWICqjMGrM2rH1LtfUQEIm4AYIC-XDtF1-1WGfZg0wxY8WQgDxBlnCc6LmWk6XrvaUX24aJ0XCsAjJU9lcnDMT4qMsMmif3FGqiiH1zm_HrpWLNWVHnt8BMGb7fKlzgD4ar1ZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P66skpl52AV6mvNzXIiwNxVhYL81rOjHuBljtUHHhOlfAH1fBe6O6KvDzuTGtfAPq8yWE5FGUQ4PF3dAUeKFE8L_cdzIlClMIO_6xhz5Bw641ZNqTba7C0zsuv6yv6TLlwWAU1VheDKbx7OIhrIJ3NGPi_iYG00ohuYW3I1nT65EjIhJhQewjrXjKuqxBadTkksx6PwMJCnOGknDzqU6Ktovi3dBpnAd-mEcazL66wbrTTbInT2bFJHE_6OoBR2roCvEY3fvoExEpKvtUIYOYpSMbUEloDhZ4IhZsatrMeG3v9FDT9oWCtttb1Hk1EUxz6wTtjev_K6NP9igiTqmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pikroo3oOEEFiBcDHEFtRsGxFRTtOKMysTxKH0XdIgC_U6qbhRTTS9ig-1_FBxMcG82bIv9k5JQxjLb3pYWRB4_e0AlT5cosAIiM0jxk066ifrMpdgHZml_AgMlff0ou5nabrTIgkvnEKCOse_JgV_WXe5skQHRXHgij0W4SlhdR4k2cS6Iu1GJM472R5qsY4QZAJ9vyyRbmIVVsjB5V5T-9CyA2nEXa2eLIxC22UPtd5Zh26MXq1k9Izf8Rcw1kDjqklOTofqeC-WaRaN9135IF_NBAwNToQU7xOFVruxZyrrZIr8KIQNrr7FsyvhH-q4Cexf-2vmzSiIwp6Sy8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpLBhqrVCm2QN2D5w6LT4UDGT0KFhJ3el8qqAcYw5KLXmDifqIdB0zYPNZaROwAaSd1HZhtulfYK8rsqIOHP3jlJdWeoWMzJ-BqbjpSzZQKDFoL0OrlecMnDmtsNeCEBMvL0s0xIdgDwtg0A0LCOEwGtkHRRZzJysobX8gTrgCn9oEFimQETtq_wh10IRgejMiuOQ7Oz8hQZABe34GP4fuZIHNVCUdr0s5uVMaUXkXdwibvv_LnsDSXve9Dl1gmmLWr4uOfhI1NCGI_V6gbyyOdLZapSp14aDd1Cxwa8Dq7ot1FO7W7UmTrYIBiHUEmVvwR-LUehME6HzMwEMGb-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEgZ_3uhRSrPNQLwkFTi7nneP2xySftWQaCC5hzEFHwh6tbpAXcw0rR5g7VTh4C_kSHUHBMHEzu3ECskUkalUriqq7fKyxkbwv9NEPA7n0qIUWy8OAaj4ThjuELt-E2dN71UrgaytCSciPU06YF_ik3pEdSp1pAPH02e4_6hL1OaVsbsl1qmETBOmC-zHD5xK8lzSnAdV4GSE1t-6i028UVUX01_SB6avPRiOSd_oLuJ88si3DptjV-9_1zGtvM5IpNJj9F6HMIqxOEd7hqr0uCmitVmE9GgEt0TJedfot2bt_CnOIgfnt8uTiKYsnyLqGw24B_sQm9PFJDFVcs_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv3x5vePC7hG0WSsA9PooDf9VfA1weMJw-nSkSLylO5MPvOS9OYj6Z2JIWEUN6DkgltI9mzDfW5ssOv9EjdmnQQklswwH28ax-NSMJxEFulF6yvv_Z_BjPnXe04QiP8583Bv4E7aqiuj_1SVgTA2y3rYprAiCzBC2VBUz1gvn5BxqUjfqxkC0JiBJO67YAkEhDFpEW4peI76HG9h4Nr24BN_1QSAR-jzDP_DyyR28266-qvnDaHJ5DIuLXe_2_1rHaOjqqjsRI__PJDzulHLlNK0Jds0yhAcB5etXje3hPqVgkThnoL89mBWBudiZb2ozP8tJAl1CsElYonTPHKKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1SEibent4O4nenwP4_IgNSgErm6F6YguXVS6kuqhmGJZaUM9hKC0Sd9P42XH8trojQSb2kh6h9LUpWlIizRKRFEjiWVxFhXL1XVr5K71qNb4HVMrJpD19chGmB-oibq9DQSZ6U0OI5eu8DiUA0oiEXiR31I9dynehWJRamQZGBF1DZph7o41ulY04powhtTPVKRE7KlFllxPCZxRyepb4tIdEsx9nZlQ-Vh7EMr4zuaTtQdB7pYucJ25nLcpph2n5m5z4N05570JdfiUG_TL3w1VN9vxaqKfuKVFWirmROMN2ko6JU9y9mMxZybIeIeNV_wwZfVOPs98nT4SrNP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS060L8YiwCM3IpDt39i4-kkKeDroptgP_PK_TdEUE8MaOek7J0JdqRqsA9s27mWEAahGy4mdsKFQuDKvOyfmPJSxdUBvpe6Su2DP8AVIvLaiVIQWisvMnk6fGm8hWKfEu7iCzVvWkibV7QdHhkLysh0MaenfM6mKj8e7ESbAVsfPMrsJj97cKKy2cq6fDcMsjLCHWGxGsfJ7eg4G3h07NTcvuIN9mRg1-5Qr_CX3cqYIcWv5LWj6MKQXCHARNWUMHw59cCQ_5mXHYg83o5ons6p0sL42jHImhlonBMPiwWGADHyJ7dWn_rX83xl70cq8v6Fd5Qt6yy1gmRlTJBFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
