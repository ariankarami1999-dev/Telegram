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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc-xv30h4RzEXN-kemBCnM_lTiz7OrVmECVyTAJZYrENACKbFlws6BpIZwkMcdqImWB2oLOUd5kvZ1k4kf_A8yx3AF0owcG1gyldXAwTb6Gb7g8inKintNZFzY7nRdo54qgBSR4aSPCvU12z4Ga7-fOMasgMA8Egtx0hEjPxF1Tjhb66DItayItxyv6i6mHszZP4RhGORZ42kAcrR023UROBZDXeyQz-fhPzTXCtFsCZEDxcc16Mkf2aGiY7Q9uK7ECIldXt2OQVQARRuJiV_zx-64Y2lqN9U0HBgz4RfopNBLfat46HwYj0KwxSiDE3et9IO9K3IsMqGjGUhT8tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrMq9Wzesq4_4qIkok0LNTAIB14CQSEIakyKX21gkiy6QjZabNqYmzz6EIYXEgVCzWSQ8i5gpnW6ttH98nPNBUNBgQChSJjPzrhx6TXqWxmPt1cEh9BlqIePYj5Hf1_vAlo-D7T0tuRgp5OxkHKi6Rc0IKl_gbnE4XOzHDyqskGJtOu3LNnwcP0MCBdNp4e2BoHVcWodBS5jOI_pOAwce-lvYG9NU5KivSYnZoizgHdfGgGf49ediMcszAmMT1snuVzRtn3w5W8F1plyjZcJgRs6q5SxOyXZKV8rwvE05KtdGrI9Be4cRL77BtfqRV34BhjixmtFO25_XCCth9WUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ktOz-ivEjARKzIhjEikGyQgqsgEyCdW3InRpcux68fv85nCkUVy3yg7hhlrfAsbG_YSxx6FTsxwqsibwLdCnFyzFPM06NroqKyarkC4wffrRoP-TfaLqrGU2pwAnuZJPeu6xWifuREXungP6D8SSv2id0Sc55ipM7urrNT_y30EN_ycf3Qmuq24Ov3V9xKXXWnsuzM_xXcCVgHBXAFiUTIGafKOrXh26j_DIgRvsvzFMEz-drCaJoLxPxn3jzogaNNuZVLbcD-sljrbfa8Cf8h87TAqFr4raGX0r038PDVqwXr4SDdtP-nEmQPXQDdokO0fU1cAztFav4Q-SaZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJllLWqGcfN7Cq1cBHIoVVC8-HFT4o0dQEABs_V_LDKdEWjve0OjyWc603JbH4fyuoFSmh_Ieiy7Pe5ZlwfgD5d9INQpOxAryvAcAA2uAt3QWnw365JnejRgdj7ync2_eXT35Fh1sdwwH6jaPvvj47jouLA_hRNoAZVB85pKvhGKXaCb5TKJxhFYJHFvMSGb77jmD_-RuUDVh_hh-tNCzEypgrR2K-nb0KO8fzqQmR1XYCuH1V7Mhb2T7LpD_BOGW8TBvecVRHMn01hbYBoh8yR1ZcsqQdhwh-YYyIHTxXIExd6aMuAzx8EsH3WQgfzZTIe5X_VSTKbSeKSxejqWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRen3YIZczMjoZKUMZfD0VYilxG_2jkAL9hsevgRE5soBwEn14A-rdwS4g7EVMhlUxMWsH-PS4ppvaI3c0xDEBoyeR-NDX-YSUvs5zDs1SZSqQts7xXckNZyl5SBAyn55Tas_hrpnVBIVpLD9F5nBT7uwREa11cezX8Yc-4vo_BxM7WEObCgy0Qay7VSXU6TiuQK9-ylvFkbdEzvO61h6p19xrQWgODiRoRxupUmdBwBfqOrB2Enci7C4e81e7nE_h1_rzswg5KVnstN391vBvS40r5eLIcXR8Ag2k4owluAa5yHX2whvQaBId8Roa-nDwI2TxZbLtGNh2ko08dqeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8Vow2FjnUqk1KK7Y09RtNGlHvYhkTHKyIsujeGN8pngecR9nRSBLHakrkJjmP_tUWYFplSicxf71LMnHfXYJMoE-FLPiG9m31JlDX7pepgQ-g0_HvqQ_-T4tM0nWqkRPEbHuRx_mhz68wJy27YQmKA7CEmoBqT3K_Kfr1N-eyftNClWCwcna7QpXnomeV23eh_73JQA7wiErOJlz4wM8gxXmC-0FfaH5vjST99QzRuejsrs4sTEIRRMsv9srRLcUd2-3f8UJH3d14LSYVF1dP6Rg6VevBxLJlk7z5GeoWvae7n1kjAS88AJQ__m3YSz2YmRWVuJ7q6zLWn7mtbAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=uj_PblOB52o4bvLsNL8wb_eeCD4Xfh39vZjKxeY-GDkB46vBapHVaj0UHq2G9BYvMCMm_PrI7oHCx5pP1gGtpIqIL09PxgL_hOEip6rvDWVUq4qQwG4EB-MVl48A6wnrxNGIaK-xiKzBqt8ROR8vBELztsrKfgV3gSvGnL69teOuyyWUGULAbgpr9UrKT0sqr1MWXw1mB0_3qTqn3gFGA7TntSMGuDo4LxMX4W1BxWoaVVAmxd6LjpZK8isX1vL8ktqAh509LwA325ky9V-p1Q3A0nuenl2LgaxbjgljozN6ktaZ-l9WwM0fK9z56RPsXDIFWRO-VhJNMDMXknhhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=uj_PblOB52o4bvLsNL8wb_eeCD4Xfh39vZjKxeY-GDkB46vBapHVaj0UHq2G9BYvMCMm_PrI7oHCx5pP1gGtpIqIL09PxgL_hOEip6rvDWVUq4qQwG4EB-MVl48A6wnrxNGIaK-xiKzBqt8ROR8vBELztsrKfgV3gSvGnL69teOuyyWUGULAbgpr9UrKT0sqr1MWXw1mB0_3qTqn3gFGA7TntSMGuDo4LxMX4W1BxWoaVVAmxd6LjpZK8isX1vL8ktqAh509LwA325ky9V-p1Q3A0nuenl2LgaxbjgljozN6ktaZ-l9WwM0fK9z56RPsXDIFWRO-VhJNMDMXknhhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd_bDbh5baQPeykr5tHC6jIqbEv4rmNxrnNqohEW9XNf10BIEkdqkSvvRAebdoWodlxKGXoRX8tKqdkvAE6270D-_XwXJoHon167RbSsuoy591heL3hG0VCbUQTKEM338lZ7_7yOmrbLK94p3PTnmfQBWT6KCWlRv7TcRwatjH51GKStgP7xO1qszQ_4oJT7yV4Bo4eDycrpLAJWIbi1LpMaMHA3s2jgfImiDMbsWHuZxmltXhlRK3dXj8tVavoM-G71T0jvQSDWvBqc6WMuik4xHvi1FX8NASodpWY8LQsdMNq11oSHvlIWJgq4s1SaaRTQSa1YeIYkB-buEhNmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=fWjlnxq3NQ0EwxXLW7PGlPMe2jlytKpaAqTnT2IKekE_1odcYFVQapMuelLhxCpK6jSLSfQ3V7N2ljMm4RTutF-F5U6kn1373JRELdoGptMOgJGYZYOpX04knh4DLijKbmPxD9e42AGZOeMun7xNC4p3BCn0UB5gSIl7UDRyrGZznFjyebSTV09lV0JxiTSosMnj9z24INWcasEFi2tmkN7E7V9C9-Ch_an3J1m2lmCCsezjgkz6tvJzSbhMH9BnH1rbrqXp4X8q0djkKbKjTABbDlEuVyJDsPjR4-_1oqs4cMqRHLmx0oGxcY2noGu4t6teZXiGoC1nyp1_kTWEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=fWjlnxq3NQ0EwxXLW7PGlPMe2jlytKpaAqTnT2IKekE_1odcYFVQapMuelLhxCpK6jSLSfQ3V7N2ljMm4RTutF-F5U6kn1373JRELdoGptMOgJGYZYOpX04knh4DLijKbmPxD9e42AGZOeMun7xNC4p3BCn0UB5gSIl7UDRyrGZznFjyebSTV09lV0JxiTSosMnj9z24INWcasEFi2tmkN7E7V9C9-Ch_an3J1m2lmCCsezjgkz6tvJzSbhMH9BnH1rbrqXp4X8q0djkKbKjTABbDlEuVyJDsPjR4-_1oqs4cMqRHLmx0oGxcY2noGu4t6teZXiGoC1nyp1_kTWEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBOVNbhSdNUGlird8pqHhhC2OJ4S-YQnZnN0zcEqQm7d0oUa3fQilTmok-R94qgf-JVLp0hot_O3OoLN8nmrGoDSGw9nCD1hGp7r5TeoU9oleJqVRPqXXLTGuTqLHxvEwlhzWVS-bHr1F_jBZKEyUOd1e8NU09gkvLpQENpp4d19ahUNniOr9ImK5V_k7X47h4vLscd0NzZgpjtdR6Lfp2_7XRM7FR3YwmAm8BY4SZ46MPPqDj4EeGnvKriBQLLtNHBulmeON4N3SymU5F8CkWCaMr9Dklog3IWSdh4dt-hCqhi9dJ6tD1RdHzazy-vWN2JsSg31vbSF4IMTUmYoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=moqgaFwYiMVrvoWoOOQABLa5dlQi9VBWKIiCYk-V6P1Tb_BhR_qyEwDg-YFW-8V9NH7wz2WGsxqRwJxxhgJi8buBhvPvjWiSI_rnjxC8UxIhbqQGJlS2xP2wq445SsIak22oQQUKXoIGhKKTcH0df_gd9GdPJ98uvgK0mNvN0ZghcDOJuAhr9TCyNnjATn3Cdhtg1ThHc0Dz5lR8LZevhrfLJUnT1CNiyX9X1eIwe1k_coQWYpJlGs_veN6F9FoybtMu-Q65qVRqboYdqcf7zGL3zcRehxEPIG4kau85jku_SPI29kIAIPQNS_bFR8adcU8y1kG7DLGS5Cr76KJ5D74Bx_1fyM3C2L-XIO1SI7-eZ1XByUR-58cODaU8ls3Wm_2jPNHgi7wO7IPOQwTfOrKII4tloObA291cnYtzd3zpz-GvJQGKeDKAGRLgz9eLwWGJxytgZBHeUII8S1zgv_dsTghllA0V9ZSYAaSrZxAU0kQICv5cvjCapCPC2DBrgrcMhc6Fz9ksD9fCZ93nmHNxhQ7K-kGvdB0H3XbVs6BlpiO2dsj1n9y7Mc_6HdsZBUt9bca800tMMDXgzubQ2jQg8jPpdIHuYdT-ZvmgFJu0KLepQrZ6MQmOeoyvZF0L_wyglvRESQBU1EeAOj6c53_ugQJz-PXGxaanWf95cmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=moqgaFwYiMVrvoWoOOQABLa5dlQi9VBWKIiCYk-V6P1Tb_BhR_qyEwDg-YFW-8V9NH7wz2WGsxqRwJxxhgJi8buBhvPvjWiSI_rnjxC8UxIhbqQGJlS2xP2wq445SsIak22oQQUKXoIGhKKTcH0df_gd9GdPJ98uvgK0mNvN0ZghcDOJuAhr9TCyNnjATn3Cdhtg1ThHc0Dz5lR8LZevhrfLJUnT1CNiyX9X1eIwe1k_coQWYpJlGs_veN6F9FoybtMu-Q65qVRqboYdqcf7zGL3zcRehxEPIG4kau85jku_SPI29kIAIPQNS_bFR8adcU8y1kG7DLGS5Cr76KJ5D74Bx_1fyM3C2L-XIO1SI7-eZ1XByUR-58cODaU8ls3Wm_2jPNHgi7wO7IPOQwTfOrKII4tloObA291cnYtzd3zpz-GvJQGKeDKAGRLgz9eLwWGJxytgZBHeUII8S1zgv_dsTghllA0V9ZSYAaSrZxAU0kQICv5cvjCapCPC2DBrgrcMhc6Fz9ksD9fCZ93nmHNxhQ7K-kGvdB0H3XbVs6BlpiO2dsj1n9y7Mc_6HdsZBUt9bca800tMMDXgzubQ2jQg8jPpdIHuYdT-ZvmgFJu0KLepQrZ6MQmOeoyvZF0L_wyglvRESQBU1EeAOj6c53_ugQJz-PXGxaanWf95cmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=YTx-uYPnNnKDPmdVYSoNn42qdfpuTQUvhdlBWe7qmUVUD-WnPOrJR6qZak4OHcTv0TZiNXYH_LYAV0av_5_18ul9cNmLvLXEeqEgmeNAPZRn6eplUkOxA2ZCcfDmjkDVPydESmc9FEsiDFv99HBi4teluRZ2pfqb1K2OpLNG7jhkjPAFiIYQhvwipGlP7xWR4Qb0FXu2y96AGfDv7oAsj4six4lbZbNn-JJfqVP4LtNfCOxf_otC_HHvglrN9_r3pLomNRLVD4_KJKinmjni-R00bxUMHUo8RvRbEh_HJtIm0rjIRcVdJ2QuKwRH1S-WRYoxJsW3DGT-BAXS0BTYxwiUPsrxWEjO_hweewQm-08C7bKgrw_syu8DZWMoSaXmzDybHWTirLkURbDUcrVUd1IuNnJjLEUGszlk7QLE_v5i3SZ4iywv687xhruzwtFzr9-GM3ZJI7YeA5gmqrb6ZXEEDUWnSTu2QqX9BOqrlygZxFLQ1-R7gTUBzLLXxWLmroyHISNhCuKNLb3AlqwnjAT1-Zdmk4q2gmyb4XaOGXQvoC4RSoWDAUdGSBECw1cz6814GWJEOCr3qKggpq7QrzDhEONVHeg5OzS3rdiIpYCsGuFqthNrraNQGkNc-Ybo5SBlN7VdOjnbkO9TSsvddT-Lp9ikI1-mXYD6woqX82c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=YTx-uYPnNnKDPmdVYSoNn42qdfpuTQUvhdlBWe7qmUVUD-WnPOrJR6qZak4OHcTv0TZiNXYH_LYAV0av_5_18ul9cNmLvLXEeqEgmeNAPZRn6eplUkOxA2ZCcfDmjkDVPydESmc9FEsiDFv99HBi4teluRZ2pfqb1K2OpLNG7jhkjPAFiIYQhvwipGlP7xWR4Qb0FXu2y96AGfDv7oAsj4six4lbZbNn-JJfqVP4LtNfCOxf_otC_HHvglrN9_r3pLomNRLVD4_KJKinmjni-R00bxUMHUo8RvRbEh_HJtIm0rjIRcVdJ2QuKwRH1S-WRYoxJsW3DGT-BAXS0BTYxwiUPsrxWEjO_hweewQm-08C7bKgrw_syu8DZWMoSaXmzDybHWTirLkURbDUcrVUd1IuNnJjLEUGszlk7QLE_v5i3SZ4iywv687xhruzwtFzr9-GM3ZJI7YeA5gmqrb6ZXEEDUWnSTu2QqX9BOqrlygZxFLQ1-R7gTUBzLLXxWLmroyHISNhCuKNLb3AlqwnjAT1-Zdmk4q2gmyb4XaOGXQvoC4RSoWDAUdGSBECw1cz6814GWJEOCr3qKggpq7QrzDhEONVHeg5OzS3rdiIpYCsGuFqthNrraNQGkNc-Ybo5SBlN7VdOjnbkO9TSsvddT-Lp9ikI1-mXYD6woqX82c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=bXnzYw6vtD5IO_3tZra3F83skuT9d1UL42gabdF8sz451RfTCOebrgFn2LmImpcWWUEpOfa9WKi24vBArY8FqSHivvw0ux5r2R8w9VVcxPEWLBtbmXRtRVNiB4GgZmtYLLsYpQ4CJqV9Fuhuqjf1MO8B2btU3SbgLDEjgUmDsdFpU0kB02maw0Vl6Nygo0n3xNgH3mjPe961c0SBVIO1OCiQ0CJ2kvpN4vLBujYQP2bBcb3esFuJFeT7Fo-Jr_694jtkyGD3p4U59609S4MUE0XUqhw8L8gvL34Qcn_4C1sELu2EFr8qgLTB3tCaz3O_Q8_n3ADTB160R6DYSTLCfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=bXnzYw6vtD5IO_3tZra3F83skuT9d1UL42gabdF8sz451RfTCOebrgFn2LmImpcWWUEpOfa9WKi24vBArY8FqSHivvw0ux5r2R8w9VVcxPEWLBtbmXRtRVNiB4GgZmtYLLsYpQ4CJqV9Fuhuqjf1MO8B2btU3SbgLDEjgUmDsdFpU0kB02maw0Vl6Nygo0n3xNgH3mjPe961c0SBVIO1OCiQ0CJ2kvpN4vLBujYQP2bBcb3esFuJFeT7Fo-Jr_694jtkyGD3p4U59609S4MUE0XUqhw8L8gvL34Qcn_4C1sELu2EFr8qgLTB3tCaz3O_Q8_n3ADTB160R6DYSTLCfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=hnqS_q7xdnnDldiY1nABZpn5uJZxSr9Lk_azZpy5nS5Y54TB8yLM0KqROhv-MAKaye9jfjRyKkjxcIOoUv35zZPl_Q8USDTm8tgYVY1niA4Of-QBNZe_WQPKYNZNTX7SO8-5rr4R0DMp9XPyExj2Cfe60bzBxyMcTl0S9yWXQZzI5Y4Xc6hTF8q0DbGhw3FqiGs6hmbmeppecdS7jG77mKcWclZG21ucQQtucczFGmIlp-GTWgFcZHygBd92E7n5sg-tzdgCtlqyeglFypHtYWXDXRQDL92ag1XdEiYcvOGuh8_-fZNG2nsNrWnhhHMToykGLvJZwY7f0s1UebM5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=hnqS_q7xdnnDldiY1nABZpn5uJZxSr9Lk_azZpy5nS5Y54TB8yLM0KqROhv-MAKaye9jfjRyKkjxcIOoUv35zZPl_Q8USDTm8tgYVY1niA4Of-QBNZe_WQPKYNZNTX7SO8-5rr4R0DMp9XPyExj2Cfe60bzBxyMcTl0S9yWXQZzI5Y4Xc6hTF8q0DbGhw3FqiGs6hmbmeppecdS7jG77mKcWclZG21ucQQtucczFGmIlp-GTWgFcZHygBd92E7n5sg-tzdgCtlqyeglFypHtYWXDXRQDL92ag1XdEiYcvOGuh8_-fZNG2nsNrWnhhHMToykGLvJZwY7f0s1UebM5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=HKzQh6cL-Wm9SwanCKHIROAWNMrbs4-MSrTxmcB9OPzdbDf321Lrx_BSIi7admDC_up3l8UL1HxzV12KgWUWXWrXIMK7ZM_sPPZ3WfU67c1zyBja_IPfv2HPkm05niQg8yeDedciuT4J68vz5Y7UZjWY2587dZsz4eWkFv1ONIArXJM0pw85bR1hZx_DhS7k2VFYMu452-JumpekqLvh2V6hNNYOxSUowVwbpdm_FTsOhxmhVCKWC6Q2L-u46QJ0gzAqvOKsdPLdcPdQT3thQEz8Vu2j-ryqRb0L3YXLb6YecQ4ZiQoKtMKWha_DiTZQuhbOdIEXvSw32mBCNkfMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=HKzQh6cL-Wm9SwanCKHIROAWNMrbs4-MSrTxmcB9OPzdbDf321Lrx_BSIi7admDC_up3l8UL1HxzV12KgWUWXWrXIMK7ZM_sPPZ3WfU67c1zyBja_IPfv2HPkm05niQg8yeDedciuT4J68vz5Y7UZjWY2587dZsz4eWkFv1ONIArXJM0pw85bR1hZx_DhS7k2VFYMu452-JumpekqLvh2V6hNNYOxSUowVwbpdm_FTsOhxmhVCKWC6Q2L-u46QJ0gzAqvOKsdPLdcPdQT3thQEz8Vu2j-ryqRb0L3YXLb6YecQ4ZiQoKtMKWha_DiTZQuhbOdIEXvSw32mBCNkfMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=CGQX7Brs5M6HSSncnDDRHrYznuXMAGSZrksedVr3HRwpJ0mt66nt2Tvegnry64A2CK9KFHL4GNGa8plIdEZymd4qV2MVlk2R3KUCyCfrK9E2BkSbmwNvhNv7Od0HNe_I1KLsMyQcRKEda5SheXKlvC8A3lPIY_3_lcdMYtIqxnSkOjduiGAtpAbARS7aD37KYjNBAoXxWYJFasNsaZ9tpprj0aQ8TTB_M7EBrPpP1H4Xo9qL9mCGeTJ-3bMH2-2vxdxdAxDIg9FdHFtjPYZphcS_5JanmREEa6cb5gyiRGIESrEdu8LZB-hVqb_YiHb_Fp-3ta5ZNt6OQTO-4Bq7cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=CGQX7Brs5M6HSSncnDDRHrYznuXMAGSZrksedVr3HRwpJ0mt66nt2Tvegnry64A2CK9KFHL4GNGa8plIdEZymd4qV2MVlk2R3KUCyCfrK9E2BkSbmwNvhNv7Od0HNe_I1KLsMyQcRKEda5SheXKlvC8A3lPIY_3_lcdMYtIqxnSkOjduiGAtpAbARS7aD37KYjNBAoXxWYJFasNsaZ9tpprj0aQ8TTB_M7EBrPpP1H4Xo9qL9mCGeTJ-3bMH2-2vxdxdAxDIg9FdHFtjPYZphcS_5JanmREEa6cb5gyiRGIESrEdu8LZB-hVqb_YiHb_Fp-3ta5ZNt6OQTO-4Bq7cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=FwpdE1uDVXVruJpesqW-YUyTupubVQz-nc4rD5O_5__sOn_2gAbcYAqnz7tnKIhm2H9JTTS-Qh9bEOh2FpBG6Hd3vTwfJ2cCdk31iebuyrohi-tBpOWtcdA-8bpTI3tSEvyZq9FUp_VbkUCyJJDCxDfLh_kEZ7tFuyFoKNwVxtOUigMZqykwE0tEOcyTq3iTPtxjjVWe0PUUV9JTn1a-5bsnk-Fk-GNm4EVXlLaPFK2FVSk4X3CwxhnzSsjim4eLF8oyfPB4RWHR9i_U6DkV5I_IH53GVpsQ0oWE6nXmlBlOwANaVI6BwtylE8DAKFDwob04ieYTTUjVjUkC6k64JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=FwpdE1uDVXVruJpesqW-YUyTupubVQz-nc4rD5O_5__sOn_2gAbcYAqnz7tnKIhm2H9JTTS-Qh9bEOh2FpBG6Hd3vTwfJ2cCdk31iebuyrohi-tBpOWtcdA-8bpTI3tSEvyZq9FUp_VbkUCyJJDCxDfLh_kEZ7tFuyFoKNwVxtOUigMZqykwE0tEOcyTq3iTPtxjjVWe0PUUV9JTn1a-5bsnk-Fk-GNm4EVXlLaPFK2FVSk4X3CwxhnzSsjim4eLF8oyfPB4RWHR9i_U6DkV5I_IH53GVpsQ0oWE6nXmlBlOwANaVI6BwtylE8DAKFDwob04ieYTTUjVjUkC6k64JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=nnVUQnEdicVTCQKs-NSCb-zM-V6-naMeZLFWYmnsozv-DNF1eesHvakSfTUFnyTNgz7saSemlgHsLDk2nZhRCqfnvfooioH0_ZanzdHDn_wlq01NjUypuFThTLjk2KGreCMsFuAM_VmtTmmPf4JzPIrRvNlnZ7dHAZQQHQB1puW0mLCm-JScTvsiz1OKcZzWct8yyfIF4mxCzTz59lxmo6jisWq5LXFethqYhCkP-mg1jxP96nhihOeD2gny_lyXOUiljk2ADlhtDcvtrApILL7fakM52h-INhU_exjeA5GA5PtwkL90t00R0h93ZL7qzMv2WjDYNdXpaIHKx8_SSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=nnVUQnEdicVTCQKs-NSCb-zM-V6-naMeZLFWYmnsozv-DNF1eesHvakSfTUFnyTNgz7saSemlgHsLDk2nZhRCqfnvfooioH0_ZanzdHDn_wlq01NjUypuFThTLjk2KGreCMsFuAM_VmtTmmPf4JzPIrRvNlnZ7dHAZQQHQB1puW0mLCm-JScTvsiz1OKcZzWct8yyfIF4mxCzTz59lxmo6jisWq5LXFethqYhCkP-mg1jxP96nhihOeD2gny_lyXOUiljk2ADlhtDcvtrApILL7fakM52h-INhU_exjeA5GA5PtwkL90t00R0h93ZL7qzMv2WjDYNdXpaIHKx8_SSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Z-BmZviO7kGE1xsRh7gxeL70veISTN7QmAIN1VFA5srOf5uPXc2COROhaWMKYOv0Mpn0J9clsjVaFHza1Jc5tLzAdfsHJlRU-sNGa4X50o3Ctqe3qmVnMmNd7ZYYTgngSwMvscCeUIfnbEdy7ymHVTEu4Inl71KP0y0ku08C5C7x1x4mH81rBWkp9DxOQu-lC6TQ5fBMF11tgn4XHDOUe9rl1F5qOzg6FYrCHjLctFX4ac01dqSZ9Qd3BeKw-9ikAWp9KTNgPrBsKig_Nvjw99s_0S4lFHYr2MIc2E0vqaE80UYGUn6k7zU3Pm7KcM0dSuK7AxayzVDGr-klX52YPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Z-BmZviO7kGE1xsRh7gxeL70veISTN7QmAIN1VFA5srOf5uPXc2COROhaWMKYOv0Mpn0J9clsjVaFHza1Jc5tLzAdfsHJlRU-sNGa4X50o3Ctqe3qmVnMmNd7ZYYTgngSwMvscCeUIfnbEdy7ymHVTEu4Inl71KP0y0ku08C5C7x1x4mH81rBWkp9DxOQu-lC6TQ5fBMF11tgn4XHDOUe9rl1F5qOzg6FYrCHjLctFX4ac01dqSZ9Qd3BeKw-9ikAWp9KTNgPrBsKig_Nvjw99s_0S4lFHYr2MIc2E0vqaE80UYGUn6k7zU3Pm7KcM0dSuK7AxayzVDGr-klX52YPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Uw1utw-rKl6OZWuNXEJVJkTJoUfN8hanWBJkwF9Ri9xBNkb_jMV44hthaYaFJ9Z5Z1ANDZSCtXWye0cW16oT2hFV38vZper6r73zKRGVAktWwY1XpRUj2wzH3QbZsYafXsCXFym81d0Tie047PYKaMbd_9eNRsb97QOfS33ltxuDXeiTDfpmtxSfp_sfPb1wEj7asFVt5-l5KIyVTOmfy9Yzm1wFSujRJxK5MhI3y4Po0pQxDaBWQUpw20zewlr_hkyDN1YxT7HJGMY3u9Y91mqIemHqOxuA8Ka5ODJpdL2rLu1b7jvplt3T3-WvfSh1zG32k8xxYUjtmXf20tElDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Uw1utw-rKl6OZWuNXEJVJkTJoUfN8hanWBJkwF9Ri9xBNkb_jMV44hthaYaFJ9Z5Z1ANDZSCtXWye0cW16oT2hFV38vZper6r73zKRGVAktWwY1XpRUj2wzH3QbZsYafXsCXFym81d0Tie047PYKaMbd_9eNRsb97QOfS33ltxuDXeiTDfpmtxSfp_sfPb1wEj7asFVt5-l5KIyVTOmfy9Yzm1wFSujRJxK5MhI3y4Po0pQxDaBWQUpw20zewlr_hkyDN1YxT7HJGMY3u9Y91mqIemHqOxuA8Ka5ODJpdL2rLu1b7jvplt3T3-WvfSh1zG32k8xxYUjtmXf20tElDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=dMGJIi3mfPd_rfkeNeLhN4IbafifKv8GkjXIcDoRShzDlHQNgLhQEMiW1dzUHtVrVIr1upcfgUzy8hih7Y57pPcYE3zRvTf9uTphf12VFLRp0CimnKcalk-KMrG8ZhoSpQRgVOo58x3rZV-TbRMB--Iuk8_Xfp2lgEFtdDWmo5OZpODROj2P0REUOk-_XL35PeAviEY8JI-3gUFA1Sjc7VTT-HLMY0Bvs7zGlinTj3ke82qzZ1kL2r60atLXgqlUG1emktMbRNXlJFz3Q970Q5FSRtl0mtUsFZhGIMhXKoYgx3qJ0ZLSFseOfWah-yT2lAeyoS-Atz39CeyN8mG1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=dMGJIi3mfPd_rfkeNeLhN4IbafifKv8GkjXIcDoRShzDlHQNgLhQEMiW1dzUHtVrVIr1upcfgUzy8hih7Y57pPcYE3zRvTf9uTphf12VFLRp0CimnKcalk-KMrG8ZhoSpQRgVOo58x3rZV-TbRMB--Iuk8_Xfp2lgEFtdDWmo5OZpODROj2P0REUOk-_XL35PeAviEY8JI-3gUFA1Sjc7VTT-HLMY0Bvs7zGlinTj3ke82qzZ1kL2r60atLXgqlUG1emktMbRNXlJFz3Q970Q5FSRtl0mtUsFZhGIMhXKoYgx3qJ0ZLSFseOfWah-yT2lAeyoS-Atz39CeyN8mG1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6cpHDfAyT9Rgw33EhOvSRnbJ75-jXH17n1pSX7lyLPgH4E_AwG8paLXYVBZgccUyq8V8e1nzJFh9m_0aOcrVT_KZK1kCg-RsNevAc47FA1Sku-O2upCFbKJpFYBkvxUODEk5VACyq9_1pysZHB5vk3w7SHHzMaOmrVPawCtILdASXvVnJj4kAjOKZC7cItyuSykLUuu33-3WFHJd-CFkLUyGmu4Rcx2gHWVV_vvgQ3Sfgxn0tbIn316qGtRiug5C1PQ6VfPqHyFJ6cZRJmMiUyv4tOVp2Vn9zOx6t7NoLeZNFoVuo5f7KLP4l_AJIDQXy5XxwcJ3yGq4p9SETbHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qgtPBYhP1GXfhx1fQTSx9YbsjwHZRYlinpejWZa7nxzRgdGvvNbBQ2DSCcDCe-z6hrXiTFvYwSprBxHa8mO7xLiQ-XxhKPsM8d2pVMbx7aYoPSZc1PZS0SsDxm5jF4VdhFvsfX0vxeShVz0gEXv1aV8mqTGQ6vDuFZJ7miFl3cx_KmwNw-MduSTTahcEEBq8oXqDpgGIFBd1dubhSV4gDzQYFeIv3BNLGreZ9-yOrKJIEXaaq8NgYlH6y4c24aKGAJdiWN40FFbaQAdFQNldk49yAhwe9XNid38AoN_VDvkdrvTa4IdCCMnXwDUDOfg5AmXsahlNw10VK_SR8j_RPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=qgtPBYhP1GXfhx1fQTSx9YbsjwHZRYlinpejWZa7nxzRgdGvvNbBQ2DSCcDCe-z6hrXiTFvYwSprBxHa8mO7xLiQ-XxhKPsM8d2pVMbx7aYoPSZc1PZS0SsDxm5jF4VdhFvsfX0vxeShVz0gEXv1aV8mqTGQ6vDuFZJ7miFl3cx_KmwNw-MduSTTahcEEBq8oXqDpgGIFBd1dubhSV4gDzQYFeIv3BNLGreZ9-yOrKJIEXaaq8NgYlH6y4c24aKGAJdiWN40FFbaQAdFQNldk49yAhwe9XNid38AoN_VDvkdrvTa4IdCCMnXwDUDOfg5AmXsahlNw10VK_SR8j_RPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=JhEjc72SVyoCPAOWOP0FZBPfzbFmWSjYr-iORfF_Sb1NSBjADf-3qSg2mQ6bAaNQ5Ef-g1NnLrnmy-bNcMjVXM5rSN84_v7XFUes0albkQBzCMzJEbsp5nysD4IJFPsaExIT2In9uubQac2MG9s6EEBjzt_K0e7tFBlwLTBdbhyF2Vwe9JTgu_1YAQTu4JERxLLDMeRIG-iSn7R5UeOMOhbaQyg9i7_AcVGS_jyViGlGNazBMd3apzquYzw0q7XPsPWoUHDlYHrJsO75B8-oA38IX0b8L_kJYnWOEJPZh4y5yNbMRNj1EUFCd-JuPHa2B21D25D1a9erVM9fxfc3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=JhEjc72SVyoCPAOWOP0FZBPfzbFmWSjYr-iORfF_Sb1NSBjADf-3qSg2mQ6bAaNQ5Ef-g1NnLrnmy-bNcMjVXM5rSN84_v7XFUes0albkQBzCMzJEbsp5nysD4IJFPsaExIT2In9uubQac2MG9s6EEBjzt_K0e7tFBlwLTBdbhyF2Vwe9JTgu_1YAQTu4JERxLLDMeRIG-iSn7R5UeOMOhbaQyg9i7_AcVGS_jyViGlGNazBMd3apzquYzw0q7XPsPWoUHDlYHrJsO75B8-oA38IX0b8L_kJYnWOEJPZh4y5yNbMRNj1EUFCd-JuPHa2B21D25D1a9erVM9fxfc3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIRt1-FPVxHn2cCohyOxJqacLPRLjQ7iBSGB8r5NJ3A32VZBYSqXWnxfPTMhELnA-tKKJ6eM11cIGhgikNOhT54YODrJRloejWJjf61S2lhnjyBh-jBvT6YqLb4uduTq4fvXRq09FlVxtuQARdDnchz3ZsJt34xuF-e7cfiokk-X-HGEtp4wFATkJczfxASx1lw2lMQtWiww4G2ko2VSnHIhtxoTAyg-G71UfLeDjgRKOw3BQQT_LjGIx_XGYLwVbsd7_6O_OELPnor5MrujX3aKhUAt97jG6JE4c1eJRvOHtq3orl8JhPn3f6ZOq6OFh22RrmwnzkvP2jpUIrZ-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQK0GcUhu5i-UviQaAfX9PCGECKzaSU7ZCMbPB9iO96xVoWvc-0ggmoRivBNa_rGL9ZyvDtZI7nwkPwUiM7nBAP5s6rUtJuJVZgnDAkuTSKA7jzE4XtVs-HAbyOfKn7mhDxrYdhAaEGpsQPxvFMMczLstA-yOxEq9vvkbkaCXSowGawudT2L-j3FEnMFh2BA_WFx2AN_j8SXjIRfCHJrYBIBrJo3giaatIJOR_UwNn6nXnnHa2L94dKGeBnhm6N2etpBdW78r7pmxeRdTDT-sClrprA3B-8Y27i05X2ETXEO5aMysSJACHgQK4DQ1yIHmPfT6Psu_GGePOiN94ex5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=lvHpFxZTZUAz3dcZfi1V6edJeDyR0DRt0hBzZIr35AMlyz-P3rVczuaClOlSEzmmReF_-nlMe4b3_ji_FJ-FAz8R26qRlyQhKb-m-cFTKS9-nrAxv59heo3axXZUxKsRqYAznnUHg0wRfR16MgxkQUv2StC03sGkS0tnUISIIh0oZmMRIbh4lWyleyfw7u4_y_EjtjVEHSpTrhZkCFJuDgEOweveXnkaoHVKRNfqyFcabecX8uWdwRV_76f5kixgxaKdlLjHhqwmE46Y2-vbv3ASlD8OBufFjthbw_V4pKRDF4AzvrVmH7nB6Sbh0OaCXtbAgokTxoio9T3AoUzEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=lvHpFxZTZUAz3dcZfi1V6edJeDyR0DRt0hBzZIr35AMlyz-P3rVczuaClOlSEzmmReF_-nlMe4b3_ji_FJ-FAz8R26qRlyQhKb-m-cFTKS9-nrAxv59heo3axXZUxKsRqYAznnUHg0wRfR16MgxkQUv2StC03sGkS0tnUISIIh0oZmMRIbh4lWyleyfw7u4_y_EjtjVEHSpTrhZkCFJuDgEOweveXnkaoHVKRNfqyFcabecX8uWdwRV_76f5kixgxaKdlLjHhqwmE46Y2-vbv3ASlD8OBufFjthbw_V4pKRDF4AzvrVmH7nB6Sbh0OaCXtbAgokTxoio9T3AoUzEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWZBm2l5YivpZhiYhACqqrUlfbs1uT_21_z-vMZxXfT5g9r9v7KRmm-MwmtQFqJJ-gsUq-TyJCJcV7W2_XgDIIM007T-aJhv80FnLWUn7jw7SIqE7oc2ncboxmBGM_j2f1ieiklkzvL1tRg4ZeF-WsTDBUC96CkQgPLUQG0hayGEkrZeKBhfdpSPKRIbZ5YfO7hBouos3Ybh4_4gq_Os2TQ1AhQhhNvIbErL2QRg58lQRmAV3jSD_pwT0PON5BvTy4mDwzNZhXWGCEDyf-AxBpUrA3pLWpAgJ5xopTigIl3c7dVPWykofF0b5-CbPF20reaRUVY6T4nC0wq4p1QGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXoIdvieWP5dPeUFnTFW7ilBeAr_sznbBcFwoG6xxY8X3SCukxw1yY38uuDMicBjgKEQ6SXa7qibwtFZYYJx8pvblXGolQvHV_LWoXIqoEG3LQ9JMnSxxDrPMSn7gpU2rLtizZ3Kuh6h0RufEaqkNchRuaqiLXPjvBPm8xAxdn-g80XBuRjlBn7RKP95gv7loAWhTKse_2u0hxd77DX-IGJGVUSS3FNojCeQgYSVHsI2yZe_bvYRD4Pca3Y83rZUgE6bMFjBr4ZM24-OFilucKnXGFMJdcFifPEDPHdLeNpLD5rr3kIQiVmWYjcs3xSbbbSQj_o3_zQSYuQfZrzFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAUOcPnLrIUSmMhuXlhr-xs3Nz6wrdy03_k4olmXy0lRnwL1G4cusBJHg1EJs_vcjori3smwm0vnZXWcQV79LQz_RJ4SW5QvGjPA3ydRb022c1DilIDu0wG5Nyqk2PrDnBNbzZ9kCNYsXgmHovd9eeiVn6PIqKqPXYfh3AxUh14uZt_qfTMWGM5bqP1q32wzLJIMw_NQrlWNNE0pthfRXfeuzOk9s1UoHk7VdQYwyf_dTVAQsrXak2erNjGYsxnih9JtnbhUF3ZFt1xf8TqRVCU8ckjXoB2yqnl7YZXXnmhUpjiu_MupIkfBj1OfHw5dC7EBxS_cvGT9pVYK8rMEQg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=TvDnI7ADbLFw1-lO0mZl1Wkd_M0TTdkLKqNTRFwjBdQq96sMMlIjpIXlg2L4C9W28xa3fIWc19oWK1mxPfeLIZOh_7rKz5nLL4c5QYsKrtgwMdrvveVvcRZZuzVL7wi9tXb4OWZLy_Sb5OKywvKoacXuBnxMoi1oT5rKPNvdJdlDUIDWgWuX0RlZJKRfgK3Mj1WVjYJnSTASj_QrUpo7j2HPx6bRo07yOA0KYwD5W6-DUwykzH85yGvQ_hDgfUrNFzBuVeC_Wh5kUOVhTJ8cAf5AaGXNZ23xQDzLR1Y_yjpIzLpTkGjm6eS4Equt0Y5mXPssVMsBDn1qj_64VpuAbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=TvDnI7ADbLFw1-lO0mZl1Wkd_M0TTdkLKqNTRFwjBdQq96sMMlIjpIXlg2L4C9W28xa3fIWc19oWK1mxPfeLIZOh_7rKz5nLL4c5QYsKrtgwMdrvveVvcRZZuzVL7wi9tXb4OWZLy_Sb5OKywvKoacXuBnxMoi1oT5rKPNvdJdlDUIDWgWuX0RlZJKRfgK3Mj1WVjYJnSTASj_QrUpo7j2HPx6bRo07yOA0KYwD5W6-DUwykzH85yGvQ_hDgfUrNFzBuVeC_Wh5kUOVhTJ8cAf5AaGXNZ23xQDzLR1Y_yjpIzLpTkGjm6eS4Equt0Y5mXPssVMsBDn1qj_64VpuAbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=OsxiLS0L0m8eAjz8S_mYD2rOISDzwxXYtsdix9fWHdQrmT0sFn1DEg_nPFVa1oRGOjzgF7X08p3YvxkrOwcAvpeO3v8XPUoBgZmxRxdnNk0xQd8d0mIeJucrDZVLTBx84irLcGMJ_73T8-7mZHxgAN7zwEpwZykLjY7NvqTgXCKDv__NB2GxlCqBvOVBAxsn9yeQetHEps9BYCnd_Ora3pfPvU1TmvQ2Ys-Jz9EQHQ9PY8cWJLx80_CrO9CV782u4dh6YyXycTN-7MBh-iWiQ-Vv9SjjeqAoxiJqx_6A2k0yy8uIglPM67iKw6c2c3XiSTS7dyYQc2mWeNjp2cHZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=OsxiLS0L0m8eAjz8S_mYD2rOISDzwxXYtsdix9fWHdQrmT0sFn1DEg_nPFVa1oRGOjzgF7X08p3YvxkrOwcAvpeO3v8XPUoBgZmxRxdnNk0xQd8d0mIeJucrDZVLTBx84irLcGMJ_73T8-7mZHxgAN7zwEpwZykLjY7NvqTgXCKDv__NB2GxlCqBvOVBAxsn9yeQetHEps9BYCnd_Ora3pfPvU1TmvQ2Ys-Jz9EQHQ9PY8cWJLx80_CrO9CV782u4dh6YyXycTN-7MBh-iWiQ-Vv9SjjeqAoxiJqx_6A2k0yy8uIglPM67iKw6c2c3XiSTS7dyYQc2mWeNjp2cHZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=RdnGCymvtvC2_MJwpxgtELUs6xNHgtaJ7H5sydKCnS5GPKRrKbnOppHJjS0zAmhVkuTTG6-l3xyp0YhmTqt-Pgvmw4A71Pn1_QOECqghqjA-oQB4pByn6r5MRuq4TNEQeI4k_FL4oYp9UFDmt3626i_ZyZhMJTIM4TpF7IaA8d7V-qpzU0-oOpI4utNXuOXcKuG45kqK6nJYZCvIikDauJjyaJbn_d61stgT3XWRmzgmrx20UztR86MPP0LwPOH8eFG9RhpwKMIQ94AGe-eI7IPmMTLR2i5-9v3SOnk50yLwd8etmNvtWKLrdaCUzcbGgXNlQTb3nP-0qQX5ytodoqEEvGOiyyHrJkrvU0E6Q69JWwiCVMviEbrTkKQ3yg8HRVgXZy6vIPgzP7IynzE67_d6N8e6zOUkvqY0zEn7VnuY-MfK751YAby_qX_6QtCz4ikhF5-DCAkNLczjSsLs4j4p_aiGRA6b3kkldQ_v4-ZhLtRhj94KRh4ceH4shAJ11ubbjomAgefn2aEj55tcWtt7nYz0FJt2xvIbD2_l0NAdqLz9v6utEOhguZTdMW3CD3LX89pubqbpHO3dSYM8c33sXFV2gw-fzpzY0vCkBNzNuO5puYP5t5zXh1XcvKjKyF2qeSkvaS7m315YVr1BL-XIAVRWdGYMH4YB-0Hremg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=RdnGCymvtvC2_MJwpxgtELUs6xNHgtaJ7H5sydKCnS5GPKRrKbnOppHJjS0zAmhVkuTTG6-l3xyp0YhmTqt-Pgvmw4A71Pn1_QOECqghqjA-oQB4pByn6r5MRuq4TNEQeI4k_FL4oYp9UFDmt3626i_ZyZhMJTIM4TpF7IaA8d7V-qpzU0-oOpI4utNXuOXcKuG45kqK6nJYZCvIikDauJjyaJbn_d61stgT3XWRmzgmrx20UztR86MPP0LwPOH8eFG9RhpwKMIQ94AGe-eI7IPmMTLR2i5-9v3SOnk50yLwd8etmNvtWKLrdaCUzcbGgXNlQTb3nP-0qQX5ytodoqEEvGOiyyHrJkrvU0E6Q69JWwiCVMviEbrTkKQ3yg8HRVgXZy6vIPgzP7IynzE67_d6N8e6zOUkvqY0zEn7VnuY-MfK751YAby_qX_6QtCz4ikhF5-DCAkNLczjSsLs4j4p_aiGRA6b3kkldQ_v4-ZhLtRhj94KRh4ceH4shAJ11ubbjomAgefn2aEj55tcWtt7nYz0FJt2xvIbD2_l0NAdqLz9v6utEOhguZTdMW3CD3LX89pubqbpHO3dSYM8c33sXFV2gw-fzpzY0vCkBNzNuO5puYP5t5zXh1XcvKjKyF2qeSkvaS7m315YVr1BL-XIAVRWdGYMH4YB-0Hremg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=fTtQA5OrdFibUVd-teYPEq9MCwl0lv6uSl04T-WeXuCGJeQ3OVlsvzHRFEde7kuevtkUYTpA6TpKKqBxfpkHgoRvBl0lGEs_NW-KXaztOhSnv9-EYOF2exDnsWj6Jk4xJXh1G1tX-RMBOmq3XQBVBN8gwhN8DQL3xAK4wGEQqcpujvHmsih_XNfzwJBp0WdwRkeMDCXpmx6iHN3mytKvaBBuoy0N1PcV3nIfEsOlORqgeueWLd50-eGQPBOQltoTXnNAz2jT9IlHAdwGdg6rfk-Zctqd84EqmTK_PvTZiajnqBgv8jwUCa75tGU_qrkaeHbyxMowfGYJeJ2q3luq859rxK-J1bdoUuu5V4uG8xd0XpaQgebza4mic1xIKV0QOdO970Fojqj00H3jml3RDLKTDeWHcf8MXc6GIoVxS6qD4CCATpqY25tsEn334lLPKoTl6JeLf8iM6ZYqMRLfru-Ff9rKa4tBRVFEczg2O_oNTkLp_v2wEDkhx-cj-iP6M-8m3fw_bBzKQInle0J3DkxigwKnS4khY4nYbOcyLRTxJ_lHCHgAzqlnXaypcErRyc_dyaLL6ujTALA9gxH7ZezJoRfblyrydxGS4axpPuJtFIeLVj_WvTMlja8IPz1eBU72Uryz4W69d7mUDXft66HFAoFT1VeQwhKOJLZ4iEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=fTtQA5OrdFibUVd-teYPEq9MCwl0lv6uSl04T-WeXuCGJeQ3OVlsvzHRFEde7kuevtkUYTpA6TpKKqBxfpkHgoRvBl0lGEs_NW-KXaztOhSnv9-EYOF2exDnsWj6Jk4xJXh1G1tX-RMBOmq3XQBVBN8gwhN8DQL3xAK4wGEQqcpujvHmsih_XNfzwJBp0WdwRkeMDCXpmx6iHN3mytKvaBBuoy0N1PcV3nIfEsOlORqgeueWLd50-eGQPBOQltoTXnNAz2jT9IlHAdwGdg6rfk-Zctqd84EqmTK_PvTZiajnqBgv8jwUCa75tGU_qrkaeHbyxMowfGYJeJ2q3luq859rxK-J1bdoUuu5V4uG8xd0XpaQgebza4mic1xIKV0QOdO970Fojqj00H3jml3RDLKTDeWHcf8MXc6GIoVxS6qD4CCATpqY25tsEn334lLPKoTl6JeLf8iM6ZYqMRLfru-Ff9rKa4tBRVFEczg2O_oNTkLp_v2wEDkhx-cj-iP6M-8m3fw_bBzKQInle0J3DkxigwKnS4khY4nYbOcyLRTxJ_lHCHgAzqlnXaypcErRyc_dyaLL6ujTALA9gxH7ZezJoRfblyrydxGS4axpPuJtFIeLVj_WvTMlja8IPz1eBU72Uryz4W69d7mUDXft66HFAoFT1VeQwhKOJLZ4iEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aYHz9oYFYq-wtfnz-b-Pud-53egZofWbRTrP-3RJbhACDNYri_8FxmILoKjctwvFZ6GLExERo9z6Zz8Di6o6mpEoot489eqd7fX0E-SOUY_q-35uM9uL_2h-vnuUxYpFFfNdT3_Pv0rXfRk4BGWzJUhQwqqaQzRx6MOv8fce-S1fk5kCdUstI52DTILTTNDs7JtjjmQI4A2BBUBBgkeQIjcvgXGvBKJC6g1PgcwwiRsms540noCDlzUSw5AKDfw0LPfnD5pzFv0_GdVsoBQ6H_hPQ8zrbhoMZURugAp1mpHRbKS1AJEA78GtMCr33ovaiJdzLqEPlzSom8KrQQnPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aYHz9oYFYq-wtfnz-b-Pud-53egZofWbRTrP-3RJbhACDNYri_8FxmILoKjctwvFZ6GLExERo9z6Zz8Di6o6mpEoot489eqd7fX0E-SOUY_q-35uM9uL_2h-vnuUxYpFFfNdT3_Pv0rXfRk4BGWzJUhQwqqaQzRx6MOv8fce-S1fk5kCdUstI52DTILTTNDs7JtjjmQI4A2BBUBBgkeQIjcvgXGvBKJC6g1PgcwwiRsms540noCDlzUSw5AKDfw0LPfnD5pzFv0_GdVsoBQ6H_hPQ8zrbhoMZURugAp1mpHRbKS1AJEA78GtMCr33ovaiJdzLqEPlzSom8KrQQnPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS-WtJruQX2cm0YwJMwntX_tuYg4ULHnBQtVtV1YK_DySv_V7rLihlhpJDMQO8ruHAfWUFJtsTAPBOX9Qm-jP0O-c8jegkTMMwTDW9tC-dWmUCSdv7y6HOiBNpYlw9wKDxm7NJoX3gfdi2pa4JUziL7p8McSY6_W1jYECLYn03OLlHiKght9EDbm3uSjgSwhO4FaFN64hFiBxKE4BQpVxt-bNRTHMh6VquftQT6Zfr0ssMcS0vbdzoe39jcZjoasVXNhbq12MZPH8ZBUzV3uXztsSLab0DIzxmpP6ramDeINGXBXYue8Ju_9ikfbdZ9cqaZK9e3orFk015BlbpUCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=i4yUzylI4xXpXvr63iWSZRnlG4imqshap2QXjpGOCbyPZU5O65hnf0Oy9JzGQ7v1h0Lu7ow60jHSw0zWPTmPzKL4ki3SYj6Lc477U9j40akLbpd3tAXfDwskgilo7lT0w2XIICj5V1k2fowBs8A3KiKmQBeH1DPl7UhTjuqufkghayWtL-CWkvzTpnhvxZNPF_BFSbXZ24uosLRL2cTngwnFRAsaCUegwucT3ImaITzdlPQlfykJFhB5bRHMDEVZkHYjEAV_NQJ9Xc69z1D4_ltRqFX-hKG_cT78rTZwAA_PU63dIV-fCbKmurND4IdBpvYqyFCcvmyHqtXBaQDKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=i4yUzylI4xXpXvr63iWSZRnlG4imqshap2QXjpGOCbyPZU5O65hnf0Oy9JzGQ7v1h0Lu7ow60jHSw0zWPTmPzKL4ki3SYj6Lc477U9j40akLbpd3tAXfDwskgilo7lT0w2XIICj5V1k2fowBs8A3KiKmQBeH1DPl7UhTjuqufkghayWtL-CWkvzTpnhvxZNPF_BFSbXZ24uosLRL2cTngwnFRAsaCUegwucT3ImaITzdlPQlfykJFhB5bRHMDEVZkHYjEAV_NQJ9Xc69z1D4_ltRqFX-hKG_cT78rTZwAA_PU63dIV-fCbKmurND4IdBpvYqyFCcvmyHqtXBaQDKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Rj8025FpEIpNmL8SHvRrcmFLIgB_0GeBi_8fkmdAyI6xQHs_vGTpsuWep8mwPcDMi2fS47tY2ZElgv5as9TkFfgds0Xh_OLCuZ_28ZGX774VyG4QDF8YlwwSAuM_ZGENOStPKwGHeoVmkpJzIbiBIqvWAlbRjxgHqwiYrWnOaKLwGW48812rzrA_RJCf5aqkJWDJGXQa04YfB2uilP2QuJQ44ytKOj5wjSN2Si9QqlEzv1L-zJMh71o0fJ4Kiu58y3pVGyG4HZFbW9eaBhIncPzB9s3fFC2DUH57e_UFrzFQl4kAX0JcRbKbPcuYq_LFSnEuhOwRC0yvGtISaxiwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=Rj8025FpEIpNmL8SHvRrcmFLIgB_0GeBi_8fkmdAyI6xQHs_vGTpsuWep8mwPcDMi2fS47tY2ZElgv5as9TkFfgds0Xh_OLCuZ_28ZGX774VyG4QDF8YlwwSAuM_ZGENOStPKwGHeoVmkpJzIbiBIqvWAlbRjxgHqwiYrWnOaKLwGW48812rzrA_RJCf5aqkJWDJGXQa04YfB2uilP2QuJQ44ytKOj5wjSN2Si9QqlEzv1L-zJMh71o0fJ4Kiu58y3pVGyG4HZFbW9eaBhIncPzB9s3fFC2DUH57e_UFrzFQl4kAX0JcRbKbPcuYq_LFSnEuhOwRC0yvGtISaxiwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pguhUEr4joZxir0s5tetZQpxkrxOOnsAH6-b1WZg0cIQnDOop7psAxKCAB7ML3zyuEelnlKCDysnpUelo1ZEXqpMoaGkeNWMZFiXW7_3oof93xfkKtgVexrvFq2xz9z5j9ZcgG2gTor1hvBZpwd4eoVC97loFfXm6EeVCBDUJWDLKpHVwJ5na3c-bB0NgpJlUR5yg7beJgEDIwELh5V1rT2DT489_qtqZdL4FRIqWpQIvVL39piOsezoqkUeyko747tlGt3z0qCLMiIzjj9mi-XZEPRbFzkYCzREx1DV2PBonib0jiVsyW7hdi1YQkP4-fW2Gt97WT7ncPjMKEoynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJ_meKGKdx7qSSkhZfE2K5xHM_1K9_HqCl8eAlUAM4N8vTPfpebr1esKoE9-9FST7xB3KnRKx1t8LmkhoicnedL-jU0VfV5gduyVTNim5uDBYvYZSOcm1lypYwoY8rHf_Q6BgqRBPSZ9iZMrzidQA4iChDGKm4pRSn6oxh4wsYk2fpn4_SNbSNb5R5gAc20xvZLgo2E0SCt97WLsFT9m-e25pvs8zGMZ8vUiLGU9KQ2PaKB4kwvxwHY2gASdxRPdboENq06V3UR7CHbIMHFil4TOMbsyc8U5Bk55LjpEdi4cKy1VV1Ou6_7qoQiQy-oVc0-_XuUCW-zPnrxYsT3w_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZSSYkXBlVWHae7IPMPP4L_8ODAJRuRz-SvS0pd6eYQX6B39UXrhnIat0uB8V497OfNkjR0JgAtrOR6FqpX9j0eizXhYdI0N4cT-Mu0snCUv49TlLtNAP0RvJkzFPP1Q1sLMO4aSiu99FrA8pIgIdzOfVZhFhzgbLrMtsY3XTwOFtuHtQOiHDLgjNjedYBJdJCPho0SuKpvaQzvn6LdcA_004YSL-An-_kKZ5rw2IKqXonk8QyS3Engo38haOHU2SO6DPLB2y2QnHjMc_wL7CvdCuDbIFx211v8EFjGrIk68agJ0hsybHVuTueKRgOtEFU0TJVSaoXicN1teAbdIpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZqhVCCT21ApbXpunjvRK61TtsOyMuBsLXxZJG_kFYlBtrpNVUBR16LARJOzN_lKMX-sW0g2KU8G8buE003JxKVQTyRBq5StED58DJBA82GKxCNtBeuZArPCB8PQSBHGEwE1BYpadvAxJmioUqWn3pIe11z13pK5bD1MS-RGdID7b5QzR70YtnSBwEdTd5FePb-cLYFSHOXpbMHpPQ_Y_ZxC7K0nAX3ymtXp7kSPUjioo4IjHrQCfSFnOxOw8nmHX6PbJ_D8w0M5fbfBK5wyGOON7VOHiWu21jh_zCNhXJPCECFVD0l_Zu5NkYZGZ68-FeiRKNwOyYgQYvcaN-DgcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGwAb8_XtDVp_dRMU9AvVxjsyJFcQhUyRJPwgLqOrwrLBhBDEx7hoRRIwUqQu9bIudcXtqc_1UXW8UY9g9GrwhfNMSYncxNLTRDHWmD6nyXMcBuBRHoIhka7FNdLoE_UsZ0HonQ6WzucMm9nMLnaNa3H7FJQSGAVTsfU-ktblXi39Fz_e1hIYw_R-3CpyUywaVBmP2Nas74W2tiwJIq_b2PUqGCbRVIgs4zMW__F2In9yI-NcG72LrBoINGpHhKeAAkLhEqUsixRxGMpcNP8b08IGMCmfOm8cHV7AeUwxocv23uL267yFCNLCLowXm35Ldi28_2Dyz5izi8mkyGvIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpdAe6YDzUlpLRtxue5zH_WFDms6thGI-zFVnbCszRI_NMYm0zZ4UGspt2cYO0-G2YJ_CPwrFfsNZ-m6qcFZ9-zwHHB0Bzice6pCTOjTyxBts4tyDVy2FnzjV1PUOuGMR6VzGE1G-amLRCIRLaLc5Tu-d9P7HgUjUC8hl3xZKP1Smoz2eTzmhhIFrTIp3LwTFmm8VIB6zzUm29ETimClvKbq8SOkeA4KYIN-uzST4JpVVO13hBbgfYbf_wg9gHGA2-b6FaP_oaVXlQ0V2JOkS7JZikH2TNbdG2FhZLNKFldVDmJ0bDXY__pKogkC5b7W_nqbrNqBBLmY47SjIFF6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLfSNnkMnWfdeutdKJG36EXKZwBAV-na73BlCY3JAWL-FEAcYjemxplgmd0IoH4fzAtXutsbBHLMyFLkY10418AWy4X31U9lUlUoCmqBd3HB_LW8_9NjCH2MDRx8TaOqjvNue__r4N44GJFuFQs88mbC4PpDr5k8PWKvKXrmhibNIGWDYINfyzX0gF5rFMUj51lgxUXIWzbWR34sxFNsb6a5w6NNYuhotMpRWl2E-9BQh1Jo8Fr2MJbq03xmC5jVbLJqZJsB8iTuGtgGWFg_jN_QO_zCf5P7O2u51Qv96fhzjB7Yfk35yhPTWrH7J_vCys90dJmXw0npEd4DG3LtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hX5wR61uTeRPMrNx24HPmo5m5-lKiCUbV27bd1y58v6qC7v0FydFs90qLRCw7ulLCtKIMttGM8Lsv-x3nvlnVOrXhEBk7ExdOZsCjpZ_xQ1zJFDD4B-3MSAOv2iY96ylZcmLtbKHJd-PHBecPbIIV5InVoY74tdXcztUNUOD4HnPOSv_y0BvEMbjq9MNXAFx9jtSspQ0O_93o4UdeKWgApjx57wRQrDnnbTsJVDc9LENkIHMnUn6DCfNFqeV7-lUNuyLXXqEaPau-nf-ueqePWWy-WQAAH3OTsy87k_5e_Z8OZ6pnLRM-XIsTiO3a-aT2pXEgZ62GPnXI9tzCzqU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-4_VmWwD_1K60cuyLuBIAumt6HAUmkGiJ2Igg1U3Wto47xqFyVk85W6F4obXlSJl1_9-Ht5l8IB6y0iw-sjqUSmnsXDdLMC6-ymeo-aJzoWXtIAvqPfJGqi61JZx0Xn-Mdg_geBI08bYVX5kCyjussSk8lQ99dcRUUhaOUlRcSK1Zto5WzXYy0Z10PdnG94qaCDHQB7QGNxCNZAjAVxjzaERlRzfW_dYD5tcAuyVyNeBCVvdnuKTInAGsH7FRObMLoBZJXpgjhaBRDIj3xe0DjwXIU4wwgSSznQP7au0zO-mGG7-J9lEC4EruSgyYJEx58haeJJi69BF4C5YuHxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbB5NMfz5GF3CQPUabJ9BwiZtVm2z4EX6XFsNMUXIoJdvizvoeBb_15ToWDApz3CElS_D96bhrbvN2zFauA-DtjdG0Ymb8pY_qO-rxXQWyGlVtXbSFUQNW6W8Q7qKaRATkQyR1gn6P9K7-4Q3KQnkU2UC9l4LeoaLnC-yLRdjljY6GXf5HYJ7hxlytVgjv5CLHU8RnjeMbqV5N8uoXpukrOkkLWXbP2eK4QKGUmA61NDyEIjIbU1C5TtJhkAcGVx_Oes608OnWxArBHoCRS0Hux5_vH86l5gEdvnSARLc0RadG3lAU8bIutdWNEoheXHyzVntzjbD1As7mqzlDLt3A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=k5Gz_XCP0vRZpGwQKZUpXZKOjq9JZCAJN7_c_q9nuXrVGx55Yl-rDzVjFVgoUMTuhGyy0TV7MTusnp5gGxWfD1WI0ooU07gVl5ljaQpzlzZZI13TFgIzp5Jvycc2DpW15a7QiONdpr0bs_dIMaF6lnFpCLfEMc47e6oACD4_vUx-rIirtHjLL5h4GT9DvUaw1Hb9ZYq00TJCcLurGXjxb2Q6YY5Z2BKIVT4yUp19SBg70wdTn1tTgQSpQSyP5TJKd4TQvg7TTfA9HMr7VuBBE2YwXpm6IEoxjoAlEY3Dz0mnJC47jfZiNE_LkFTXSfzRGxv66cdvtjLYUgCjIz86cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=k5Gz_XCP0vRZpGwQKZUpXZKOjq9JZCAJN7_c_q9nuXrVGx55Yl-rDzVjFVgoUMTuhGyy0TV7MTusnp5gGxWfD1WI0ooU07gVl5ljaQpzlzZZI13TFgIzp5Jvycc2DpW15a7QiONdpr0bs_dIMaF6lnFpCLfEMc47e6oACD4_vUx-rIirtHjLL5h4GT9DvUaw1Hb9ZYq00TJCcLurGXjxb2Q6YY5Z2BKIVT4yUp19SBg70wdTn1tTgQSpQSyP5TJKd4TQvg7TTfA9HMr7VuBBE2YwXpm6IEoxjoAlEY3Dz0mnJC47jfZiNE_LkFTXSfzRGxv66cdvtjLYUgCjIz86cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDeJhNCTWJaqCFE7-kTojcA_4A4ov7kD5SDymcjhbfcrGlJ1MitXzrhEIrQNZa1vBgHOElu91_Hmg81E9fLjJc2_e1LVuQMbil1h78IHy_3gF0sgg8pTl-r2zMCwW5olR7ukPDnzs3Xyf42dsPCFcCipwy1gcHQsUk-HdBPtpZ-HKRJ8uh0PxAG_V6zkzG-QFpkc6fBuqxSqtrNAiTOAwTlW_SlxZ1Dl7vsmnHVzwcmlXJ29CPdNdCQZRKRuaJRp0ogPcCqkpnj12YxbuwdBGvYcQMbgnhXmnnggbV_KepKwVtsvKjFNIsvD6KDdAgGWhpOUvUNcRroSww_N_wq_lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvJslMWSVFd1eqzR-Lt0SVohg6cbYzu4-NvuuxLBEV1AIztcZ289d5HwcNcUdwLwWce-fwqcbPWpQwlvK6t26OjiiNTqzL3DuDIseCdx9XJ4f7rUOGjzvAWhesg8yY6gjjdYLZJufDw-VJxOYDOBX3DBv9L8Jshke8Ow1RfqmKEf--_0Sy7k6CLum7wEy93OamgjURCR_jlteKEMYRcDRbya15qSVnEaSIVjthaDTnd6-TkVruNmssF2qgu5guKv2H9rg3gJpVmwg2-mT9WhNvvOARcY1MRNE9QZ8kiXqqb9Z96cqxgcVJtR6GlLmRXaBMHz6FfyspZE5xX_YTGAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=O-kAwp6-vXDxdyeb3zMo1GZpApAjQFzyNjOq4xMS8_a6bOgOZaEW0Bjh2TvilTXIQ-uVGskHmjmAAjycQs7SScRFvX_Y6OQHOIAZZ2LchtQgaoA6EiBoddZ2iV4oIIRAyimZwBaSEfb6FmJMyERON07QJVF463i8bnWxDnmQ0VcPWX9FtkWMRc-0MfYZYT2Fhw77YMgWMk6kL4f41SBnFdCzKMURjLhdOUCHpntoRxGNO-scdvYOIdoevH8hme2ObD6xiFVz-gF8-H_PtCZ0k7H3r_wF4zl0rAM8TXDSXePRLtdsrez5aOBc5OAhaQL9cieq3hxJ8epWUqq4aFY5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=O-kAwp6-vXDxdyeb3zMo1GZpApAjQFzyNjOq4xMS8_a6bOgOZaEW0Bjh2TvilTXIQ-uVGskHmjmAAjycQs7SScRFvX_Y6OQHOIAZZ2LchtQgaoA6EiBoddZ2iV4oIIRAyimZwBaSEfb6FmJMyERON07QJVF463i8bnWxDnmQ0VcPWX9FtkWMRc-0MfYZYT2Fhw77YMgWMk6kL4f41SBnFdCzKMURjLhdOUCHpntoRxGNO-scdvYOIdoevH8hme2ObD6xiFVz-gF8-H_PtCZ0k7H3r_wF4zl0rAM8TXDSXePRLtdsrez5aOBc5OAhaQL9cieq3hxJ8epWUqq4aFY5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=U1AQck4yklzQbIrScmK7eYOf7OpiN3bTAYFUJdTLeQa0ftPoIc0ExCGYqA4foTm0l6nsQQ9Ei3pFmDhzj21g0QPnr4aQqpyWdm2H70gGOqzFw6wEyTR4TWfSeAtGKvuYZYA_RylLo3vMfLkOaDFm6d7kNBodiSvxlr3QCO3VQjKB02oKiNd9-zycpPcEcSxoj7INixlZGNcYDUL7Fa5nQTShZKqRqBYmVhFM1ijpVcu0-oxzDqlXXHoSmTahEOvkP5k4QeRlj5qBhs_iBTa6eC48zQ4trqEvlIiEO7gordwj9yRqCTQgX4cxIRn8KIQ4KuW7pi95BPSV5vycdQV3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=U1AQck4yklzQbIrScmK7eYOf7OpiN3bTAYFUJdTLeQa0ftPoIc0ExCGYqA4foTm0l6nsQQ9Ei3pFmDhzj21g0QPnr4aQqpyWdm2H70gGOqzFw6wEyTR4TWfSeAtGKvuYZYA_RylLo3vMfLkOaDFm6d7kNBodiSvxlr3QCO3VQjKB02oKiNd9-zycpPcEcSxoj7INixlZGNcYDUL7Fa5nQTShZKqRqBYmVhFM1ijpVcu0-oxzDqlXXHoSmTahEOvkP5k4QeRlj5qBhs_iBTa6eC48zQ4trqEvlIiEO7gordwj9yRqCTQgX4cxIRn8KIQ4KuW7pi95BPSV5vycdQV3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQKYE62RQooRXvK5UPKAPal9HRl9m0ra0-APy3ilBSYNwzEnAdXQ8QcJv_XBLmiGaoAmfMDrL22buRov3eiI9UobNWA0BY1uZC_-BBGJo7JKs6KotxHgvcJ67cUzNPW8mY35igFWXxHzWqq7fQXRdmbpwubLMCjSjWmGp_xd98CAvf0Nml4coEw8PJIacjxkSb-esZRU3Yuip0QAN0ZYPUPgovUdSY27dhjXuLvzMyaJ00qmY3M8fdiEfqrWn2-iDrmeoY4z7Q3jNlqkBCpCc-e91n8AsIOW152q0NdyYqLngkVGYFMHCF9qKd7X_9ttvOaHw4k89UlVKvIq9gqQgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMEz2yrmfNCYys2AAUGStz-wNx21ksggdFctV9R97KKAoiyOOe_LaJ0Rh8mYvWSkWiSBMz-Y9XwLXxKFmCzuUkIfQRYlhfZcK6PQI9F4NEa5KvpJK6o_B1tbz4eG1xgXT6_rWGVoIN1d_eobU3vr3TKyjNjRuxQRoPJ-265xIopA-DkDiR5AIla6fgydL1x_OmwDKZ3HzYlnP5ziBBTsbqwtzNYaq3h0IXVL0Jq9aDxo7SG0l4cz6gG87qygyJXjbkkYG16EHSpokt69_CHpPcuO7Ut0OOVN0a4RAJuyIrA-1Y0IoOTWxBp2-uvSKkRSYV4ZkX463rLJ_Pn55TrJRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEzij9ZjIbiiwzyrUSByUDS0NeYBp_2Kt42O3PH2h3dRSpIqfX4zmzLC-C3y2Wore28kFvyH_8RAD7qqBgo1s503iKGQcZKEvNkYwlfvkl32gn-GVs9ysuWtHtk3tCMqrFa3JBl4TpecMH4KM1vQk-CwkFOxbhpODObp1XIvj6RbrrzuUWT4OfFC-RqBr236DG05s-U3Z4ISAzQxIJ3PKESva-w-Wt9ms9x1LwjbTn0wJUic-24PjrKhvh91u8NoMjfxxHcsluj489cp62yhEhlT-ZhEgNX7-cy1jb1zZFBnqKPKmoz2vDx6SSVgck7PXnbHOhzSj2wmE0kR8uee4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJf_4xKeDl-II91-9hQlpwvwBS2LTX6BtvXbcMEI6J3f-sr1eiVQLHpUve1RgU8ewOSJbAC6cNlUphayegpHyNZqa43AS-Zf3yzj7QQFulDBThrqA_V2Oac_dAXmdHMuf5mVsTl7CJHfFbqq78wtr3aucxRTFi88xBcmK19ooYLoBHxY3sIfWn4TIpdAFRb4wiXDu7wvjeemP1SonEq00dyejssytky8EZyd0u_ejTvbG18rQnf4riWlerjhJONkaCmN34uZEvDPir-VdoEqyBbCITkAPc_tbOzr4V2Zt4UrTTWhwI25uabfcrScv5hRgtD-fhltrXndGOGbnzufPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgLI4AXmzQcCD5Auk3XeB8G4bbUT-aBg4RnfHyYe7T7I9QZnDja8nnvSGK8Gv88urmcwbJobRU0dzzkQbBvQ_bCJXMzl27e3SE0aep4W8mcUVkkFP_WXA4650XoqPEPiN8Gg1qm1dmI6uaW12_gXap_gwZpq0S9BXcjJSlY2XERQwQtaxVVQQzupCN-JwAvokR3ZlfUTl6qI_QfXROsR0-EVgbXofHY5fNk9XqSoxthaJb0i5NQTK1cU58HLTV1yWJ9L_w7_FdC-xChEFqPo_isXba4m8zuam-PJuH337X3E1DAdVYa5u5rptBkKiGH2WwA9RD0ts185lvowKu1rBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaFrs5VCUMBmpO1jR9VjJOKstwyWGMPGQaQ59bWSUpRxJ7Sj20DFDeI3tYxD7geNTzqJ0_bClqAFPE8YG5P1JxVSBtmCg4iRNNmIEtjsPniw8xjILLvMAuPL7k3peJVT93ZyNdeeU_EZNzrzPjVVuOyN6sGbsJnT9yi23GQSi2GpIYr-DQ_RW3MAoZyb81N75VRYgrM4qee3JNNfUDy4ZmtSzgw_Gx1NYgr9EJAbhgY_bXuHtUU2ZMpPu2xIgntlVy1yHSVHV-ucklxs1u3qqwVrcI0StphNjPSLe1kuN3Jzga8werNEDZiy3TAe4gP0t79ZioWYQV-sVgL7xGNMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
